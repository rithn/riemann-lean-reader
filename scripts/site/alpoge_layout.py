"""Offline collision passes layered over the original Alpöge constellation."""

import numpy as np


def separate_disks(anchors, radii, *, gutter, spring, iterations, fixed=None):
    """Keep the seeded ordering and pull toward anchors while resolving contacts."""
    points = anchors.copy()
    first, second = np.triu_indices(len(points), 1)
    clearance = radii[first] + radii[second] + gutter
    mobility = np.ones(len(points))
    if fixed is not None:
        mobility[fixed] = 0
    first_share = mobility[first] / (mobility[first] + mobility[second])
    # Stable direction for exactly coincident centers.
    angles = (first + second * len(points)) * 2.399963229728653
    fallback = np.column_stack((np.cos(angles), np.sin(angles)))
    for iteration in range(iterations):
        # Finish with contact-only passes so anchoring does not leave merged cores.
        if iteration < iterations * 0.75:
            points += (anchors - points) * (spring * mobility[:, None])
        delta = points[second] - points[first]
        distance = np.linalg.norm(delta, axis=1)
        colliding = distance < clearance
        if not colliding.any() and iteration >= iterations * 0.75:
            break
        a, b = first[colliding], second[colliding]
        d = distance[colliding, None]
        direction = np.divide(delta[colliding], d, out=fallback[colliding].copy(), where=d > 0)
        correction = direction * (clearance[colliding, None] - d)
        share = first_share[colliding, None]
        shifts = np.zeros_like(points)
        np.add.at(shifts, a, -correction * share)
        np.add.at(shifts, b, correction * (1 - share))
        contacts = np.bincount(np.concatenate((a, b)), minlength=len(points))
        points += shifts / np.maximum(1, contacts[:, None])
    return points


def pack_constellation(themes, centers, radii, positions, files, main):
    """Return adjusted theme centers, enclosing radii and cluster coordinates."""
    theme_ids = sorted(themes)
    local = {}
    envelopes = {}
    for theme in theme_ids:
        ids = sorted(themes[theme])
        offsets = np.array([positions[cluster] for cluster in ids]) - centers[theme]
        # Match Canvas core sizes at its approximate desktop fit. Glow has no
        # hard boundary and touch targeting is intentionally larger than a dot.
        cores = np.array([8 if cluster == main else 1.7 + files[cluster] ** 0.5 * 0.42
                          for cluster in ids]) * (0.43 ** -0.55 / 22)
        if len(ids) > 1:
            distance = np.linalg.norm(offsets, axis=1)
            knee = radii[theme] * 0.65
            tail = np.maximum(0, distance - knee)
            # This bounded radial adjustment preserves the order and bearing.
            contraction = 0.7 * tail / (1 + tail / knee)
            weights = 1 - np.divide(contraction, distance, out=np.zeros_like(distance), where=distance > 0)
            fixed = ids.index(main) if main in ids else None
            if fixed is not None:
                weights[fixed] = 1
            offsets = separate_disks(offsets * weights[:, None], cores, gutter=0.055,
                                     spring=0.055, iterations=200, fixed=fixed)
        local[theme] = dict(zip(ids, offsets))
        # Include all cores plus roundoff slack. The renderer derives the
        # quieter halo footprint separately so a tail cannot inflate it.
        envelopes[theme] = float(np.max(np.linalg.norm(offsets, axis=1) + cores)) + 0.025

    old_centers = np.array([centers[theme] for theme in theme_ids])
    mean_center = old_centers.mean(axis=0)
    anchors = mean_center + 0.84 * (old_centers - mean_center)
    bounds = np.array([envelopes[theme] for theme in theme_ids])
    packed = separate_disks(anchors, bounds, gutter=0.65, spring=0.09, iterations=260)
    new_centers = dict(zip(theme_ids, packed))
    new_positions = {cluster: new_centers[theme] + offset
                     for theme, clusters in local.items()
                     for cluster, offset in clusters.items()}
    return new_centers, envelopes, new_positions
