# Prerequisite tree (diagram)

Generated from [tree.yaml](tree.yaml) by `scripts/tree_check.py`. Do not edit by hand.

Arrows point from a result to what it needs. Green: explained · blue: textbook · orange: research · pink: new in this proof · grey dashed: not mapped yet.

```mermaid
graph TD
  riemann_hypothesis[["The Riemann hypothesis"]]
  grh_dirichlet[["GRH for Dirichlet L-functions"]]
  step_rh_of_every["L2 for all characters ⇒ RH"]
  step_rh_of_right["No zeros right of ½ ⇒ RH"]
  step_crit_line["L2 ⇒ GRH (mirror trick for L-functions)"]
  every_character["L2: no zeros right of ½, every Dirichlet L-function"]
  l2_literature_of_vwin["L2 from literature + 'VWin' ?"]
  l2_local_langlands["Local Langlands existence (recTExists) ?"]
  l2_galois_local_global["Galois local–global compatibility ?"]
  l2_vwin_of_row["'VWin' from a modularity argument ?"]
  rh_statement["What RH says"]
  zeta_series["ζ(s) as a series"]
  analytic_continuation["Analytic continuation"]
  trivial_zeros["Trivial zeros −2, −4, …"]
  functional_equation_zeta["Functional equation of ζ"]
  factors_nonzero["Γ and cos factors are nonzero"]
  gamma_function["The Gamma function"]
  fourier_analysis["Fourier analysis, Poisson summation"]
  complex_analysis["Complex analysis"]
  complex_powers["Complex powers n^s"]
  real_analysis["Real analysis"]
  dirichlet_characters["Dirichlet characters"]
  dirichlet_l_function["Dirichlet L-functions"]
  primitive_characters["Primitive characters, conductor"]
  functional_equation_dirichlet["Functional equation of L(χ, s)"]
  groups["Groups and homomorphisms"]
  lean_placeholder_conditions["Placeholder conditions Sw and TrivialCondition"]
  lean_polynomial_function["Polynomial function ℂ → A (IsPF)"]
  lean_unipotent_upper_triangular["Unipotent upper-triangular matrix (UT)"]
  lean_lower_iff["Downward-closed sets are initial segments"]
  lean_padic_norm_p["|p| = 1/p in the algebraic closure of ℚ_p"]
  lean_algclosure_q["Instance: AlgebraicClosure ℚ is an algebraic closure"]
  lean_common_denominator["Common denominator in a number field"]
  lean_char_extend["Characters of a subgroup extend to the group"]
  lean_sesquilinear_additive["u·M·conj(v) is additive in v"]
  number_fields["Number fields, algebraic integers"]
  p_adic_numbers["p-adic numbers"]
  algebraic_closure["Algebraic closure"]
  rings_fields["Rings, fields and algebras"]
  linear_algebra(["Linear algebra"])
  polynomials(["Polynomials"])
  counting(["Finite sets and counting"])
  complex_numbers(["Complex numbers"])
  trigonometry(["Trigonometry"])
  calculus(["Calculus"])
  infinite_series(["Infinite series"])
  primes_divisibility(["Primes and divisibility"])
  modular_arithmetic(["Modular arithmetic"])
  proofs(["Reading and writing proofs"])
  concept_group_representations["Groups as matrices: representations and characters"]
  concept_group_actions["Group actions: orbits, stabilizers, fixed points"]
  concept_sylow_theorems["Sylow subgroups: big subgroups of prime-power size"]
  concept_normal_subgroups_quotients["Cosets, normalizers and quotient groups"]
  concept_complex_analytic_sets["Shapes cut out by equations in complex space, and their germs"]
  concept_point_set_topology["Topology: open sets, closed sets, compact and connected sets"]
  concept_lattices_in_the_plane["Lattices in the complex plane"]
  concept_ideals_and_discriminant["Ideals, ideal norm and discriminant of a number field"]
  concept_ultrametric_norm["A stranger way to measure size: ultrametric absolute values"]
  concept_newton_polygon["Counting roots from coefficient sizes: the Newton polygon"]
  concept_field_extensions_transcendence["Algebraic and transcendental numbers over a field"]
  concept_discrete_valuation_ring["Discrete valuation rings: numbers with one prime, and reducing mod it"]
  concept_finitely_generated_algebras["Rings built from finitely many generators, and the Nullstellensatz"]
  concept_separable_polynomials["Separable polynomials (no repeated roots) and the derivative test"]
  concept_schemes_basics["Schemes: spaces glued from rings (Spec, Zariski topology)"]
  concept_categorical_pullbacks["Pullbacks (fibre products) and maps that 'factor through'"]
  concept_galois_fixed_fields["A group acting on a field, and its fixed subfield"]
  concept_flat_modules["Tensor products, base change and flatness"]
  concept_valuation_rings["Valuation rings and lattices over them"]
  concept_local_rings["Local rings and residue fields: one big ideal of small elements"]
  concept_hermitian_unitary_matrices["Hermitian, skew-Hermitian and unitary matrices; the spectral theorem"]
  concept_chain_complexes_homology["Chain complexes, homology and exact sequences"]
  concept_finitely_generated_abelian_groups["Finitely generated abelian groups"]
  concept_integral_closure_fraction_fields["Fraction fields, integral elements and integrally closed (normal) rings"]
  concept_coordinate_rings_dimension["Prime ideals, coordinate rings and dimension of a solution set"]
  concept_prime_ideals_localization["Prime ideals, localization and quotient rings"]
  concept_etale_ring_maps["Etale ring maps (extensions without branching)"]
  concept_dedekind_domains["Dedekind domains (unique factorisation of ideals)"]
  concept_hensel_lifting["Hensel lifting (improving an approximate root)"]
  concept_tensor_product_of_algebras["Tensor products of rings and algebras"]
  concept_smooth_morphisms["Smooth morphisms (families of smooth shapes)"]
  concept_noetherian_and_irreducible_components["Noetherian spaces and irreducible components"]
  concept_modular_forms["Modular forms, level groups and cusps"]
  concept_hecke_operators["Hecke operators U, V and T"]
  concept_petersson_product["The Petersson inner product"]
  concept_derivations_smoothness["Partial derivatives on polynomials, differentials and smoothness"]
  concept_exterior_powers["Exterior powers and wedge products"]
  concept_witt_vectors_ainf["Witt vectors, the tilt and the ring A-inf"]
  concept_roots_of_unity_kummer["Roots of unity and Kummer generators"]
  concept_picard_group["The Picard group: rank-one 'twists' over a ring"]
  concept_group_homology["Group homology: measuring how a group acts on a vector space"]
  concept_frobenius_perfect_rings["Frobenius and perfect rings: raising to the p-th power in characteristic p"]
  concept_gl_infinity_homology_stability["GL_n, the limit GL_infinity, and stability of group homology"]
  concept_haar_measure_fundamental_domain["Integration on a group, Haar measure and fundamental domains"]
  concept_lattice_point_counting["Lattices in n dimensions, covolume and counting points"]
  concept_chebyshev_functions["Chebyshev functions theta and psi"]
  concept_dual_numbers["Dual numbers: a number with a tiny part that squares to zero"]
  concept_group_schemes["Group schemes: tori, abelian varieties and torsion points"]
  concept_adic_completion["Adic completion: approximating by ever higher powers of an ideal"]
  concept_schwartz_functions["Schwartz functions and their seminorms"]
  concept_semisimple_algebras_radical["Semisimple algebras and the Jacobson radical"]
  concept_filtered_colimits["Filtered colimits: a ring that is the union of an ever-growing chain of rings"]
  concept_projective_modules["Projective modules and finite presentation"]
  concept_ample_nef_line_bundles["Ample and nef line bundles, and intersection numbers"]
  concept_symmetric_polynomials["Symmetric polynomials and elementary symmetric functions"]
  concept_regular_local_rings["Regular local rings"]
  concept_weierstrass_elliptic_functions["Elliptic functions: the Weierstrass functions on a lattice"]
  concept_highest_weight_casimir["Weights, highest-weight vectors and the Casimir operator"]
  concept_nilpotent_jordan_chains["Nilpotent operators and chain bases (Jordan form)"]
  concept_class_group["The ideal class group of a number field"]
  concept_hausdorff_measure["Measuring curved shapes of any dimension (Hausdorff measure)"]
  f_ab_by_p_of_comm["Definitions: characters, induction, pairing, abelian-by-p groups"]
  f_linear_map_short_exact_commute["Trace adds up over a block-triangular split"]
  f_is_character_over_subfield_of_representation["Characters also work for representations on any vector space"]
  f_finite_group_function_pairing_character_eq_finrank_inte["Pairing two characters counts the maps that respect the group"]
  f_exists_character_quotient_of_injective_intertwining["A sub-representation splits off its own character"]
  f_exists_is_char_eq_add_of_pair_ne_zero["A non-zero pairing means an irreducible character is a summand"]
  f_exists_coprime_order_of_pow_prime_pow["Some p-power of an element has order not divisible by p"]
  f_card_fixed_by_pow_prime_pow_mod_eq["Fixed points of x^(p^k) and of x agree mod p"]
  f_exists_sylow_over_subgroup["Building a subgroup above C from a Sylow subgroup"]
  f_card_fixed_by_quotient_eq_rel_index_of_p_regular["Cosets fixed by an element of order prime to p count a relative index"]
  f_exists_abelian_by_prime_power_not_dvd_card_fixed_by["A subgroup that is abelian-by-p and fixes a number of cosets not divisible by p"]
  f_analytic_germ["Definitions: analytic near a point, and an irreducible germ"]
  f_st_analytic_root_branch["Roots of a polynomial move analytically as its coefficients do"]
  f_st_irreducible_germ_projection_image_near["Irreducible germ: the projection's image stays full at nearby points"]
  f_st_finite_projection_sheets_dense["Points where X is a clean sheet over the target are dense"]
  f_st_primitive_form_sheeted_off_discriminant["Away from the thin exceptional set (delta = 0), every point of X is a clean sheet"]
  f_st_primitive_form_sheeted_locus_cut_out["Being a clean sheet is a zero-set condition"]
  f_st_primitive_form_sheeted_iff_root_full["A point is a clean sheet exactly when its root lifts to points of X"]
  f_st_primitive_form_full_branch_constant["Lifting a root is all-or-nothing on a connected region"]
  f_st_polynomial_root_predicate_factor["Splitting a polynomial into two analytic factors by a yes/no property of roots"]
  f_st_primitive_form_window["Shrinking to a clean window around w"]
  f_st_primitive_form_full_root_factor["Statement: the polynomial splits into factors C and E by root lifting"]
  f_p_primitive_form_full_root_factor["Proof: the root-factor statement follows from four other stated claims"]
  f_regular_locus["Regular points: where a complex shape is smooth"]
  f_st_irreducible_finite_germ_projection_open_at["Statement: projecting an irreducible germ onto fewer coordinates covers a full neighbourhood"]
  f_st_irreducible_germ_points_off_discriminant["Statement: the projection hits every point off a thin set"]
  f_st_irreducible_germ_primitive_form["Statement: one linear function generates all the coordinates of the germ"]
  f_st_manifold_zeros_complement_connected["Statement: removing the zeros of an analytic function leaves a smooth shape in one piece"]
  f_st_primitive_form_sheeted_points_near["Statement: smooth sheet points exist arbitrarily close to the base point"]
  f_p_irreducible_germ_points_off_discriminant["Proof: the projection hits every point off the exceptional set"]
  f_exists_irr_char_add["Every non-zero character contains an irreducible one"]
  f_is_character_over_subfield_induction_irreducible["Prove things about characters by peeling off irreducible pieces"]
  f_lat_defs["Lattice definitions: the grid, its area, and standard sums"]
  f_period_integrals__area_lat["Statement: area of the lattice from two generators"]
  f_period_integrals__ideal_lattice["Statement: area of a lattice built from an ideal of an imaginary quadratic field"]
  f_im_conj_mul_combo["Proof: area of the lattice from two generators"]
  f_orbital_bounds_conclusion__area_lat["Named version of the lattice area formula"]
  f_ideal_basis_alt["Statements of the three ingredients for the ideal-lattice area"]
  f_ideal_basis["Proof: a nonzero ideal has a two-element basis whose determinant equals its norm"]
  f_o_k_area["Proof: the lattice of integers has area sqrt|D|/2"]
  f_assemble["Proof: putting the pieces together for the ideal lattice formula"]
  f_orbital_bounds_conclusion__ideal_lattice["Named version of the ideal lattice theorem"]
  f_induced_class_function_from_subgroup_eq_finsum_cosets["Induced function as a sum over cosets"]
  f_is_character_finsum_conj_subgroup_function_extend_by_zer["Summing a subgroup character over cosets gives a character of the whole group"]
  f_is_character_over_subfield_restrict_class_function_one["Basic properties of characters"]
  f_is_character_over_subfield_induced_class_function["A character of a subgroup induces a character of the whole group"]
  f_newton_polygon_dominant_index_x_sub_c_mul["Multiplying by (X - a) with a outside the disc keeps the dominant index"]
  f_newton_polygon_last_dominant_index_mul_x_sub_c["Multiplying by (X - a) with a inside the disc raises the dominant index by one"]
  f_card_roots_closed_ball_eq_dominant_index["The number of roots in a disc equals the dominant index"]
  f_card_roots_closed_ball_bounds_ultrametric["Any dominant coefficient pins down the root count in a disc"]
  f_onto_o_c_additive_poly["An equation a_0 W + a_1 W^l + ... = b always has a solution in the unit disc"]
  f_exists_transcendence_basis_algebraic["A finite list has a transcendence basis that everything is algebraic over"]
  f_monic_polynomial_primitive_over_basis["Rescale an algebraic element so its equation is monic with polynomial coefficients"]
  f_primitive_element_finite_algebraic["One element generates finitely many algebraic elements"]
  f_primitive_element_coordinate_polynomials["Write each element as a polynomial in theta with one common denominator"]
  f_primitive_element_denominator_clearing["Specialising to another field by clearing denominators"]
  f_polynomial_system_specialization["Description of a finitely generated field, ready to carry to other fields"]
  f_finsum_fiberwise_of_finite_support_complex["Summing in two stages: group by label, then add the group totals"]
  f_finsum_orbits_inv_stabilizer_card_mass["Orbit sum weighted by 1/|stabilizer| equals the average over the whole set"]
  f_finsum_orbit_rel_fibred_equivariant["Summing over orbits: first over the base, then inside each fibre"]
  f_stabilizer_eq_centralizer["Conjugation action on a group: stabilizer equals centralizer, and pair terms"]
  f_finite_support_stabilizer_weighted_pair_term["Only finitely many pair orbits contribute"]
  f_finsum_conj_classes_centralizer_orbits_eq_pair_orbits["Sum over conjugacy classes equals sum over pair orbits"]
  f_st_irreducible_germ_meet_over_hypersurface["Statement only: two shapes overlap over a thin set"]
  f_st_isolated_fibre_local_unbranched["Statement only: a branched cover is unbranched off one thin set"]
  f_st_open_projection_dominant_components["Statement only: a shape splits into irreducible pieces that cover the target"]
  f_p_isolated_fibre_local_unbranched["Unbranched off a thin set, assuming four unproved claims"]
  f_weighted_orbit_sum_eq_pair_orbit_sum["Two ways to total a function over a group action agree"]
  f_dvr_matrix_proj_preimage["Integer vectors inside a subspace form a summand, via a projection matrix"]
  f_exists_residue_annihilator_of_not_standard_column_form_a["Not in standard form forces a missing direction mod the uniformizer"]
  f_residue_top_factor_through_bottom["Top part is determined by bottom part, after reducing"]
  f_gl_factor_from_blocks_mod_uniformizer["A matrix equal to a block matrix mod the uniformizer is a unit times it"]
  f_exists_hyperplane_residue_outside_translates["Column-space of a matrix over a DVR is fixed by a block matrix times a unit"]
  f_exists_prime_gt_dvd_eval["A whole-number polynomial takes values divisible by huge primes"]
  f_exists_large_prime_dvd_int_polynomial_eval["Large-prime divisor of a polynomial value (re-export)"]
  f_sep_int_poly_root_mod_prime_sq["Separable polynomials hit values divisible by a prime squared"]
  f_divisor_proofs__finite_type_to_number_field["A finitely generated domain maps to a number field without killing a"]
  f_divisor_proofs__number_field_to_mod_p_squared["A number field's finite subring maps into integers mod p squared"]
  f_nadel_vanishing_lemmas__finite_type_to_number_field["Number-field point lemma (forwarding file)"]
  f_nadel_vanishing_lemmas__number_field_to_mod_p_squared["Mod p squared lemma for number fields (forwarding file)"]
  f_finite_type_to_mod_p_squared["Finitely generated domains map to mod p squared, keeping a invertible"]
  f_whisker_left_left_is_pullback_snd["Product with a fixed object gives a pullback square"]
  f_exists_factor_closed_immersion_of_locally_on_source["A map factoring locally through a closed immersion factors globally"]
  f_exists_glue_closed_immersions_open_cover["Gluing closed subspaces defined on an open cover"]
  f_finite_flat_surjective_closed_subscheme_of_open_cover["Finite, flat, surjective can be checked on an open cover"]
  f_exists_closed_immersion_represents_of_affine_opens["Representing a local condition by a closed finite flat subspace"]
  f_foundations__coset_trace["Definitions for approximate p-th roots and almost separating families"]
  f_valuation_frobenius_sum_sub_le_nat_cast_prime["A sum to the p-th power is close to the sum of p-th powers"]
  f_coset_representative_trace_fixed_properties["Properties of the coset trace"]
  f_foundation_proofs__exists_pth_power_scale_thin_shell["Rescale any element by a p-th power to land in a thin shell"]
  f_pow_mul_approx_pow_of_almost_etale_separating_family["A separating family gives approximate p-th roots on the fixed field of N"]
  f_approx_pth_root_fixed_subfield_of_almost_etale["Approximate p-th roots pass from the full fixed field to the fixed field of N"]
  f_affine_hilbert_scheme_valuative_criterion_existence["Hilbert scheme of an algebra has the lifting property for properness"]
  f_divisor_proofs__comap_bc_comp["The 'good sub-pieces' functor and its base-change rules"]
  f_exists_flat_ideal_valuation_ring_pullback["Ideals over the fraction field extend to flat ideals over a valuation ring"]
  f_flat_subscheme_of_quotient_flat_affine["Flat quotient ring means the cut-out piece is flat"]
  f_divisor_proofs__ideal_sheaf_data_comap_ideal_top_of_is_affine["Pulled-back ideal on affine spaces is generated by the image"]
  f_divisor_proofs__imports_alt["Over a valuation ring, ideals extend uniquely to flat ideals"]
  f_finite_projection_pushforward["An irreducible analytic germ contains a disc cover of the line"]
  f_st_centred_disc_cover_curve["Statement only. A disc cover contains a holomorphic curve through its centre"]
  f_st_finite_germ_projection_open_at["Statement only. Finite-fibre projection of a germ is open at the point"]
  f_complex_analytic_sets__st_unbranched_proper_count_constant["Statement only. Unbranched proper covers have a constant number of sheets"]
  f_exists_isotropic_graph_unitary_is_unit_lower_block["Over a local ring, a form-preserving matrix has an invertible lower combination"]
  f_exists_isotropic_graph_det_lower_row_ne_zero_field["Over a field, a form-preserving matrix has an invertible lower combination"]
  f_exists_skew_hermitian_mul_add_det_ne_zero_of_pair["A pair of matrices can be made invertible by a skew correction"]
  f_skew_hermitian_perturb_idempotent_det_ne_zero["The projection case of the skew correction"]
  f_exists_rank_normal_form_matrix_field["Any square matrix over a field reduces to a 0/1 diagonal matrix"]
  f_lift_mod_maximal_skew["A skew equation solved approximately over a local ring is solved exactly"]
  f_card_quot_prime_smul_eq_card_ker_mul_pow_finrank["Counting M/pM against p-torsion and rank"]
  f_card_zmod_tensor_eq_card_quot_prime_multiples["Z/p tensor M has as many elements as M/pM"]
  f_nat_card_homology_restrict_scalars["Forgetting extra scalars does not change the size of homology"]
  f_nat_card_homology_of_short_exact_mul["Size of homology from a 'times p' short exact sequence"]
  f_short_exact_mul_prime_zmod_tensor_complex["Times p, then reduce mod p, is a short exact sequence"]
  f_finrank_homology_mod_prime_universal_coefficients["Universal coefficients, mod p dimension formula"]
  f_complex_analytic_sets__st_holomorphic_on_subset["Definition of 'holomorphic on a subset'"]
  f_complex_analytic_sets__st_normal_model["Zero sets of ideals, and a normal model of a space"]
  f_st_normal_riemann_extension["Riemann extension on a normal set (claim only)"]
  f_st_normal_maximum_principle["Maximum principle on a normal set (claim only)"]
  f_complex_analytic_sets__st_normal_locally_irreducible["Normal sets stay in one piece near each point (claim only)"]
  f_st_normal_open_mapping["One-to-one holomorphic images are open in a normal set (claim only)"]
  f_st_branch_fill_dimension["A parametrisation that fills the set forces its dimension (claim only)"]
  f_st_branch_inverse_off_hypersurface["Inverse of a parametrisation is holomorphic off a bad set (claim only)"]
  f_st_branch_contains_normal_point["A branch that fills a neighbourhood contains the point (claim only)"]
  f_st_branch_inverse_holomorphic["The inverse of a filling parametrisation is holomorphic (claim only)"]
  f_p_branch_contains_normal_point["Proof that a filling branch contains the point"]
  f_p_branch_inverse_holomorphic["Proof that the inverse of a filling parametrisation is holomorphic"]
  f_iwasawa_decomposition__exists_basis_in_finite_domain_trace_mem["A basis from C with trace products in T"]
  f_iwasawa_decomposition__flat_tensor_embeds_tensor_fraction_fields["U tensor C sits inside the tensor of fraction fields"]
  f_iwasawa_decomposition__integral_of_finite_base_change_image["Roots of monic equations over U tensor C are integral over U"]
  f_iwasawa_decomposition__is_unit_map_of_mem_non_zero_divisors_tensor["Non-zero-divisors of U tensor C become invertible"]
  f_iwasawa_decomposition__discr_mul_mem_of_is_integral["One denominator d clears all integral elements of the tensor fraction field"]
  f_divisor_proofs__is_excision_nbhd_self["Excision neighbourhood: the definition, and the trivial case"]
  f_divisor_proofs__is_excision_nbhd_trans["Excision neighbourhoods can be stacked"]
  f_divisor_proofs__is_excision_nbhd_away["Inverting an element that is already invertible mod h keeps an excision neighbourhood"]
  f_divisor_proofs__exists_excision_nbhd_adjoin_root["A unit that is a q-th power mod h gets an exact q-th root in an excision neighbourhood"]
  f_divisor_proofs__exists_pow_sub_mem_span_of_is_unit_mod_of_is_alg_closed["Over an algebraically closed field, a unit mod f is a q-th power mod f"]
  f_unit_power_on_excision_neighbourhood["A unit with a coprime numerator and denominator becomes a q-th power on an excision neighbourhood"]
  f_coprime_unit_etale_extension["Restatement: the unit-power result on an excision neighbourhood"]
  f_is_integral_of_is_idempotent_elem["Idempotents over a smooth algebra come from the algebra itself"]
  f_exists_idempotent_tmul_one_eq_of_smooth_algebra["Restatement: idempotents of the fibre over the fraction field come from A"]
  f_range_comap_include_right_field["Which primes come from a tensor product with a field"]
  f_closure_generic_fibre_clopen_split["Splitting the generic fibre into two separated pieces splits the whole space"]
  f_smooth_generic_fibre_closure_partition["The same splitting statement, for schemes instead of rings"]
  f_is_open_connected_component_of_is_locally_noetherian["In a locally Noetherian scheme, connected components are open"]
  f_section_mem_component_generic_of_closed_valuation["A section that meets the right component at the closed point does so at the generic point"]
  f_adelic_hermitian_forms__adelic_pair["Vocabulary file for the adelic and Hermitian-form arguments"]
  f_exists_is_hermitian_log_of_pos_def_gram["Every invertible matrix x has a Hermitian log for x-star times x"]
  f_is_closed_is_hermitian_log_of_pos_def["The set of pairs (H, A) with H a Hermitian log of A is closed"]
  f_matrix_entries_bounded_of_hermitian_log_trace_sq_le["A small energy forces the entries of x and its log to be small"]
  f_entries_bounded_of_conj_spanning_bounded["If all conjugates of a spanning family stay small, the conjugating matrix is bounded"]
  f_exists_energy_min["A best basis exists that minimises the Hermitian-log energy"]
  f_foundations__pet_eq_rel_index_mul_pet_prod["Level group, Hecke operators and Petersson sum (definitions)"]
  f_cusp_form_gamma1_inter_gamma0_slash_rat_is_zero_at["Moved cusp forms still vanish at cusps"]
  f_foundation_proofs__hecke_u_operator_explicit_eq_sum_slash["The U operator is a sum of q matrix moves"]
  f_foundation_proofs__hecke_u_operator_explicit_slash_invariant_gamma1_inter_g_statement["U keeps level symmetry (restated)"]
  f_foundation_proofs__hecke_u_operator_explicit_slash_invariant_gamma1_inter_gamma0["U preserves level-group symmetry"]
  f_is_zero_at_finset_sum["U sends cusp forms to cusp forms"]
  f_foundation_proofs__mdifferentiable_hecke_operators_explicit["Hecke operators keep functions holomorphic"]
  f_exists_det_ne_zero_of_rows_separating["Rows that pin down every vector contain a nonzero determinant"]
  f_mem_sq_localization_of_pderiv_mem["Vanishing slopes force vanishing to second order"]
  f_exists_mul_mem_of_forall["Minimal generators of a prime, seen locally"]
  f_exists_minimal_local_generators["Minimal local generators (forwarding file)"]
  f_exists_generic_jacobian_data_of_prime["A prime always has generators with an invertible Jacobian"]
  f_exists_generic_jacobian_data_iterated["Invertible Jacobian for polynomials in two groups of variables"]
  f_divisors__xi_mul_nu["Teichmuller identities and the Datum structure (definitions)"]
  f_divisor_base__sandwich_maps["Eigenspace lattices and the unproved LemmaDet statement"]
  f_determinant_lattice_principal["The determinant lattice is generated by one vector"]
  f_divisor_proofs__eigen_projection_quotient_lattice["Projecting onto one eigenspace"]
  f_divisor_proofs__exists_spanning_image_lattice["Integer vectors map onto the lattice spanned by h vectors"]
  f_exterior_power_span_of_lattice["Wedges of lattice vectors come from wedges of generators"]
  f_exterior_power_top_finrank_one["The top wedge power is a line, with a nonzero generator wedge"]
  f_rank_one_lattice_span_singleton["A lattice in a line has a single generator"]
  f_splits["Definitions of the ring conditions used by the block-decomposition lemmas"]
  f_absolutely_closed_polynomial_splits["If every monic polynomial has a root, every monic polynomial splits fully"]
  f_absolutely_closed_unit_coefficient_root["Polynomial with constant term 1 and one unit coefficient has a root"]
  f_polynomial_roots_of_closed_quotient["Divisors of powers of varpi are units times i-th powers"]
  f_newton_polygon_slope_existence["A first Newton-polygon slope exists in a divisibility-chain ring"]
  f_newton_approximation_of_dichotomy["One Newton step improves an approximate root by a power of varpi"]
  f_valuation_add_pow_sub_le["(y + b)^p minus y^p minus b^p is small when p is small"]
  f_valuation_sub_one_pow_eq_prime["Size of zeta minus 1, to the power p - 1, equals size of p"]
  f_exists_improved_approx_kummer_generator["One step improves an approximation to a Kummer generator"]
  f_kummer_generator_approx_critical_radius["A Kummer generator can be approximated down to a critical radius"]
  f_kummer_automorphism_moves_integers_almost_unit["A Kummer symmetry moves some small element by almost a full unit"]
  f_orbital_bounds_conclusion__sigma_star_uniq["Uniqueness of the lattice function, named version"]
  f_period_integrals__sigma_star_uniq["Statement: the lattice function is unique"]
  f_coef_shift["Fourier coefficients and shifting by a lattice step"]
  f_complete["Definitions: Fourier coefficient, completeness, shifted-function setup"]
  f_siegel_set_completeness["A smooth repeating function with all Fourier coefficients zero is zero"]
  f_siegel_set_shift_invariance["Sliding the Fourier averaging path does not change the coefficient"]
  f_sigma_star_uniq_of["The lattice function is unique, given the area formula"]
  f_zero_of_coef["Two lattice functions with the same rules are equal"]
  f_hecke_u_operator_preserves_modular_form_gamma1_inter_gam_statement["U operator keeps modular forms modular (restated)"]
  f_hecke_u_operator_preserves_modular_form_gamma1_inter_gamma0["U operator keeps modular forms modular"]
  f_slash_rat_is_bounded_at_gamma1_inter_gamma0_level["Moving a modular form by a rational matrix keeps it bounded at cusps"]
  f_unit_eq_mul_pow_on_etale_excision_nbhd_zero_locus["Fixing a unit to be a q-th power times a given unit, near a zero locus"]
  f_q_act_m_sub_algebra_map["Definitions: the subspace cut by a character, and the action on the quotient"]
  f_character_augmentation_subspace_top_eq_ker_smul["The character subspace equals the augmentation ideal times the whole space"]
  f_character_augmentation_subspace_top_eq_ker_smul_statement["Character subspace equals kernel times whole space (restated)"]
  f_exists_idempotent_local_of_character["A character picks out a local piece of a finite algebra"]
  f_exists_idempotent_local_of_character_statement["Local idempotent for a character (restated)"]
  f_finrank_quot_one_sub_idempotent_eq_mul["Dimension of a quotient by an idempotent, as a product"]
  f_finrank_quot_one_sub_idempotent_eq_mul_statement["Dimension of a quotient by an idempotent (restated)"]
  f_weight_space_iff_idempotent_fixed["Generalised eigenspace equals the vectors fixed by the idempotent"]
  f_weight_space_iff_idempotent_fixed_statement["Weight space equals idempotent-fixed vectors (restated)"]
  f_finrank_weight_space_projective_tensor_eq["Dimension of a weight space factors as a product"]
  f_adjoin_inverse_is_localization_away["Adding the inverse of g to a ring of numbers is the localization at g"]
  f_kaehler_basis_tower["Bases of differentials combine along a tower of smooth rings"]
  f_kaehler_finrank_fraction_field["Differentials over fraction fields have the expected dimension"]
  f_localization_kaehler_prime_ideal["Vanishing conditions survive renaming variables and passing to a bigger ring"]
  f_kaehler_rank_localization_bound["Differentials after inverting one element give a basis one rank larger"]
  f_exists_nat_mul_mem_range_pi_quotient_minimal_primes["One whole number clears all mixed-up residues at the minimal primes"]
  f_is_of_fin_order_of_is_of_fin_order_map_ring_hom["Finite order descends along an injective ring map with bounded denominators"]
  f_pic_is_of_fin_order_of_finite_int["Picard classes of an integral domain finite over the integers have finite order"]
  f_pic_pi_is_of_fin_order["Picard classes of a finite product of rings are of finite order if each factor's are"]
  f_is_of_fin_order_pic_of_is_reduced_finite_int["Picard classes of a reduced ring finite over the integers have finite order"]
  f_toroidal_compactification__is_completed_strict_hens["Vocabulary for schemes over a ring, and the 'completed strict henselisation' bundle"]
  f_represents_kill_ideal["Properties of ring maps that are 'exactly killing an ideal'"]
  f_ideal_represents_of_away_cover["Glue 'represented by an ideal' from a cover by basic pieces"]
  f_ideal_represents_of_away_cover_statement["Restatement of gluing 'represented by an ideal' (cover by basic pieces)"]
  f_exists_basic_open_cover_ideal_represents["Locally represented properties are represented on a cover by basic opens"]
  f_exists_basic_open_cover_ideal_represents_statement["Restatement of the basic-open cover result"]
  f_ideal_killed_by_ring_maps_with_property_le_ker_app["A point with the property is killed by the kill ideals"]
  f_ideal_killed_by_ring_maps_with_property_le_ker_app_statement["Restatement of 'points with the property are killed by the kill ideals'"]
  f_affine_point_property_of_le_ker_app["Killing the ideals is enough to have the property"]
  f_is_closed_of_local_ideal_point_property["A local, ideal-cut-out property of points is represented by a closed subscheme"]
  f_diamond_operator_of_matrix_modular_form_gamma1_inter_gam["The diamond operator keeps modular forms at the same level"]
  f_gamma1_inter_gamma0_modular_form_has_sum_q_expansion["A modular form of this level equals its q-series"]
  f_has_sum_hecke_u_operator_explicit["The U operator keeps every q-th coefficient"]
  f_has_sum_hecke_v_operator_explicit["The V operator spreads the coefficients out by a factor q"]
  f_q_expansion_coeff_period_one_eq_of_has_sum["A convergent q-series gives the true Fourier coefficients"]
  f_q_expansion_coeff_hecke_t_operator_gamma1_inter_gamma0["The coefficients of the Hecke operator T"]
  f_adelic_hermitian_forms__is_herm_hyperbolic["Hermitian forms, unitary matrices and transvections, with the hyperbolic example"]
  f_existence_of_lattices__hat1["Definitions for lattices over the finite adeles"]
  f_exists_nsmul_mul_vec_mem["One whole number clears the denominators of a matrix acting on a lattice"]
  f_adelic_lattice_proofs__imports_ter["One whole number pulls any vector into a spanning lattice"]
  f_adelic_lattice_proofs__transvection_identities_unitary["Rules for computing with transvections"]
  f_exists_trace_zero_adjustment_of_hermitian_lattice["Nudging a transvection parameter so the lattice is almost preserved"]
  f_unitary_transvection_submonoid_adjust_integral_away["Every product of transvections can be approximated by one keeping the lattice integral"]
  f_homogeneous_ideals__exists_ring_equiv_of_is_transcendence_basis["Symmetries of polynomial rings extend to symmetries of algebraically closed fields"]
  f_adelic_lattice_proofs__exists_ring_equiv_apply_ne_of_is_algebraic["An irrational algebraic complex number is moved by some symmetry of the complex numbers"]
  f_adelic_lattice_proofs__exists_ring_equiv_ne_of_transcendental["A transcendental complex number is moved by some symmetry of the complex numbers"]
  f_adelic_lattice_proofs__exists_rat_of_forall_complex_ring_equiv_fixed["A complex number fixed by every ring symmetry of the complex numbers is rational"]
  f_adelic_lattice_proofs__galois_stable_submodule_le_span_rational["A symmetry-stable subspace is spanned by its rational-coordinate vectors"]
  f_mem_span_rational_kronecker_invariants["Invariant tensors under a symmetric set of matrices have a rational spanning set"]
  f_convex_nerve_complexes__nerve_face_closed["Definitions - tuples, boundary map, 'no holes', the nerve"]
  f_alt_double_sum["Boundary of a boundary is zero"]
  f_bd_mem["Boundaries stay inside a face-closed family"]
  f_acyc_cone["A cone point makes a family hole-free"]
  f_acyc_directed["Hole-free on every finite piece means hole-free"]
  f_acyc_union["Gluing two hole-free pieces along a hole-free overlap"]
  f_nerve_cut["Cutting a convex set by a hyperplane splits its nerve"]
  f_nerve_sep["Finding a separating cut when no common point exists"]
  f_nerve_compact["Nerve of a compact convex set is hole-free"]
  f_nerve_convex["Nerve of a convex cover is hole-free (nerve lemma)"]
  f_pow_form["Definitions for a Gaussian convolution series"]
  f_divisor_proofs__poly_mul_gaussian_bounded["A polynomial times a Gaussian is bounded"]
  f_gaussian_iterated_f_deriv_weighted_exp_bounded["Derivatives of a Gaussian, weighted, stay bounded"]
  f_norm_gaussian_convolution_series_coefficient_le_integr["A coefficient is at most an absolute-value integral"]
  f_norm_iterated_f_deriv_multilinear_diagonal_le["Derivative bound for a polynomial-like form on the diagonal"]
  f_gaussian_convolution_series_coefficient_desc_factoria["Pointwise estimate for coefficient times a factorial ratio"]
  f_summable_seminorm_gaussian_convolution_series_term["The Gaussian convolution series converges in every seminorm"]
  f_nonempty_alg_hom_adjoin["A map defined on a subring extends after clearing a denominator"]
  f_adjoin_hom_extend_of_denominator["Restatement - extending a map by clearing a denominator"]
  f_extend_alg_hom_adjoin_integral_root["Extending a map by sending a root to a root"]
  f_is_integrally_closed_adjoin["Polynomial rings are integrally closed; evaluating away zeros"]
  f_linear_indep_on_pow_of_is_domain_tensor_purely_inseparabl["In characteristic p, p-th powers keep independence"]
  f_exists_primitive_element_separability_certificate["A single generator with a separability certificate"]
  f_exists_finite_separable_point_of_separable_closure_poin["A point over the separable closure lives in a finite separable field"]
  f_exists_separable_point_of_geometrically_domain["Geometrically integral algebras have a separable point"]
  f_divisors__has_q_iff["Definitions for q-expansions, plus an equivalent form"]
  f_divisors__zeta_act_refl["Definitions for torsion-point series and their coefficients"]
  f_root_of_unity_exp_z_mod_additive_character_properties["Roots of unity form a character of the integers mod N"]
  f_tsum_residue_class_split_by_sign["Splitting a sum over one residue class into signs"]
  f_has_sum_lambert_double_series_divisors["Lambert-type double series equals a divisor-sum series"]
  f_torsion_point_row_sum_eq_q_expansion_series["One row of a lattice sum equals a q-series"]
  f_torsion_point_rows_sum_eq_divisor_series["Summing all rows gives a divisor-sum q-series"]
  f_hermitian_local_continuous_congruence_section["In a Dedekind domain, high powers of P clear a multiple of f"]
  f_dedekind_power_localization["Restatement - high powers of P clear a multiple of f"]
  f_divisor_proofs__tensor_involution_algebra_properties["Flat extensions - divisibility upstairs descends downstairs"]
  f_flat_localization_membership["Restatement - divisibility descends along a flat extension"]
  f_gram_fiber_measures_unique_ae["Elements outside P become units modulo f after inverting g"]
  f_localization_inverse_mod_f["Restatement - inverses modulo f after inverting g"]
  f_primitive_vector_quadratic_level_measure["Residue approximation survives inverting g"]
  f_localization_residue_approximation["Restatement - residue approximation after inverting g"]
  f_divisor_proofs__local_hermitian_diagonalization_units["Approximation mod I lifts to approximation mod K when I to the N is small"]
  f_nilpotent_approximation_surjective["Restatement - lifting approximation past a nilpotent ideal"]
  f_etale_unique_prime_le_map_maximal["Etale extensions - a lone prime over P is inside P extended"]
  f_isolate_maximal_among_primes_containing_etale["Isolating one maximal ideal among primes containing f"]
  f_etale_away_quotient_eq_localization["Quotient by f equals a localization, for etale extensions of a Dedekind domain"]
  f_commuting_semisimple_eigenspaces_span["Commuting diagonalisable maps share a basis of eigenvectors"]
  f_dvr_rep_eigenspaces_span_top["A p-adic ring acting by matrices has eigenvectors spanning everything"]
  f_exists_ring_hom_of_joint_eigenvalue["A shared eigenvalue pattern is really a ring map into the integers"]
  f_exists_separable_annihilating_poly["Every element is killed by a polynomial with no repeated roots"]
  f_padic_ring_hom_unique_adic_complete["Only one ring map from the p-adic integers into a p-adically complete ring"]
  f_ring_hom_from_padic_unique_of_sep["Ring maps from the p-adic integers agree when p-power divisibility separates points"]
  f_scalar_rep_commute_and_annihilate["A matrix action that is scalar on a subring gives commuting maps killed by polynomials"]
  f_period_integrals__add_int_g["Integrality of the addition law for formal groups of elliptic curves (statement)"]
  f_period_integrals__exp_int_w["Exponentials of integral series stay integral (statement)"]
  f_period_integrals__inv_ser_sub["Substitution and inversion keep coefficients in a ring (statements)"]
  f_exponential_integrality__development["Exponential integrality follows from two steps"]
  f_exponential_integrality__inv_nat_cast_mem_witt_integers["The inverse of a number prime to p lies in the Witt-type ring"]
  f_roots_of_unity_ring_le_witt_integers["Dividing a small element of the Witt-type ring by p stays inside it"]
  f_step_i_i_i["Bounded denominators plus size at most 1 puts a number in Wp"]
  f_flog_constant_coeff["Multiplying by an integer-like constant preserves integrality (conditional)"]
  f_w2pair["Multiplication by a constant on a formal group, and the pair-of-Frobenius ring (statements)"]
  f_wf_ring["Series with bounded p-denominators form a ring (statement)"]
  f_wf_subst["Substituting one series into another keeps coefficients in the ring (statements)"]
  f_divisor_proofs__div_fractions_bilinear_formula["Averages over the sphere do not change when the matrix is rotated"]
  f_fibre_cosine_explicit_formula["Cosine and density in explicit Möbius form"]
  f_fibre_cosine_pushforward_uniform["The cosine is uniformly distributed on 0 to 1"]
  f_divisor_proofs__fs_one["Definitions of the norm, cosine and density for a 2 by 2 matrix"]
  f_divisor_proofs__h_poly_add_two["Definitions behind the sphere average, and a three-term recursion"]
  f_divisor_proofs__mobius_change_of_variables["A Möbius change of variables on the plane, with the right Jacobian weight"]
  f_divisor_proofs__stereographic_measure_change["The sphere density pushes forward to a uniform measure on 0 to 1"]
  f_period_integrals__primes_dyadic_r_s["Many primes between y and 2y (statement)"]
  f_period_integrals__sqf_lab["Labelled polynomials over a finite field and their bad-case conditions (definitions)"]
  f_sqf_prime_factor["Most polynomials have a big prime-degree factor (statement)"]
  f_ana_core["The numerical inequality that closes the counting argument"]
  f_squarefree_prime_factor__analytic["The numerical inequality holds, given the prime-gap claim"]
  f_big_primes["Counting definitions for degree-d polynomials over a finite field"]
  f_squarefree_prime_factor__claim_of["Three counting claims together give the prime-factor claim"]
  f_irreducible_count_lower_bound["Many irreducible polynomials of prime degree over a finite field"]
  f_monic_deg_fn_nat_degree["Facts about monic polynomials of fixed degree over a finite field"]
  f_sqf_prime_factor_of["The prime-factor claim, given the prime-gap claim"]
  f_squarefree_count_estimate["Counting polynomials with a big irreducible factor"]
  f_commutative_algebra__dual_order["Restricting, quotienting and dualising orders in function algebras (definitions)"]
  f_commutative_algebra__models["A finite flat group scheme models a function algebra (definition)"]
  f_commutative_algebra__translate_mem_ind_order["Orders in function algebras, and operations on them (definitions)"]
  f_global_geometry__exists_unit_form_localization_etale_nbhd["Quasi-finite flat group schemes with marked points, and regular functions (definitions)"]
  f_base_change_points_compat["Base change respects the marked points at the generic point"]
  f_regular_at_base_change["Regular functions stay regular under base change"]
  f_htat_bc_pull["Pulling a regular section back along base change"]
  f_p_adic_hodge__finite_flat["Finite flat group schemes as Hopf algebras"]
  f_global_twisting__perm_rep_single["Spreading a representation over the points of a set"]
  f_exists_free_resolution_short_exact["Every representation is a quotient of a free one"]
  f_group_homology_dimension_shift_is_iso["Dimension shifting: an iso one level down gives an iso one level up"]
  f_group_homology_long_exact_maps_natural_of_res["Group homology maps commute with the long exact sequence"]
  f_perm_coef_preserves_short_exact["Spreading over points keeps exact sequences exact"]
  f_projective_perm_tensor_free["A free representation spread over a set is still projective"]
  f_projective_rep_group_homology_pos_vanishes["Projective representations have no higher group homology"]
  f_projective_res_free_rep_of_injective["Restricting a free representation to a subgroup keeps it projective"]
  f_shapiro_is_iso_group_homology_zero["Shapiro's lemma in degree 0"]
  f_shapiro_lemma_transitive_group_homology["Shapiro's lemma for a transitive action"]
  f_witt_exact_sequences__is_compl["Vocabulary for perfect rings, covers and solvable systems"]
  f_cov_of_alg_hom["The covering property passes along ring maps"]
  f_block_decomposition__exists_fg_tmul_eq_zero["A vanishing in a tensor product involves only finitely many equations"]
  f_block_decomposition__exists_perfect_radical["Building a perfect ring from a ring of characteristic p"]
  f_block_decomposition__exists_p_q["Every characteristic-p ring has a perfect quotient"]
  f_block_decomposition__exists_ring_hom_pow_prime_pow["In characteristic p, raising to the p^k-th power respects sums"]
  f_block_decomposition__pf_facts["Basic facts about perfect rings"]
  f_block_decomposition__perfect_frobenius_root_solution["Solving a system after taking p-power roots of the coefficients"]
  f_block_decomposition__frobenius_power_solution_lift["Lifting a solution from a perfect quotient, up to p-powers"]
  f_block_decomposition__one_tmul_mem_range_iff["A criterion for membership in a base-changed image, and a covering criterion"]
  f_exists_retraction["Adjoining a root of a monic polynomial keeps a perfect, covering extension"]
  f_global_geometry__is_cpt_gen["Vocabulary: points above a generic point, and where numbers are regular"]
  f_global_geometry__coords_at["Vocabulary: coordinates that are well behaved at a point"]
  f_global_geometry__etale_localization_at_prime_tensor_of_low_height["Vocabulary: lattices at every point and frames"]
  f_global_geometry__exists_gen_of_is_v_b_one["A rank-one lattice has a local generator, plus order-of-vanishing tools"]
  f_global_geometry__is_generic_flag["Vocabulary: flags and generic flags"]
  f_global_geometry__is_line_gen_on["Vocabulary: when two wedge powers share a line"]
  f_global_geometry__level_sections_exact_kernel_locus_open["Vocabulary: exactness modulo a number, and the line lattice"]
  f_geometry_proofs__gen_map_germ_eq_gen_map_germ["Being regular at a point spreads to a neighbourhood"]
  f_frame_near_generic_point["A basis that frames the generic point frames a whole neighbourhood"]
  f_additive_poly_taylor_coeff_sub_norm_le["Shifting an additive polynomial barely changes its coefficients"]
  f_few_roots_small_disc["An additive polynomial has few roots in a small disc"]
  f_multiset_many_separated_points["A crowded list contains many well-separated points"]
  f_separated_roots_additive_poly["An additive polynomial has many well-separated roots in the unit disc"]
  f_commutative_algebra__invariant_subspace_mobius_inverse_rec_eq_of_finrank_lt["Vocabulary for class functions on matrices, plus a recursion over invariant subspaces"]
  f_character_theory__charpoly_block_and_invariant_under_stabilizer_nilradic["The characteristic polynomial of a block-triangular map is the product of its blocks"]
  f_exists_perm_of_sum_min_eq_positive_family["Two lists with the same 'capped sums' are rearrangements of each other"]
  f_primary_endomorphism_cyclic_decomposition_finrank_ker["A primary linear map splits into cyclic blocks, with computable kernel sizes"]
  f_conj_of_primary_finrank_ker_pow_eq["Primary maps with equal kernel sizes are conjugate"]
  f_ker_aeval_add_stabilizer_nilradical_socle["Adding a nilradical element can only grow the kernel"]
  f_primitive_end_class_function_eq_zero_of_primary["A primitive class function vanishes if it vanishes on the 'simplest' primary maps"]
  f_block_decomposition__perfect_tensor_product["Tensoring perfect rings gives a perfect ring"]
  f_block_decomposition__pq_lift["Maps out of a 'perfected quotient' are determined uniquely"]
  f_block_decomposition__perfect_tensor_generated_lift["The perfected-quotient property survives base change"]
  f_pq_base_change_polynomial["The perfected-quotient property for polynomial rings, base-changed"]
  f_valuation_at_centre_order["Order of a function at a point gives its valuation power"]
  f_order_valuation_compare["Order versus valuation (restated)"]
  f_character_theory__card_subspaces_of_finrank_mul_card_bases["Counting subspaces by counting bases"]
  f_card_subspaces_mul_general_linear_group_card["Subspaces times invertible matrices count"]
  f_endomorphism_mass_eq_of_linear_equiv_invariant["Mass depends only on the dimension, if the weight is basis-free"]
  f_finsum_subspace_stabilizer_mul_block_functions["Summing over maps that preserve a subspace"]
  f_endomorphism_mass_mul_parabolic_induction_trivial["Mass of maps preserving a subspace splits over factorisations"]
  f_real_place_analysis__statement_a["Claims about Casimir operators of gl(n) (statements only)"]
  f_real_place_analysis__statement_b["Claims about trace powers on highest-weight vectors (statements only)"]
  f_real_place_analysis__statement_e["Quantum determinant and RTT relation (statements only)"]
  f_is_top["Polynomial representations of matrices and their Lie action"]
  f_coef_diff["Entries of such a representation are smooth"]
  f_curve["Derivative along a curve through the identity"]
  f_inv_curve["Explicit curves with velocity equal to a unit matrix"]
  f_line_deriv["Intertwining survives differentiation"]
  f_bracket["The Lie action respects commutators"]
  f_gl_rel["The matrix-unit operators obey the gl(n) rules"]
  f_subsingleton_of_adic_completion_tensor["A torsion module with vanishing completed tensor is zero"]
  f_torsion_of_localization_flat["Flatness after inverting f makes kernels f-power torsion"]
  f_quotient_flat_of_completion_flat["Flat after completion implies flat modulo f"]
  f_smul_regular_tensor_of_quotient_flat["Non-zero-divisors survive tensoring when flat mod f"]
  f_localization_projective_kernel_finite["Kernel of a cover has finite localisation, if the localisation is projective"]
  f_completion_flat_kernel_finite["Kernel of a cover is finite after completion, if projective"]
  f_finite_of_localization_and_completion["Finite after localising and completing implies finite"]
  f_finite_projective["Finite projective modules descend from localisation and completion"]
  f_commute_image_abelian_by_prime_power_of_normal_central["Matrices that commute with a big normal piece commute everywhere"]
  f_exists_character_eigenvector_of_commuting_representat["Commuting matrices share an eigenvector, giving a character"]
  f_exists_monomial_basis_abelian_by_prime_power["Abelian-by-prime-power groups act by 'monomial' matrices"]
  f_exists_monomial_basis_of_imprimitive["Monomial basis from a subgroup that shuffles copies of a piece"]
  f_character_theory__imports["Commuting matrices have a common eigenvector"]
  f_invariant_eq_top_of_irreducible["Irreducible actions are either one-dimensional or imprimitive"]
  f_is_abelian_by_prime_power_group_subgroup["Subgroups of abelian-by-prime-power groups are again so"]
  f_complex_analytic_sets__p_manifold_zeros_complement_connected["Proof that removing zeros of an analytic function keeps a smooth shape in one piece"]
  f_p_proper_open_projection_local_cover["Proof of the local cover for proper open projections"]
  f_p_unbranched_proper_count_constant["Proof that the number of sheets is constant over a connected base"]
  f_p_unbranched_proper_count_locally_constant["Proof that the fibre count is locally constant"]
  f_st_proper_open_projection_local_cover["Statement of the local cover for proper open projections"]
  f_st_proper_open_projection_local_unbranched["Statement of the locally unbranched version"]
  f_st_unbranched_proper_count_locally_constant["Statement that the fibre count is locally constant"]
  f_divisor_proofs__etale_localization_at_prime_tensor_of_low_height["Etale-ness survives passing to a bigger ring's localization"]
  f_exists_smul_dvd_of_localization_at_prime_tensor["Divisibility after localizing can be cleared by a unit outside the prime"]
  f_finite_etale_of_galois_descent_hartogs["Descent argument that a Galois-type extension is finite etale"]
  f_finite_of_galois_trace_relation["A trace relation forces the extension to be finitely generated"]
  f_gal_map_gal_elt["The Galois comparison map and a special element"]
  f_galois_comparison_map_injective_of_flat["The Galois comparison map is injective over a flat base"]
  f_galois_element_dvd_of_formally_unramified["Formally unramified forces the special element to be divisible"]
  f_hart_tensor_of_flat["The Hartogs-style division property survives flat base change"]
  f_divisor_proofs__torsion_free_over["Definitions of the Hartogs property, torsion-free and etale-in-low-height"]
  f_algebra_trace_map_of_cokernel_killed_by_scalar["Traces agree when the cokernel is killed by a nonzero scalar"]
  f_discr_is_unit["Etale over a local ring means the discriminant is a unit"]
  f_etale_of_etale_at_height_one_primes["A finite free algebra etale at all height-one primes is etale"]
  f_exists_smul_mem_range_of_surjective_localized_map["Surjective after localizing means surjective up to one denominator each"]
  f_finite_length_coker_of_etale_punctured_spectrum["Cokernel of an etale-away-from-the-point map is killed by a power of the maximal ideal"]
  f_localization_tensor_map_injective_coker_killed["Injectivity and scalar-killed cokernel survive localization"]
  f_smul_mem_of_maximal_ideal_pow_of_locally_surjective["Locally clearable denominators give a power of the maximal ideal"]
  f_surjective_of_trace_of_smul_mem_range["Equal traces and a scalar-killed cokernel force surjectivity"]
  f_commutative_algebra__chain_conn_in_dim["Definitions for connectedness in each dimension, and depth"]
  f_cohen_macaulay__mod_depth_g_e["Definitions of depth and Cohen-Macaulay for modules"]
  f_exists_sq_zero_extend_localization_away_pow["Lifting a map through a square-zero thickening after inverting one element"]
  f_exists_square_zero_lift_basic_open_pair_agree["Lifting a point of a smooth scheme over a thickening, compatibly on two overlapping pieces"]
  f_divisor_proofs__is_affine_combination_in_chart_spec_map_comp["Chart rings and affine combinations behave well under pullback"]
  f_divisor_proofs__is_comb_in["Definitions of a chart ring and an affine combination of maps"]
  f_divisor_proofs__lift_at["Definitions of 'a lift exists over a basic open piece'"]
  f_divisor_proofs__preimage_eq_of_square_zero_thickening["Maps agreeing on a square-zero thickening have the same preimages"]
  f_adelic_hermitian_forms__mem_pow_sub["Subgroups of 'p-th powers' and 'norms' (definitions)"]
  f_adelic_hermitian_forms__sq_sub_le_norm_sub["Squares are norms, and other small definitions"]
  f_adelic_lattice_proofs__pow_index_torsion_ker_range_mul["Counting p-th powers across a group map (index times torsion)"]
  f_rel_index_one_units_mul_eq_card_quotient["Counting units that are 1 modulo t versus 1 modulo st"]
  f_subgroup_pow_image_units_congruent_one_mod_of_is_adic_comp["In a complete ring, p-th powers of units near 1 fill out units nearer to 1"]
  f_subgroup_pow_rel_index_units_of_is_adic_complete["How many cosets of p-th powers in the units of a complete ring"]
  f_global_twisting__mem_split_seq_iff["Split sequences of vectors, and the group acting on them"]
  f_global_twisting__sub_closed["Chains of lists and a boundary map (definitions)"]
  f_link_exactness_stability__seq_chain_boundary_comp_boundary_apply["Taking the boundary twice gives zero"]
  f_split_set_perm_rep_chains_iso_split_seq_chains["The group-representation chains are the same as the list chains"]
  f_split_sequence_rep_complex_exact["Exactness of the split-sequence complex follows from the list version"]
  f_published_theorems__k_acyclic_homology["Five published K-theory claims, stated but not proved"]
  f_tensor_hom_cubes__is_acyclic_space["Acyclic spaces and the plus construction (definitions)"]
  f_tensor_hom_cubes__simplex_face["Cubes to simplices, the Hurewicz map and a number table (definitions)"]
  f_tensor_hom_cubes__stab_directed_system["Padding matrices, GL_infinity and group homology"]
  f_period_integrals__minkowski["Minkowski's bound on finite matrix groups (statement)"]
  f_period_integrals__minkowski_q["Minkowski bound over the rationals (statements)"]
  f_orbital_bounds_conclusion__minkowski["Minkowski's bound proved, by plugging in two steps"]
  f_orbital_bounds_conclusion__minkowski_q["Minkowski's bound over the rationals, proved"]
  f_minkowski_bound__assemble["From prime-power subgroups to the full Minkowski bound"]
  f_charpoly_dvd_of_pow_eq_one["Traces of matrices of prime-power order"]
  f_minkowski_bound_of_steps["Trace step plus power-sum step gives the prime-power step"]
  f_power_sum["The group size divides every power sum of traces"]
  f_power_sum_step["The three steps of Minkowski's argument (statements)"]
  f_minkowski_torsion_free__lattice["Making a finite rational matrix group integral"]
  f_unit_t_zpow["Base change for rings with a Laurent variable"]
  f_haar_transversals__fold_bound["A pointwise bound on sums over a transversal"]
  f_haar_transversals__poincare_series_square_integrable["Square-integrability of Poincare series (statements only)"]
  f_period_integrals__fold_mult["Properties of the overlap-count function (statement)"]
  f_period_integrals__fold_unfold["The unfolding identity (statement)"]
  f_orbital_bounds_conclusion__fold_mult["The overlap-count claim, proved"]
  f_orbital_bounds_conclusion__fold_unfold["The unfolding identity, proved"]
  f_poincare_series_mem_lp["Poincare series are square-integrable, proved"]
  f_measurable_mult["The overlap count is at least 1, finite, invariant and measurable"]
  f_fold_l2_double_coset["Proof that the Poincare series is square-integrable"]
  f_unfolding_identity__fold_unfold_main["Proof of the unfolding identity"]
  f_character_theory__eq_zero_of_not_primary["A class function that is 'primitive' vanishes on non-prime-power matrices"]
  f_character_theory__exists_conj_eq_add_of_is_coprime["Adding a small nilpotent piece to a matrix gives a conjugate matrix"]
  f_finite_monic_nat_degree["Sums over polynomials equal sums over roots of unity"]
  f_is_unit_iff_charpoly_coeff_zero_ne["A matrix inner product becomes a sum over characteristic polynomials"]
  f_invertible_end_inner_product_root_power_sum_eq_torus_sum["Inner product with a root power sum equals a sum over roots of unity"]
  f_inner_product_root_power_sum_eq_of_frobenius_mod_eq["Root power sums agree when the exponents match up to Frobenius"]
  f_exists_integral_hecke_eigensystem_deligne_serre["Deligne-Serre lifting, an integral eigensystem for Hecke operators"]
  f_exists_matrices_intertwining_of_semilinear["Turning a lattice action into integer matrices"]
  f_finite_joint_eigensystems["Commuting matrices have only finitely many joint eigenvalue lists"]
  f_matrix_exists_common_eigenvector_mem["Commuting matrices share an eigenvector inside any stable subspace"]
  f_norm_eigenvalue_le_one_of_entries["Eigenvalues of a matrix with small entries are small"]
  f_dvd_trace_of_balanced_tensor["A balanced tensor forces the trace to be a multiple of c"]
  f_finite_open_le_closed_fibre["An open piece that is finite over a local ring is decided by its closed fibre"]
  f_is_fin_open_sub_of_finite["A finite open part of a group scheme containing the closed fibre is a finite open subgroup-like piece"]
  f_hodge_tate_points__val_at_restrict["Evaluating sections at points, and the finite-over-local-ring lemma"]
  f_geometry_proofs__coord_tie_comp_equiv["Reordering the coordinates keeps a coordinate system valid"]
  f_geometry_proofs__germ_gen_pt_injective_range_reg_at["Sections on an open set are exactly the common regular values at its points"]
  f_piece_localization_at_element["Inverting an element of a piece gives another piece"]
  f_geometry_proofs__prod_update_div["Pieces, adjoining an inverse, and a product-ratio identity"]
  f_reg_at_is_local_ring_is_fraction_ring_stalk["The regular elements at a point form a local ring with the field as its fractions"]
  f_exists_kill["Killing finitely many equations at once in a ring that is p-power-friendly"]
  f_c_m_moduli__projective_space_over_spec["Projective space over a ring, and the real-to-complex example"]
  f_divisor_proofs__closure_finite_etale["Definitions - the integral closure being finite etale, and 'Good'"]
  f_etale_away_of_is_etale_at_off_submonoid["Etale away from a set implies etale after inverting one element"]
  f_divisor_proofs__etale_localization_at_prime_is_domain_is_integrally_clos["Etale over a normal domain gives normal domain local rings"]
  f_divisor_proofs__good_iff_etale_at["Good unpacked as etale at each prime plus a point at zero"]
  f_divisor_proofs__origin_ideal["Definitions - a cyclic-group torsor, and the origin ideal"]
  f_divisor_proofs__point_at_zero["Definitions - 'Fits', 'Retracts' and 'PointAtZero'"]
  f_divisor_proofs__torsors_trivial["Claims - every cyclic torsor is trivial (stated, not proved)"]
  f_divisor_proofs__zmod_torsor_exists_point_finite_separable["A cyclic torsor has a point over a finite separable field extension"]
  f_homogeneous_ideals__is_domain_and_is_integrally_closed_at_prime_of_smooth_of_co["Smooth over a normal base gives normal local rings"]
  f_eval_complex_poly_eq_zero_on_rat_zariski_closure["Complex equations vanishing on a Galois-stable set vanish on its rational closure"]
  f_adelic_lattice_proofs__mem_span_rat_polys_vanishing_of_aut_stable["A vanishing complex polynomial is a combination of rational ones"]
  f_coords_left_mul_matrix_const_base_change["Coordinates and multiplication matrices are unchanged by base change"]
  f_exists_is_q_group_weil_restriction["Weil restriction of a matrix group is a group defined over the rationals"]
  f_exists_rational_coord_polynomial_base_change["Coordinates of a polynomial value are rational polynomials in the coordinates"]
  f_exists_rational_equations_weil_restriction["Rational equations describing the Weil restriction"]
  f_gl_free_algebra_to_special_linear_emb_injective_hom["Embedding invertible matrices into determinant-one matrices"]
  f_mem_rat_zariski_closure_points_iff_of_is_reduced["Points of the rational closure are solutions, in a reduced ring"]
  f_restrict_scalars_matrix_of_basis_hom_injective_is_unit["Replacing matrix entries by multiplication matrices keeps the algebra"]
  f_foundations__curve_cl["Definitions - polynomials for flag-variety degree computations"]
  f_exists_class_degree_one["A polynomial pairing to exactly one with the low power sum"]
  f_limits_of_shift_functionals["Two coefficient sequences converge if their combination does"]
  f_shift_functional_power_sum["How the shift and total functionals act on a power sum times Q"]
  f_degree_formula__flag_deg_formula["The degree functional, and the flag degree formula (stated, not proved)"]
  f_point_degree__perm_exp_inj["The 'point' degree equals one, so the staircase is normalized"]
  f_point_degree__pow_sum["The degree functional kills power sums, and vanishes off the top degree"]
  f_etale_localization_at_prime_tensor_of_etale_away["Etale after inverting b gives etale after localizing at a prime missing b"]
  f_corank_share__statement_f_r["Statements about averages and families of subspaces"]
  f_eichler_equivalence_holds["Eichler transformations are reversible and preserve the form"]
  f_has_deriv_at_sphere_chart_last["Splitting sums over subsets by the last coordinate"]
  f_lf_prod["A prime sits under at most degree-many prime ideals"]
  f_neighbourhood_hilbert_schmidt_holds["Trace formulas for sums of frame operators"]
  f_kernel_bound_rel["Collecting the six proven kernel-bound ingredients"]
  f_statement_c_s["Statements about kernel bounds and character sums"]
  f_statement_e_i["Statements about Eichler transformations"]
  f_statement_f_u["Statements about frames, projections and compression"]
  f_statement_l_f["Statements about products over places, box counts and prime ideals"]
  f_statement_m_v["Statements about a kernel built from moves"]
  f_statement_n_c["Statements about counting solutions of norm equations"]
  f_statement_s_b["Statement of an n-dimensional Sobolev inequality"]
  f_character_theory__character_coset_sum_eq_zero_of_subgroup_sum["A character summing to zero on a subgroup sums to zero on every coset"]
  f_exists_standard_unipotent_radical_bij_on_nilradical["A standard block-triangular subgroup matching the nilradical"]
  f_general_linear_function_extend_zero_end_properties["Extending a function on invertible matrices by zero"]
  f_is_primitive_extend_zero_of_sum_unipotent_radical["Vanishing sums on unipotent subgroups make the extended character primitive"]
  f_p_number_field_box_count_x["Closing the proof of the number-field box count"]
  f_heights__kernels_lattice["Hermitian lattices over number fields, degree and slope"]
  f_p_covolume_rel_index["Covolume of a sublattice equals index times covolume"]
  f_p_embedding_sum_places["Summing over embeddings equals summing over places with multiplicity"]
  f_p_lattice_count_volume["Volume of a set is at most lattice points in a difference set times covolume"]
  f_p_lattice_image_z_lattice["A full additive subgroup of a number field becomes a lattice"]
  f_p_mixed_box_count["Counting lattice points in a box in the mixed space"]
  f_p_number_field_box_count["Number-field box count, assuming four earlier claims"]
  f_statements_covolume_rel_index["Statement that covolume scales with index"]
  f_statements_embedding_sum_places["Statement about summing over embeddings and places"]
  f_statements_lattice_count_volume["Statement that volume is bounded by lattice points times covolume"]
  f_statements_lattice_image_z_lattice["Statement that a number-field subgroup maps to a lattice"]
  f_statements_mixed_box_count["Statement of the mixed-space box count"]
  f_statements_number_field_box_count["Statement of the number-field box count"]
  f_card_step["Sizes multiply along an exact sequence"]
  f_torsion_bounds_chains__face_d_single["Vocabulary for homology size bounds"]
  f_fin_group["Size bound for homology of a finite group"]
  f_group_homology_long_exact["The long exact sequence for group homology"]
  f_torsion_bounds_chains__imports_alt["Higher homology of a finite group is killed by its order"]
  f_ind_perm["Induced module from the stabilizer is the permutation module"]
  f_map_nsmul["A factorisation through zero homology forces n times zero"]
  f_orb_step["Splitting off one orbit"]
  f_perm_card["Size bound for homology of a permutation module"]
  f_perm_empty["Empty permutation module has trivial homology"]
  f_perm_split["Short exact sequence from splitting a set into two pieces"]
  f_perm_trans["Size bound for homology of a transitive permutation module"]
  f_torsion_bounds_chains__shapiro["Shapiro's lemma for a transitive action"]
  f_subquot["A quotient of a lattice subgroup killed by n is small"]
  f_torsion_bounds_chains__transport["Size bounds are preserved by isomorphism and weakening"]
  f_period_integrals__prime_count["Statement of a prime-counting upper bound"]
  f_chebyshev_prime_bounds__log_factorial_eq_sum_of_le["Counting prime powers in factorials, and the psi sandwich"]
  f_chebyshev_prime_bounds__log_factorial_le["Stirling-type bounds on the log factorial and on D(x)"]
  f_chebyshev_prime_bounds__prime_count_bound_of["Definitions for Chebyshev bounds and the split prime-count bound"]
  f_chebyshev_prime_bounds__psi_lower_bound_holds["Chebyshev's psi bounds, assembled"]
  f_chebyshev_prime_bounds__psi_upper_bound_of_lt_thirty_mul_six_pow["Proving the psi upper bound by induction on scale"]
  f_claim_of_two["Prime counts in (y, 2y], assuming two inputs"]
  f_floor_half["Many primes between y and 2y"]
  f_theta_diff["Statements for the dyadic prime-interval argument"]
  f_wedge_line_lattice_vector_bundle["Wedge-ratio line lattice is a vector bundle (restated)"]
  f_line_lattice_vector_bundle["Ratio of two wedge lattices forms a line bundle"]
  f_complex_analytic_sets__st_zariski_analytic_normality["Germs of analytic functions, and normality statement"]
  f_complex_analytic_sets__st_analytic_germs_noetherian["Statement - rings of analytic germs are Noetherian"]
  f_complex_analytic_sets__st_germ_weierstrass_division["Statement - Weierstrass division for analytic germs"]
  f_complex_analytic_sets__st_germ_general_coordinates["Statement - a generic change of coordinates makes a germ regular"]
  f_complex_analytic_sets__p_analytic_germs_noetherian["Analytic germ rings are Noetherian, assuming two facts"]
  f_complex_analytic_sets__st_prime_germ_nullstellensatz["Statement - Nullstellensatz for prime analytic germ ideals"]
  f_complex_analytic_sets__st_prime_germ_primitive_presentation["Statement - a prime germ has a primitive-element presentation"]
  f_st_finite_germ_projection_objects["What a finite projection of a germ ideal is"]
  f_st_prime_germ_projection_step["Statement - the induction step for finite projections"]
  f_st_germ_projection_function_form["Statement - finite projections give explicit function formulas"]
  f_complex_analytic_sets__st_prime_germ_finite_projection["Statement - prime germs have a finite projection"]
  f_p_prime_germ_finite_projection["Prime germs have finite projections, from two assumed steps"]
  f_real_place_analysis__complexify["Sign matrices, indefinite unitary groups and related claims"]
  f_pf_d["Definitions for interlacing partial fractions"]
  f_partial_fraction_diagonal_identity["Partial fraction identity at each root"]
  f_partial_fraction_off_diagonal_identity["Partial fraction identity for two different roots"]
  f_partial_fraction_square_identity["Partial fraction identity with squared denominators"]
  f_exists_unitary_interlacing_realization["Realising interlacing numbers by a matrix that preserves a signed form"]
  f_smith_zp["Smith normal form over the p-adic integers"]
  f_mahler_measure__statement["Mahler measure toolkit, part 1 (statements only)"]
  f_mahler_measure__statement_b["Mahler measure toolkit, part 2 (statements only)"]
  f_mahler_measure__statement_d["Mahler measure toolkit, part 3 (statements only)"]
  f_defs_d_v_r["Chaining the discrete-valuation-ring size bounds"]
  f_defs_gram["Gram determinant bounds, how the pieces assemble"]
  f_smith_exists["Smith normal form for a map on a free module"]
  f_statement_d_v_r["Smith data and size bounds over a DVR (statements only)"]
  f_smith_determinants__statement_gram["Gram determinants of factorial-weighted polynomials (statements)"]
  f_truncation_chain_bound_nonneg_exponents["Smith form existence (alias)"]
  f_closure_prime_regular_height["Etale at primes avoiding nonzero base elements (restated)"]
  f_counting_bound["The closure is etale at primes away from the base"]
  f_dixmier_schur_of_rank_le_aleph0["Schur's lemma for countable-size complex spaces"]
  f_operator_stable_pi_tensor_pure_kernel_span["Product of stable pieces stays stable"]
  f_simple_over["Definitions for operators on tensor products"]
  f_simple_over_stable_submodule_pi_tensor["Simplicity survives a finite tensor product"]
  f_simple_over_stable_submodule_tensor_pure_kernel_span["Simplicity survives a two-fold tensor product"]
  f_simple_tensor_product_operator_stable_countable["Tensor product of irreducible pieces is irreducible"]
  f_coker_tors["Torsion of a quotient by short vectors is small"]
  f_det_nat_abs_le_prod_l1_norms["Hadamard-style bound on integer determinants"]
  f_full_enum["Independent vectors with enough reach can be listed"]
  f_torsion_bounds_chains__imports["Bound on the degree-zero homology of a group action"]
  f_index_le["A lattice spanned by short vectors has small index"]
  f_ker_orb["Collapsing a set onto its orbits, in vectors"]
  f_l1_map_domain_le_and_l1_face_d_single_le["Moving points around never grows vector size"]
  f_torsion_bounds_chains__max_indep["Maximal independent families span up to multiples"]
  f_quotients_equiv_of_ker_eq["Degree-zero homology as an orbit quotient"]
  f_tors_sat["Torsion of a quotient is controlled by a sub-lattice"]
  f_tors_sat_mult["Multiples that land in a subgroup are closed under combining"]
  f_character_theory__virtual_characters_mul_comap_conj_ind_linear["Virtual characters are closed under the usual operations"]
  f_exists_lt_commutator_mem_of_ne_top["A proper subgroup of a nilpotent group has a bigger commuting-mod-K subgroup"]
  f_inertia_eigenvalues__ind_apply_one["Basic facts about induced characters"]
  f_galois_cohomology₂__brauer_degree_zero["Statement of a Brauer-style character identity"]
  f_analytic_forms__ma_int_empty["The Levi form and the Monge-Ampere integral"]
  f_potential_theory__is_potential_of_fun["Local potentials on a complex space"]
  f_divisor_base__model_ddc_forms["Definitions and statement for the Poincare-type form"]
  f_divisor_proofs__boundary_potential_smooth_off_divisor["Boundary potentials are smooth away from the divisor"]
  f_divisor_proofs__levi_form_log_potential_formula["Levi form of a potential plus log terms"]
  f_divisor_proofs__potential_smooth_in_chart["A potential stays smooth in a compatible chart"]
  f_poincare_form_bound_of_ddc["Two-sided bound for the Poincare-type form"]
  f_sup_meas["A measure on a product of normal and acting subgroups"]
  f_semidirect_quotient_measure_conjugation_invariant["The glued measure is sigma-finite and shifts invariantly"]
  f_conjugation_measure_preserving_semidirect["The glued measure is preserved by inversion"]
  f_semidirect_measure_restriction_normal_part["The glued measure agrees with the original on N"]
  f_countable_transversal_measure_extension["Fundamental domains transfer to the bigger group"]
  f_normalizing_element_fundamental_domain_scaling["Conjugating a fundamental domain by a normalizing element"]
  f_quotient_measure_conjugation_invariant["A shared measure for a quotient and its conjugate"]
  f_global_geometry__has_values["What it means for a function to take prescribed values on a finite set of points"]
  f_global_geometry__lie_model["A module of numbers that matches the tangent vectors of a group shape"]
  f_geometry_proofs__exists_unique_tangent_dual_number["Each tangent vector lifts uniquely into the torsion points over the dual numbers mod N"]
  f_torsion_embedding_base_change["Torsion points embedded in a group shape behave well under change of base ring"]
  f_htat_bc_tors["Proof that torsion embeddings are compatible with base change"]
  f_htat_ht["The Hodge-Tate condition survives products and compatible maps"]
  f_abelian_scheme_quotients__is_abelian_scheme["Definitions of abelian schemes and semiabelian schemes"]
  f_split_tori__split_torus_aff["Definitions of split tori, characters and N-torsion subgroups"]
  f_eq_of_sec_alg_top["Setup for pulling back a Hilbert-scheme ideal, and maps into Spec A are fixed by global sections"]
  f_kappa_apply_eq["The tensor-product map into the sub-shape factors through the pullback"]
  f_section_tensor_pullback_ring_hom_bijective["Functions on a pullback over an affine piece are exactly a tensor product"]
  f_ideal_sheaf_comap_ideal_affine_open_of_is_affine["Pulling back an ideal sheaf from an affine shape, piece by piece"]
  f_divisor_proofs__affine_hilbert_ideal_sheaf_of_quotient_ideal_top["The ideal sheaf of a quotient has, over the whole space, the image of the ideal"]
  f_affine_hilbert_base_change_app_l_e_comp_spec_tensor["Two ways of mapping the tensor ring into functions on a base change agree"]
  f_ker_affine_hilbert_tensor_pullback_eq_map["The kernel of kappa on a pulled-back ideal is the pushed-forward ideal"]
  f_foundation_proofs__finite_index_of_gamma_le["Toolkit for modular forms of any level, plus finite index"]
  f_slash_q_expansion_coeff_width_transform["How q-expansion coefficients change under the group action"]
  f_slash_sub_q_expansion_partial_sum_is_big_o["A modular form minus its first M terms decays like e^(-2π·height)"]
  f_coeff_eq_zero_of_sum_plus_minus_reps_eq_zero["If coefficient sums vanish on coset representatives, all low coefficients vanish"]
  f_exists_level_one_form_one_add_exp_decay["Level-one forms that are 1 plus something exponentially small"]
  f_exists_eq_discriminant_mul_of_exp_decay_cusps["A form that decays at every cusp is the discriminant times a lower-weight form"]
  f_reduces_to_smaller_odd_weight_of_leading_coeff_matrix_det["A vanishing determinant of leading coefficients gives a smaller-weight form"]
  f_one_add_smul_mem_of_sq_zero["If 1 + ε is in a polynomial matrix group and ε² = 0, then so is 1 + tε for every t"]
  f_exists_rat_projector_of_aut_stable_matrices["A subspace of matrices stable under field automorphisms has a rational projector"]
  f_exists_rat_linear_param_block_diag_kernel["Rational linear parametrisation of the off-diagonal block of a matrix group"]
  f_uniformization_proofs__exists_graded_ring_kernel_lift["A Noetherian ring in which solutions of matrix equations lift one power of I higher"]
  f_moduli_proofs__is_noetherian_ring_of_is_adic_complete["An I-adically complete ring with Noetherian R/I is Noetherian"]
  f_iwasawa_decomposition__is_noetherian_ring_adic_completion_of_noetherian["The adic completion of a Noetherian ring is Noetherian"]
  f_algebra_tools__is_cpl_at_self["Definition of 'B is the completion of R at the prime p'"]
  f_algebra_tools__ca_cpl_ex["The concrete completion really satisfies the definition"]
  f_algebra_tools__ca_cpl_map["Powers of p extend to powers of the maximal ideal of the completion"]
  f_algebra_tools__ca_cpl_lift["Maps out of R extend uniquely to the completion, if the target is complete"]
  f_algebra_tools__ca_cpl_uniq["Any two completions of R at p are isomorphic"]
  f_algebra_tools__ca_cpl_flat["The completion of R at p is flat over R"]
  f_ca_cpl_spec["Primes below p lift to the completion, and kernel elements die after clearing denominators"]
  f_global_geometry__eig_lat["Lattices of eigenvectors in a Lie model (definitions)"]
  f_quadratic_character_prescribed_places["Integer coordinates can be checked at height-one primes"]
  f_exists_point_localization_prime["A prime of a point's ring comes from a nearby point"]
  f_lattice_eq_of_codim_one_eq["Lattices agreeing in codimension one agree everywhere"]
  f_geometry_proofs__reg_at_fraction_noetherian_closed["A point's coordinate ring has Ω as fraction field"]
  f_lattices_agree_of_height_one["Proof that codimension-one agreement forces equality"]
  f_toric_varieties__krull_domain["Integral at height-one primes means integral"]
  f_class_number_bounds__totally_real_roots["Smallest power of p dividing u^t minus 1"]
  f_gal_abelian["Galois image on p-power roots of unity matches a level group"]
  f_totally_real_roots__gal_aut["Symmetries of roots of unity are power maps"]
  f_totally_real_roots__gal_defs["Galois image and valuation of u^t minus 1 (definitions)"]
  f_gal_roots["Trivial on roots of unity, and the Galois image is closed"]
  f_totally_real_roots__le_nu_iff_pow_mem_princ["l-adic units, principal subgroups and level groups (definitions)"]
  f_level_group_sup_level_inertia["Level groups are open and sometimes everything"]
  f_level_lift["Lifting a residue class to a higher level"]
  f_nu_basic["When is u^t minus 1 divisible by l, and the case l=2"]
  f_princ_top["Principal subgroups are open and neighbourhoods of 1 contain one"]
  f_units_map_surj_of_zmod["Reduction of l-adic units is onto"]
  f_line_lattice_generic_sections["Elements of a line lattice are fractions of one generator"]
  f_regular_everywhere_is_integral["Regular at every point implies integral over the base"]
  f_valuation_centre_regular_unit["Centre of a valuation ring (restated)"]
  f_valuation_centre_exists["Every valuation ring has a centre on a proper scheme"]
  f_exists_basis_of_lattice_span["A valuation ring span of finitely many vectors has a basis"]
  f_exists_basis_quotient_lattice_eigen["Eigenspace lattice has a basis whose wedge generates the determinant lattice"]
  f_exterior_power_basis_lattice_principal["Wedges of a lattice's vectors are multiples of one wedge"]
  f_dual_lattices__small_level_class_set["Definitions and unproved claims about dual lattices and Newton lifting"]
  f_wedge_ne_zero_of_linear_independent["Wedge of independent vectors is nonzero and detects lattice membership"]
  f_induced_class_function_from_subgroup_trans["Inducing in two steps equals inducing in one"]
  f_divisors__orth_subrepresentation["Orthogonality passes to sub-representations, plus a shared toolbox of definitions"]
  f_alpha_kernel_derivative_vanishes["Lifting a regular pair to a bigger field keeps it regular"]
  f_exists_formal_germ_open_affine["Lifting a whole list of pairs keeps total size and regularity"]
  f_lift_all_preserves_degree_and_regularity["Lifting a list keeps total degree and regularity (restated claim)"]
  f_lift_l_deg_reg["Splitting a pair into l copies keeps total size and regularity"]
  f_not_mod_eq_of_lt["Regular pairs never repeat within a window of length m"]
  f_regular_pair_lift_to_prime_power_field["Regular pair lifts to the prime-power field (restated claim)"]
  f_capelli_identities__det_mul_expand["Expanding the determinant of a product of two matrices"]
  f_algebraic_independent_of_adjoin["A list generating an independent list of the same size is independent"]
  f_geometry_proofs__exists_unit_of_sum_eq_one["In a local ring, some term of a sum equal to 1 is an invertible element"]
  f_contour_shift_gaussian_decay["Shifting a vertical-line integral when the function decays like a Gaussian"]
  f_gauss_tube_of_tube_good["Multiplying by a Gaussian turns a bounded function into one that decays"]
  f_tube_transform_horizontal_invariance["The tube transform does not change when the base point slides horizontally"]
  f_tube_transform_vertical_invariance["The tube transform does not change when the base point slides vertically"]
  f_tube_transform_independent_of_base["The tube transform is the same at every base point of a convex region"]
  f_siegel_eisenstein_continuation__strip_entire["Definitions for tubes and for continuing Eisenstein series"]
  f_exists_derivations_dual_to_family_of_nilpotent_aug["Correcting approximate derivations into exact dual ones"]
  f_exists_generators_dual_point_derivations_augmented["Generators of a finite algebra with matching point derivations"]
  f_exists_invariant_derivation_of_counital_comul["A point derivation extends to a full derivation using the coproduct"]
  f_exists_square_presentation_of_tower["Square presentations compose along a tower of algebras"]
  f_frobenius_subalgebra_counital_comul["The subalgebra of p-th powers inherits the coproduct"]
  f_ker_aeval_truncated_polynomial_presentation["Kernel of evaluation is generated by x^n minus a constant"]
  f_square_presentation_of_counital_comul["Finite algebras with a coproduct and nilpotent augmentation have square presentations"]
  f_truncated_monomials_linear_independent_over_constants["Monomials with exponents below p are independent over the p-th powers"]
  f_localization_closure_equal["Two localised subrings coincide when each is generated from the other"]
  f_lu_decomposition_of_minors["A matrix with non-zero corner determinants splits into triangular pieces"]
  f_finite_point_extends_section["A point over the fraction field extends to a section over the base ring"]
  f_regular_at_translate["Regularity at a point survives translating by a group element"]
  f_translate_into_smaller_open["Any point can be translated into a smaller open piece"]
  f_bt_order_eq_of_le["The order of the finite group does not change when the open piece shrinks"]
  f_foundations__alt_coeff_rho["Definitions for reading off flag degrees from polynomial coefficients"]
  f_flag_degree_formula["The degree of a flag variety is a product of differences"]
  f_flag_degree_eq_discriminant_multiple["The flag degree is a positive multiple of a Vandermonde-type product"]
  f_divisor_proofs__flag_degree_vandermonde["A second proof of the flag degree as a Vandermonde product"]
  f_coarse_lipschitz_exponential_estimate["Bounding a shifted Eisenstein-type series by a fixed summable series"]
  f_coset_series_summable_shifted["A coset sum with a shifted exponent still converges"]
  f_holomorphic_series_uniform_tube["A uniformly dominated sum of holomorphic functions is holomorphic"]
  f_section_invariance_coset_sum["Summing over cosets in two stages gives the same Eisenstein sum"]
  f_crossing_of_walls_and_heights["Eisenstein-type series cross walls with controlled holomorphy"]
  f_expansion_coeff_valuation_ge["Definitions comparing two ways to bound coefficients of a derived polynomial"]
  f_minor_prod_span_has_compl["Statement that the span of minor products has a complement"]
  f_nabla_span_c["Definitions of the three steps used to prove the coefficient equivalence"]
  f_step_back["Small weights on determinant products give small coefficients"]
  f_monomial_frame_span__det_submatrix_fun["Two facts about determinants of chosen column blocks"]
  f_basis_monomials_apply["The derived polynomial lies in the span of determinant products"]
  f_sat_defs["Statement that a projection onto the determinant-product span exists"]
  f_sat_proj["Building the projection from per-block projections"]
  f_sat_fin["A projection lets us pass from integer to p-adic weights of small size"]
  f_gen_frame_s_b_of["Three steps combine to give the coefficient equivalence"]
  f_gen_frame_s_b_of_span["Plugging in the proven steps, only the span step remains"]
  f_gen_frame_s_b["The conditional equivalence of the two coefficient properties"]
  f_dominating_pieces_smooth["Smoothness of a map can be checked on small pieces"]
  f_gen_map_stalk_map["Maps of schemes respect generic points and stalks"]
  f_geometry_proofs__gen_map_stalk_specializes["Functions regular at a special point are regular nearby"]
  f_holomorphic_continuation__is_sing_test["Singular test functions on 2n by 2n matrix groups"]
  f_holomorphic_continuation__null_sec["Gaussian integrals of polynomials, and four unproved claims"]
  f_polynomial_derivatives__fock_mono["Creation operators and the Fock map on polynomials"]
  f_polynomial_derivatives__core_st["Operator families on polynomials, and seven unproved claims"]
  f_polynomial_derivatives__equiv_lift["Equivariant lifting claim (stated only)"]
  f_fform_smul_right["The weighted form and contraction are linear"]
  f_monomial_mem_supported["Spans of monomials, finiteness and splitting"]
  f_adjoin_first_operators_preserves_family["First-family operators keep polynomials in the first family"]
  f_polynomial_derivatives__null_stable_alt["Fock-map and null-stability claims (stated only)"]
  f_k_alg_of_adjoin_restrict["Core functional claim from four assumed claims"]
  f_metric_periods__in_flag_domain_one["Flag-domain definitions for matrices (Gram matrices, potentials)"]
  f_metric_proofs__cont_diff_at_frame_entry["Entries of a changed-frame matrix are twice differentiable"]
  f_exists_holomorphic_normal_frame["How the potential and log-sine change under a change of frame"]
  f_weighted_polynomial_homogeneous_coeff_bound["Normal holomorphic frame for 2 by 2 matrices (restatement)"]
  f_projective_line_normal_frame["Constructing a normal holomorphic frame"]
  f_triple_deriv["Product rule for a sandwiched matrix V-star G V"]
  f_local_unitary_normal_frame2x2["Local unitary normal frame for 2 by 2 matrices"]
  f_analytic_charts__osgood["Osgood's lemma via the Cauchy formula"]
  f_analytic_charts__osgood_a["Cauchy's formula on a polydisc"]
  f_formalism__statement_o_c["Statement-only definitions for the prime-sum error term"]
  f_formalism__statement["Landau-style claims linking zeros to a sign condition"]
  f_zero_free_region__statement["Statements of the zero-free region and its consequences"]
  f_zero_free_region__small_height_log_deriv["Definitions and claims for the zero-free region argument"]
  f_norm_log_deriv_le_lam_f["Log-derivative of zeta is bounded by the prime-power series"]
  f_log_deriv_right["Log-derivative of zeta is at most 1/(Re s - 1) plus a constant"]
  f_zeta_inv_bound["1/zeta is bounded by s/(s - 1) to the right of Re s = 1"]
  f_landau_zero_free_bounds__statement["Zero-free region for Dirichlet L-functions (stated)"]
  f_landau_zero_free_bounds__no_zero_complex_of["Statement-only claims for Landau's zero-free region"]
  f_l_right["Bounds for Dirichlet L-functions to the right of Re s = 1"]
  f_divisor_proofs__exists_mul_mem_integral_closure_over_generic_fibre["One common multiplier makes finitely many elements integral"]
  f_injective_trace_galois_data["A cyclic Galois-style action gives trace and dual bases"]
  f_integral_closure_over_generic_fibre_hartogs["Hartogs-type property passes to the integral closure"]
  f_integral_closure_zmod_torsor_generic_fibre_data["The integral closure inherits the cyclic-torsor data"]
  f_divisor_proofs__loc_hom_algebra_map["Two maps into the normalisation of a tensor product"]
  f_algebra_map_integral_closure_tensor_eq["The structure map is that same map"]
  f_etale_adjoin_root_x_pow_sub_c["Adjoining an n-th root of a unit gives an etale extension"]
  f_finite_integral_closure_of_formally_unramified["Finiteness of integral closures for unramified extensions"]
  f_kummer_uniformiser_adjoin_root_tensor_is_reduced["The Kummer tensor product has no nonzero nilpotents"]
  f_localization_integral_closure_artinian_reduced_domain["Localizing the normalisation of a reduced Artinian ring gives a nice domain"]
  f_normalisation_dvr_tensor_separable_finite["The normalisation over a DVR is a finite module"]
  f_localization_normalization_root_adjoin_is_d_v_r["Local rings of the Kummer normalisation are discrete valuation rings"]
  f_period_integrals__zeros_window["What 'few zeros in a window' means"]
  f_period_integrals__zeros_window_in["Three size bounds on L-functions, stated as assumptions"]
  f_right_half_with["Definitions for counting zeros in the right half"]
  f_jensen["Few zeros in a disc, from Jensen's formula"]
  f_right_chi["Zeros in the right half for non-trivial characters"]
  f_right_one["Zeros in the right half for the zeta function"]
  f_zero_window__transfer["Zeros reflect across the critical line"]
  f_finsum_mem_le_finsum_mem["From the right half to the whole window"]
  f_zero_window__assemble["Putting the zero-window bound together"]
  f_orbital_bounds_conclusion__zeros_window["The zero-window conclusion"]
  f_is_h_t_form_over["Definition of 'HT form' linear functions on a Lie model"]
  f_geometry_proofs__std_smooth_mv_polynomial["The additive line is a smooth group with a Lie model"]
  f_ga_is_h_t_form_over["The identity function on the additive line is of HT form"]
  f_localization_closure_smooth["A localized polynomial-like ring is smooth over its base"]
  f_induced_one_sub_index_mem_degree_one_character_diff["Induced trivial character minus its index is a sum of degree-one differences"]
  f_lattice_generator_invert_constant["A rank-one lattice generator, spread out by inverting one constant"]
  f_geometry_proofs__stalk_closed_point_to_germ_top["A constant from the base ring is invertible exactly off the prime"]
  f_geometry_proofs__zmod_torsor_base_change_transport_point["Invertible at a point means the image of an invertible element"]
  f_line_lattice_spread["Rank-one lattice generators spread to an open set"]
  f_gaussian_polynomial_density["Polynomial times Gaussian is dense, given the right Taylor control"]
  f_gaussian_quadratic_form_schwartz_bounds["A Gaussian with a quadratic exponent is tamed by polynomial and exponential weights"]
  f_norm_iterated_f_deriv_trunc_exp_i_comp_le["Size of the derivatives of a Gaussian"]
  f_divisor_proofs__schwartz_continuous_at_of_pointwise_of_bounded["Pointwise convergence plus uniform bounds gives Schwartz continuity"]
  f_schwartz_taylor_partial_sum_deriv_bound["Derivatives of Taylor partial sums are controlled by an exponential"]
  f_schwartz_taylor_series_converges["The Taylor series of a Schwartz function with exponential-type derivatives converges to it"]
  f_schwartz_tendsto_of_pointwise_uniform_bounds["A sequence of Schwartz functions converges if it does so pointwise with uniform bounds"]
  f_aeval_sum_elim_eq_zero_of_mem_pts["Polynomial identities on pairs of matrices pass to all rational algebras"]
  f_eq_zero_of_contractions["A tensor is zero if all its contractions are zero"]
  f_rat_component_mem_rat_polys_vanishing_on_matrix_set["Rational components of a complex vanishing polynomial still vanish"]
  f_fourier_modulated_schwartz_bounds["Multiplying by a wave keeps a Schwartz function Schwartz, with controlled growth"]
  f_iterated_f_deriv_weighted_integral["Differentiating under the integral sign, any number of times"]
  f_schwartz_family_pairing_integral_commute["A continuous linear functional commutes with integrals of Schwartz families"]
  f_schwartz_fourier_superposition["Every Schwartz function is an integral of waves with fast-decaying weights"]
  f_tempered_functional_vanish_mul["A functional killing all waves times g kills g times any Schwartz function"]
  f_exists_rat_idempotent_block_diag_part_kills_span["A non-semisimple set of matrices has a rational projection with a nonzero block-free element"]
  f_exists_rat_idempotent_of_aut_stable_subspace["A subspace stable under all field automorphisms comes from a rational projection"]
  f_invariant_subspace_not_semisimple["Failing semisimplicity gives an invariant subspace and an element crossing it"]
  f_normalized_minor_extends["Chains of good minors can be exchanged"]
  f_period_integrals__weil_quot_meas["Statement of the 'Weil quotient measure' claims"]
  f_weil_quotient_measure__step_bruhat["Two helper claims about measures on groups"]
  f_weil_quotient_measure__lintegral_mul_avg_comm["Building the quotient measure from three ingredients"]
  f_weil_quotient_measure__bruhat["A weight function that sums to 1 on every coset"]
  f_closed_subgroup_quotient_measure["Weight function for a closed subgroup, on the right side"]
  f_finite_covolume_unimodular["A finite-size fundamental domain forces a symmetric measure"]
  f_quotient_measure_tower["Averaging a sum over cosets, tower version"]
  f_modular_character_trivial_finite_covolume["Size-scaling character is trivial when covolume is finite"]
  f_l2_dbar_estimates__is_local_homeomorph["Vocabulary for complex manifolds with coordinates"]
  f_holo_section_statement["Statements for the symmetric-functions vanishing argument"]
  f_esymm_zero["If all symmetric sums vanish, all numbers are zero"]
  f_line_finite["A nonzero polynomial vanishes at finitely many points of a line"]
  f_removable_finset["A bounded function with finitely many holes extends, then is zero"]
  f_symmetric_sections__section["Holomorphic functions stay holomorphic along local sections"]
  f_sheets["Above a good point, the fibre splits into continuous sheets"]
  f_symm_diff["Symmetric sums over a fibre are complex-differentiable"]
  f_symm_growth["Symmetric sums inherit a growth bound"]
  f_symm_vanish["Symmetric sums vanish to high order too"]
  f_norm_vanish_of_parts["Assembling the vanishing argument from its parts"]
  f_norm_vanish_of_holo_section["The vanishing claim, with all parts plugged in"]
  f_jets__sum_io_pr["Vocabulary for weights, Casimir bounds and tensor splittings"]
  f_real_place_analysis__statement_k_t["Statements about highest-weight vectors for sub-block symmetry"]
  f_formal_degree_bessel__statement_d_s["Statements about formal degree of highest-weight data"]
  f_wt_near_orth_decomp["Vectors near a target weight split into orthogonal weight pieces"]
  f_weight_near_diagonal_operators_bounds["Size bounds for diagonal operators on near-weight vectors"]
  f_spec_hom_ext_of_localization_away_span_eq_top["Maps out of a ring's spectrum are decided on a cover"]
  f_is_affine_combination_in_chart_unique["An affine combination in a chart is unique"]
  f_is_affine_combination_independent_of_chart["Being an affine combination does not depend on the chart"]
  f_exists_affine_combination_square_zero_lifts_chart["Affine combinations of lifts exist over a square-zero thickening"]
  f_exists_lifts_agree_of_cocycle["Local lifts that satisfy the cocycle condition glue to one lift"]
  f_orbital_bounds_conclusion__sqf_root_shift["The 'squarefree root shift' counting bound, proved"]
  f_period_integrals__sqf_root_shift["Statement: few bad polynomials over a finite field"]
  f_arith_p["The prime-power sum is small enough"]
  f_count_a["Few roots of unity have prime-power order"]
  f_count_b["Roots of a good polynomial give a nicely behaved number"]
  f_count_c["Counting good polynomials, and polynomials with a given factor"]
  f_count_d["Every bad polynomial has a good factor; the counting half"]
  f_squarefree_root_shift__development["Setup: the two halves of the squarefree root shift bound"]
  f_sum_le_prod_of_two_le["Prime-power sums are small: lifting the exponent and friends"]
  f_in_p_apply_eq_zero["Matrices of 'off-diagonal type' vanish on same-sign blocks"]
  f_closure_k["Exponentials of K-type matrices keep vectors in the closure"]
  f_conj_transpose_eq_of_in_g["Exponentials of Lie-algebra elements stay in the group"]
  f_iterated_deriv_orbit["Derivatives of a vector moving along a one-parameter path"]
  f_analytic_vectors__taylor["Taylor expansion of a vector path, with error bound"]
  f_bochner_inequality__cas_val_k["Layers grown by mixed-sign operators (definitions)"]
  f_bochner_inequality__layer_basic["Basic properties of the layers"]
  f_casimir_algebra__mul_mul_sub_mul_mul_eq_add["The Casimir operator commutes with everything"]
  f_discrete_series__defs_rep["Definitions: sign matrices, unitary representations, derived action"]
  f_discrete_series__is_inf_unitary["Definitions: operators on a vector space, weights, Casimir, gaps"]
  f_ca_cpl_quot["A quotient of a completion is a completion of the quotient"]
  f_one_mom["Statement: the basic complex Gaussian integrals"]
  f_integrable_rpow_gauss["Proof of the basic complex Gaussian integrals"]
  f_integrable_monomial["Gaussian moments of monomials factor into one-variable integrals"]
  f_gaussian_moment_recurrence["Differentiating a polynomial moves a variable to its conjugate"]
  f_contr_eq_of_subset["The contraction of a polynomial, as a weighted sum over monomials"]
  f_fock_mom_of_basic["The Fock map preserves Gaussian moments, given the basic facts"]
  f_affine_hilbert_scheme_functor_is_sheaf_zariski["Good sub-pieces of a finite algebra glue over open covers"]
  f_exists_ideal_sheaf_comap_eq_of_open_cover_statement["Statement: ideal data on an open cover glue"]
  f_exists_ideal_sheaf_comap_eq_of_open_cover["Ideals on an open cover glue to one ideal"]
  f_exists_ideal_sheaf_data_of_compatible["Compatible ideals on small opens glue to one ideal sheaf"]
  f_ideal_sheaf_data_ext_of_open_cover["Two ideal sheaves agreeing on an open cover are equal"]
  f_ideal_sheaf_data_ext_of_open_cover_statement["Statement: ideal sheaves are determined on an open cover"]
  f_ideal_sheaf_glue_of_open_immersions["Gluing ideal sheaves along open embeddings"]
  f_is_finite_flat_rank_closed_subscheme_of_open_cover["Being finite, flat and of fixed rank can be checked on an open cover"]
  f_is_finite_flat_rank_closed_subscheme_of_open_cover_statement["Statement: goodness of sub-pieces is local on covers"]
  f_noether_normalization_chart["A change of variables that makes a polynomial monic"]
  f_proof_simp["Generic Noether normalisation, proved"]
  f_pseudo_division["Dividing polynomials over a ring, after scaling"]
  f_sum_r_mul_ne["Different digit lists give different base-b numbers"]
  f_p_generic_freeness["Generic freeness, assuming Noether normalisation"]
  f_p_generic_freeness_closed["Generic freeness, unconditional"]
  f_p_generic_freeness_loc["The notion of generically free, and how it behaves under gluing"]
  f_p_generic_noether_normalisation["Generic Noether normalisation, with a second route"]
  f_st_generic_freeness["Statement of generic freeness"]
  f_st_generic_noether_normalisation["Statement of generic Noether normalisation"]
  f_high_degree_in_power_sum_ideal["High-degree polynomials lie in the power-sum ideal"]
  f_polynomial_reduction_mod_elementary["Reducing polynomials to a small set of monomials (Artin basis)"]
  f_power_sum_decomposition_homogeneous["Top-degree polynomials are sums of power sums times polynomials"]
  f_span_psum_eq_span_esymm["Power sums and elementary symmetric polynomials generate the same ideal"]
  f_exists_perm_normalized_minors["One row order that normalises all leading minors at once"]
  f_covolume_bounds__linear_independent_real_of_int_of_discrete["Gram determinants, Hadamard's bound and covolume of a lattice"]
  f_norm_det_mul_prod_sq_le_of_entry_le["Discriminant of an étale algebra is nonzero exactly for a basis"]
  f_integral_closure_fg_finite_etale_dvr["Integral closure over a discrete valuation ring is finitely generated"]
  f_period_integrals__unimod_loc_std["Setup and statement of the unimodular local standard claim"]
  f_unimodular_local_standard__key_def["The 'key representation' claim, stated"]
  f_key_exact["From a close-enough approximation to an exact vector"]
  f_key_newton["Doubling the accuracy of an approximation, Newton-style"]
  f_unimodular_local_standard__rep_arith["Arithmetic of the CM number and the standard lattice"]
  f_unimodular_local_standard__rep_basic["Basic rules for the Hermitian form and saturated vectors"]
  f_unimodular_local_standard__rep_defs["Definitions of the start, Newton and exact steps, and how they combine"]
  f_unimodular_local_standard__rep_exact["Scaling a vector by M scales its length squared by M²"]
  f_rep_key["The key representation claim follows from the start step alone"]
  f_unimodular_local_standard__rep_newton["The multiplier τ and the length scaling rule"]
  f_mollified_integrability__cls_bound_alt["Seven stated claims about smooth Gaussian-type integrals"]
  f_continuous_cexp_ip["Recovering a function by smoothing, then un-smoothing"]
  f_dens_defs["Definitions and four stated claims for the damped transform"]
  f_exp_combine["Combining exponentials and swapping the order of integration"]
  f_moll_id["Toolkit for the smoothing argument"]
  f_moll_id_a["The Gaussian bump has total weight one, and its Fourier transform"]
  f_step_b["Swapping the order of two integrals in the smoothing argument"]
  f_step_c["The kernel integral equals the Gaussian-smoothed function"]
  f_poincare_form_two_sided_bound["A two-sided bound on a Poincare-type form gives growth bounds"]
  f_square_norm_bound["Biggest entry squared is at most the sum of all squares"]
  f_has_f_deriv_at_ev_x["Differentiating a polynomial in entries and their conjugates"]
  f_null_operator_evaluation["Integration by parts kills the moment of a derivative"]
  f_null_stable["Null-stability, under its short name"]
  f_partial_deriv_quadratic_pairing["Derivatives of the basic quadratic polynomials"]
  f_poly_exp_bound["A polynomial times a Gaussian is integrable"]
  f_sum_pderiv_x_mem["Null polynomials stay null under four operators"]
  f_abstract["Averaging against an idempotent kernel gives zero"]
  f_band_cc["Averaging a compact bump along N gives a band function"]
  f_band_kill["A killing function times a band function convolves to zero"]
  f_conv_assoc["Associativity of convolution"]
  f_conv_eig["Convolving an eigenfunction gives another eigenfunction"]
  f_eig_band["Fourier-transforming a band function along the ray gives an eigenfunction"]
  f_eq_zero_of_test["A continuous function that integrates to zero against every bump is zero"]
  f_exists_compact_tail["Convolution bounds hold for nearby frequencies, with a small loss"]
  f_fourier["A function with zero Fourier transform is zero"]
  f_is_band["Definitions for rays, eigenfunctions and bands"]
  f_kills_of_idem["An idempotent kernel kills every eigenfunction"]
  f_op_le_half["Some frequency has operator bound one half"]
  f_real_bands__transl["Translating an integrable function a little changes it a little"]
  f_unfold["Convolving with an averaged bump equals averaging the translates"]
  f_foundations__is_d_c_reps["Definitions for Hecke-type operators and Eichler integrals"]
  f_coeff_eq_zero_of_exp_decay_of_integral_identity["A decaying function with a fixed-shape increment forces the coefficient to vanish"]
  f_cusp_form_eq_zero_of_periodic_of_bound["A cusp form with a periodic, slowly growing Eichler combination is zero"]
  f_foundation_proofs__eichler_integral_from_i_slash_change_of_variables["How the Eichler integral changes under a modular substitution"]
  f_green_formula_periodic_rectangle_upper_half_plane["Green's formula on a rectangle with periodic sides"]
  f_integral_conj_mul_exp_eq_conj_q_expansion_coeff["Integrating a conjugated periodic function against a wave picks out a coefficient"]
  f_wirtinger_eichler["The conjugate-variable derivative of an Eichler combination"]
  f_st_sandwich["Setting and claims about lattices in a local Hermitian space"]
  f_witt_statement["Frames in a Hermitian space are all equivalent (Witt)"]
  f_witt_extension_theorem["Witt's extension theorem, assembled"]
  f_anisotropic["Two claims: one-vector move and a vector with nonzero self-pairing"]
  f_anisotropic_holds["A nonzero form has a vector with nonzero self-pairing"]
  f_enlarge_step["Extending a structure-preserving map to a bigger subspace"]
  f_witt_decomposition__imports["Every linear functional is a pairing with some vector"]
  f_witt_decomposition__nondeg["Extending an isometry from a non-degenerate subspace"]
  f_one_vector["Moving one vector to another by a reflection"]
  f_witt_of["Witt's theorem from the two basic claims"]
  f_witt_extension["Statement of Witt's extension theorem"]
  f_adic_completion_principal_perfect["Completing a perfect ring along one element keeps it perfect"]
  f_adic_completion_valuation_ring_complete_valuation_doma["Completing a valuation ring along a non-unit gives a valuation ring"]
  f_bounded_powers_or_exists_valuation_subring_dvd["Either powers stay bounded, or a valuation-ring point shows the failure"]
  f_descent_of_points_killed["Elements that agree at all perfect valuation points come from the base"]
  f_dvd_all_pow_of_frobenius_eq_killed_by_perfect_points["Vanishing at all perfect valuation points forces divisibility by every power"]
  f_exists_valuation_subring_alg_closed_not_is_unit["A non-unit survives in some valuation ring of an algebraically closed field"]
  f_frobenius_pow_equation_dvd_all_pow["A p-th-power relation plus bounded powers gives divisibility by every power"]
  f_pow_dvd_of_vanishing_at_perfect_valuation_points["Vanishing at perfect valuation points bounds the powers"]
  f_period_integrals__unitary_approx["Statement: approximating a local unitary matrix by a global one"]
  f_unitary_approx_fin["Statement: approximating at finitely many primes at once"]
  f_unitary_approximation__assembly["The Cayley step: approximate a unitary matrix through a skew one"]
  f_unitary_approximation__cayley["The Cayley transform sends skew matrices to unitary ones and back"]
  f_unitary_approximation__development["Chaining the approximation claims together"]
  f_mem_int_o_e_of_is_integral["Helper facts: integral elements and clearing denominators"]
  f_sigma_mem_int_o_e["Helper facts: matrices with integral entries"]
  f_skew_approx["Approximating skew matrices by a global one"]
  f_weak_approx_f["Statements of the basic approximation claims"]
  f_general_b_fact_right_ter__imports["A common nonzero multiple for finitely many conditions"]
  f_complex_analytic_sets__osgood_separate["Osgood's theorem: separately holomorphic and continuous means holomorphic"]
  f_p_non_isolated_fibre_curve["A non-isolated point of a fibre lies on a holomorphic curve"]
  f_st_analytic_germ_components["Statement: an analytic germ splits into irreducible pieces"]
  f_st_irreducible_germ_curve["Statement: an irreducible germ with accumulation contains a curve"]
  f_st_non_isolated_fibre_curve["Statement: fibres with accumulation points contain curves"]
  f_regularisation__p_riemann_extension_slices["Riemann extension in several variables via a torus integral"]
  f_regularisation__st_riemann_slices["Statement: Riemann extension across coordinate axes"]
  f_alpha_uniqueness__statement["Statements about Gauss sums and a canonical mod-2 quadratic form"]
  f_fock_gram__statement_herm["Statements: dual lattices and Gram determinants for Hermitian forms"]
  f_fock_gram__statement_lat["Statements: how Gram matrices change and combine"]
  f_hermitian_lattices__defs_c_s["Statements: lattices over number fields become real lattices"]
  f_discr_finite["Statements: the discriminant group is finite, and its theta transformation"]
  f_hermitian_lattices__genus_covol_bound["Statements: genus covolumes are bounded and automorphisms are finite"]
  f_hermitian_lattices__statement_lat["Definitions and statements for lattices with a Hermitian form"]
  f_hermitian_lattices__statement_theta["Definitions and statements for theta functions of lattices"]
  f_theta_l_euclid["Statements: theta of a Hermitian lattice equals a Euclidean theta"]
  f_lattice_theta__statement["Statements: Poisson summation and theta inversion for real lattices"]
  f_card_nonregular_residues_mod_pow_sub_one_le["Few residues are fixed by a smaller power-of-q shift"]
  f_no_norm_eight_of_fourier_vanishing_order_fifteen["No integer vector of squared length 8 with vanishing 15-point Fourier values"]
  f_no_norm_twelve_order_sixtythree["No integer vector of squared length 12 with vanishing 63-point Fourier values"]
  f_orthogonal_int_vectors_not_agree_on_regular["Two orthogonal short integer vectors cannot share all regular Fourier values"]
  f_parseval_bound_integer_vector_small_fourier_support["Parseval bound for an integer vector with few nonzero Fourier values"]
  f_separation_numerical_ineq_cuspidal_g_l["A numerical inequality separating the counting bound"]
  f_mahler_measure__level_sum["Binomial identity and the 'tie' operators (statements)"]
  f_mahler_measure__good_count["Letters, polynomial spaces and counting 'good' lattice vectors (definitions)"]
  f_mahler_measure__is_frozen_inv["'Freezing' a polynomial: definitions and four statements"]
  f_mahler_measure__has_order["Order of vanishing, leading part, and two statements about a tie quantity"]
  f_mahler_measure__cs_saturated["Weight spaces, highest-weight vectors and lattices (definitions)"]
  f_mahler_measure__quotient_upper_bounds_of_power_bounds["Counting small p-adic values along an arithmetic progression (statements)"]
  f_mahler_measure__statement_t["Hypotheses on projections and Gram determinants (statements)"]
  f_mahler_measure__statement_t_m["Theorem M and its supporting claims (statements)"]
  f_fock_resolution_onto__shift_last_letter_thresholds["Shifting the last letter: definitions for a surjectivity claim"]
  f_fock_resolution_onto__statement_a["Partner determinant and graded piece bounds (statements)"]
  f_meets_open_cosets["Semisimple matrix groups and the 'Div core' statements"]
  f_div_w_core_lac_use_type["Variants of the Div core statement (statements only)"]
  f_open_coset["Matrices as polynomial functions: the vocabulary and open-coset claim"]
  f_chain_pf["Proof of the chain rule for polynomial pullback"]
  f_sep_poly_proof["A discriminant polynomial detects separable characteristic polynomials"]
  f_coset_of_cover["Chain rule implies the open-coset property (Noetherian argument)"]
  f_open_coset_pf["Open-coset property follows from the chain rule"]
  f_cycle_count["A list of matrix claims: eigenvalue projections, matrix units, density (statements)"]
  f_fin_dense_pf["Proof of the density claim from separability and open cosets"]
  f_fin_fin_dense["Assembling the density result with no assumptions left"]
  f_geometry_proofs__section_eq_zero_of_values["A function vanishing at all marked points is zero"]
  f_hodge_tate_functional_unique["Hodge-Tate functionals are unique up to adding N times another"]
  f_archimedean_orbit_measures__upq["The unitary group U(p,q) as a group of matrices"]
  f_archimedean_orbit_measures__omega_density["U(p,q) with its topology, its Lie algebra and a density condition"]
  f_cay_dens_ex_om["The Lie algebra of U(p,q) is a nice space for measure theory"]
  f_archimedean_orbit_measures__imports["Dual of a lattice with respect to a Hermitian form"]
  f_archimedean_orbit_measures__is_unimodular["Unimodular lattices and isometries of a Hermitian form"]
  f_archimedean_orbit_measures__is_c_m_unram["Unramified CM fields (definition)"]
  f_archimedean_orbit_measures__base_lattice_is_unimodular["CM data and Hermitian spaces with a unimodular base lattice"]
  f_archimedean_orbit_measures__inst_topological_space_h_a["Unitary groups over rings, adeles and self-dual measures (definitions)"]
  f_archimedean_orbit_measures__is_inf_emb["Embeddings at infinity (definition)"]
  f_archimedean_orbit_measures__meas_lie["Cayley transform and 'locally tamed' measures (definitions)"]
  f_archimedean_orbit_measures__one_per_place["One embedding per place, and the statement InfCmpG"]
  f_archimedean_orbit_measures__cay_dens_ex_sk["Four stated claims about the infinite-place measures"]
  f_archimedean_orbit_measures__cay_dens_ex_top["U(p,q) is a closed matrix group; Haar measure is unique up to a constant"]
  f_diamond_diag_mul_eq_mul_of_dvd_lower_left_gamma1_inter_gamm["Hecke matrix slides past a level-group element (divisible case)"]
  f_diamond_diag_mul_eq_mul_upper_triangular_of_not_dvd_lower_l["Hecke matrix slides past a level-group element (non-divisible case)"]
  f_hecke_operators_on_half_plane_functions_agree_explicit["Matrix-sum Hecke operators equal the explicit formulas"]
  f_hecke_t_slash_invariant["The Hecke operator T_q preserves invariance under the level group"]
  f_hecke_tq_representatives_cosets_distinct["The q+1 Hecke representatives are genuinely different"]
  f_upper_mul_eq_mul_diamond_diag_gamma1_inter_gamma0["Upper-triangular Hecke matrix times level element becomes the 'diagonal' one"]
  f_upper_triangular_mul_eq_mul_upper_triangular_gamma1_inte["Upper-triangular Hecke matrix times level element stays upper-triangular"]
  f_has_fderiv_at_schwartz_operator_first["Differentiating an operator applied slice by slice"]
  f_has_temperate_growth_prod_mk_const["Freezing one variable of a Schwartz function"]
  f_schwartz_operator_parametric_extension["A Schwartz-function operator extends to a family of inputs"]
  f_divisor_proofs__schwartz_seminorm_translate_sub_line_deriv_le["Translating a Schwartz function is almost its first-order Taylor term"]
  f_schwartz_slice_seminorm_le["Slicing does not increase Schwartz size"]
  f_schwartz_translate_taylor_second_order["Uniform second-order Taylor bound for shifting Schwartz functions"]
  f_adelic_hermitian_forms__is_herm_form["Definitions for Hermitian forms and reflections over number fields"]
  f_exists_denominator_primes_prescribed["Clearing denominators using only chosen primes"]
  f_exists_nat_smul_mem["Every vector has a whole-number multiple in the lattice"]
  f_exists_norm_one_reflection_correction_at_level["Correcting a norm-one reflection so it nearly preserves a lattice"]
  f_exists_pos_nat_mul_mem_ring_of_integers["Some whole-number multiple of any number is an algebraic integer"]
  f_norm_one_approximation_at_level_primes["Approximating a norm-one number by a better-behaved one"]
  f_adelic_lattice_proofs__unitary_quasi_reflection_laws["Algebra rules for reflection matrices"]
  f_valuation_eq_one_of_norm_one_of_not_moved["Norm-one numbers have size 1 at unmoved primes"]
  f_foundations__same_part_iff_of_ne_zero["Counting set-up for squarefree polynomials, and 'same l-part' characterised"]
  f_card_monic_squarefree_unit_const_polys_ge["Most monic polynomials are squarefree with nonzero constant term"]
  f_foundation_proofs__mem_monic_squarefree_unit_const_polys_iff_monic_squarefr["What it means to be in the squarefree-polynomial set"]
  f_one_sub_two_div_le_squarefree_label_mass["The total weight of squarefree polynomials is at least 1 - 2/g"]
  f_foundation_proofs__squarefree_label_torus_card_bounds_and_mul["Torus count is positive, at most g^N, and multiplicative"]
  f_cyclotomic_norms__statement_i["Statements about bad primes, counting and idempotents (not proved here)"]
  f_cyclotomic_norms__statement_t["Definitions and a statement of an irreducibility criterion (not proved here)"]
  f_orbital_bounds_conclusion__sigma_star_ex["Named copy of the existence of the special odd function"]
  f_period_integrals__sigma_star_ex["Statement that a special odd function exists on every lattice"]
  f_theta_series_existence__development["Plan for building the special function from theta pieces"]
  f_gen_eq_of["Building the function from the Jacobi theta function"]
  f_lat_ext["Shift rule for two generators extends to the whole lattice"]
  f_theta_series_existence__reduce["Every lattice has a well-shaped basis"]
  f_theta_series_existence__sigma_star_ex["Existence of the special odd function, assembled"]
  f_theta_a["Symmetries of the shifted Jacobi theta function"]
  f_theta_deriv_ne["Definitions for the theta function, plus two statements"]
  f_theta_nz["The theta derivative never vanishes in the needed range"]
  f_commutative_algebra__is_tight["Lattices of functions mod p, and the 'tight' condition"]
  f_commutative_algebra__step_order_res["Eigen-pieces and step lattices of function lattices"]
  f_hopf_order_contains_add_characters["Additive characters lie in every Hopf order"]
  f_hodge_tate_points__ra_char["Proof: additive characters belong to a Hopf order"]
  f_dual_lattices__cotangent_surjective["Hodge-Tate data bundle and size-of-quotient definitions"]
  f_dual_lattices__tensor_span["Function lattices, Hopf orders and duals: definitions"]
  f_dual_lattices__valuation_det_eq_of_span_eq["Dual of a dual lattice, and equal lattices have equal determinant size"]
  f_dual_lattices__valuation_fourier_le_one["Fourier transform of a dual element has size at most 1"]
  f_fock_resolution_onto__statement_b["Six unproved claims about 'filtered' polynomial lattices"]
  f_non_galois_descent__fourier_match["Matching orbital integrals under Fourier transform (statements)"]
  f_non_galois_descent__linear_descent["Counting lattices and a descent formula (statements)"]
  f_non_galois_descent__unit_lemma_group["The 'unit lemma': set-up and two identities (statements)"]
  f_exists_finset_cosets_integral_norm_units["Finitely many cosets cover the 'norm' units"]
  f_inertia_eigenvalues__exists_power_basis_of_charpoly_separable["Separable characteristic polynomial gives a power basis"]
  f_fg_units_quot_integral_units_finite_field_ext["Units modulo integral units: finitely generated for a field extension"]
  f_fg_units_quot_integral_units_reduced_finite_algebra["Units modulo integral units: finitely generated for reduced algebras"]
  f_is_reduced_of_separable_marked_charpoly["Separable characteristic polynomial makes the algebra reduced"]
  f_complex_witt_basis_normal_form["Normal form for a Witt basis of a Hermitian form"]
  f_conj_transpose_mul_mul_self_of_unitary_conj["A unitary rotation of a Witt frame preserves a positive form"]
  f_exists_levi_element_isotropic_orthogonal_complex["A shift making a complement orthogonal"]
  f_hermitian_flag_complement_pos_def_factorization["A Schur-complement step for a positive form"]
  f_hermitian_flag_unipotent_matrix_exists_sparse["The shift matrix has a sparse strictly upper-triangular form"]
  f_pos_def_exists_conj_transpose_mul_mul_eq_one["A positive definite matrix is a change of basis away from the identity"]
  f_radical_elt_moving_dual_to_majorant["A form-preserving map moving a dual frame to a given one"]
  f_min_weight_sum_add_cost_abs_bound["Four unproved bounds: minimum-weight sums, jets, and minors"]
  f_sizes_rows7["Two unproved size inequalities for row sums"]
  f_gauss_jet_bounds__statement["Dwork weight definitions and the first bound statements"]
  f_gauss_jet_bounds__statement_a["Assembly of the radii for Theorem A (statement)"]
  f_gauss_jet_bounds__statement_c["Rank spanning and 'pure' coefficients (statements)"]
  f_gauss_jet_bounds__statement_e["Theorem A for jets: a bound on one coefficient (statement)"]
  f_gauss_jet_bounds__statement_g["A general jet bound and its Theorem A form (statements)"]
  f_gauss_jet_bounds__statement_h["Minors of structured matrices and the shape of their monomials (statements)"]
  f_gauss_jet_bounds__statement_i["Theorem A for operators: a jet-pairing bound (statement)"]
  f_gauss_jet_bounds__statement_n["Pairings, matchings and Theorem B (statements)"]
  f_statement_q["Integrality of jet pairings and a matching bound (statements)"]
  f_incoming_bounds__incoming_bound["Flow problem constants and the 'incoming bound' (statements)"]
  f_quot_meas_uniq["Quotient measures are unique, assembled"]
  f_orbital_bounds_conclusion__weil_quot_meas["The Weil quotient measure exists and is unique"]
  f_q_lift_is_mul_left_invariant["Lifting a measure from cosets back to the group"]
  f_qmu_weight["Two ingredients for uniqueness, stated"]
  f_weight["A weight that sums to a positive finite number on each coset"]
  f_wq_unique_of["Uniqueness of quotient measures from the two ingredients"]
  f_inv_inv["Haar measure and the flip to inverses"]
  f_box_le_first_family["Equivariant lifting proved from assumed claims"]
  f_sym_k_eq_zero_of_om["Positivity forces the operators to vanish"]
  f_symbol_first_family_of_mem["Polynomials of bounded degree stay closed under the operators"]
  f_zero_right["Positive Hermitian pairings, basic facts"]
  f_lattice_theorem_of_discharge["Lattice height bound from Theorem M and one implication"]
  f_trace_isometry_weights__statement_c["Statements about Fock pairings and projections"]
  f_trace_isometry_weights__statement_f["Statements that the hypotheses can be discharged"]
  f_trace_isometry_weights__statement_g["The lattice theorem height bound, stated"]
  f_adelic_lattice_proofs__is_quadratic_sqrt_extension_basic_facts["Basic facts about a square-root extension"]
  f_adelic_lattice_proofs__height_one_spectrum_places_over_finite_set["Primes of a number field above a given prime"]
  f_two_places_of_embeddings["Two embeddings give two distinct primes"]
  f_adelic_lattice_proofs__exists_two_places_over_of_is_square_local["A prime splits when delta is a local square"]
  f_adelic_lattice_proofs__kummer_galois["Kummer extensions are Galois of degree p"]
  f_ncard_places_over_eq_of_prime_degree["Prime degree gives all or one primes above"]
  f_prime_mul_card_places_le_card_over_kummer["Counting primes above in a Kummer extension"]
  f_parabolic_induction_trivial_preserves_virtual_charact["Summing over invariant subspaces keeps a virtual character"]
  f_statement_p_w["Two bounds on 'bad' lattice vectors, stated but not proved"]
  f_dedekind_finite_type_ideal_codimension["Quotients of a curve's coordinate ring are finite-dimensional and add up"]
  f_exists_degree_lt_two_correction_simple_zero["Nudging an element so it vanishes exactly once at a chosen point"]
  f_exists_linear_system_maximal_degree_factorization["Building a bounded-degree family of functions with a prescribed zero pattern"]
  f_exists_low_degree_coords_mod_mul["Reducing coordinates to low degree modulo a product"]
  f_exists_norm_form["The norm of a combination is a polynomial of known degree in the coordinates"]
  f_exists_squarefree_poly_distinct_zeros_on_curve["A polynomial with distinct simple roots that cuts the curve in distinct points"]
  f_norm_degree_bound_polynomial_combination["Degree of the norm of a polynomial combination (restated)"]
  f_reduced_fibres_almost_all["Almost every vertical slice of a curve is reduced"]
  f_bad_crit["A criterion for counting good vectors, proved"]
  f_jet_harmonics__cas_k_is_symmetric_and_form["The Casimir sum is symmetric and acts as a sum of squares"]
  f_compact_casimir_le_subspace_monotone["Vectors with a Casimir bound form a growing subspace-like family"]
  f_lev_subspace_mono["Vectors of a given level form a subspace-like, growing family"]
  f_jet_harmonics__re_inner_le_on_image_of_intertwining["A quadratic bound passes across a map that commutes with the operator"]
  f_wt_near_le_of_add_dist_le["Weight spans grow when the allowed distance grows"]
  f_hypersurface_diff_is_preirreducible_of_no_splitting["No splitting of f means the shape f = 0 minus g = 0 is one piece"]
  f_hypersurface_part_geometric_irreducible_spreads["One-piece hypersurface pieces stay one piece for nearby fields"]
  f_no_common_zero_spreads_constructible_nbhd["If equations have no common solution at one field, the same holds nearby"]
  f_no_splitting_factorisation_of_pderiv_ne_zero["A smooth one-piece hypersurface cannot split into two factors"]
  f_preirreducible_fibre_standard_etale_spreads["Irreducible fibres of an etale family stay irreducible nearby"]
  f_preirreducible_space_fibre_hypersurface_spectrum_iff["Fibre of a hypersurface ring is one piece exactly when its shape is"]
  f_splitting_absence_spreads["If no splitting exists at one field, none exists nearby"]
  f_standard_etale_mv_polynomial_hypersurface["A standard etale algebra is a hypersurface with smooth slope"]
  f_fock_gram_proofs__covol_gram["Lattice volume equals the square root of the Gram determinant"]
  f_det_sym_pow["Helper definitions for powers of a matrix acting on polynomials"]
  f_fock_herm["The Fock pairing is conjugate-symmetric"]
  f_fock_perm["Helper facts for computing the Fock pairing as a permanent"]
  f_fock_sesq["The Fock pairing is linear in one slot and conjugate-linear in the other"]
  f_herm_dual_of["Dual lattice of a Hermitian form, from the index-equals-norm fact"]
  f_hermitian_tensor_mul_hermitian["Tensor product of two Hermitian forms"]
  f_sub_index_norm["Index of a sublattice equals the norm of a determinant"]
  f_statement_fock["Definitions and claims: the Fock pairing and symmetric powers"]
  f_statement_sym_pos["Claims: symmetric powers keep a Gram matrix positive"]
  f_statement_tensor["Definitions and claims: tensor product of Hermitian forms"]
  f_sym_gram_pos_semidef["Wiring together the Hermitian-form proofs"]
  f_orbital_fiber_card_formula["Counting the pieces of a fibre in a coset space"]
  f_orbital_fiber_decomposition["Splitting a weighted orbit count into pieces"]
  f_orbital_fiber_of_bot["Weighted orbit count with the trivial subgroup"]
  f_orbital_fiber_pushforward["Pushing a weighted orbit count forward along a map"]
  f_orbital_fiber_pushforward_eq_zero["Weighted orbit count as a plain sum over an invariant function"]
  f_symmetric_fiber_covering["Covering formula for fibres of symmetric orbit counts"]
  f_fib_abs["Statements: the toolkit of orbit-count identities"]
  f_trace_formula_eigenvalues__forms_fin["Statements: finite-dimensional form spaces and trace-formula steps"]
  f_trace_formula_eigenvalues__is_gen_eig["Definitions: weighted orbit count, form spaces and twisted operators"]
  f_symmetric_power_transfer__wcount["Definitions: orbit counts for the symmetric-power transfer"]
  f_global_signature__invariant_radon_fibre["Definitions and claims: invariant measures on a quotient of a group"]
  f_exists_bruhat_function_closed_subgroup["A weight function that integrates to 1 along every coset"]
  f_global_interpolation__exists_unique_haar_of_invariant_radon_on_cosets["Gluing an invariant measure on cosets with Haar measure on the subgroup"]
  f_quotient_invariant_measure_exists_unique_unimodular["Invariant measure on cosets, when both groups are unimodular"]
  f_quotient_measure_normalised_by_haar_unique["Normalising the coset measure against Haar measures"]
  f_weil_criterion_invariant_measure_homogeneous_space["Weil's criterion: when the coset space has an invariant measure"]
  f_content_distance_bounds["Claims: small helper inequalities for column windows and prime counts"]
  f_params_window["Claims: window parameter inequalities and a cross-term bound"]
  f_joint_exact_exponent_stop_high["Two small ordering facts about the 'cloud' and 'rest' lists"]
  f_local_component_g_l["Proof that no residues land in the window"]
  f_max_val_eq_zero_of_lt["Binomial coefficients are not divisible by a prime above n"]
  f_pieri_block_ideals__statement["Definitions and claims: binomial valuations, window sums, index bounds"]
  f_pieri_block_ideals__statement_c["Claims: a corollary bounding a weighted prime sum"]
  f_pieri_block_ideals__statement_j["Claims: the joint version with explicit weight lists"]
  f_rank_gap_bounds__cloud_min_false["Definitions and claims: exponent sums over pairs, and a failed bound"]
  f_rank_gap_bounds__large_prime_factor["Definitions and claims: the data bundle and a prime-sum corollary"]
  f_card_large_prime_factors_le_one_holds["Proofs of five classical prime and sum estimates"]
  f_one_letter_gauss_jets__odd_level_gain_sum["Definitions: bookkeeping for odd-level gains in the one-letter case"]
  f_one_letter_gauss_jets__statement_j["Claims: size bounds on Gauss-sum jets, one-letter versions"]
  f_gauss_jet_bounds__statement_j["Claims: linear change of variables, and the general jet bound"]
  f_descend["Determinant rules defined over a bigger ring come from the smaller ring"]
  f_determinant_representations__ext_gen["A determinant rule is fixed by its value on generic elements"]
  f_extend_poly["Building a determinant rule from compatible polynomial values"]
  f_determinant_representations__gen_eval["Evaluating the generic determinant at chosen numbers"]
  f_determinant_representations__gen_span["Every element is a finite combination of group elements"]
  f_determinant_representations__inj_test["Checking determinant rules by testing over many rings"]
  f_lift_indep["Polynomial determinant values do not depend on how an element is written"]
  f_determinant_representations__map_api["How determinant rules behave when the base ring changes"]
  f_commutative_algebra__res_map_bijective["Complete local rings and lifts of representations (definitions)"]
  f_weil_group_characters__rep_alg["Determinant rules on groups, defined"]
  f_metric_periods__has_multiplier["A 'multiplier' that changes sizes by a controlled amount (definitions)"]
  f_metric_proofs__hermitian_line_shift_properties["Scaling a size rule by a constant keeps its good properties"]
  f_aeval_eq_zero_of_mem["Points with a nonzero coordinate in every block form an open set"]
  f_rational_sup_metrics__hermitian_line_shift_properties["Proof that constant rescaling preserves smoothness, nefness and bounds"]
  f_birational_geometry__arithmetic_hilbert_samuel_lower_bound["Arithmetic Hilbert-Samuel claims, stated but not proved"]
  f_birational_geometry__is_intersection_family["Intersection numbers on arithmetic varieties (definitions)"]
  f_birational_geometry__is_semipositive_on["Metrics, curvature and heights (definitions)"]
  f_birational_geometry__pen_host["Number-field upper-bound claim, stated but not proved"]
  f_birational_geometry__pen_vol["Small sections and volume (definitions)"]
  f_p_hol_germs_domain["Analytic germs have no zero divisors"]
  f_st_germ_weierstrass_preparation["Weierstrass preparation, stated but not proved"]
  f_weierstrass_polynomial_ring["Weierstrass polynomials divide and stay irreducible over germs"]
  f_weierstrass_remainder_unique["A low-degree remainder equal to a multiple of W must be zero"]
  f_exists_value_basis["Tangent-space lattices give a basis at a special point"]
  f_formally_smooth_section_stalk["A smooth map with a section has a good local chart"]
  f_formally_smooth_surjective_derivation["Tangent directions of a smooth local chart are coordinates"]
  f_one_left_congr["Adding tangent vectors is multiplying in the group"]
  f_span_linear_independent_base["Matching a basis after reducing a lattice of coordinates"]
  f_norm_iterated_f_deriv_rem_comp_le["Operators fixed by phase twists must kill linear multiples"]
  f_schwartz_family_phase_bound["Phase twists of a Schwartz function vary continuously and grow slowly"]
  f_schwartz_fourier_representation["Every Schwartz function is a superposition of waves"]
  f_schwartz_inner_product_continuous["Pairing with a fixed Schwartz function is a continuous linear map"]
  f_schwartz_integral_superposition["A continuous linear map passes inside an integral of Schwartz functions"]
  f_translation_character_invariant_form["Moving a multiplier from one side of a pairing to the other"]
  f_first_lemma_f["Products of integral power series stay integral"]
  f_first_lemma_g["Derivatives of integral power series stay integral"]
  f_imports_ter_alt["The p-adic numbers of size at most 1 form a ring"]
  f_int_mv_pderiv["Integrality survives differentiation (copy)"]
  f_capelli_identities__integral_mv["The constant series 1 is integral"]
  f_integral_polynomial_fifth["Each variable X_i is an integral series"]
  f_integral_polynomial_first["Sums of integral power series are integral"]
  f_integral_polynomial_fourth["Negatives of integral power series are integral"]
  f_integral_polynomial_second["Products of integral power series are integral (second proof)"]
  f_integral_polynomial_sixth["The zero series is integral"]
  f_integral_polynomial_third["Constant series with integral value are integral"]
  f_capelli_identities__is_integral_nat_cast["Whole numbers have p-adic size at most 1"]
  f_unit_ball["Integral series with constant term 1 have integral inverses"]
  f_jets_ph_w["Definitions for exp, log and jets on Weierstrass curves"]
  f_jet_integrality__exp_log["When exp of a series is integral, its derivative is too"]
  f_period_integrals__fold_d_c_unfold["Folding and unfolding over double cosets (statement)"]
  f_orbital_bounds_conclusion__fold_d_c_unfold["Folding and unfolding over double cosets (proved from pieces)"]
  f_complex_double_coset["Double-coset unfolding for complex-valued functions"]
  f_cplx_d_c["The complex-valued unfolding identity (statement)"]
  f_double_coset_translation["Double cosets give a clean set of coset representatives"]
  f_fold_d_c_unfold_of["Double-coset unfolding follows from four lemmas and the simple case"]
  f_trans_exists["Four claims about coset representatives (statements)"]
  f_translation_independent["Coset representatives exist and sums over them are well defined"]
  f_global_geometry__is_cochar_lie["Definitions for tangent vectors of a split torus"]
  f_lie_chart["Definition of a Lie chart"]
  f_toroidal_compactification__is_grp_pullback["Definitions for group pullbacks and line bundles by gluing"]
  f_cubical_structures__cube_symmetric_swap_first["Line bundles by gluing, and cubical structures"]
  f_cubical_structures__cubical_pull_base_change_st["Pulling cubical structures back (statements)"]
  f_eventually_finite_base_change_filtered_colimit["Finiteness over the colimit already holds at a finite stage"]
  f_exists_presentation_matrix_of_projective_base_change["Projective base change gives a pair of matrices"]
  f_gen_fib_map_algebra_map["Maps between generic fibres"]
  f_is_z_mod_torsor_iff["Helpers for torsors and 'eventually' statements"]
  f_polynomial_system_eventually_solvable_colimit["Solutions in a colimit come from a finite stage"]
  f_projective_base_change_of_presentation_matrix_split["Two matrices make a base change projective"]
  f_projective_eventually_filtered_colimit_algebra["Projectivity over a colimit holds at a finite stage"]
  f_divisor_proofs__torsors_trivial_iff["Torsors are trivial iff they have a base-point map"]
  f_k_h_free_bad_finite_st["Finiteness of integer vectors with fixed block sums (statement)"]
  f_kleiman_ampleness__k_h_free_obj["Definitions for Čech chains on a multigraded polynomial ring"]
  f_p_k_h_free_bad_finite["Only finitely many vectors with fixed block sums and one sign per block"]
  f_kleiman_nefness__alg_defs["Definitions for Čech cohomology of multigraded rings"]
  f_kleiman_nefness__alg_s_free_st["Cohomology of graded pieces is finite and vanishes (statement)"]
  f_kleiman_nefness__ample_st["Global generation, ampleness and Siu-type claims (statements)"]
  f_kleiman_nefness__kleiman_st["Kleiman's nefness criterion (statements)"]
  f_multihomogeneous_ideals__is_field_intersection["Definitions of intersection-number families over a field"]
  f_period_integrals__explicit_formula["The explicit formula linking primes and zeros (statement only)"]
  f_explicit_formula__good_height_exists["Named steps for proving the explicit formula (statements only)"]
  f_l_growth_defs["What 'zeta grows at most like a power' means"]
  f_l_growth_gamma["A size bound for the Gamma function in a strip"]
  f_l_growth_f_e["Bounding L at 1−w by L at w, via the functional equation"]
  f_l_growth_zeta["Size bounds for (s−1)ζ(s), assuming a right-hand bound"]
  f_l_growth_main["Power-growth bound for Dirichlet L-functions, assuming a right-hand bound"]
  f_l_growth_final["Final packaging of the L-function growth bound"]
  f_foundations__not_coboundary_constant_one["The p-adic Laurent/roots-of-unity setting, and why 1 is not a coboundary"]
  f_laurent_series_eq_sum_single_mul_pow["Laurent series mod p are sums of t^j times p-th powers"]
  f_laurent_series_padic_exists_pth_power_combination["The same statement with p-adic coefficients, up to a multiple of p"]
  f_p_adic_completion_laurent_eq_sum_pth_powers_mod_p["Same decomposition for the completed ring"]
  f_frobenius_surjective_mod_prime_cyclotomic_kummer_tower["Everything in the root tower is a p-th power plus p times something"]
  f_cusp_span_norm_bounds__psi_e_def["Local data at a prime, and the residue characteristic"]
  f_period_integrals__tr_dual_loc["Statement of the local trace bound (statement only)"]
  f_d_surj_def["The map from Q_ℓ ⊗ K to the local field, and 'it is onto'"]
  f_t2_space_of_nonarchimedean_local_field["The tensor map is onto, via closedness of finite-dimensional subspaces"]
  f_trace_of_ker["Trace is unchanged by a surjection that the element respects"]
  f_is_integral_of_tmul_mem["The integral lattice inside Q_ℓ ⊗ K, and a denominator criterion"]
  f_trace_dual_local__is_integral_nat_cast["Lattice membership can be tested on powers"]
  f_trace_dual_local__imports["Proof of the local trace bound"]
  f_orbital_bounds_conclusion__tr_dual_loc["The local trace bound, assembled"]
  f_cusp_span_norm_bounds__point["Points as block anti-diagonal matrices built from a list"]
  f_cusp_span_norm_bounds__fraction_field_to_generic_stalk_algebra_map_eq["Local model for a quadratic algebra, with Gauss-type sums (definitions)"]
  f_twisted_trace_formula__inverse_chamber_map["Sign vectors, chains and roots, the geometry toolkit"]
  f_root_decompose_orthogonal["Roots split into a smaller root plus a multiple of another root"]
  f_gram_det_option_formula["A Gram determinant formula for a sheared family"]
  f_projection_erase_root_formula["Projection onto a span equals smaller projection plus the root part"]
  f_exists_root_involution_parabolic["Each chain extension has a partner extension (an involution)"]
  f_gram_root_determinant_erase["How a root-volume term changes when one root is erased"]
  f_parabolic_residue_sum_zero["The residue terms cancel in pairs"]
  f_commutative_algebra__flag_minor["Locally free lattices, dual generation and flag minors (definitions)"]
  f_commutative_algebra__lie_lattice_data["A bundle of lattices with compatibility conditions (definitions)"]
  f_x_pt_seq_lin["Image and kernel of a lattice map for a test-point datum"]
  f_hodge_kernel_image_lattice["Image and kernel lattice claim (restatement)"]
  f_algebra_statements__polarised_flag_statement["Flag claims for tight lattices of functions (statements only)"]
  f_herbrand_prime_order["Herbrand-style index identity for a map of prime order"]
  f_index_range_ker_iterate_endomorphism["Index and kernel size of a repeated group map"]
  f_norm_difference_index_identity["An index identity linking the norm and difference maps"]
  f_pow_index_torsion_finite_ker_range["Finiteness passes to the kernel and the range of a group map"]
  f_pow_prime_range_eq_iterated_difference["p-th powers equal the range of the (p−1)-fold difference map"]
  f_aff_char["Definitions for exponential polynomials and their degree pieces"]
  f_generators["Statement-only claims about pieces, substitution and generators"]
  f_matrix_entry_abs_sum_unitary_lie_coordinates_split["The coefficient-sum size of a polynomial behaves like a norm"]
  f_int_mv_polynomial_coeff_abs_sum_add_le["Size bound for the k-th degree piece of an exponential polynomial"]
  f_piece_add["The degree pieces add up, and a formula for a single term"]
  f_piece_hom["The k-th piece is a degree-k homogeneous polynomial"]
  f_aeval_single_zero["Renaming variables commutes with taking degree pieces"]
  f_gen_fund["Symmetrised monomials are polynomials in elementary symmetric functions"]
  f_gen_red["Reducing any monomial to small exponents, with a size bound"]
  f_gen_trunc["Trimming high-degree terms without increasing size"]
  f_coeff_l1_norm_nonneg["Symmetric polynomials as polynomials in elementary ones, with size control"]
  f_gen_pieces["Pieces of a symmetric expression are small polynomials in elementary symmetric functions"]
  f_gen_pieces_k["The same piece bound with extra parameter variables"]
  f_discharge["Turning three hypotheses into a height bound, conditionally"]
  f_gauss_jet_bounds__statement_k["Theorem A for a chosen frame (statement only)"]
  f_gauss_jet_bounds__statement_m["Theorem A at a generic point, and a generic-point existence claim (statements)"]
  f_gauss_jet_bounds__statement_p["Theorem A over the ℓ-adic complex numbers, via a frame-jet polynomial (statement)"]
  f_gauss_jet_bounds__statement_w["A product rule for jet bounds on independent variable sets (statement)"]
  f_global_twisting__link_exact_aff["Definitions for 'unimodular' lists and link exactness"]
  f_link_exactness_stability__sub_closed_and_perm_and_linear_equiv_invariant_uni_m["Unimodular lists are closed under dropping, reordering and invertible maps"]
  f_link_exactness_stability__cons_mem_uni_m_iff_map_sub_smul["A list with a unit-valued reader is unimodular iff its shifted tail is"]
  f_link_exactness_stability__link_in_uni_m_eq_shorter_of_form_eq_one["A link in the unimodular lists can be computed from a shorter list"]
  f_link_exactness_stability__seq_chain_boundary_prefix_chain["Boundary of a chain after adding a fixed prefix"]
  f_link_exactness_stability__seq_chain_cycle_retraction_of_link_exact["Pushing a cycle into a smaller family, using exact links"]
  f_link_exactness_stability__exists_homologous_cycle_with_entries_in_of_exact_at_links["A cycle is homologous to one living in the link of the empty list"]
  f_link_exactness_stability__seq_complex_exact_at_of_all_links_exact_at["If all links are exact, so is the whole complex"]
  f_exact_at_link_succ_union_translate_of_coord_one["Link exactness passes to the next size when a vector has coordinate one"]
  f_orbital_bounds_conclusion__sqf_roots_inj["Squarefree roots are injective, assembled"]
  f_period_integrals__sqf_roots_inj["The statement 'squarefree roots injective'"]
  f_squarefree_roots_injective__claim_of["Witness and count together give the claim"]
  f_div_count["Few polynomials are divisible by a given one"]
  f_two_pow_card_prime_factors_le["Small counting facts about primes and roots"]
  f_sum_sq_pow_le_two["Sums of e squared times t to the e are small"]
  f_card_le_sum_of_cover["Bad polynomials are covered by a countable-in-size family"]
  f_rpow_quarter_pow_four["The final size estimate for the counting bound"]
  f_wit_base["Powers of an element agree with their prime-part"]
  f_wit_main["Every bad polynomial has a witness"]
  f_charpoly_eq_finsum_psi["A function of the characteristic polynomial splits over invariant subspaces"]
  f_character_theory__invariant_subspace_mobius_inverse_charpoly_linear_equi["The quantity psi does not depend on the choice of basis"]
  f_finsum_mobius_inverse_charpoly_invariant_le["Summing psi over invariant subspaces inside a given one"]
  f_finsum_mobius_inverse_charpoly_transversal_subspaces["Summing psi over complements of a subspace"]
  f_sum_primitive_end_class_function_restrict_mixed_subspac["Mixed subspaces contribute zero to the sum"]
  f_is_primitive_end_class_function_invariant_subspace_mobi["Psi is primitive when s is additive"]
  f_gauss_jet_bounds__statement_u["A one-prime Gauss sum bound (statement only)"]
  f_minor_defs["Definitions for the minor formula"]
  f_minor_b["Derivative of a determinant, and commuting operators"]
  f_minor_core_a["Helper facts for the core determinant identity"]
  f_minor_core["Core formula for the determinant operator on 1"]
  f_minor_iter["Applying the determinant operator N times"]
  f_minor_formula["The minor formula, proved"]
  f_minor_formulas__cay_div_of["Cayley operator claims, stated only"]
  f_mollified_integrability__cls_gain_st["Six claims about a Cayley-type operator (stated only)"]
  f_misc_lemmas_p__imports["Powers of a matrix whose entries are operators"]
  f_anti_e_is_gl_rep["The negative-transpose of a matrix representation"]
  f_gelfand["The Gelfand invariants commute with everything"]
  f_gelfand_series["A power series for the Gelfand values"]
  f_gelfand_h_w["Gelfand invariants on a highest-weight vector"]
  f_tensor_v["Tensoring with the standard n-dimensional space"]
  f_partial_trace["Partial trace links powers on n copies to Gelfand invariants"]
  f_resolvent["The partial trace acts by residue-series coefficients"]
  f_tensor_representations__residue["Residue series as a sum of simple residues"]
  f_fock_resolution_onto__statement_c["Eight claims about restricting and projecting p-adic polynomials"]
  f_fock_resolution_onto__statement_e["Divided powers, mod-p conditions and lifting claims"]
  f_compact_casimir_bound_elementary_apply["The matrix of the commutator action of a unit matrix"]
  f_jet_harmonics__compact_casimir_le_tensor_operator_raise["A Casimir bound survives a tensor-style splitting, costing c plus s"]
  f_jet_harmonics__sum_norm_add_sq_le_of_bounds["Squared sizes add up like (c+s)²"]
  f_base_change_lift_class_function["Lifting a class function along a finite-field extension"]
  f_frobenius_shape_of_side_preserving["The lifted class function is well defined and twisted-invariant"]
  f_divisor_proofs__galois_twisted_norm_g_l_basic_properties["Basic facts about the twisted norm on matrices"]
  f_is_conj_of_is_conj_gl_field_extension_inclusion["Conjugate over a bigger finite field means conjugate over the small one"]
  f_divisor_proofs__nonempty_equiv_of_card_hom["Finite modules with equal counts of maps are isomorphic"]
  f_divisor_proofs__nonempty_linear_equiv_of_pi_fin_pow_finite["If l copies of M and of N match, so do M and N"]
  f_orbital_bounds_conclusion__prime_count["The prime-counting bound, assembled from two ranges"]
  f_chebyshev_prime_bounds_log_fact["Large range, y at least 131072, prime count below 1.26 y over log y"]
  f_count_succ_le["Small range, below 131072, via a checked certificate"]
  f_small_loop["A computer loop that checks the small range"]
  f_cay_dens_ex_cay_s["Statement that the Cayley chart carries Haar measure to a nearly constant density"]
  f_cay_dens_ex_cay_k["The Cayley claim follows from a density claim plus three side facts"]
  f_abhyankar_exists_fraction_localisation_normalisation["Every element of the local ring is a fraction of simple pieces"]
  f_abhyankar_exists_local_kummer_element["A hidden m-th root and a k-th power relation"]
  f_abhyankar_ramification_idx_eq_one["Adjoining a root of π kills the ramification (Abhyankar's lemma)"]
  f_abhyankar_root_mem_maximal_ideal_non_zero_divisors["The adjoined root is small but not a zero-divisor"]
  f_divisor_proofs__is_artinian_ring_kummer_adjoin_root_quotient_root["A certain two-step root extension, modulo its root, is Artinian"]
  f_kummer_unit_radicand_quotient_root_is_reduced["The same quotient has no non-zero nilpotents"]
  f_maximal_ideal_localization_eq_span_of_reduced_artinian_a["Reduced and Artinian quotient makes the local maximal ideal principal"]
  f_maximal_ideal_span_image_uniformizer["Pushing a uniformizer forward generates the maximal ideal"]
  f_uniformizer_eq_pow_ramification_idx_mul_unit_integral_cl["π is a unit times ϖ to the ramification index"]
  f_cauchy_parallelogram_upper_half_plane["Integrals around a slanted parallelogram add up"]
  f_eichler_integral_from_i_tail_exponential_decay["The Eichler integral is a fixed polynomial plus a tiny tail"]
  f_eichler_period_polynomial_limit_at_cusp["Eichler integrals under a modular change settle to a polynomial at the cusp"]
  f_integrable_on_vertical_ray_norm_integral_le["A function that decays exponentially has a convergent, bounded ray integral"]
  f_poly_degree_slash_action_right_action_properties["A matrix acting on polynomials of bounded degree"]
  f_top_side_integral_tendsto_zero["The top edge of the parallelogram shrinks to nothing"]
  f_ext_v_statement["Maps over the fraction field extend over a complete valuation ring (claim only)"]
  f_toroidal_compactification__two_weight_eq_one_add_root["Vocabulary for the CM-field family of abelian schemes"]
  f_extension_descent__const_gen["Theta groups and the Weil pairing condition (definitions)"]
  f_extension_descent__nonzero_locus["Ample, rigidified and symmetric line bundles on group schemes (definitions)"]
  f_rt0_conj_neg_ne_zero["The chosen square root of −d is purely imaginary"]
  f_conjugate_root_zero_second["The chosen square root of −d is purely imaginary (second proof)"]
  f_abs_zeta_prime_sum_error_le_of_large["Error bound for prime sums when the cutoff is large"]
  f_abs_zeta_prime_sum_error_le_of_one_le["A crude bound on the prime-sum error for every y at least 1"]
  f_gz_p_n_t_of["Prime-sum error is small, given the zeta-function inputs"]
  f_integral_eq_interval_integral_add_compl["Splitting an integral, and a triangle-inequality identity"]
  f_norm_integral_compl_le["Tail integrals and small exponential/logarithm estimates"]
  f_riemann_zeta_ne_zero_of_mem_rectangle["Size bounds for the integrand on each side of the rectangle"]
  f_is_full_level_at["The 'full level' condition for a point on an abelian scheme"]
  f_conjugate_root_zero_third["A square root of minus d is purely imaginary"]
  f_cor_a3prime_b["Lifting a good polynomial from a quotient (statement only)"]
  f_jacobi_path_weights__defs_col["Words of wedge and contraction steps, defined"]
  f_jacobi_path_weights__det_letters["Valuations on polynomials from a diagonal rescaling, defined"]
  f_jacobi_path_weights__index_weights_dominance["Path polynomials, their space, and counting claims (statements)"]
  f_jacobi_path_weights__lift_word["Lifted words, minors and a 'frame' rescaling, defined"]
  f_jacobi_path_weights__statement_a["Tableau minors and path polynomials (statements)"]
  f_jacobi_path_weights__statement_b["Strip paths, columns and 'lowest part' claims (statements)"]
  f_jacobi_path_weights__statement_e["Valuation rules and divisibility by letter determinants (statements)"]
  f_jacobi_path_weights__statement_p["Counting Gelfand–Tsetlin patterns and paths (statements)"]
  f_jacobi_path_weights__valuation_products_components["Equivariance, truncation and index-weight claims (statements)"]
  f_conjugate_root_zero["Complex conjugation sends the chosen root to its negative"]
  f_dual_lattices__map_smul_one_mul_vec["Turning a matrix identity into integrality facts"]
  f_dual_lattices__moduli_points_state["Dual pairs of rings and 'height' (definitions and one claim)"]
  f_dual_lattices__nset_exp_injective_surjective["A tower of rings, and a claim that pairings agree with heights (statement)"]
  f_one_add_pow_of_sq["Proof of the pairing-versus-height claim, assuming two statements"]
  f_dual_lattices__series_state["Basic properties of the pairing (statement only)"]
  f_dual_lattices__sq_zero_of_span["Local algebras, the abstract group functor, and the pairing (definitions)"]
  f_dual_lattices__st_thm_a["Theorem A at one level: a proof from the tangent pairing formula"]
  f_dual_lattices__st_thm_a_full["Theorem A in matrix form (statement only)"]
  f_dual_lattices__tangent_pairing_statement["The tangent pairing formula (statement only)"]
  f_thm_a_full["Proof of Theorem A in matrix form, from two assumed statements"]
  f_smooth_group_tangent_lift["A smooth group has a nice local chart around its identity section"]
  f_nontrivial_transvection["Transvection rules, and examples of what is and is not one"]
  f_exists_isotropic_basis_nonorthogonal_two_vectors["A basis of 'null' vectors, none orthogonal to two given vectors"]
  f_quasi_reflection_eq_mul_transvections_of_hyperbolic_pla["A reflection in a plane is a product of transvections"]
  f_quasi_reflection_eq_unitary_transvection_mul["Any two quasi-reflections differ by a product of transvections"]
  f_special_unitary_hyperbolic_plane_mem_transvections["Helper definitions for a two-dimensional plane (no theorems)"]
  f_unitary_transvection_submonoid_normal_det_one["Transvection products form a normal set of determinant-one unitary matrices"]
  f_exists_coordinate["Elements of Q[√−d] have two rational coordinates"]
  f_one_letter_gauss_jets__statement_f["Theorem A for a chosen frame, and at a generic point (statements only)"]
  f_differentiable_class_function_param["A parameter family is smooth in z, and a vanishing factor can be pulled out"]
  f_iterated_deriv_zero_of_bound["Small near zero forces the first derivatives to vanish"]
  f_s_prime_of["Extending a Gaussian-type integral to all complex z, assuming six claims"]
  f_continuous_herm["Toolbox for integrals with a complex power, differentiable in z"]
  f_differentiable_of_top["Repeated derivatives, a nice class of functions, and repeated integration by parts"]
  f_mem_right_inv_right_twisted["Four spaces of 'twisted invariant' functions on a group"]
  f_mem_tw_inv["Spaces of cocycles, extensions and a three-term relation"]
  f_finrank_twisted_left_invariant_mul_of_free_action["Counting twisted invariant functions when the action is free"]
  f_finrank_order_three_relation_add_twisted_invariant_le["Dimension bound linking the three-term relation to twisted invariants"]
  f_finrank_cocycle_extension_le_order_three_relation_add["Dimension bound for extensions of cocycles"]
  f_finrank_cocycles_add_twisted_invariant_le_extension["Cocycles plus twisted invariants fit inside the extensions"]
  f_finrank_eichler_shimura_cocycles_le_gamma1["Size bound for Eichler-Shimura cocycles on a level-N subgroup"]
  f_fundamental_domains__signature["Vocabulary for Hermitian forms over a CM field and a fundamental domain"]
  f_hermitian_trace_forms__exists_orthogonal_basis_dot_product_apply_eq["Hermitian forms can be diagonalised by a change of basis"]
  f_exists_anisotropic_orthogonal_basis_hermitian["A Hermitian form over a number field has an orthogonal basis of non-null vectors"]
  f_exists_quasi_reflection_prod_mul_vec_eq["Moving one vector to another with at most two reflections"]
  f_unitary_matrix_eq_prod_quasi_reflections["Every form-preserving matrix is a product of quasi-reflections"]
  f_product_formula_haar__norm_mod["The Haar modulus of a local field, and two stated counting claims"]
  f_norm_index["Proof of the index formula for a local field"]
  f_card_quotient_eq_abs_norm["Proof that residue-class counts equal an ideal norm"]
  f_mod_f_iota_finite_place["Haar modulus on a local field matches the p-adic absolute value"]
  f_product_formula_haar__res_char_iff["Four stated claims about local fields (definitions only)"]
  f_norm_st["Haar modulus equals the p-adic absolute value, with no assumptions left"]
  f_product_formula_haar__tr_base["Local fields over a prime l, and three stated trace claims"]
  f_period_integrals__prod_formula_e["The product formula over all primes, stated only"]
  f_w0_eq_of_rt_eq["Two small facts, about good primes and the trace on the complex numbers"]
  f_period_integrals__iso_inv_metric["The claim that the natural length is the only invariant one"]
  f_orbital_bounds_conclusion__iso_inv_metric["The invariant-length claim, now proved"]
  f_col_choice_fintype["Finiteness, and a list of small named claims"]
  f_hermitian_vector_map["Acting on the special vectors just changes the matrix"]
  f_hv_scalar["Triangular data gives a multiple of the standard vector"]
  f_iso_inv_metric_of_hw["The invariant-length claim follows from the weight claim"]
  f_metric_constant_bound["Cauchy-Binet for rectangular matrices"]
  f_oe_eq_of_range_sub["The diagonal rule and the norm of the standard vector"]
  f_poly_eq_zero_of_circle["The weight claim, proved by a circle trick"]
  f_quotient_rank["Any matrix can be made upper triangular by a unitary one"]
  f_symmetric_measure_l2_norm_eq_resolution_l2["The invariant-length claim, assuming its ingredients"]
  f_vnu_map_zero["Basic rules for acting by matrices on the vector tables"]
  f_mem_range_of_integral_at_height_one_over["Integral at the codimension-one primes above one element"]
  f_mem_reg_at_of_codim_one["Being regular at a point can be checked at codimension one"]
  f_line_lattice_generator_codim_one["A generator of a line lattice, checked in codimension one"]
  f_scheme_cohomology__regular_local_domain["Regular local rings are domains; cutting by a good element stays regular"]
  f_scheme_cohomology__regular_u_f_d_serre["Regular local rings have finite projective dimension (Serre)"]
  f_scheme_cohomology__regular_u_f_d_localization["Localising a regular local ring at a prime stays regular"]
  f_st_adic_completion_regular["Claim - completing a regular local ring keeps it regular"]
  f_st_derivation_adic_completion["Claim - a derivative extends to the completion"]
  f_st_derivation_cotangent_independent["Claim - a nonzero Jacobian gives independent directions"]
  f_complex_analytic_sets__st_flat_normal_fibres["Claim - flat with normal fibres implies normal"]
  f_complex_analytic_sets__st_formal_fibres_regular["Claim - formal fibres of finite-type algebras are regular"]
  f_st_formal_fibres_regular_polynomial["Claim - the same, for polynomial rings"]
  f_complex_analytic_sets__st_jacobian_prime_derivations["Claim - every prime has equations with a nonzero Jacobian"]
  f_st_regular_quotient_independent["Claim - cutting by independent elements keeps a ring regular"]
  f_p_formal_fibres_regular_polynomial["Formal fibres of polynomial rings are regular, given five claims"]
  f_link_exactness_stability__seq_chain_cycle_bounded_by_cone["Cone trick - a cycle becomes a boundary"]
  f_exact_at_of_links_outside_exact_at_of_coned["Exactness from exactness of links plus a cone point"]
  f_exact_at_link_nil_coord_subspace_union_translate["Exactness of the link of the empty list in low and affine pieces"]
  f_divisor_base__omega_factorization["Hecke Eisenstein series over a totally real field - setup"]
  f_divisor_proofs__k_fac_differentiable["Definitions for the zero-frequency part, and the factor is smooth"]
  f_hecke_phi_fourier_constant_at_zero_zero["The Fourier constant vanishes at zero"]
  f_divisor_proofs__hecke_phi_fourier_constant_at_zero_differentiable_on["The Fourier constant is complex-differentiable in sigma"]
  f_is_smooth_holomorphic_in_sigma_family_mul_left["Multiplying a good family by a holomorphic factor"]
  f_divisor_proofs__is_smooth_holomorphic_in_sigma_family_add["The sum of two good families is good"]
  f_upper_half_plane_product_prod_im_rpow_cont_diff_on["Product of powers of imaginary parts is smooth"]
  f_prod_im_iterated_wirtinger_deriv_word_differentiable_on["Derivatives of the imaginary-part product stay holomorphic in sigma"]
  f_hecke_eisenstein_zero_frequency_part_is_smooth_holomorphic["The zero-frequency part is a good family"]
  f_hecke_eisenstein_zero_frequency_part_is_smooth_holomorp_statement["Statement - the zero-frequency part is smooth and holomorphic"]
  f_divisors₂__partial_zeta_functional_equation["Published claim - functional equation for partial zeta functions"]
  f_ferrand_pushout_affine_flat_and_pushouts["Gluing flat families over a thickened point, on affine pieces"]
  f_flat_ferrand_pushout_over_fibre_product["Gluing flat families over a fibre product of rings (global version)"]
  f_flat_quotient_smul_top_of_surjective_flat["A quotient of a module stays flat over the quotient ring"]
  f_is_pullback_of_forall_is_pushout_app["A square of spaces is a pullback if it is so on every affine piece"]
  f_is_pushout_app_l_e_of_is_pullback_of_is_affine["Pullbacks of spaces give pushouts of rings on affine pieces"]
  f_mul_tensor_injective_of_flat_base_change_ker_inf["Multiplying into a module is injective when a quotient is flat"]
  f_r_tensor_injective_of_pow_smul_eq_bot["Flatness lifts across a nilpotent ideal"]
  f_schlessinger_flat_fibre_product["Schlessinger's flatness for fibre products of rings"]
  f_base_change_kernels__affine["Base change of affine pieces and of a monoid-algebra description"]
  f_pt_af_type_main["Description of 'af' and 'hh' lattices via a matrix (restated)"]
  f_x_pt_af_type["Membership in the 'af' and 'hh' lattices, proved by matrix change of basis"]
  f_divisor_base__trace_dual_different["Trace dual, covolume and the Lipschitz formula (definitions and basics)"]
  f_exists_equiv_fourier_classes_pos_cone_summand["Matching Fourier-term classes with points of a positive cone"]
  f_exists_equiv_lattice_classes_fibre_summand["Matching lattice-term classes with a fibre over each class"]
  f_hilbert_eisenstein_nonconstant_terms_has_sum["Non-constant terms of a Hilbert Eisenstein series converge to a cone sum"]
  f_lattice_sum_eq_cone_sum["For each fixed class, the lattice sum equals a constant times the cone sum"]
  f_lipschitz_constant_inverse_different_eisenstein["The Lipschitz constant matches the Eisenstein normalising constant"]
  f_mem_trace_dual_signed_positive_cone_iff_totally_positive["The signed dual cone is the totally positive cone"]
  f_rep_ne_zero["Chosen representatives of nonzero elements modulo units"]
  f_dense_coordinate_torus["Points with all coordinates nonzero are dense"]
  f_integral_ang_meas["Averaging around a circle as an integral against a probability measure"]
  f_section_boundary_closed_and_codense["The zero set of a section is closed with dense complement"]
  f_snc_boundary_coordinate_chart["Near any point, the boundary is a set of coordinate hyperplanes"]
  f_levi_forms__is_reg_family_inhabit_statement["Statements about smoothing plurisubharmonic weights (many claims, no proofs)"]
  f_plurisubharmonic_functions__is_psh_locally_integrable_statement["Plurisubharmonic functions, definitions and unproved basic claims"]
  f_potential_theory__psh_shift_a["Rules for the Levi form (second derivative in complex directions)"]
  f_root_power_sum_character_additive_and_x_sub_one_pow["Sums of powers of roots are additive on products and equal j on (X-1)^j"]
  f_divisor_proofs__exists_block_parabolic_subgroup_levi_projection["Block-triangular matrices form a subgroup that projects onto the diagonal blocks"]
  f_pairing_cuspidal_character_g_l_root_power_sum_character["Pairing a product of cuspidal characters against root power sums"]
  f_pairing_harish_chandra_induction_charpoly_function["Pairing an induced class function with a function of the characteristic polynomial"]
  f_twisted_harish_chandra_induction_g_l_is_twisted_class_fun["Induced and characteristic-polynomial functions are conjugation-invariant"]
  f_compact_casimir_bound_embedded_component["A size bound on a piece carries over to the whole stacked space"]
  f_tensor_product_action["Letting a ring act on a base-changed space (definitions, one unproved claim)"]
  f_iota_scalar_one["Matrix bookkeeping definitions, plus two trivial facts"]
  f_charpoly_eq_quotient_charpoly_pow["Characteristic polynomial equals that of the quotient, raised to a power"]
  f_cyclic_generators_invariant_top["A few vectors generate everything under two commuting matrices"]
  f_exists_cyclic_generators_separable_min["N vectors generate a space when the polynomial is a separable power"]
  f_c_m_type_galois__statement_field["Claims about fields built from square roots (statements only)"]
  f_c_m_type_galois__statement_group["Counting 'CM types' in a finite group (statements only)"]
  f_quad_discr["Discriminant of a quadratic field with a square-root generator"]
  f_dirichlet_density__statement["Prime densities and discriminant claims (statements only)"]
  f_omega_poly["Two small definitions for quadratic fields"]
  f_dedekind_factor_k["Lattice sums and a factorisation claim (definitions, claims unproved)"]
  f_lat_i_top_basis["The integers of Q(√-d) form a lattice of area √d/2"]
  f_formalism__statement_c_m["CM types modulo a prime (statements only)"]
  f_p_holomorphic_kernel_fibre["Near a point, a map is constant along a slice of the kernel's size"]
  f_p_injective_holomorphic_inverse["An injective holomorphic map is open with a holomorphic inverse"]
  f_st_holomorphic_kernel_fibre["Statement: slices where a map is constant to first order"]
  f_st_injective_holomorphic_inverse["Statement: injective holomorphic maps have holomorphic inverses"]
  f_st_injective_holomorphic_jacobian_ne_zero["Statement: an injective holomorphic map has nonzero Jacobian"]
  f_st_injective_holomorphic_open["Statement: injective holomorphic maps are open, with an example"]
  f_cyclic_kummer_norm_fixed_hilbert90["Basic facts for a cyclic p-th root extension, including Hilbert 90"]
  f_adelic_lattice_proofs__exists_superset_mem_s_units["A finite set of primes can be enlarged so given numbers are units outside it"]
  f_exists_unit_valuation_eq_of_adm["Choosing a number with prescribed prime-by-prime sizes"]
  f_galois_places_transitive["Symmetries act on the primes over a prime, and reach them all"]
  f_hilbert90_s_units_kummer["Hilbert 90 with prime-restricted units in a Kummer extension"]
  f_valuation_unramified_kummer_of_coprime_unit["Kummer extensions do not change sizes at primes not dividing p or δ"]
  f_adelic_lattice_proofs__with_zero_eq_of_le_exp_iff["Valuations compared through ideals, and conjugate primes"]
  f_compact_casimir_bound_projection_dual_tensor["A Casimir bound survives projecting a dual tensor"]
  f_p_poly_local_generators_diff["Slopes of polynomials at a point, and tangent directions"]
  f_arithmetic_bezout__statements["Definitions and claims for heights of shapes (Chow forms)"]
  f_statements_poly_local_generators["Claim - a prime shape is locally cut out by few equations"]
  f_p_jacobian_prime_derivations["Jacobian prime claim follows from four smaller claims"]
  f_st_cotangent_basis_in_prime["Claim - a prime has generators giving a cotangent basis"]
  f_st_derivation_minor_of_detection["Claim - detecting derivations yield a nonzero determinant"]
  f_st_local_generators_clear_denominators["Claim - local generators work globally after one factor"]
  f_st_poly_derivations_detect_square["Claim - derivations detect second-order vanishing"]
  f_complex_analytic_sets__statements_area["Claims about area and volume of complex shapes"]
  f_local_hermitian_forms__even_val["Local setting for counting lattices with a twisted form"]
  f_local_hermitian_forms__is_fix_map_iff["Fixed lattices are carried to fixed lattices by compatible maps"]
  f_local_hermitian_forms__lcount_norm["A list of claims about the local counts (stated, not proved)"]
  f_local_orbit_counts__dat_smul["Rescaling the form keeps the data admissible"]
  f_local_orbit_counts__descent["Integral elements of the quadratic extension, described by coordinates"]
  f_split_m["Multiplying the form by a unit does not change the count"]
  f_local_orbit_counts__w_trans["Equal weighted counts across a matching of orbits"]
  f_local_hermitian_forms__norm_one_is_coboundary_unramified_quadratic["Setup for local counts, plus many stated claims"]
  f_split_unit_elements__split_s["A fixed lattice splits into its two coordinate pieces"]
  f_divisors__gal_map_mul["Cohomology toolkit and the Galois action on it"]
  f_divisors__ind_et_of_forall_finset["More cohomology definitions; ind-etale from finite pieces"]
  f_galois_geometry__is_matrix_form["Galois action on pro-etale cohomology as matrices"]
  f_galois_geometry__is_strictly_semistable_alt["Transfer maps, roots-of-unity sheaves, semistable reduction"]
  f_divisor_proofs__preserves_filtered_colimits_add_comm_grp_iff_elements["Preserving filtered colimits, checked element by element"]
  f_preserves_filtered_colimits_module_cat_iff_forget_iff_el["The same filtered-colimit criterion for module-valued functors"]
  f_moduli_proofs__is_ind_etale_of_forall_finset["A union of etale pieces is ind-etale"]
  f_divisor_proofs__comap_maximal_ideal_eq_origin["Base-change tools; the strict henselisation sits over the origin"]
  f_etale_at_prime_base_change_of_integral_closure_etale["Etale at a prime is preserved by base change"]
  f_divisor_proofs__is_z_mod_torsor_finite_projective_base_change["A cyclic torsor stays a torsor after base change"]
  f_orbital_bounds_conclusion__self_dual_loc["The 'self-dual at each prime' claim, packaged as a theorem"]
  f_period_integrals__self_dual_loc["What 'self-dual at a prime' means (a stated claim)"]
  f_self_dual_local_basis__assembly["Assembling the self-dual claim from smaller claims"]
  f_dual_basis["Names for the local pieces and the six sub-claims (stated)"]
  f_hform_sum_right["The pairing is additive and scales correctly"]
  f_hvec_apply["A pairing with no blind spots gives a dual basis"]
  f_self_dual_local_basis__loc_basis["A local basis exists (borrowed from the padded-families lemma)"]
  f_self_dual_local_basis__nondeg["The pairing has no blind spots on a lattice with a dual"]
  f_one_tmul_mem_oloc["Twist-stability and local units, proved"]
  f_self_dual_loc_of_dirs["Forward and backward halves give the 'if and only if'"]
  f_self_dual_loc_of_loc_basis["Chaining all the steps from a local basis to the self-dual claim"]
  f_pad_fam["Padding a short generating family up to n vectors; the local basis theorem"]
  f_alternating_coefficient_formula["A formula for one signed coefficient of a power times a linear form"]
  f_hook_functional_power_sum["The 'hook' functional on (power sum × G) equals the degree of G"]
  f_hook_functional_power_sum_other["The hook functional kills the 'wrong' power sums"]
  f_kappa_formula_hook_schur["An explicit formula for the pairing 'kappa', via hook and Schur ideas"]
  f_uniform_theta_substitution__odd_log_relation["Power-series definitions and stated identities for a rescaled logarithm"]
  f_uniform_theta_substitution__cyclic_power_class_of_exp_equiv["Statements about the theta substitution and a 'class' of power series"]
  f_uniform_theta_substitution__statement_m["Statement of an exact substitution formula and of 'places add'"]
  f_places_add_class["Statement of 'places add' for classes of power series"]
  f_tensor_relations_g_l__k_type_data["Vocabulary for tensor-product models of gl(n)"]
  f_tensor_relations_g_l__step_formula["A list of stated claims about tensor products of gl(n) actions"]
  f_casimir_bounds__expand["Expanding the Casimir operator into identity plus swaps"]
  f_re_swap_sum_le["Swapping one box with an antisymmetric group never gains length"]
  f_count_same["Counting boxes in the same column and the same row label"]
  f_count_cross["Bounding cross-column terms, and the combined counting bound"]
  f_cas_bound_holds["The Casimir bound, proved"]
  f_unramified_integrals__mod_defs["Definitions for modular forms, j and q-series with integer coefficients"]
  f_unramified_integrals__mod_basic["Basic facts about modular-form notions, roots of unity and divisor triples"]
  f_unramified_integrals__mod_delta_int["The q-series of Δ has integer coefficients"]
  f_unramified_integrals__mod_eis_int["E4 and E6 have the classical integer q-series"]
  f_unramified_integrals__mod_g_eis["Lattice Eisenstein sums and g2, g3 in terms of E4, E6"]
  f_unramified_integrals__mod_j_tau["The j-invariant of a lattice equals j(τ)"]
  f_unramified_integrals__mod_q_prin["Integral q-series means integral polynomial in j (q-principle)"]
  f_c_m_good_models__statement["Statements about complex multiplication and good p-adic models (stated)"]
  f_is_fam_const_level_one["A constant family of modular forms transforms correctly"]
  f_k_h_free_indep_st["Independence of the 'pieces' in a Čech chain group (statement)"]
  f_p_k_h_free_indep["Proof that the Čech pieces are independent"]
  f_regular_local_ring_fraction_field["A field is the fraction field of its local ring at a point"]
  f_geometry_proofs__spec_stalk_specializes_comp["Regular subrings and how they behave when a point specializes"]
  f_rep_g_apply["Definitions for matrices acting on polynomials, and a 'swap'"]
  f_th_facts["The list of trace claims about symmetric powers (statements only)"]
  f_coeff_scale["Proof that degree-homogeneous means every monomial has that degree"]
  f_fin_m_h["Proof that the homogeneous polynomial spaces are finite-dimensional"]
  f_mem_homogeneous_exponents_one_block["Trace of a map on homogeneous polynomials as a sum over monomials"]
  f_h_option["Proof of the two-variable formula for complete symmetric polynomials"]
  f_hq_three["Proof of the three-variable formula with one variable equal to 1"]
  f_homogeneous_trace_diagonal["Proof that the trace on degree-n polynomials is h_n of the eigenvalues"]
  f_tr_swap["Proof of the trace formula for a product with the swap"]
  f_twine_c["Proof of the 'twined' trace formula for 3×3 matrices"]
  f_eps_of_c_zero["Damped versions of the exponential and the epsilon factor"]
  f_gamma_function_bounded_support["The cone-sum function vanishes outside a bounded region"]
  f_exponential_gamma_integral_formula["Integral of a damped exponential against the cone-sum function"]
  f_gamma_integral_alternating_sum["Integral of the exponential against the cone-sum function, with damping removed"]
  f_epsilon_alternating_sum_zero["The alternating sum of epsilon-factor products vanishes"]
  f_gauss_jet_bounds__statement_y["Theorem B for Gauss sums, as a p-adic size bound (statement)"]
  f_cube_map_triple_product_unique["A cube map is pinned down by its first component"]
  f_p_eq_q_of_neg["Two linear-algebra facts about maps that square to a scalar"]
  f_discrete_valuation_numbers__objects["Multi-graded polynomial rings, cycles and intersection numbers over a DVR"]
  f_statements_clopen_components["Statement - a clopen piece of the complex points is a union of components"]
  f_statements_component_degree["Statement - integrating over one component gives its intersection number"]
  f_statements_components_additive["Statement - the integral over a union of components is the sum"]
  f_statements_int_num_components["Statement - intersection numbers add over components"]
  f_statements_clopen_degree["Statement - integral over a clopen piece equals an intersection number"]
  f_p_clopen_degree["Clopen degree follows from four component claims"]
  f_intersections__statements["Degree of a generic fibre, and checks that the hypotheses are not empty"]
  f_birational_geometry__inter_st["Arithmetic intersection theory - stated claims and four test values"]
  f_adelic_euler_products__count_data["Definitions for theta series, Eisenstein series and lattice-point counting over a number field"]
  f_cusp_representatives_finite["Finitely many matrices complete any pair to a determinant-one matrix"]
  f_exists_cusp_reduction_bound["A small pair (c, d) exists for every upper-half-plane tuple"]
  f_mobius_action_upper_half_plane["Matrices of determinant one act on the upper half-plane"]
  f_unit_balancing_imaginary_parts["Multiplying by a unit balances the imaginary parts"]
  f_reduction_to_siegel_domain["Every point can be moved into a balanced, high-up region"]
  f_fock_resolution_onto__statement_d["Operators on p-adic polynomials, and ten stated claims about them"]
  f_e_arith["A counting inequality for exponents, proved by induction"]
  f_bijective_linear_combination_of_rank_at_stalk["Generators of the right count form a basis"]
  f_exists_open_affine_hilbert_chart_basic_locus["The 'good' chart locus is open (and compact when it should be)"]
  f_free_module_complement_support_compact["The 'bad set' complement is compact"]
  f_is_pullback_pb_map["Pulling a family back along a map gives a pullback square"]
  f_mem_support_quotient_iff["Where a quotient is nonzero survives base change"]
  f_mem_support_quotient_span_iff_of_is_pushout["Same base-change fact, for ring squares"]
  f_sections_finite_flat_rank_of_finite_flat["Finite flat maps stay finite flat on affine pieces"]
  f_support_of_quotient_flat_module["Compactness of where chosen elements generate a flat module"]
  f_tangent_vector_of_dual_hom["Tangent vectors at a point of a group, as ring maps to dual numbers"]
  f_continuous_on_cos_sq["The 'cosine squared' of a line varies continuously"]
  f_cosine_square_pushforward_uniform["Squared cosine is uniformly spread on 0 to 1"]
  f_local_density_bound_near_point["Squared cosine has a bounded density near any point"]
  f_foundations__exp_upper["A 'tower' of modular-function fields, and Möbius maps"]
  f_foundations__letter["Operators on p-adic function spaces, and the alphabet of Hecke letters"]
  f_foundations__op_l_d_one_sub_mem_triv["Slash action, 'potential' functions, and the semisimple condition"]
  f_foundations__is_root_one["Kummer-type conditions and cocycle vocabulary"]
  f_foundations__eigen_of_two_step["A two-step eigenvector test"]
  f_foundation_proofs__gl_two_pos_rat_mobius_basic_laws["Möbius maps preserve the upper half-plane and compose"]
  f_kummer_class_eval_eq_zero_of_vanishing_on_congruence["A Kummer class that is trivial on a congruence subgroup vanishes"]
  f_kummer_potential_relation_trivial_eq_zero["A trivial potential gives the zero class"]
  f_map_eisenstein_div_period["Eisenstein series scale correctly under a field automorphism"]
  f_harish_chandra_induction_g_l_trivial_orthogonal_hyperpl["Inducing the constant function gives zero against a 'hyperplane-free' character"]
  f_gauss_jet_bounds__statement_s["Setup for Theorem A over the l-adic numbers, and a statement of it (not proved)"]
  f_gauss_jet_bounds__statement_v["Theorem A as a bound on any bounded linear measurement (statement only)"]
  f_gauss_jet_bounds__statement_x["Theorem A as a bound on any bounded measurement, without the saturation assumption (statement only)"]
  f_p_n_t_dens_ls_a["A series with bounded partial sums converges for positive real part (Abel summation)"]
  f_l_function_bounds_proofs__l_function_eq_g_of_one_lt["A Dirichlet L-function equals its Abel-summed series for positive real part"]
  f_l_function_bounds__positivity_bound["A list of named claims about L-functions and character sums (statements only)"]
  f_l_function_bounds__statement["Triple-sum setup and unproved claims about prime moduli l (statements only)"]
  f_formalism__statement_f_l["Landau-style claims for a family of Dirichlet characters (statements only)"]
  f_formalism__statement_u["Landau-type zeta claims with smoothed prime-sum errors (statements only)"]
  f_formalism__zeta_nonvanishing_chebyshev_weights["Zeta has no zeros, assuming a one-sided bound on Chebyshev-weighted averages (statement only)"]
  f_formalism__zeta_nonvanishing_general_weights["Zeta has no zeros, assuming a bound on some positive weighted average (statement only)"]
  f_augmentation_quotient_equiv_lattice["A quotient of lattices is a quotient of coordinate vectors by a sublattice"]
  f_comap_fg_of_valuation_ring["Over a valuation ring, a preimage of a finitely generated submodule is finitely generated"]
  f_form_mem_lin["Integer forms give functions that are additive mod p; finiteness and quotient identification"]
  f_misc_lemmas_l__imports["Inside a span over the fraction field, some nonzero multiple lands in the original module"]
  f_dual_lattices__exists_smul_mem_of_mem_span["Lattices over a valuation ring are finitely generated, free, and have projections"]
  f_period_integrals__fgl_gram["Formal-group setup and the 'Gram formula' claims (statements only)"]
  f_period_integrals__fgl_ph_split["The same formal-group setup over any field, and the 'splitting' target (statement only)"]
  f_ph_dual_gram["The phase formula for a dual pair of bases, by citing its proof"]
  f_dual_gram_substitution__be_mul_by_zero["Bookkeeping lemmas for addition in the formal group, including scaling by zero"]
  f_dual_gram_substitution__has_subst_ren["Renaming the variables of a power series respects the formal group operations"]
  f_ph_dual_gram_main["Proof that the Gram formula passes to a dual pair of bases"]
  f_formal_group_splitting__add_preserves_exp_congruence["Exponentials turn sums into products, so congruences can be added"]
  f_formal_group_splitting__development["Splitting target reduced to three smaller steps"]
  f_formal_group_splitting__exp_congruence_extends_to_sum["A congruence in some variables stays true when extra variables are added"]
  f_formal_group_splitting__orthogonal_split_polarization_vanishes["Inverse series, and the correction term vanishes for orthogonal families"]
  f_exists_kummer_character_of_upper_half_plane_root["A root of a modular function gives a 'Kummer character'"]
  f_foundation_proofs__upper_half_plane_holomorphic_germ_properties["Smooth functions on the upper half-plane are rigid"]
  f_exists_eichler_shimura_potential_of_homogeneous_poly_co["A cocycle on the upper half-plane has a 'potential'"]
  f_gamma1_cap_gamma0_level_acts_freely_upper_half_plane["Level-N matrices never fix a point of the upper half-plane"]
  f_flag_measures__prim_of_is_unit_det["Vocabulary for Hermitian dot products over a finite ring"]
  f_exists_primitive_add_char_involution_invariant["A nondegenerate additive character that ignores conjugation"]
  f_is_primitive_tuple_of_linear_independent_finite_ring["Linearly independent vectors over a finite ring are primitive"]
  f_norm_gauss_sum_hermitian_form_linear_le["A Gauss sum over a Hermitian form has size at most q^n"]
  f_card_hermitian_quadric_affine_subspace_residue_ring["Counting solutions of one Hermitian equation plus linear conditions"]
  f_ncard_dependent_vectors_affine_gram_le["Few solutions are linearly dependent on the given vectors"]
  f_card_primitive_tuple_extensions_le["Counting ways to extend a primitive list by one vector"]
  f_ncard_primitive_tuples_with_gram_matrix_residue_ring["Counting lists of vectors with a prescribed Gram matrix"]
  f_form_off_variety_mul["Products of 'forms off the variety' are again such forms"]
  f_rational_sup_metrics__aeval_coord_prod["Bookkeeping for multi-homogeneous polynomials"]
  f_is_form_off_mul["A product of two forms off a point is off the point"]
  f_k_h_free_decomp_st["Statement - Čech chains split into embedded block pieces"]
  f_p_k_h_free_decomp["Proof that Čech chains split into block pieces"]
  f_foundation_proofs__diag_mod["Level-M invariance, integrality and 'diagonal mod M' vocabulary"]
  f_exists_unit_eval_eq_kummer_class["Every element of a certain span is the 'class' of a locally-power unit"]
  f_local_power_units_tower_closure_properties["Units that are m-th powers 'up to size one' everywhere are closed under the usual operations"]
  f_foundation_proofs__tower_unit_class_mod_prime_pow_properties["The class of a unit modulo l^n behaves like 'x mod l^n'"]
  f_small_on_walls_near_discriminant["Small on the walls means close to discriminant times a linear form"]
  f_vanishing_on_walls_divisible["Vanishing on the walls forces P = discriminant times a linear form"]
  f_wall_set_compact_dominant["The 'wall set' is compact, ordered, and has an open piece of the wall"]
  f_x_sub_x_dvd_of_vanish_on_open_hyperplane["A polynomial vanishing on part of a hyperplane is divisible by the hyperplane's equation"]
  f_chebotarev__n_z_ideal["Definitions - nonzero ideals, primes, and the prime sums used for Chebotarev"]
  f_chebotarev__euler_fac["Ideals built only from a chosen finite set of primes"]
  f_chebotarev__euler_fin["Finite Euler product for a multiplicative function on ideals"]
  f_chebotarev__euler_lim["The Euler product over all primes, and its exponential-of-logs form"]
  f_chebotarev__euler_sum["The sums over ideals and primes converge for s > 1"]
  f_chebotarev__prime_asymp["The prime sum is log(1/(s-1)) plus a bounded error"]
  f_chebotarev__prime_cont["The log Euler sum is continuous in s on (1, infinity)"]
  f_chebotarev__prime_sum["The log version and the plain prime sum differ by a bounded amount"]
  f_chebotarev__casimir_power_surjective_symmetric["Statements about Euler products, prime sums and L-series near s = 1 (stated only)"]
  f_chebotarev__chebyshev_lambda_sub_psi_bounded["Proofs of the first two Euler-product statements, and renamed collections"]
  f_chebotarev__split_def["The prime of a smaller field lying under a prime of a bigger field"]
  f_chebotarev__split_f["Adding up over fibres - two inequalities for sums"]
  f_chebotarev__split_c["Not almost every prime can split into k or more equal-norm primes"]
  f_lie_model_pullback_equivalence["Lie models can be carried along a group pullback, in both directions"]
  f_eisenstein_translation_products__semi_char["Definitions - zeta, sigma, area, the translation operator and the normalised theta"]
  f_eisenstein_translation_products__legendre["Basic properties of zeta and sigma, and the Legendre relation (stated only)"]
  f_eisenstein_translation_products__theta_line["Elliptic-function facts, sigma identities, and 'theta functions form a line' (stated only)"]
  f_eisenstein_translation_products__theta_zero_log_derivative["Area, the alternating pairing, quasi-periodicity of sigma and theta (stated only)"]
  f_eisenstein_translation_products__theta_zero_translate_product["Translate-product formula for the normalised theta, and isogeny relation (stated only)"]
  f_eisenstein_translation_products__translate_product["Scaling, complex multiplication, isogeny formulas and the translate-product law (stated only)"]
  f_eisenstein_translation_products__c_m_quasi_period_const["Complex-multiplication lattices and the quasi-period constant (stated only)"]
  f_quadratic_semicharacters__is_semi_char["Definitions - Hermitian forms, theta spaces, semicharacters on a lattice"]
  f_quadratic_semicharacters__product_theta_mem["Product theta functions and fourth-root uniqueness (stated only)"]
  f_period_integrals__ker_tens["Definitions and the statement 'tensor powers of a spanning theta span' (stated only)"]
  f_mat_h_h_one["Restricting a theta function on many copies to one copy gives a theta function"]
  f_tens_spans["Proof that a theta function on many copies is a multiple of the product of one-copy thetas"]
  f_orbital_bounds_conclusion__ker_tens["Restating 'tensor spans' as a named theorem"]
  f_etale_integrally_closed_in_localization["Etale extensions keep 'integrally closed' after inverting things"]
  f_extension_descent__base_over["Level structures - a basis of torsion points with a prescribed pairing"]
  f_extension_descent__lin_comb_triv_g["The trivial line bundle and the zero-dimensional abelian scheme"]
  f_theta1["Sanity check - theta structures on the zero-dimensional case"]
  f_extension_descent__theta_pt["Theta points - definitions for sections of line bundles"]
  f_theta_v_v["The VV module, and two claims stated but not proved"]
  f_annihilator_quotient_smul_top_of_free["Enough depth and few generators force a module to be free"]
  f_module_free_of_regular_of_free_quotient_local["Free after dividing by a regular element implies free"]
  f_divisor_proofs__purity_free["PurityFree - a property of a local ring, defined but not asserted"]
  f_general_b_fact_side__imports["One element that is a non-zero-divisor on two modules at once"]
  f_cohen_macaulay__bridge["Depth and Cohen-Macaulay are stable under quotients and isomorphisms"]
  f_cohen_macaulay__exists_is_regular_append_of_mod_depth_g_e["A regular sequence can be extended up to the depth"]
  f_maximal_ideal_squares__ring_krull_dim_quotient_span_singleton_add_one["Cutting a regular local ring by one good element lowers dimension by one"]
  f_lie_lattice_range_of_stalk["The lattice at a point is the image of the stalk model (restated)"]
  f_normal_lattice_range["Proof that the lattice at a point equals the image of the stalk model"]
  f_multihomogeneous_value_well_defined["Values of fractions of forms are well defined (restated)"]
  f_valuation_unique_on_forms["Proof that the value of a ratio of forms is unique"]
  f_gen_pt_specializes["Below a generic point there is nothing else"]
  f_gen_pt_specializes_of_specializes["Points between a generic point and another point"]
  f_is_unit_of_basic_open_nonempty_of_universally_closed["On a connected proper space, a function nonzero somewhere is invertible everywhere"]
  f_function_on_connected_fibre_unit["A function invertible at one point of a connected fibre is invertible on all of it"]
  f_harish_chandra_descent__descent["Statements for the descent argument on unitary representations"]
  f_positive_negative_holds["A self-adjoint operator splits into a positive and a negative part"]
  f_simultaneous_eigenvectors__bl_simeig["Commuting diagonal operators share an eigenvector"]
  f_bochner_inequality__is_k_unitary_of_is_inf_unitary["Unitary implies unitary on the compact part, and highest-weight vectors exist"]
  f_bochner_inequality__k_unit_b["The Casimir is bounded by its values on highest-weight vectors"]
  f_casimir_algebra__casimir_k_khw_vec["The Casimir on a highest-weight vector is a computed number"]
  f_sl2_raise_pow_succ_lower_apply_eq["Raising and lowering operators for sl2, and an injectivity claim"]
  f_is_chain["Definitions of a chain basis and a frame"]
  f_exists_chains_of_range["Every nilpotent operator has a chain basis"]
  f_cb_is_chain_apply["Basic facts about chain bases"]
  f_cb_exists_chain_of_gen["Changing the starting vectors of a chain basis"]
  f_chain_a["What a matrix commuting with N does to chain coordinates"]
  f_chain_b["Choosing the chain basis so that a given vector is well placed"]
  f_centralizer_representatives__normal["Normal form for a vector and a nilpotent operator"]
  f_dex_block_frame["The normal form when a ring acts through a field"]
  f_dex_global["The normal form over a finite reduced commutative algebra"]
  f_centralizer_representatives__imports["Frames for matrices commuting with a reduced commutative family"]
  f_cauchy_slice_eq_removable_extension["Cauchy's formula along one coordinate recovers a bounded function"]
  f_differentiable_at_coordinate_cauchy_integral["The one-coordinate Cauchy integral is differentiable in all variables"]
  f_riemann_extension_coordinate_hyperplane["Riemann extension across one coordinate hyperplane"]
  f_extension_across_zero_of_exp_two_pi_i_bound["One-variable extension when exp(2πiH) is not too big"]
  f_locally_bounded_off_coordinate_hyperplanes["A function with a growth bound is locally bounded in a polydisc"]
  f_extension_across_coordinate_hyperplanes["Holomorphic extension across coordinate hyperplanes"]
  f_matrix_bound_holds["A matrix-weighted combination of operators is close to its diagonal part"]
  f_general_b_fact_rest__imports["Dividing out by a regular element lifts an associated prime"]
  f_cohen_macaulay__ass_dim["A regular sequence is no longer than the dimension at any associated prime"]
  f_cohen_macaulay__unmixed["Cohen-Macaulay modules are 'unmixed' and behave well under quotients"]
  f_cohen_macaulay__ring_krull_dim_quotient_of_mem_associated_primes["The same Cohen-Macaulay facts, stated for the ring itself"]
  f_gor_indep_statement["Definitions and unproved claims about Gorenstein rings"]
  f_ring_krull_dim_quotient_add_one_le_of_lt["A strictly smaller prime gives a strictly bigger dimension"]
  f_basis_e_apply["Matching a quadratic extension with its local completion at a prime"]
  f_den_eq_one_of_forall_padic_norm_le_one["A rational that is p-adically small everywhere is an integer, and a product of phases"]
  f_prod_formula_e_of["The product formula follows from five local ingredients"]
  f_exp_sum_lower_bound["Definitions and unproved claims for L-function bounds, plus the rectangle integral"]
  f_rect_residue["The rectangle integral of simple poles is 2πi times the residues"]
  f_rect_double_pole["A double pole adds nothing to the rectangle integral"]
  f_capelli_identities__fixed_subgroup["Vectors fixed by a subgroup"]
  f_hecke_algebras__continuous_torus_character["Definitions for Iwahori-type groups, U operators and function spaces"]
  f_ordinary_hecke_characters__iw_mem_mul["Elements of Iw factor as x times t times y"]
  f_ordinary_hecke_characters__iwahori_pro_unipotent_finite_index["Iw and I1 have finite index in the base Iwahori group"]
  f_ordinary_hecke_characters__u_op_sum["The U operator is a sum over coset representatives"]
  f_ordinary_hecke_characters__u_op_mul["U operators multiply and preserve fixed vectors"]
  f_ordinary_hecke_characters__u_op_nat["The U operator commutes with structure-preserving maps"]
  f_ordinary_hecke_characters__u_op_level["The U operator keeps fixed-by-level vectors and eigenvectors"]
  f_ordinary_hecke_characters__sp_stab["The special function spaces are stable under the U operators"]
  f_mem_val_in_of_invariant_and_values_mem_pow["Small at finitely many points means small everywhere"]
  f_kummer_character_additive_on_congruence["A Kummer-type character is additive on the congruence subgroup"]
  f_markov_inequality_holds["A Markov-type inequality for a positive operator"]
  f_algebra_map_norm_tensor_eq_prod_conjugates["A norm is the product of its Galois conjugates"]
  f_exists_ring_hom_adic_completion_under["Local completions of a number field sit inside those of an extension"]
  f_hasse_norm_principle_of_cyclic_tower["The norm principle passes through a tower of cyclic fields"]
  f_hilbert90_base_change["Hilbert's Theorem 90 after base change"]
  f_is_norm_from_base_change_base_change_properties["Basic rules for 'is a norm after base change'"]
  f_is_norm_from_base_change_of_pow_finrank_cyclic["If a power of a number is a norm, so is the number (cyclic case)"]
  f_of_intermediate_field_tower["Norms from E over F give norms from E over a middle field M"]
  f_tensor_exists_of_galois_fixed["Elements fixed by Galois symmetries come from the smaller field"]
  f_cont_diff_on_hecke_eisenstein_fourier_term["The Fourier term of a Hecke Eisenstein series is smooth"]
  f_has_deriv_at_hecke_term_decay_integrand["Derivative of the decay integrand, in the integration variable"]
  f_hecke_y_derivative_term_integral_polynomial_decay["Fourier pieces decay faster than any power of frequency times height"]
  f_int_z_eq_fourier["The Hecke term integral is a Fourier transform"]
  f_integrable_hecke_term_decay_integrand["The decay integrand can be integrated over the real line"]
  f_norm_hecke_term_decay_fourier_integral_le["A first size bound for the Hecke Fourier integral"]
  f_orbital_bounds_conclusion__unit_det_root["The 'unit determinant root' claim, in its final form"]
  f_period_integrals__unit_det_root["Definitions and statement of the unit determinant root property"]
  f_det_mem_of_entries["Determinants of lattice symmetries lie in a small number field and have size one"]
  f_glob_fin["The global l-unit statement is proved"]
  f_glob_top["From four volume facts to the global l-unit statement"]
  f_glob_vol["Facts about volume ideals of lattices"]
  f_global_l_unit["Vocabulary for the unit determinant root argument"]
  f_ideal_pow_principal["Ideals raised to the class number are principal"]
  f_norm_le_one_of_root["Size-one facts for the unit determinant root"]
  f_nsmul_rel_idx_mem["The local step - lattices agree away from l"]
  f_unit_determinant_root__partial["The unit determinant root property from the global l-unit statement"]
  f_unit_det_root_of["The reduction behind the unit determinant root property"]
  f_general_b_fact_left_ter__imports["A root of a monic integer polynomial is small in an ultrametric field"]
  f_chebotarev__abs_prod_sub_prod_le_sum_abs_sub["Tent bumps that add up to exactly 1"]
  f_c_trick["Splitting an ideal sum by multiples and by class"]
  f_chebotarev__ucoord["Coordinates and weights on ideal lattices (definitions)"]
  f_ker_base_changed_reduction_eq_span_x["Kernel of a reduction map is generated by X"]
  f_det_leading_minor_gram_iwasawa["Corner determinants of a matrix written as k·a·n"]
  f_exists_hermite_reduced_lattice_basis["Every lattice basis can be Hermite-reduced"]
  f_gram_leading_minor_lower_bound_integral["Corner Gram determinants stay bounded away from zero"]
  f_gram_minor_swap_adjacent_columns["Swapping two adjacent columns changes only one corner determinant"]
  f_iwasawa_decomposition_real_matrix["Iwasawa decomposition of a real matrix"]
  f_siegel_cover["Every determinant-1 matrix reduces into a Siegel set"]
  f_unipotent_upper_size_reduction["Shrinking the above-diagonal entries by integer column operations"]
  f_hyperboloid_chart_measure_formula["Measure on a hyperboloid equals half a chart volume"]
  f_period_integrals__rhs_w_lim["Setup for a weighted limit of a matrix-group integral (a claim)"]
  f_chart_jac["Small-ball volume ratio under a smooth change of variables"]
  f_chart_lim["Averages of a continuous density over tiny balls"]
  f_weighted_limit_gauge__orbit_push_cut["Pushing a group measure onto a hyperboloid (conditional proof)"]
  f_weighted_limit_gauge__orbit_push_e["The hyperboloid image is measurable and locally finite"]
  f_orbit_push_loc["From chart facts to a local limit on the hyperboloid"]
  f_orbit_push_q["Real coordinates versus complex-plus-angle coordinates"]
  f_weighted_limit_gauge__volume_lie_e["Vocabulary of claims for the weighted limit (mostly stated only)"]
  f_link_exactness_stability__exists_g_l_moving_unimodular_pair_to_last_basis["Moving a vector and its dual to the last basis vector"]
  f_link_exactness_stability__exists_g_l_split_seq_standard_of_stable_range_le["Moving a whole split list of vector pairs to standard basis vectors"]
  f_g_l_transitive_split_set_of_stable_range_le["GL_n acts transitively on split sequences"]
  f_period_integrals__loc_lat_eq["Statement: two lattices agree locally exactly when they agree prime by prime"]
  f_orbital_bounds_conclusion__loc_lat_eq["The lattice-equality claim follows from three ingredients"]
  f_avoid_p["Numbers outside p are invertible locally; ideals dodging p contain one"]
  f_core_fg_of_le["Core step: a vector in the local span is in the lattice after scaling"]
  f_core_gen_ideal["Every ideal is principal once numbers outside p are allowed"]
  f_local_lattice_equality__development["Three named properties, and the lattice claim assuming them"]
  f_ep_nontrivial["Locally integral elements become integral after scaling by a number outside p"]
  f_local_lattice_equality__imports["Definitions: local image of a number, and the integrality property"]
  f_exists_finite_iwahori_double_coset_representatives["Finitely many double-coset representatives for Iwahori levels"]
  f_desc_st["Statement: Galois descent for subspaces"]
  f_desc_pf["Proof of Galois descent via the trace"]
  f_fin_det_pf["Finitely many functionals are enough to cut out a subspace"]
  f_finite_detect_statement["Definitions and statements for the rationality argument"]
  f_finite_dimensional_base_span["Toolbox: extending scalars of a subspace"]
  f_fun_ker_st["Statement: a Galois-compatible kernel comes from a rational subspace"]
  f_fun_ker_pf["Proof: the kernel is rational, using rationality and Galois descent"]
  f_ker_core_st["Statement: a family of number-field functionals has a rational core"]
  f_ker_core_pf["Proof of the rational-core claim for number-field families"]
  f_rationality_holds["Proof of the rationality statement"]
  f_commutative_algebra_height__is_local_hom["Definitions: rings that are completions of a ring at a prime"]
  f_commutative_algebra_height__cpl_is["The concrete completion satisfies the four completion conditions"]
  f_commutative_algebra_height__cpl_uniq["The completion is unique and has a universal property"]
  f_commutative_algebra_height__highest_weight_space_finite["Completing at a maximal ideal is flat and respects primes"]
  f_capelli_identities__level_of_congruence["Maps out of a completion exist and extend a given map"]
  f_saturated_chains__is_saturated_chain["Definitions: saturated chains, catenary rings, dimension formula"]
  f_covolume_bounds__differentiable_on_of_tendsto_locally_uniformly_on["Limits and sums of complex-differentiable functions stay differentiable"]
  f_analytic_doubling_map_local_inverse["A doubling map with derivative 2 has an analytic halving map"]
  f_analytic_group_law_bounded_commutator["A bounded analytic function vanishing on axes is small near the corner"]
  f_doubling_limit_local_logarithm["Limit of repeated halving, rescaled, exists (Koenigs-style)"]
  f_iter_differentiable_on["Repeated application of a shrinking map, and the medial identity"]
  f_local_logarithm_homomorphism["The limit map turns the group law into addition"]
  f_riemann_form_period_determinant["A commutative analytic group law is additive in local coordinates"]
  f_harish_chandra_induction_g_l_is_character["Gluing two matrix-group characters gives a character of the big group"]
  f_hermite_normal_forms__smul_strict_mono["Lattices over a number field, positive forms, and a group action on cells"]
  f_reduction_bounds_torsion__act_l_pos["Group chains, forms on a cone, and positivity preserved by the action"]
  f_rank_span_le["A rank bound from a linear map to a short list of numbers"]
  f_s_b_star_odd_of["The odd-degree torsion rank bound follows from assumed claims"]
  f_is_prim_cmap["Pushing a cycle along a group map gives a cycle"]
  f_res_ring["Turning a matrix over S into a bigger matrix over R"]
  f_reduction_bounds_torsion__s_b_star["Statement of the torsion bound 'B-star' (not proved)"]
  f_reduction_bounds_torsion__s_b_star_odd["Statement of the odd-degree rank bound (not proved)"]
  f_reduction_bounds_torsion__s_bridge_alt["A long list of claims about group chains and forms (statements only)"]
  f_exists_nsmul_eq_zero_of_tmul["If 1⊗a is zero with real coefficients, some multiple of a is zero"]
  f_s_b_star_of["Iterating a chain construction while tracking weights and homology"]
  f_inertia_ramification__average["Ramification index is 1 exactly when no conductor is divisible by l"]
  f_inertia_ramification__cond_dvd["Characters of conductor dividing m, and conductors of groups of characters"]
  f_conductor_dvd_field_conductor_of_mem["Counting a 'host' group of characters built from two odd quadratic ones"]
  f_inertia_ramification__conductor_local_part_dvd_iff["The l-part of a character is trivial exactly when l misses its conductor"]
  f_inertia_ramification__duality["Subgroups of characters correspond to subgroups of units"]
  f_exists_host_data_wild["Definitions of the 'host data' for a wildly ramified setup (no theorem)"]
  f_inertia_ramification__host_degree["Counting the host group for one extra character"]
  f_inertia_ramification__is_imag_quad["Definitions for imaginary quadratic characters and host data"]
  f_inertia_ramification__log_root_disc_char["Definitions of conductor exponents, kernels, local parts and ramification index"]
  f_inertia_ramification__quadratic_character_legendre_symbol["Quadratic characters are Legendre symbols, with mod-8 consequences"]
  f_inertia_ramification__two_power["Even characters of 2-power conductor, how many and their ramification"]
  f_exists_local_zero_expansion_of_bound["Near a point, a bounded analytic function is its few zeros plus a small error"]
  f_local_zero_expansion_with_multiplicity["The local zero expansion in the form the zero-free argument asks for"]
  f_landau_local_of["The local zero expansion follows from factorization and a log-derivative bound"]
  f_log_deriv_bound["A bounded, zero-free analytic function has a bounded log-derivative"]
  f_zero_factor["An analytic function factors as its zeros times a nonvanishing part"]
  f_coefficient_bound_membership["Every coefficient of a frame-jet lies in the span of minors of the frame"]
  f_orbital_bounds_conclusion__phi_cube_of_factor["The 'cube factor' lemma, handed on to the orbital bounds"]
  f_period_integrals__phi_cube_of_factor["Cube-factor lemma, set-up and statement"]
  f_exp_mv_eq["Proof of the cube-factor lemma"]
  f_formal_group_common__coeff_single_lg["Small facts about substituting into a series"]
  f_formal_group_common__exp_log["Exponential and logarithm series, and integral inverses"]
  f_divisor_proofs__exists_filtered_colimit_finite_type_int_rings["Every ring is a union of finitely generated rings"]
  f_locally_surjective_of_iso_on_finite_type_approximation["Locally surjective if an isomorphism on finite-type rings"]
  f_p_normal_germ_integrally_closed["Integral relations give divisibility on normal analytic sets"]
  f_complex_analytic_sets__st_normal_germ_integrally_closed["Statement: integral relations give divisibility (not proved here)"]
  f_st_rueckert_nullstellensatz["Statement: a Nullstellensatz for analytic functions (not proved here)"]
  f_exists_form_defining_value["A form that pins down a prescribed value (restated)"]
  f_exists_form_with_valuation["Existence of a form with a prescribed valuation condition"]
  f_exists_adic_limit_mem_automorphic_space["Limits of converging sequences stay in the automorphic space"]
  f_u_operator_pow_eventually_invariant_mod_pow["Repeated U operators make a function almost invariant"]
  f_approximation_of_square_identity["A 'square identity' gives good approximations in a subspace"]
  f_toroidal_compactification__push_invertible["Vocabulary for models of moduli spaces of abelian varieties"]
  f_dominates_lift_unique["Maps between models commute with the structure maps"]
  f_join_col["Gaussian weight and the Levi matrix (definitions)"]
  f_gaussian_det_square_integral["Integral of a Gaussian times a squared determinant"]
  f_gaussian_det_levi_integral["Gaussian integral of a squared determinant, Levi version"]
  f_complex_analytic_sets__st_area_multiplicity["Area-with-multiplicity statement (a claim, not proved here)"]
  f_p_area_multiplicity["Proof of the area formula with multiplicity"]
  f_statements_area_multiplicity_weight["Weighted area formula (a claim, not proved here)"]
  f_p_area_multiplicity_weight["Proof of the weighted area formula"]
  f_foundation_proofs__two_var_poly_subst_matrix_basic_laws["Matrices acting on two-variable polynomials: basic laws"]
  f_cocycle_is_coboundary_of_neg_central_element["A cocycle is a coboundary when −1 acts by an element"]
  f_foundation_proofs__exists_scalar_gamma1_cap_gamma0_mod_level["A matrix that is −1 at one prime power and central at another level"]
  f_homogeneous_poly_cocycle_diff_coboundary_of_eq_on["Two polynomial cocycles agreeing on a deep subgroup differ by a coboundary"]
  f_height_one_prime_dvr_stalk["A height-one prime has a nicely behaved neighbour point"]
  f_g_field["The Gauss norm on polynomials and a field that realises it"]
  f_k_irreducible_existence_holds["Inside any finite stable piece there is a smallest stable piece with a top vector"]
  f_root_bound_of_square_identity["A bound on lowering a top vector, assuming a square identity"]
  f_behrend_sets__statement["Definitions and claims for Behrend sets and random subsets"]
  f_behrend_sets__statement_e["More claims for Behrend sets (orders, spacing, selection, counting)"]
  f_coeff_pow_eq_zero_of_lt["A power series D with D plus X times D to the Q equals 1"]
  f_mem_window_iff["A small fact about remainders"]
  f_mul_abs_sub_lt["If c times a and c times b are below n, so is c times their gap"]
  f_prob_eq_sum_ite["Basic rules for the probability of a random subset"]
  f_prod_dim_v_ne_zero["A sum of logarithms of factorials (definition only)"]
  f_select["A random subset exists that is both the right size and not too heavy"]
  f_space_free_of_behrend_free["A space-free set cannot put three points on a short stretch of an orbit"]
  f_totient_le_of_is_primitive_root["A finite group of prime-power size in small matrices over a number field is trivial"]
  f_two_le_cast_of_two_le["A few inequalities for dividing by one less than a product"]
  f_two_pow_dvd_pow_two_pow_sub_one["The odd residues mod 2 to the s plus 2 form a group of size 2 to the s plus 1"]
  f_final_e["The trivial-stabiliser claim, handed on"]
  f_exists_regular_local_extension_with_simple_root["Growing a regular local ring so a simple root appears"]
  f_regular_smooth["Smooth over a regular base means regular"]
  f_generic_fiber_gluing__plus_condition_to_zero_condition["The 'plus' semistable reduction claim implies the plain one"]
  f_generic_fiber_gluing__semistable_complete_split["Statements about completing and splitting semistable models"]
  f_generic_fiber_gluing__semistable_reduction_plus_split["Vocabulary and statements for semistable reduction"]
  f_precomplete_bases__is_precomplete_of_basis["Any finite residue extension lifts to a complete valuation ring"]
  f_split_tori__is_torus["What a torus is, over a field"]
  f_range_j_subset_ab_locus["A model's boundary-free part lies in its abelian locus"]
  f_cone_b_defs["Fourier toolkit on products of complex lines, with weights"]
  f_gaussian_fourier_conj_power["Fourier transform of a conjugate power times a Gaussian"]
  f_schwartz_fourier_preimage["Smooth compact-support functions are Fourier transforms of fast-decaying ones"]
  f_fourier_nonvanishing_unit_point["A nonzero nice function has a Fourier transform nonzero at a generic point"]
  f_fourier_weight_integral_symmetry["A symmetry between a function and its Fourier transform, with weights"]
  f_exists_test_fourier_nonvanishing["A test function that is Gaussian-like with the right weight"]
  f_fourier_continuous_nonvanishing["A bump function that keeps a family integral nonzero"]
  f_convolution_decay_integrable_fourier["Convolving with a rapidly decaying function keeps things integrable"]
  f_convolution_family_integrable["Swapping the order of integration for a family of convolutions"]
  f_exists_convolution_nonvanishing_weight["Some convolution always gives a nonzero weighted integral"]
  f_foundations__is_herm_n_d["Hermitian forms and lattices over a local field"]
  f_semilocal_frames__complement_reference_compact_subgroup["Frames, lattices and counting terms in a local Hermitian space"]
  f_semilocal_frames__g_frames["Gluing local frames across all primes of a number field"]
  f_flag_measures__imports_tail["A vector in the span of a lattice has a whole-number multiple in it"]
  f_local_lattice_between_scaled_standard_lattices["A lattice sits between two scalings of the standard one"]
  f_mem_span_single_iff["Integral vectors are exactly the span of the standard basis"]
  f_complex_analytic_sets__p_riemann_extension_analytic["Riemann extension in several complex variables"]
  f_complex_analytic_sets__st_riemann_extension_analytic["Statement of Riemann extension in several variables"]
  f_p_growth_off_hypersurface_polynomial["Polynomial growth off a hypersurface forces a polynomial"]
  f_st_entire_polynomial_growth["Statement that polynomially bounded entire functions are polynomials"]
  f_st_growth_off_hypersurface_polynomial["Statement of polynomial growth off a hypersurface"]
  f_hida_complete_rings__cofinal_compl["Completeness survives a change of ideal"]
  f_hida_complete_rings__fin_compl["Finite modules over a complete ring are complete"]
  f_hida_complete_rings__fin_max["Maximal ideals of a finite algebra over a local ring"]
  f_hida_complete_rings__idem_lift["Lifting idempotents in a complete ring"]
  f_hida_complete_rings__loc_char["Characterising the part cut out by an idempotent"]
  f_capelli_identities__precomplete_of_finite["Finite modules over a precomplete ring, and a split of finite algebras"]
  f_hida_complete_rings__loc_abs["A finite algebra over a complete local ring splits off a local piece"]
  f_hida_complete_rings__max_idem["An idempotent isolating one maximal ideal"]
  f_hecke_restr["Restricting a Hecke algebra to a generalized-eigen piece"]
  f_arithmetic_bezout__cone_ball["Claims about the unit ball inside a cone of a shape"]
  f_arithmetic_bezout__statements_cone_slab["Claim that thin slabs of the cone ball have small measure"]
  f_ring_krull_dim_quot_bot_one["Vocabulary and claims for the area of complex shapes"]
  f_frame_proj_eq["Two ways to write the graph of a function agree"]
  f_st_graph_jac_continuous["The graph area factor and a claim that it varies continuously"]
  f_st_area_graph_piece["Claim that a nearly linear graph has nearly linear area"]
  f_p_area_graph_piece["Proof that a nearly linear graph has nearly linear area"]
  f_volume_lt_hausdorff_unit_ball_twenty["Area of a linear image, proved from a library fact"]
  f_parts_of_square_identity["From a square identity to three inequalities for highest-weight vectors"]
  f_test_obj["Sanity checks that the definitions are not empty"]
  f_dual_weyl_coordinates__defs_obj["Definitions for matrices, weights and paths of weights"]
  f_dual_weyl_coordinates__defs_mod["Definitions for column families and standard indices"]
  f_dual_weyl_coordinates__statement_a["Claim that the standard bracket monomials are independent"]
  f_dual_weyl_coordinates__statement_b["Claims about the standard vectors of a column family"]
  f_dual_weyl_proofs__b_core_w["Weights of standard index choices stay below mu"]
  f_dual_weyl_proofs__b_core_t["The torus acts diagonally on the column matrix"]
  f_dual_weyl_proofs__qb_indep_field["Column-family vectors are independent over any field, given Lemma A"]
  f_dual_weyl_proofs__qb_basis_apply["Standard vectors form a basis over any ring, given Lemma A"]
  f_window_bound_odd_cases["Lemma A implies the standard vectors form a basis"]
  f_dual_weyl_coordinates__filtration_theorem_of_clauses["Assembling the filtration claims from six separate claims"]
  f_jet_harmonics__is_adic_colimit_of_factor["A space inside one thickening is built up by its thickenings"]
  f_is_adic_complete_of_pow_le_of_pow_le["Completeness for one ideal transfers to a comparable ideal"]
  f_extension_descent__deg_unif["Definitions for a smooth group with a coordinate at every thickening"]
  f_extension_descent__thick_trans_comp["Degeneration data and the thickening maps"]
  f_abelian_scheme_quotients__q_surjective["Definition of an extension of an abelian scheme by a torus"]
  f_abelian_scheme_quotients__split_ext_defs["Definition of the data of a split extension"]
  f_local_hermitian_forms__even_of_norm["Local facts about numbers of the form a² − εb²"]
  f_local_orbit_counts__hs_n_e["Sign function is trivial exactly on the norms"]
  f_nonsq_mul["The sign function is multiplicative"]
  f_local_orbit_counts__norm_ex["Every unit is a norm of an integral element"]
  f_local_orbit_counts__sqrt_o["Square roots lift in a complete local ring"]
  f_sum_shift["Sums over norm classes can be shifted"]
  f_p_normal_zeros_nowhere_dense["Zeros of an analytic function on a normal shape are thin (conditional proof)"]
  f_st_irreducible_germ_regular_connected["Claim — smooth part of an irreducible germ is connected"]
  f_complex_analytic_sets__st_normal_zeros_nowhere_dense["Claim — zeros of an analytic function on a normal shape are thin"]
  f_st_regular_locus_dense["Claim — smooth points are dense in an analytic shape"]
  f_dual_lattices__cokernel_length_comparison_of["Cokernel length comparison, assuming two determinant claims"]
  f_dual_lattices__cokernel_length_comparison_statement["Claim — two cokernels have lengths in a fixed order"]
  f_eigen_quotient_smith_statement["Claim — a quotient length is a product of elementary divisors"]
  f_dual_lattices__restricted_hopf_order_approximation_statement["Claims — a restricted Hopf order exists and approximates linear maps"]
  f_dual_lattices__unramified_cokernel_length_statement["Claim — exact formula for the ratio of two cokernel lengths"]
  f_dual_lattices__unramified_cokernel_lower_bound_of["Cokernel lower bounds, assuming several length claims"]
  f_dual_lattices__unramified_cokernel_lower_bound_statement["Claims — lower bounds for cokernel lengths"]
  f_commutative_algebra_height__k_stable_highest_weight_vector["Completing a local ring preserves the dimension of quotients"]
  f_moduli_nonempty_of_obj["A suitable coefficient field always exists for a CM field"]
  f_casimir_and_root_bounds["Descent for highest-weight vectors, assuming three claims"]
  f_bt_order_value_eval["Values of a function on a group scheme are computed by its marked points"]
  f_der_ring_injective["Tangent maps to dual numbers are determined by their linear part"]
  f_geometry_proofs__exists_lie_model["Every commutative group scheme has a tangent module"]
  f_is_irreducible_iff["Irreducible representations, smooth ones and twists by a character"]
  f_foundations__smooth_part_stable["The smooth part of a representation is closed under the group"]
  f_double_coset_operators_comm_of_anti_involution["Counting lemma behind the Gelfand trick for commuting operators"]
  f_infinity_type["Infinity types, the exponent data of algebraic characters"]
  f_is_open_stabilizer["A fixing set that contains a neighbourhood of 1 is open"]
  f_is_open_stab_of_mem_nhds["Open fixing sets, twisted representations and unipotent matrices"]
  f_reg_alg_fam["Which exponent lists come from regular algebraic infinity types"]
  f_transpose_inv["The inverse-transpose map on invertible matrices"]
  f_finrank_fixed_eq_one["An irreducible representation has at most a line of fixed vectors"]
  f_trace_mul_of_finrank_one["On a line, the trace of a product is the product of traces"]
  f_witt_logarithm["The formal logarithm has coefficients in the Witt-type ring"]
  f_additive_integral_groups__coeff_pow_mem_s["Power-series coefficients of the Weierstrass equation stay in a ring"]
  f_additive_integral_groups__d_x_eq_derivative["The invariant differential times a partial derivative equals minus one"]
  f_additive_integral_groups__glue_holds_var["Integral addition law follows from a key statement and substitution lemmas"]
  f_additive_integral_groups__gu_line["Definitions for the elliptic-curve series computation"]
  f_additive_integral_groups__subst_mem["Substituting series with coefficients in a ring keeps coefficients in it"]
  f_inv_nat_mem_wf["Whole-number inverses lie in the Witt-type ring Wf"]
  f_coef_wf_iff["One-variable coefficient test for the Witt-type ring"]
  f_formal_logarithm_holds["The elliptic-curve formal logarithm has Witt-type coefficients"]
  f_wf_log_of["Witt-type logarithm follows from two assumed ingredients"]
  f_fock_q_row_div_adj["Divided row operators are adjoint to each other (rational version)"]
  f_fock_row_adj["Mixing the rows of the variable grid is adjoint to the conjugate-transposed mixing"]
  f_fock_sub_adj["Substituting variables is adjoint to the conjugate-transposed substitution"]
  f_l_fockq_lemmas["The rational pairing is symmetric, positive and additive"]
  f_fock_space_tableaux__l_focks_lemmas["Calculation rules for variable substitution and the complex pairing"]
  f_graded_weyl_divisibility__statement_a["Definitions and unproved claims about Weyl modules in a variable grid"]
  f_graded_weyl_divisibility__statement_b["More unproved claims about the Weyl module over the rationals"]
  f_real_place_analysis__fock_pair_gl["The Fock pairing, and a claim that the oscillator operators form a Lie algebra action"]
  f_real_place_taylor__prod_factorial_support_sub_single["Fock pairing is additive; derivative and multiplying by a variable are adjoint"]
  f_archimedean_gaussian_fourier["Gaussians over a totally real number field transform to Gaussians"]
  f_quadratic_level_set_density["A Gaussian-weighted quadratic map has a continuous density"]
  f_real_gaussian_fourier_transform["Fourier transform of a complex Gaussian on real space"]
  f_schur_function_compact_support_modulo_unipotent["A probability measure with integrable Fourier transform has a continuous density"]
  f_simultaneous_normal_form_majorant["Two matrices can be put into simple form at the same time"]
  f_alternating_difference_term_window["Terms of an alternating sum vanish outside a narrow window"]
  f_inertia_eigenvalues__dlt_eq_zero["Definitions for the alternating lattice sums, and when they cancel to zero"]
  f_finite_scheme_map_from_special_fibre["A map between finite schemes is a ring map, and it restricts to the special fibre"]
  f_cpl_quot["A completion of a quotient is the quotient of the completion"]
  f_kur_defs["The l-adic numbers with no ramification: the basic definitions"]
  f_norm_eq_of_norm_sub_lt["Sizes of l-adic numbers: close numbers have equal size, and near-roots are close to roots"]
  f_norm_nat_cast_cl_of_not_dvd["Sizes of integers and roots of unity; Teichmüller points near almost-fixed numbers"]
  f_mu_m_eval_pow_eq_zero["A Frobenius map on the ring generated by roots of unity"]
  f_frob_fix_neg_one["Elements that are almost fixed by raising to the p-th power, modulo p"]
  f_exists_power_mul_unit_norm["Every element has the shape l^m times a size-1 fraction"]
  f_exists_teichmuller_rep_mod_prime["Every element of size at most 1 is within |l| of a Teichmüller point"]
  f_exists_extend_endomorphism_fractions["Extending the Frobenius map from the ring to its fraction field"]
  f_kmu_incl_dense_range["A Frobenius map on the whole completed field"]
  f_capelli_identities__is_closed_embedding_to_m["Matrices preserving a sign form: a group that is a closed set of matrices"]
  f_casimir_coefficients__is_closed_embedding_to_m["The sign-form group is locally compact; its unitary subgroup"]
  f_casimir_coefficients__is_closed_kset["Closedness of the unitary subgroup, and averaging operators"]
  f_casimir_coefficients__psi_exists_statement["Statement: a Casimir eigenfunction with prescribed behaviour exists"]
  f_casimir_coefficients__deriv_g_a["Derivatives of matrix exponentials along a line"]
  f_cas_chain_a["A complex-differentiable function is infinitely smooth"]
  f_cas_chain_b["Differentiating along the group: a chain rule for g·exp(tX)"]
  f_cas_chain["Group derivatives of locally holomorphic functions, and smoothness"]
  f_exists_virtual_character_semidirect_orbit_cross_terms["Cross terms of a product of characters come from a bigger group"]
  f_square_identity_holds["A positivity identity for the Casimir of a unitary representation"]
  f_hecke_isogeny_kernels["Statement: Hecke correspondences on CM moduli spaces (definitions only)"]
  f_l_partial_sum["Tail of an L-function series is small"]
  f_l_growth["L-functions grow at most linearly in the input"]
  f_complex_analytic_sets__st_holomorphic_fibre_infinite["Statement - a map to fewer dimensions has an infinite fibre"]
  f_complex_analytic_sets__st_implicit_curve["Statement - a curve of solutions through a point"]
  f_st_irreducible_germ_regular_dim_ge["Statement - an irreducible shape is at least as big as its image"]
  f_complex_analytic_sets__p_implicit_curve["Proof - a curve of solutions through a point"]
  f_complex_analytic_sets__p_holomorphic_fibre_infinite["Proof - a map to fewer dimensions has an infinite fibre"]
  f_p_irreducible_germ_regular_dim_ge["Proof - an irreducible shape is at least as big as its image"]
  f_mem_flag_sub_iff["Which vectors lie in the n-th step of a coordinate flag"]
  f_mem_first_lattice_iff["Plain descriptions of lattices of functions, and two ideals agreeing"]
  f_card_perm_partition_parts_mul_centralizer["Counting shuffles with a given cycle shape"]
  f_squarefree_label_mass_degree_type_le["Weighted share of polynomials with a given factor-degree pattern"]
  f_mass_deg_type_le_cycle_type["Polynomial mass is bounded by the share of shuffles"]
  f_squarefree_label_torus_mass_divisor_bound["Divisor bound for the weighted polynomial count"]
  f_fixed_nondeg["A fixed element that pairs trivially with all fixed elements is tiny"]
  f_block_decomposition__norm_fibre_card_zero["How many elements have norm zero"]
  f_block_decomposition__norm_fibre_card_nonzero["How many elements have a given nonzero norm"]
  f_gauss_sum_hermitian_norm_level_one["A Gauss sum over the norm has size exactly q"]
  riemann_hypothesis --> rh_statement
  riemann_hypothesis --> step_rh_of_every
  grh_dirichlet --> step_crit_line
  step_rh_of_every --> step_rh_of_right
  step_rh_of_every --> every_character
  step_rh_of_every --> dirichlet_l_function
  step_rh_of_right --> functional_equation_zeta
  step_rh_of_right --> factors_nonzero
  step_rh_of_right --> trivial_zeros
  step_rh_of_right --> rh_statement
  step_crit_line --> every_character
  step_crit_line --> functional_equation_dirichlet
  step_crit_line --> primitive_characters
  step_crit_line --> gamma_function
  every_character --> dirichlet_l_function
  every_character --> l2_literature_of_vwin
  every_character --> l2_local_langlands
  every_character --> l2_galois_local_global
  every_character --> l2_vwin_of_row
  rh_statement --> zeta_series
  rh_statement --> analytic_continuation
  rh_statement --> trivial_zeros
  zeta_series --> complex_powers
  zeta_series --> infinite_series
  analytic_continuation --> complex_analysis
  trivial_zeros --> functional_equation_zeta
  functional_equation_zeta --> gamma_function
  functional_equation_zeta --> fourier_analysis
  functional_equation_zeta --> analytic_continuation
  factors_nonzero --> gamma_function
  factors_nonzero --> complex_powers
  factors_nonzero --> trigonometry
  gamma_function --> complex_analysis
  gamma_function --> calculus
  fourier_analysis --> real_analysis
  fourier_analysis --> complex_numbers
  complex_analysis --> real_analysis
  complex_analysis --> complex_numbers
  complex_analysis --> infinite_series
  complex_powers --> complex_numbers
  complex_powers --> calculus
  real_analysis --> calculus
  real_analysis --> infinite_series
  real_analysis --> proofs
  dirichlet_characters --> groups
  dirichlet_characters --> modular_arithmetic
  dirichlet_characters --> complex_numbers
  dirichlet_l_function --> dirichlet_characters
  dirichlet_l_function --> zeta_series
  dirichlet_l_function --> analytic_continuation
  primitive_characters --> dirichlet_characters
  functional_equation_dirichlet --> dirichlet_l_function
  functional_equation_dirichlet --> primitive_characters
  functional_equation_dirichlet --> gamma_function
  functional_equation_dirichlet --> fourier_analysis
  groups --> proofs
  groups --> modular_arithmetic
  lean_placeholder_conditions --> proofs
  lean_polynomial_function --> polynomials
  lean_polynomial_function --> complex_numbers
  lean_unipotent_upper_triangular --> linear_algebra
  lean_lower_iff --> counting
  lean_lower_iff --> proofs
  lean_padic_norm_p --> p_adic_numbers
  lean_padic_norm_p --> algebraic_closure
  lean_algclosure_q --> algebraic_closure
  lean_common_denominator --> number_fields
  lean_char_extend --> groups
  lean_char_extend --> complex_numbers
  lean_sesquilinear_additive --> linear_algebra
  lean_sesquilinear_additive --> complex_numbers
  number_fields --> rings_fields
  number_fields --> polynomials
  p_adic_numbers --> primes_divisibility
  p_adic_numbers --> infinite_series
  p_adic_numbers --> real_analysis
  algebraic_closure --> rings_fields
  algebraic_closure --> polynomials
  rings_fields --> groups
  concept_group_representations --> groups
  concept_group_representations --> linear_algebra
  concept_group_representations --> complex_numbers
  concept_group_representations --> rings_fields
  concept_group_actions --> groups
  concept_group_actions --> counting
  concept_group_actions --> modular_arithmetic
  concept_sylow_theorems --> groups
  concept_sylow_theorems --> primes_divisibility
  concept_sylow_theorems --> concept_normal_subgroups_quotients
  concept_normal_subgroups_quotients --> groups
  concept_complex_analytic_sets --> complex_analysis
  concept_complex_analytic_sets --> polynomials
  concept_complex_analytic_sets --> linear_algebra
  concept_complex_analytic_sets --> concept_point_set_topology
  concept_complex_analytic_sets --> complex_numbers
  concept_point_set_topology --> real_analysis
  concept_lattices_in_the_plane --> complex_numbers
  concept_lattices_in_the_plane --> linear_algebra
  concept_lattices_in_the_plane --> groups
  concept_ideals_and_discriminant --> number_fields
  concept_ideals_and_discriminant --> rings_fields
  concept_ideals_and_discriminant --> linear_algebra
  concept_ideals_and_discriminant --> groups
  concept_ultrametric_norm --> p_adic_numbers
  concept_ultrametric_norm --> rings_fields
  concept_newton_polygon --> concept_ultrametric_norm
  concept_newton_polygon --> polynomials
  concept_newton_polygon --> algebraic_closure
  concept_field_extensions_transcendence --> rings_fields
  concept_field_extensions_transcendence --> polynomials
  concept_field_extensions_transcendence --> linear_algebra
  concept_field_extensions_transcendence --> algebraic_closure
  concept_discrete_valuation_ring --> rings_fields
  concept_discrete_valuation_ring --> p_adic_numbers
  concept_discrete_valuation_ring --> modular_arithmetic
  concept_discrete_valuation_ring --> concept_ultrametric_norm
  concept_discrete_valuation_ring --> linear_algebra
  concept_discrete_valuation_ring --> concept_valuation_rings
  concept_finitely_generated_algebras --> rings_fields
  concept_finitely_generated_algebras --> polynomials
  concept_finitely_generated_algebras --> number_fields
  concept_finitely_generated_algebras --> linear_algebra
  concept_separable_polynomials --> polynomials
  concept_separable_polynomials --> calculus
  concept_separable_polynomials --> rings_fields
  concept_schemes_basics --> rings_fields
  concept_schemes_basics --> concept_point_set_topology
  concept_schemes_basics --> polynomials
  concept_schemes_basics --> concept_prime_ideals_localization
  concept_categorical_pullbacks --> counting
  concept_categorical_pullbacks --> groups
  concept_galois_fixed_fields --> concept_group_actions
  concept_galois_fixed_fields --> concept_normal_subgroups_quotients
  concept_galois_fixed_fields --> rings_fields
  concept_galois_fixed_fields --> groups
  concept_flat_modules --> rings_fields
  concept_flat_modules --> linear_algebra
  concept_flat_modules --> groups
  concept_valuation_rings --> rings_fields
  concept_valuation_rings --> concept_ultrametric_norm
  concept_valuation_rings --> primes_divisibility
  concept_valuation_rings --> concept_schemes_basics
  concept_valuation_rings --> p_adic_numbers
  concept_valuation_rings --> concept_lattices_in_the_plane
  concept_valuation_rings --> linear_algebra
  concept_local_rings --> rings_fields
  concept_local_rings --> modular_arithmetic
  concept_hermitian_unitary_matrices --> linear_algebra
  concept_hermitian_unitary_matrices --> complex_numbers
  concept_hermitian_unitary_matrices --> calculus
  concept_chain_complexes_homology --> groups
  concept_chain_complexes_homology --> linear_algebra
  concept_chain_complexes_homology --> concept_normal_subgroups_quotients
  concept_finitely_generated_abelian_groups --> groups
  concept_finitely_generated_abelian_groups --> modular_arithmetic
  concept_finitely_generated_abelian_groups --> primes_divisibility
  concept_finitely_generated_abelian_groups --> counting
  concept_integral_closure_fraction_fields --> rings_fields
  concept_integral_closure_fraction_fields --> polynomials
  concept_integral_closure_fraction_fields --> number_fields
  concept_integral_closure_fraction_fields --> concept_field_extensions_transcendence
  concept_integral_closure_fraction_fields --> primes_divisibility
  concept_coordinate_rings_dimension --> polynomials
  concept_coordinate_rings_dimension --> rings_fields
  concept_coordinate_rings_dimension --> concept_ideals_and_discriminant
  concept_coordinate_rings_dimension --> concept_integral_closure_fraction_fields
  concept_coordinate_rings_dimension --> concept_complex_analytic_sets
  concept_prime_ideals_localization --> rings_fields
  concept_prime_ideals_localization --> modular_arithmetic
  concept_prime_ideals_localization --> polynomials
  concept_prime_ideals_localization --> primes_divisibility
  concept_prime_ideals_localization --> concept_ideals_and_discriminant
  concept_etale_ring_maps --> rings_fields
  concept_etale_ring_maps --> polynomials
  concept_etale_ring_maps --> calculus
  concept_etale_ring_maps --> concept_prime_ideals_localization
  concept_dedekind_domains --> rings_fields
  concept_dedekind_domains --> primes_divisibility
  concept_dedekind_domains --> concept_prime_ideals_localization
  concept_hensel_lifting --> polynomials
  concept_hensel_lifting --> calculus
  concept_hensel_lifting --> modular_arithmetic
  concept_hensel_lifting --> p_adic_numbers
  concept_tensor_product_of_algebras --> rings_fields
  concept_tensor_product_of_algebras --> linear_algebra
  concept_smooth_morphisms --> concept_etale_ring_maps
  concept_smooth_morphisms --> concept_schemes_basics
  concept_smooth_morphisms --> calculus
  concept_noetherian_and_irreducible_components --> rings_fields
  concept_noetherian_and_irreducible_components --> concept_point_set_topology
  concept_noetherian_and_irreducible_components --> concept_schemes_basics
  concept_modular_forms --> complex_analysis
  concept_modular_forms --> complex_numbers
  concept_modular_forms --> groups
  concept_modular_forms --> linear_algebra
  concept_modular_forms --> modular_arithmetic
  concept_modular_forms --> concept_group_actions
  concept_hecke_operators --> concept_modular_forms
  concept_hecke_operators --> infinite_series
  concept_hecke_operators --> complex_numbers
  concept_petersson_product --> concept_modular_forms
  concept_petersson_product --> calculus
  concept_petersson_product --> complex_numbers
  concept_petersson_product --> linear_algebra
  concept_derivations_smoothness --> polynomials
  concept_derivations_smoothness --> calculus
  concept_derivations_smoothness --> linear_algebra
  concept_derivations_smoothness --> concept_prime_ideals_localization
  concept_derivations_smoothness --> concept_field_extensions_transcendence
  concept_exterior_powers --> linear_algebra
  concept_exterior_powers --> counting
  concept_witt_vectors_ainf --> p_adic_numbers
  concept_witt_vectors_ainf --> rings_fields
  concept_witt_vectors_ainf --> concept_ultrametric_norm
  concept_witt_vectors_ainf --> modular_arithmetic
  concept_roots_of_unity_kummer --> complex_numbers
  concept_roots_of_unity_kummer --> polynomials
  concept_roots_of_unity_kummer --> groups
  concept_roots_of_unity_kummer --> primes_divisibility
  concept_roots_of_unity_kummer --> concept_field_extensions_transcendence
  concept_picard_group --> groups
  concept_picard_group --> rings_fields
  concept_picard_group --> concept_dedekind_domains
  concept_picard_group --> concept_flat_modules
  concept_group_homology --> groups
  concept_group_homology --> concept_group_representations
  concept_group_homology --> concept_chain_complexes_homology
  concept_group_homology --> linear_algebra
  concept_group_homology --> concept_group_actions
  concept_frobenius_perfect_rings --> rings_fields
  concept_frobenius_perfect_rings --> modular_arithmetic
  concept_frobenius_perfect_rings --> primes_divisibility
  concept_gl_infinity_homology_stability --> groups
  concept_gl_infinity_homology_stability --> linear_algebra
  concept_gl_infinity_homology_stability --> concept_chain_complexes_homology
  concept_gl_infinity_homology_stability --> concept_point_set_topology
  concept_haar_measure_fundamental_domain --> real_analysis
  concept_haar_measure_fundamental_domain --> groups
  concept_haar_measure_fundamental_domain --> concept_point_set_topology
  concept_haar_measure_fundamental_domain --> concept_normal_subgroups_quotients
  concept_haar_measure_fundamental_domain --> concept_group_actions
  concept_haar_measure_fundamental_domain --> infinite_series
  concept_lattice_point_counting --> concept_lattices_in_the_plane
  concept_lattice_point_counting --> linear_algebra
  concept_lattice_point_counting --> real_analysis
  concept_chebyshev_functions --> primes_divisibility
  concept_chebyshev_functions --> real_analysis
  concept_chebyshev_functions --> infinite_series
  concept_dual_numbers --> rings_fields
  concept_dual_numbers --> calculus
  concept_dual_numbers --> concept_schemes_basics
  concept_group_schemes --> concept_schemes_basics
  concept_group_schemes --> groups
  concept_group_schemes --> concept_categorical_pullbacks
  concept_group_schemes --> concept_smooth_morphisms
  concept_adic_completion --> concept_local_rings
  concept_adic_completion --> concept_prime_ideals_localization
  concept_adic_completion --> p_adic_numbers
  concept_adic_completion --> rings_fields
  concept_schwartz_functions --> calculus
  concept_schwartz_functions --> real_analysis
  concept_schwartz_functions --> fourier_analysis
  concept_semisimple_algebras_radical --> linear_algebra
  concept_semisimple_algebras_radical --> rings_fields
  concept_semisimple_algebras_radical --> concept_group_representations
  concept_filtered_colimits --> rings_fields
  concept_filtered_colimits --> concept_categorical_pullbacks
  concept_projective_modules --> concept_flat_modules
  concept_projective_modules --> linear_algebra
  concept_projective_modules --> rings_fields
  concept_ample_nef_line_bundles --> concept_picard_group
  concept_ample_nef_line_bundles --> concept_schemes_basics
  concept_ample_nef_line_bundles --> concept_coordinate_rings_dimension
  concept_symmetric_polynomials --> polynomials
  concept_symmetric_polynomials --> rings_fields
  concept_regular_local_rings --> concept_local_rings
  concept_regular_local_rings --> concept_coordinate_rings_dimension
  concept_regular_local_rings --> concept_prime_ideals_localization
  concept_weierstrass_elliptic_functions --> concept_lattices_in_the_plane
  concept_weierstrass_elliptic_functions --> complex_analysis
  concept_weierstrass_elliptic_functions --> infinite_series
  concept_highest_weight_casimir --> concept_group_representations
  concept_highest_weight_casimir --> linear_algebra
  concept_nilpotent_jordan_chains --> linear_algebra
  concept_class_group --> concept_ideals_and_discriminant
  concept_class_group --> concept_dedekind_domains
  concept_class_group --> number_fields
  concept_class_group --> groups
  concept_hausdorff_measure --> real_analysis
  concept_hausdorff_measure --> linear_algebra
  concept_hausdorff_measure --> calculus
  f_ab_by_p_of_comm --> concept_group_representations
  f_ab_by_p_of_comm --> groups
  f_ab_by_p_of_comm --> rings_fields
  f_ab_by_p_of_comm --> linear_algebra
  f_linear_map_short_exact_commute --> linear_algebra
  f_linear_map_short_exact_commute --> rings_fields
  f_is_character_over_subfield_of_representation --> f_ab_by_p_of_comm
  f_is_character_over_subfield_of_representation --> concept_group_representations
  f_is_character_over_subfield_of_representation --> linear_algebra
  f_finite_group_function_pairing_character_eq_finrank_inte --> f_ab_by_p_of_comm
  f_finite_group_function_pairing_character_eq_finrank_inte --> concept_group_representations
  f_finite_group_function_pairing_character_eq_finrank_inte --> groups
  f_finite_group_function_pairing_character_eq_finrank_inte --> linear_algebra
  f_exists_character_quotient_of_injective_intertwining --> f_is_character_over_subfield_of_representation
  f_exists_character_quotient_of_injective_intertwining --> f_linear_map_short_exact_commute
  f_exists_character_quotient_of_injective_intertwining --> f_ab_by_p_of_comm
  f_exists_character_quotient_of_injective_intertwining --> concept_group_representations
  f_exists_is_char_eq_add_of_pair_ne_zero --> f_finite_group_function_pairing_character_eq_finrank_inte
  f_exists_is_char_eq_add_of_pair_ne_zero --> f_exists_character_quotient_of_injective_intertwining
  f_exists_is_char_eq_add_of_pair_ne_zero --> f_ab_by_p_of_comm
  f_exists_is_char_eq_add_of_pair_ne_zero --> concept_group_representations
  f_exists_coprime_order_of_pow_prime_pow --> groups
  f_exists_coprime_order_of_pow_prime_pow --> primes_divisibility
  f_exists_coprime_order_of_pow_prime_pow --> modular_arithmetic
  f_card_fixed_by_pow_prime_pow_mod_eq --> concept_group_actions
  f_card_fixed_by_pow_prime_pow_mod_eq --> groups
  f_card_fixed_by_pow_prime_pow_mod_eq --> counting
  f_card_fixed_by_pow_prime_pow_mod_eq --> modular_arithmetic
  f_card_fixed_by_pow_prime_pow_mod_eq --> primes_divisibility
  f_exists_sylow_over_subgroup --> concept_sylow_theorems
  f_exists_sylow_over_subgroup --> concept_normal_subgroups_quotients
  f_exists_sylow_over_subgroup --> groups
  f_exists_sylow_over_subgroup --> primes_divisibility
  f_card_fixed_by_quotient_eq_rel_index_of_p_regular --> concept_group_actions
  f_card_fixed_by_quotient_eq_rel_index_of_p_regular --> concept_normal_subgroups_quotients
  f_card_fixed_by_quotient_eq_rel_index_of_p_regular --> groups
  f_card_fixed_by_quotient_eq_rel_index_of_p_regular --> counting
  f_card_fixed_by_quotient_eq_rel_index_of_p_regular --> primes_divisibility
  f_card_fixed_by_quotient_eq_rel_index_of_p_regular --> modular_arithmetic
  f_exists_abelian_by_prime_power_not_dvd_card_fixed_by --> f_ab_by_p_of_comm
  f_exists_abelian_by_prime_power_not_dvd_card_fixed_by --> f_exists_coprime_order_of_pow_prime_pow
  f_exists_abelian_by_prime_power_not_dvd_card_fixed_by --> f_card_fixed_by_pow_prime_pow_mod_eq
  f_exists_abelian_by_prime_power_not_dvd_card_fixed_by --> f_exists_sylow_over_subgroup
  f_exists_abelian_by_prime_power_not_dvd_card_fixed_by --> f_card_fixed_by_quotient_eq_rel_index_of_p_regular
  f_exists_abelian_by_prime_power_not_dvd_card_fixed_by --> concept_group_actions
  f_exists_abelian_by_prime_power_not_dvd_card_fixed_by --> concept_sylow_theorems
  f_exists_abelian_by_prime_power_not_dvd_card_fixed_by --> concept_normal_subgroups_quotients
  f_exists_abelian_by_prime_power_not_dvd_card_fixed_by --> groups
  f_exists_abelian_by_prime_power_not_dvd_card_fixed_by --> primes_divisibility
  f_analytic_germ --> concept_complex_analytic_sets
  f_analytic_germ --> complex_analysis
  f_analytic_germ --> concept_point_set_topology
  f_st_analytic_root_branch --> polynomials
  f_st_analytic_root_branch --> complex_analysis
  f_st_analytic_root_branch --> concept_complex_analytic_sets
  f_st_irreducible_germ_projection_image_near --> f_analytic_germ
  f_st_irreducible_germ_projection_image_near --> concept_complex_analytic_sets
  f_st_irreducible_germ_projection_image_near --> linear_algebra
  f_st_irreducible_germ_projection_image_near --> concept_point_set_topology
  f_st_finite_projection_sheets_dense --> f_st_irreducible_germ_projection_image_near
  f_st_finite_projection_sheets_dense --> f_analytic_germ
  f_st_finite_projection_sheets_dense --> concept_complex_analytic_sets
  f_st_finite_projection_sheets_dense --> concept_point_set_topology
  f_st_primitive_form_sheeted_off_discriminant --> f_st_finite_projection_sheets_dense
  f_st_primitive_form_sheeted_off_discriminant --> f_analytic_germ
  f_st_primitive_form_sheeted_off_discriminant --> polynomials
  f_st_primitive_form_sheeted_off_discriminant --> linear_algebra
  f_st_primitive_form_sheeted_off_discriminant --> concept_complex_analytic_sets
  f_st_primitive_form_sheeted_locus_cut_out --> f_st_primitive_form_sheeted_off_discriminant
  f_st_primitive_form_sheeted_locus_cut_out --> f_analytic_germ
  f_st_primitive_form_sheeted_locus_cut_out --> polynomials
  f_st_primitive_form_sheeted_locus_cut_out --> concept_complex_analytic_sets
  f_st_primitive_form_sheeted_iff_root_full --> f_st_primitive_form_sheeted_locus_cut_out
  f_st_primitive_form_sheeted_iff_root_full --> polynomials
  f_st_primitive_form_sheeted_iff_root_full --> complex_analysis
  f_st_primitive_form_sheeted_iff_root_full --> concept_complex_analytic_sets
  f_st_primitive_form_full_branch_constant --> f_st_primitive_form_sheeted_iff_root_full
  f_st_primitive_form_full_branch_constant --> concept_point_set_topology
  f_st_primitive_form_full_branch_constant --> concept_complex_analytic_sets
  f_st_polynomial_root_predicate_factor --> polynomials
  f_st_polynomial_root_predicate_factor --> complex_analysis
  f_st_polynomial_root_predicate_factor --> concept_point_set_topology
  f_st_polynomial_root_predicate_factor --> concept_complex_analytic_sets
  f_st_primitive_form_window --> f_st_primitive_form_sheeted_locus_cut_out
  f_st_primitive_form_window --> f_analytic_germ
  f_st_primitive_form_window --> concept_point_set_topology
  f_st_primitive_form_window --> concept_complex_analytic_sets
  f_st_primitive_form_full_root_factor --> f_st_primitive_form_sheeted_iff_root_full
  f_st_primitive_form_full_root_factor --> polynomials
  f_st_primitive_form_full_root_factor --> concept_complex_analytic_sets
  f_st_primitive_form_full_root_factor --> concept_point_set_topology
  f_p_primitive_form_full_root_factor --> f_st_primitive_form_full_root_factor
  f_p_primitive_form_full_root_factor --> f_st_primitive_form_window
  f_p_primitive_form_full_root_factor --> f_st_analytic_root_branch
  f_p_primitive_form_full_root_factor --> f_st_primitive_form_full_branch_constant
  f_p_primitive_form_full_root_factor --> f_st_polynomial_root_predicate_factor
  f_p_primitive_form_full_root_factor --> concept_point_set_topology
  f_regular_locus --> f_analytic_germ
  f_regular_locus --> concept_complex_analytic_sets
  f_regular_locus --> linear_algebra
  f_regular_locus --> complex_analysis
  f_st_irreducible_finite_germ_projection_open_at --> f_analytic_germ
  f_st_irreducible_finite_germ_projection_open_at --> concept_complex_analytic_sets
  f_st_irreducible_finite_germ_projection_open_at --> linear_algebra
  f_st_irreducible_germ_points_off_discriminant --> f_analytic_germ
  f_st_irreducible_germ_points_off_discriminant --> f_st_irreducible_finite_germ_projection_open_at
  f_st_irreducible_germ_points_off_discriminant --> concept_complex_analytic_sets
  f_st_irreducible_germ_primitive_form --> f_analytic_germ
  f_st_irreducible_germ_primitive_form --> f_st_irreducible_finite_germ_projection_open_at
  f_st_irreducible_germ_primitive_form --> concept_complex_analytic_sets
  f_st_irreducible_germ_primitive_form --> polynomials
  f_st_irreducible_germ_primitive_form --> linear_algebra
  f_st_irreducible_germ_primitive_form --> rings_fields
  f_st_manifold_zeros_complement_connected --> f_regular_locus
  f_st_manifold_zeros_complement_connected --> concept_complex_analytic_sets
  f_st_manifold_zeros_complement_connected --> concept_point_set_topology
  f_st_manifold_zeros_complement_connected --> complex_analysis
  f_st_primitive_form_sheeted_points_near --> f_st_primitive_form_sheeted_off_discriminant
  f_st_primitive_form_sheeted_points_near --> f_analytic_germ
  f_st_primitive_form_sheeted_points_near --> concept_complex_analytic_sets
  f_p_irreducible_germ_points_off_discriminant --> f_st_irreducible_germ_points_off_discriminant
  f_p_irreducible_germ_points_off_discriminant --> f_st_irreducible_germ_primitive_form
  f_p_irreducible_germ_points_off_discriminant --> f_st_primitive_form_sheeted_off_discriminant
  f_p_irreducible_germ_points_off_discriminant --> f_st_primitive_form_sheeted_points_near
  f_p_irreducible_germ_points_off_discriminant --> f_st_manifold_zeros_complement_connected
  f_p_irreducible_germ_points_off_discriminant --> f_regular_locus
  f_p_irreducible_germ_points_off_discriminant --> f_analytic_germ
  f_p_irreducible_germ_points_off_discriminant --> concept_complex_analytic_sets
  f_p_irreducible_germ_points_off_discriminant --> concept_point_set_topology
  f_exists_irr_char_add --> f_ab_by_p_of_comm
  f_exists_irr_char_add --> f_exists_character_quotient_of_injective_intertwining
  f_exists_irr_char_add --> f_is_character_over_subfield_of_representation
  f_exists_irr_char_add --> concept_group_representations
  f_exists_irr_char_add --> linear_algebra
  f_exists_irr_char_add --> groups
  f_is_character_over_subfield_induction_irreducible --> f_exists_irr_char_add
  f_is_character_over_subfield_induction_irreducible --> f_ab_by_p_of_comm
  f_is_character_over_subfield_induction_irreducible --> concept_group_representations
  f_is_character_over_subfield_induction_irreducible --> proofs
  f_is_character_over_subfield_induction_irreducible --> groups
  f_is_character_over_subfield_induction_irreducible --> rings_fields
  f_lat_defs --> concept_lattices_in_the_plane
  f_lat_defs --> complex_numbers
  f_lat_defs --> complex_analysis
  f_lat_defs --> infinite_series
  f_lat_defs --> real_analysis
  f_period_integrals__area_lat --> f_lat_defs
  f_period_integrals__area_lat --> concept_lattices_in_the_plane
  f_period_integrals__area_lat --> complex_numbers
  f_period_integrals__ideal_lattice --> f_lat_defs
  f_period_integrals__ideal_lattice --> concept_ideals_and_discriminant
  f_period_integrals__ideal_lattice --> concept_lattices_in_the_plane
  f_period_integrals__ideal_lattice --> number_fields
  f_period_integrals__ideal_lattice --> complex_numbers
  f_im_conj_mul_combo --> f_period_integrals__area_lat
  f_im_conj_mul_combo --> f_lat_defs
  f_im_conj_mul_combo --> complex_numbers
  f_im_conj_mul_combo --> groups
  f_orbital_bounds_conclusion__area_lat --> f_im_conj_mul_combo
  f_orbital_bounds_conclusion__area_lat --> f_period_integrals__area_lat
  f_orbital_bounds_conclusion__area_lat --> f_lat_defs
  f_ideal_basis_alt --> f_period_integrals__ideal_lattice
  f_ideal_basis_alt --> f_period_integrals__area_lat
  f_ideal_basis_alt --> concept_ideals_and_discriminant
  f_ideal_basis_alt --> number_fields
  f_ideal_basis --> f_ideal_basis_alt
  f_ideal_basis --> concept_ideals_and_discriminant
  f_ideal_basis --> linear_algebra
  f_o_k_area --> f_ideal_basis_alt
  f_o_k_area --> concept_ideals_and_discriminant
  f_o_k_area --> number_fields
  f_o_k_area --> complex_numbers
  f_o_k_area --> linear_algebra
  f_assemble --> f_ideal_basis_alt
  f_assemble --> f_orbital_bounds_conclusion__area_lat
  f_assemble --> f_period_integrals__ideal_lattice
  f_assemble --> f_period_integrals__area_lat
  f_assemble --> concept_ideals_and_discriminant
  f_assemble --> concept_lattices_in_the_plane
  f_assemble --> complex_numbers
  f_assemble --> groups
  f_orbital_bounds_conclusion__ideal_lattice --> f_assemble
  f_orbital_bounds_conclusion__ideal_lattice --> f_o_k_area
  f_orbital_bounds_conclusion__ideal_lattice --> f_ideal_basis
  f_orbital_bounds_conclusion__ideal_lattice --> f_period_integrals__ideal_lattice
  f_induced_class_function_from_subgroup_eq_finsum_cosets --> f_ab_by_p_of_comm
  f_induced_class_function_from_subgroup_eq_finsum_cosets --> groups
  f_induced_class_function_from_subgroup_eq_finsum_cosets --> counting
  f_induced_class_function_from_subgroup_eq_finsum_cosets --> rings_fields
  f_is_character_finsum_conj_subgroup_function_extend_by_zer --> f_ab_by_p_of_comm
  f_is_character_finsum_conj_subgroup_function_extend_by_zer --> f_is_character_over_subfield_of_representation
  f_is_character_finsum_conj_subgroup_function_extend_by_zer --> concept_group_representations
  f_is_character_finsum_conj_subgroup_function_extend_by_zer --> groups
  f_is_character_finsum_conj_subgroup_function_extend_by_zer --> linear_algebra
  f_is_character_over_subfield_restrict_class_function_one --> f_ab_by_p_of_comm
  f_is_character_over_subfield_restrict_class_function_one --> concept_group_representations
  f_is_character_over_subfield_restrict_class_function_one --> groups
  f_is_character_over_subfield_restrict_class_function_one --> linear_algebra
  f_is_character_over_subfield_induced_class_function --> f_induced_class_function_from_subgroup_eq_finsum_cosets
  f_is_character_over_subfield_induced_class_function --> f_is_character_finsum_conj_subgroup_function_extend_by_zer
  f_is_character_over_subfield_induced_class_function --> f_is_character_over_subfield_restrict_class_function_one
  f_is_character_over_subfield_induced_class_function --> f_ab_by_p_of_comm
  f_is_character_over_subfield_induced_class_function --> concept_group_representations
  f_newton_polygon_dominant_index_x_sub_c_mul --> concept_newton_polygon
  f_newton_polygon_dominant_index_x_sub_c_mul --> concept_ultrametric_norm
  f_newton_polygon_dominant_index_x_sub_c_mul --> polynomials
  f_newton_polygon_last_dominant_index_mul_x_sub_c --> concept_newton_polygon
  f_newton_polygon_last_dominant_index_mul_x_sub_c --> concept_ultrametric_norm
  f_newton_polygon_last_dominant_index_mul_x_sub_c --> polynomials
  f_card_roots_closed_ball_eq_dominant_index --> f_newton_polygon_dominant_index_x_sub_c_mul
  f_card_roots_closed_ball_eq_dominant_index --> f_newton_polygon_last_dominant_index_mul_x_sub_c
  f_card_roots_closed_ball_eq_dominant_index --> concept_newton_polygon
  f_card_roots_closed_ball_eq_dominant_index --> concept_ultrametric_norm
  f_card_roots_closed_ball_eq_dominant_index --> algebraic_closure
  f_card_roots_closed_ball_eq_dominant_index --> polynomials
  f_card_roots_closed_ball_bounds_ultrametric --> f_card_roots_closed_ball_eq_dominant_index
  f_card_roots_closed_ball_bounds_ultrametric --> concept_newton_polygon
  f_card_roots_closed_ball_bounds_ultrametric --> concept_ultrametric_norm
  f_card_roots_closed_ball_bounds_ultrametric --> algebraic_closure
  f_card_roots_closed_ball_bounds_ultrametric --> polynomials
  f_onto_o_c_additive_poly --> f_card_roots_closed_ball_bounds_ultrametric
  f_onto_o_c_additive_poly --> concept_ultrametric_norm
  f_onto_o_c_additive_poly --> p_adic_numbers
  f_onto_o_c_additive_poly --> algebraic_closure
  f_onto_o_c_additive_poly --> polynomials
  f_exists_transcendence_basis_algebraic --> concept_field_extensions_transcendence
  f_exists_transcendence_basis_algebraic --> rings_fields
  f_exists_transcendence_basis_algebraic --> counting
  f_monic_polynomial_primitive_over_basis --> concept_field_extensions_transcendence
  f_monic_polynomial_primitive_over_basis --> polynomials
  f_monic_polynomial_primitive_over_basis --> rings_fields
  f_primitive_element_finite_algebraic --> concept_field_extensions_transcendence
  f_primitive_element_finite_algebraic --> linear_algebra
  f_primitive_element_finite_algebraic --> rings_fields
  f_primitive_element_coordinate_polynomials --> concept_field_extensions_transcendence
  f_primitive_element_coordinate_polynomials --> polynomials
  f_primitive_element_coordinate_polynomials --> rings_fields
  f_primitive_element_denominator_clearing --> concept_field_extensions_transcendence
  f_primitive_element_denominator_clearing --> polynomials
  f_primitive_element_denominator_clearing --> rings_fields
  f_polynomial_system_specialization --> f_exists_transcendence_basis_algebraic
  f_polynomial_system_specialization --> f_primitive_element_finite_algebraic
  f_polynomial_system_specialization --> f_monic_polynomial_primitive_over_basis
  f_polynomial_system_specialization --> f_primitive_element_coordinate_polynomials
  f_polynomial_system_specialization --> f_primitive_element_denominator_clearing
  f_finsum_fiberwise_of_finite_support_complex --> complex_numbers
  f_finsum_fiberwise_of_finite_support_complex --> counting
  f_finsum_fiberwise_of_finite_support_complex --> infinite_series
  f_finsum_orbits_inv_stabilizer_card_mass --> f_finsum_fiberwise_of_finite_support_complex
  f_finsum_orbits_inv_stabilizer_card_mass --> concept_group_actions
  f_finsum_orbits_inv_stabilizer_card_mass --> groups
  f_finsum_orbits_inv_stabilizer_card_mass --> counting
  f_finsum_orbits_inv_stabilizer_card_mass --> complex_numbers
  f_finsum_orbit_rel_fibred_equivariant --> f_finsum_fiberwise_of_finite_support_complex
  f_finsum_orbit_rel_fibred_equivariant --> concept_group_actions
  f_finsum_orbit_rel_fibred_equivariant --> groups
  f_stabilizer_eq_centralizer --> concept_group_actions
  f_stabilizer_eq_centralizer --> groups
  f_stabilizer_eq_centralizer --> complex_numbers
  f_finite_support_stabilizer_weighted_pair_term --> f_stabilizer_eq_centralizer
  f_finite_support_stabilizer_weighted_pair_term --> concept_group_actions
  f_finite_support_stabilizer_weighted_pair_term --> counting
  f_finsum_conj_classes_centralizer_orbits_eq_pair_orbits --> f_stabilizer_eq_centralizer
  f_finsum_conj_classes_centralizer_orbits_eq_pair_orbits --> f_finsum_orbit_rel_fibred_equivariant
  f_finsum_conj_classes_centralizer_orbits_eq_pair_orbits --> f_finite_support_stabilizer_weighted_pair_term
  f_finsum_conj_classes_centralizer_orbits_eq_pair_orbits --> concept_group_actions
  f_finsum_conj_classes_centralizer_orbits_eq_pair_orbits --> groups
  f_st_irreducible_germ_meet_over_hypersurface --> f_analytic_germ
  f_st_irreducible_germ_meet_over_hypersurface --> concept_complex_analytic_sets
  f_st_irreducible_germ_meet_over_hypersurface --> complex_analysis
  f_st_irreducible_germ_meet_over_hypersurface --> linear_algebra
  f_st_isolated_fibre_local_unbranched --> concept_complex_analytic_sets
  f_st_isolated_fibre_local_unbranched --> concept_point_set_topology
  f_st_isolated_fibre_local_unbranched --> complex_analysis
  f_st_isolated_fibre_local_unbranched --> linear_algebra
  f_st_open_projection_dominant_components --> f_analytic_germ
  f_st_open_projection_dominant_components --> concept_complex_analytic_sets
  f_st_open_projection_dominant_components --> complex_analysis
  f_st_open_projection_dominant_components --> linear_algebra
  f_p_isolated_fibre_local_unbranched --> f_st_isolated_fibre_local_unbranched
  f_p_isolated_fibre_local_unbranched --> f_st_open_projection_dominant_components
  f_p_isolated_fibre_local_unbranched --> f_st_irreducible_germ_meet_over_hypersurface
  f_p_isolated_fibre_local_unbranched --> f_st_irreducible_germ_primitive_form
  f_p_isolated_fibre_local_unbranched --> f_st_primitive_form_sheeted_off_discriminant
  f_p_isolated_fibre_local_unbranched --> f_analytic_germ
  f_p_isolated_fibre_local_unbranched --> concept_complex_analytic_sets
  f_p_isolated_fibre_local_unbranched --> concept_point_set_topology
  f_p_isolated_fibre_local_unbranched --> complex_analysis
  f_weighted_orbit_sum_eq_pair_orbit_sum --> f_stabilizer_eq_centralizer
  f_weighted_orbit_sum_eq_pair_orbit_sum --> f_finsum_orbit_rel_fibred_equivariant
  f_weighted_orbit_sum_eq_pair_orbit_sum --> f_finsum_orbits_inv_stabilizer_card_mass
  f_weighted_orbit_sum_eq_pair_orbit_sum --> f_finite_support_stabilizer_weighted_pair_term
  f_weighted_orbit_sum_eq_pair_orbit_sum --> concept_group_actions
  f_weighted_orbit_sum_eq_pair_orbit_sum --> groups
  f_weighted_orbit_sum_eq_pair_orbit_sum --> counting
  f_weighted_orbit_sum_eq_pair_orbit_sum --> complex_numbers
  f_dvr_matrix_proj_preimage --> concept_discrete_valuation_ring
  f_dvr_matrix_proj_preimage --> linear_algebra
  f_dvr_matrix_proj_preimage --> rings_fields
  f_exists_residue_annihilator_of_not_standard_column_form_a --> concept_discrete_valuation_ring
  f_exists_residue_annihilator_of_not_standard_column_form_a --> linear_algebra
  f_exists_residue_annihilator_of_not_standard_column_form_a --> rings_fields
  f_residue_top_factor_through_bottom --> linear_algebra
  f_residue_top_factor_through_bottom --> rings_fields
  f_gl_factor_from_blocks_mod_uniformizer --> concept_discrete_valuation_ring
  f_gl_factor_from_blocks_mod_uniformizer --> linear_algebra
  f_gl_factor_from_blocks_mod_uniformizer --> groups
  f_exists_hyperplane_residue_outside_translates --> f_exists_residue_annihilator_of_not_standard_column_form_a
  f_exists_hyperplane_residue_outside_translates --> f_residue_top_factor_through_bottom
  f_exists_hyperplane_residue_outside_translates --> f_dvr_matrix_proj_preimage
  f_exists_hyperplane_residue_outside_translates --> f_gl_factor_from_blocks_mod_uniformizer
  f_exists_hyperplane_residue_outside_translates --> concept_discrete_valuation_ring
  f_exists_hyperplane_residue_outside_translates --> linear_algebra
  f_exists_hyperplane_residue_outside_translates --> groups
  f_exists_prime_gt_dvd_eval --> polynomials
  f_exists_prime_gt_dvd_eval --> primes_divisibility
  f_exists_prime_gt_dvd_eval --> modular_arithmetic
  f_exists_prime_gt_dvd_eval --> proofs
  f_exists_large_prime_dvd_int_polynomial_eval --> f_exists_prime_gt_dvd_eval
  f_sep_int_poly_root_mod_prime_sq --> f_exists_large_prime_dvd_int_polynomial_eval
  f_sep_int_poly_root_mod_prime_sq --> concept_separable_polynomials
  f_sep_int_poly_root_mod_prime_sq --> polynomials
  f_sep_int_poly_root_mod_prime_sq --> modular_arithmetic
  f_sep_int_poly_root_mod_prime_sq --> primes_divisibility
  f_divisor_proofs__finite_type_to_number_field --> concept_finitely_generated_algebras
  f_divisor_proofs__finite_type_to_number_field --> number_fields
  f_divisor_proofs__finite_type_to_number_field --> rings_fields
  f_divisor_proofs__number_field_to_mod_p_squared --> f_sep_int_poly_root_mod_prime_sq
  f_divisor_proofs__number_field_to_mod_p_squared --> concept_separable_polynomials
  f_divisor_proofs__number_field_to_mod_p_squared --> number_fields
  f_divisor_proofs__number_field_to_mod_p_squared --> concept_field_extensions_transcendence
  f_divisor_proofs__number_field_to_mod_p_squared --> modular_arithmetic
  f_divisor_proofs__number_field_to_mod_p_squared --> polynomials
  f_nadel_vanishing_lemmas__finite_type_to_number_field --> f_divisor_proofs__finite_type_to_number_field
  f_nadel_vanishing_lemmas__number_field_to_mod_p_squared --> f_divisor_proofs__number_field_to_mod_p_squared
  f_finite_type_to_mod_p_squared --> f_nadel_vanishing_lemmas__finite_type_to_number_field
  f_finite_type_to_mod_p_squared --> f_nadel_vanishing_lemmas__number_field_to_mod_p_squared
  f_finite_type_to_mod_p_squared --> concept_finitely_generated_algebras
  f_finite_type_to_mod_p_squared --> modular_arithmetic
  f_whisker_left_left_is_pullback_snd --> concept_categorical_pullbacks
  f_whisker_left_left_is_pullback_snd --> concept_schemes_basics
  f_exists_factor_closed_immersion_of_locally_on_source --> concept_schemes_basics
  f_exists_factor_closed_immersion_of_locally_on_source --> concept_categorical_pullbacks
  f_exists_factor_closed_immersion_of_locally_on_source --> concept_point_set_topology
  f_exists_glue_closed_immersions_open_cover --> concept_schemes_basics
  f_exists_glue_closed_immersions_open_cover --> concept_categorical_pullbacks
  f_exists_glue_closed_immersions_open_cover --> concept_point_set_topology
  f_finite_flat_surjective_closed_subscheme_of_open_cover --> concept_schemes_basics
  f_finite_flat_surjective_closed_subscheme_of_open_cover --> concept_categorical_pullbacks
  f_finite_flat_surjective_closed_subscheme_of_open_cover --> concept_point_set_topology
  f_exists_closed_immersion_represents_of_affine_opens --> f_whisker_left_left_is_pullback_snd
  f_exists_closed_immersion_represents_of_affine_opens --> f_exists_factor_closed_immersion_of_locally_on_source
  f_exists_closed_immersion_represents_of_affine_opens --> f_exists_glue_closed_immersions_open_cover
  f_exists_closed_immersion_represents_of_affine_opens --> f_finite_flat_surjective_closed_subscheme_of_open_cover
  f_exists_closed_immersion_represents_of_affine_opens --> concept_schemes_basics
  f_exists_closed_immersion_represents_of_affine_opens --> concept_categorical_pullbacks
  f_foundations__coset_trace --> concept_ultrametric_norm
  f_foundations__coset_trace --> concept_galois_fixed_fields
  f_foundations__coset_trace --> concept_group_actions
  f_foundations__coset_trace --> concept_normal_subgroups_quotients
  f_valuation_frobenius_sum_sub_le_nat_cast_prime --> concept_ultrametric_norm
  f_valuation_frobenius_sum_sub_le_nat_cast_prime --> primes_divisibility
  f_valuation_frobenius_sum_sub_le_nat_cast_prime --> rings_fields
  f_valuation_frobenius_sum_sub_le_nat_cast_prime --> f_foundations__coset_trace
  f_coset_representative_trace_fixed_properties --> f_foundations__coset_trace
  f_coset_representative_trace_fixed_properties --> concept_galois_fixed_fields
  f_coset_representative_trace_fixed_properties --> concept_ultrametric_norm
  f_coset_representative_trace_fixed_properties --> concept_normal_subgroups_quotients
  f_foundation_proofs__exists_pth_power_scale_thin_shell --> f_foundations__coset_trace
  f_foundation_proofs__exists_pth_power_scale_thin_shell --> concept_ultrametric_norm
  f_foundation_proofs__exists_pth_power_scale_thin_shell --> primes_divisibility
  f_foundation_proofs__exists_pth_power_scale_thin_shell --> rings_fields
  f_pow_mul_approx_pow_of_almost_etale_separating_family --> f_foundations__coset_trace
  f_pow_mul_approx_pow_of_almost_etale_separating_family --> f_valuation_frobenius_sum_sub_le_nat_cast_prime
  f_pow_mul_approx_pow_of_almost_etale_separating_family --> f_coset_representative_trace_fixed_properties
  f_pow_mul_approx_pow_of_almost_etale_separating_family --> concept_galois_fixed_fields
  f_pow_mul_approx_pow_of_almost_etale_separating_family --> concept_ultrametric_norm
  f_pow_mul_approx_pow_of_almost_etale_separating_family --> primes_divisibility
  f_approx_pth_root_fixed_subfield_of_almost_etale --> f_foundation_proofs__exists_pth_power_scale_thin_shell
  f_approx_pth_root_fixed_subfield_of_almost_etale --> f_pow_mul_approx_pow_of_almost_etale_separating_family
  f_approx_pth_root_fixed_subfield_of_almost_etale --> f_foundations__coset_trace
  f_approx_pth_root_fixed_subfield_of_almost_etale --> concept_galois_fixed_fields
  f_approx_pth_root_fixed_subfield_of_almost_etale --> concept_ultrametric_norm
  f_affine_hilbert_scheme_valuative_criterion_existence --> f_divisor_proofs__comap_bc_comp
  f_affine_hilbert_scheme_valuative_criterion_existence --> f_exists_flat_ideal_valuation_ring_pullback
  f_affine_hilbert_scheme_valuative_criterion_existence --> f_flat_subscheme_of_quotient_flat_affine
  f_affine_hilbert_scheme_valuative_criterion_existence --> f_divisor_proofs__ideal_sheaf_data_comap_ideal_top_of_is_affine
  f_affine_hilbert_scheme_valuative_criterion_existence --> concept_schemes_basics
  f_affine_hilbert_scheme_valuative_criterion_existence --> concept_valuation_rings
  f_affine_hilbert_scheme_valuative_criterion_existence --> concept_flat_modules
  f_divisor_proofs__comap_bc_comp --> concept_schemes_basics
  f_divisor_proofs__comap_bc_comp --> concept_flat_modules
  f_exists_flat_ideal_valuation_ring_pullback --> f_divisor_proofs__imports_alt
  f_exists_flat_ideal_valuation_ring_pullback --> concept_valuation_rings
  f_exists_flat_ideal_valuation_ring_pullback --> concept_flat_modules
  f_exists_flat_ideal_valuation_ring_pullback --> concept_schemes_basics
  f_flat_subscheme_of_quotient_flat_affine --> concept_schemes_basics
  f_flat_subscheme_of_quotient_flat_affine --> concept_flat_modules
  f_divisor_proofs__ideal_sheaf_data_comap_ideal_top_of_is_affine --> concept_schemes_basics
  f_divisor_proofs__imports_alt --> concept_valuation_rings
  f_divisor_proofs__imports_alt --> concept_flat_modules
  f_divisor_proofs__imports_alt --> rings_fields
  f_finite_projection_pushforward --> f_analytic_germ
  f_finite_projection_pushforward --> f_st_finite_germ_projection_open_at
  f_finite_projection_pushforward --> f_st_irreducible_germ_primitive_form
  f_finite_projection_pushforward --> f_st_primitive_form_sheeted_off_discriminant
  f_finite_projection_pushforward --> f_complex_analytic_sets__st_unbranched_proper_count_constant
  f_finite_projection_pushforward --> f_st_centred_disc_cover_curve
  f_finite_projection_pushforward --> concept_complex_analytic_sets
  f_finite_projection_pushforward --> concept_point_set_topology
  f_finite_projection_pushforward --> complex_analysis
  f_st_centred_disc_cover_curve --> concept_complex_analytic_sets
  f_st_centred_disc_cover_curve --> concept_point_set_topology
  f_st_centred_disc_cover_curve --> complex_analysis
  f_st_finite_germ_projection_open_at --> f_analytic_germ
  f_st_finite_germ_projection_open_at --> concept_complex_analytic_sets
  f_st_finite_germ_projection_open_at --> concept_point_set_topology
  f_st_finite_germ_projection_open_at --> complex_analysis
  f_complex_analytic_sets__st_unbranched_proper_count_constant --> concept_complex_analytic_sets
  f_complex_analytic_sets__st_unbranched_proper_count_constant --> concept_point_set_topology
  f_complex_analytic_sets__st_unbranched_proper_count_constant --> complex_analysis
  f_exists_isotropic_graph_unitary_is_unit_lower_block --> f_exists_isotropic_graph_det_lower_row_ne_zero_field
  f_exists_isotropic_graph_unitary_is_unit_lower_block --> f_lift_mod_maximal_skew
  f_exists_isotropic_graph_unitary_is_unit_lower_block --> concept_local_rings
  f_exists_isotropic_graph_unitary_is_unit_lower_block --> concept_hermitian_unitary_matrices
  f_exists_isotropic_graph_unitary_is_unit_lower_block --> linear_algebra
  f_exists_isotropic_graph_det_lower_row_ne_zero_field --> f_exists_skew_hermitian_mul_add_det_ne_zero_of_pair
  f_exists_isotropic_graph_det_lower_row_ne_zero_field --> concept_hermitian_unitary_matrices
  f_exists_isotropic_graph_det_lower_row_ne_zero_field --> linear_algebra
  f_exists_skew_hermitian_mul_add_det_ne_zero_of_pair --> f_exists_rank_normal_form_matrix_field
  f_exists_skew_hermitian_mul_add_det_ne_zero_of_pair --> f_skew_hermitian_perturb_idempotent_det_ne_zero
  f_exists_skew_hermitian_mul_add_det_ne_zero_of_pair --> concept_hermitian_unitary_matrices
  f_exists_skew_hermitian_mul_add_det_ne_zero_of_pair --> linear_algebra
  f_skew_hermitian_perturb_idempotent_det_ne_zero --> concept_hermitian_unitary_matrices
  f_skew_hermitian_perturb_idempotent_det_ne_zero --> linear_algebra
  f_exists_rank_normal_form_matrix_field --> linear_algebra
  f_exists_rank_normal_form_matrix_field --> rings_fields
  f_lift_mod_maximal_skew --> concept_local_rings
  f_lift_mod_maximal_skew --> concept_hermitian_unitary_matrices
  f_lift_mod_maximal_skew --> linear_algebra
  f_card_quot_prime_smul_eq_card_ker_mul_pow_finrank --> concept_finitely_generated_abelian_groups
  f_card_quot_prime_smul_eq_card_ker_mul_pow_finrank --> concept_normal_subgroups_quotients
  f_card_quot_prime_smul_eq_card_ker_mul_pow_finrank --> groups
  f_card_quot_prime_smul_eq_card_ker_mul_pow_finrank --> counting
  f_card_quot_prime_smul_eq_card_ker_mul_pow_finrank --> linear_algebra
  f_card_zmod_tensor_eq_card_quot_prime_multiples --> concept_flat_modules
  f_card_zmod_tensor_eq_card_quot_prime_multiples --> modular_arithmetic
  f_card_zmod_tensor_eq_card_quot_prime_multiples --> concept_normal_subgroups_quotients
  f_card_zmod_tensor_eq_card_quot_prime_multiples --> rings_fields
  f_nat_card_homology_restrict_scalars --> concept_chain_complexes_homology
  f_nat_card_homology_restrict_scalars --> rings_fields
  f_nat_card_homology_restrict_scalars --> counting
  f_nat_card_homology_of_short_exact_mul --> concept_chain_complexes_homology
  f_nat_card_homology_of_short_exact_mul --> concept_normal_subgroups_quotients
  f_nat_card_homology_of_short_exact_mul --> counting
  f_short_exact_mul_prime_zmod_tensor_complex --> concept_chain_complexes_homology
  f_short_exact_mul_prime_zmod_tensor_complex --> concept_flat_modules
  f_short_exact_mul_prime_zmod_tensor_complex --> modular_arithmetic
  f_short_exact_mul_prime_zmod_tensor_complex --> concept_normal_subgroups_quotients
  f_finrank_homology_mod_prime_universal_coefficients --> f_card_quot_prime_smul_eq_card_ker_mul_pow_finrank
  f_finrank_homology_mod_prime_universal_coefficients --> f_card_zmod_tensor_eq_card_quot_prime_multiples
  f_finrank_homology_mod_prime_universal_coefficients --> f_nat_card_homology_restrict_scalars
  f_finrank_homology_mod_prime_universal_coefficients --> f_nat_card_homology_of_short_exact_mul
  f_finrank_homology_mod_prime_universal_coefficients --> f_short_exact_mul_prime_zmod_tensor_complex
  f_finrank_homology_mod_prime_universal_coefficients --> concept_chain_complexes_homology
  f_finrank_homology_mod_prime_universal_coefficients --> concept_flat_modules
  f_finrank_homology_mod_prime_universal_coefficients --> linear_algebra
  f_finrank_homology_mod_prime_universal_coefficients --> modular_arithmetic
  f_complex_analytic_sets__st_holomorphic_on_subset --> complex_analysis
  f_complex_analytic_sets__st_holomorphic_on_subset --> concept_point_set_topology
  f_complex_analytic_sets__st_holomorphic_on_subset --> concept_complex_analytic_sets
  f_complex_analytic_sets__st_normal_model --> concept_complex_analytic_sets
  f_complex_analytic_sets__st_normal_model --> concept_coordinate_rings_dimension
  f_complex_analytic_sets__st_normal_model --> concept_integral_closure_fraction_fields
  f_complex_analytic_sets__st_normal_model --> polynomials
  f_st_normal_riemann_extension --> f_complex_analytic_sets__st_holomorphic_on_subset
  f_st_normal_riemann_extension --> f_complex_analytic_sets__st_normal_model
  f_st_normal_riemann_extension --> concept_coordinate_rings_dimension
  f_st_normal_riemann_extension --> complex_analysis
  f_st_normal_maximum_principle --> f_complex_analytic_sets__st_holomorphic_on_subset
  f_st_normal_maximum_principle --> f_complex_analytic_sets__st_normal_model
  f_st_normal_maximum_principle --> concept_coordinate_rings_dimension
  f_st_normal_maximum_principle --> complex_analysis
  f_complex_analytic_sets__st_normal_locally_irreducible --> f_complex_analytic_sets__st_normal_model
  f_complex_analytic_sets__st_normal_locally_irreducible --> concept_coordinate_rings_dimension
  f_complex_analytic_sets__st_normal_locally_irreducible --> concept_point_set_topology
  f_complex_analytic_sets__st_normal_locally_irreducible --> concept_complex_analytic_sets
  f_st_normal_open_mapping --> f_complex_analytic_sets__st_normal_model
  f_st_normal_open_mapping --> concept_coordinate_rings_dimension
  f_st_normal_open_mapping --> concept_point_set_topology
  f_st_normal_open_mapping --> complex_analysis
  f_st_branch_fill_dimension --> f_complex_analytic_sets__st_normal_model
  f_st_branch_fill_dimension --> concept_coordinate_rings_dimension
  f_st_branch_fill_dimension --> complex_analysis
  f_st_branch_inverse_off_hypersurface --> f_complex_analytic_sets__st_holomorphic_on_subset
  f_st_branch_inverse_off_hypersurface --> f_complex_analytic_sets__st_normal_model
  f_st_branch_inverse_off_hypersurface --> f_st_normal_open_mapping
  f_st_branch_inverse_off_hypersurface --> concept_coordinate_rings_dimension
  f_st_branch_inverse_off_hypersurface --> complex_analysis
  f_st_branch_contains_normal_point --> f_complex_analytic_sets__st_normal_model
  f_st_branch_contains_normal_point --> concept_coordinate_rings_dimension
  f_st_branch_contains_normal_point --> complex_analysis
  f_st_branch_inverse_holomorphic --> f_complex_analytic_sets__st_holomorphic_on_subset
  f_st_branch_inverse_holomorphic --> f_complex_analytic_sets__st_normal_model
  f_st_branch_inverse_holomorphic --> concept_coordinate_rings_dimension
  f_st_branch_inverse_holomorphic --> complex_analysis
  f_p_branch_contains_normal_point --> f_st_branch_contains_normal_point
  f_p_branch_contains_normal_point --> f_complex_analytic_sets__st_normal_locally_irreducible
  f_p_branch_contains_normal_point --> f_st_branch_inverse_holomorphic
  f_p_branch_contains_normal_point --> f_st_normal_riemann_extension
  f_p_branch_contains_normal_point --> f_st_normal_maximum_principle
  f_p_branch_contains_normal_point --> f_complex_analytic_sets__st_holomorphic_on_subset
  f_p_branch_contains_normal_point --> f_complex_analytic_sets__st_normal_model
  f_p_branch_contains_normal_point --> concept_point_set_topology
  f_p_branch_contains_normal_point --> complex_analysis
  f_p_branch_inverse_holomorphic --> f_st_branch_inverse_holomorphic
  f_p_branch_inverse_holomorphic --> f_st_branch_fill_dimension
  f_p_branch_inverse_holomorphic --> f_st_normal_open_mapping
  f_p_branch_inverse_holomorphic --> f_st_branch_inverse_off_hypersurface
  f_p_branch_inverse_holomorphic --> f_st_normal_riemann_extension
  f_p_branch_inverse_holomorphic --> f_complex_analytic_sets__st_normal_locally_irreducible
  f_p_branch_inverse_holomorphic --> f_p_branch_contains_normal_point
  f_p_branch_inverse_holomorphic --> f_complex_analytic_sets__st_holomorphic_on_subset
  f_p_branch_inverse_holomorphic --> f_complex_analytic_sets__st_normal_model
  f_p_branch_inverse_holomorphic --> concept_point_set_topology
  f_p_branch_inverse_holomorphic --> complex_analysis
  f_iwasawa_decomposition__exists_basis_in_finite_domain_trace_mem --> concept_integral_closure_fraction_fields
  f_iwasawa_decomposition__exists_basis_in_finite_domain_trace_mem --> linear_algebra
  f_iwasawa_decomposition__exists_basis_in_finite_domain_trace_mem --> rings_fields
  f_iwasawa_decomposition__exists_basis_in_finite_domain_trace_mem --> number_fields
  f_iwasawa_decomposition__flat_tensor_embeds_tensor_fraction_fields --> concept_flat_modules
  f_iwasawa_decomposition__flat_tensor_embeds_tensor_fraction_fields --> concept_integral_closure_fraction_fields
  f_iwasawa_decomposition__flat_tensor_embeds_tensor_fraction_fields --> rings_fields
  f_iwasawa_decomposition__integral_of_finite_base_change_image --> concept_integral_closure_fraction_fields
  f_iwasawa_decomposition__integral_of_finite_base_change_image --> concept_flat_modules
  f_iwasawa_decomposition__integral_of_finite_base_change_image --> polynomials
  f_iwasawa_decomposition__is_unit_map_of_mem_non_zero_divisors_tensor --> concept_integral_closure_fraction_fields
  f_iwasawa_decomposition__is_unit_map_of_mem_non_zero_divisors_tensor --> concept_flat_modules
  f_iwasawa_decomposition__is_unit_map_of_mem_non_zero_divisors_tensor --> linear_algebra
  f_iwasawa_decomposition__is_unit_map_of_mem_non_zero_divisors_tensor --> rings_fields
  f_iwasawa_decomposition__discr_mul_mem_of_is_integral --> f_iwasawa_decomposition__exists_basis_in_finite_domain_trace_mem
  f_iwasawa_decomposition__discr_mul_mem_of_is_integral --> f_iwasawa_decomposition__flat_tensor_embeds_tensor_fraction_fields
  f_iwasawa_decomposition__discr_mul_mem_of_is_integral --> f_iwasawa_decomposition__integral_of_finite_base_change_image
  f_iwasawa_decomposition__discr_mul_mem_of_is_integral --> f_iwasawa_decomposition__is_unit_map_of_mem_non_zero_divisors_tensor
  f_iwasawa_decomposition__discr_mul_mem_of_is_integral --> concept_integral_closure_fraction_fields
  f_iwasawa_decomposition__discr_mul_mem_of_is_integral --> concept_flat_modules
  f_iwasawa_decomposition__discr_mul_mem_of_is_integral --> concept_ideals_and_discriminant
  f_iwasawa_decomposition__discr_mul_mem_of_is_integral --> linear_algebra
  f_divisor_proofs__is_excision_nbhd_self --> concept_etale_ring_maps
  f_divisor_proofs__is_excision_nbhd_self --> concept_prime_ideals_localization
  f_divisor_proofs__is_excision_nbhd_self --> rings_fields
  f_divisor_proofs__is_excision_nbhd_trans --> f_divisor_proofs__is_excision_nbhd_self
  f_divisor_proofs__is_excision_nbhd_trans --> concept_etale_ring_maps
  f_divisor_proofs__is_excision_nbhd_away --> f_divisor_proofs__is_excision_nbhd_self
  f_divisor_proofs__is_excision_nbhd_away --> concept_prime_ideals_localization
  f_divisor_proofs__is_excision_nbhd_away --> concept_etale_ring_maps
  f_divisor_proofs__exists_excision_nbhd_adjoin_root --> f_divisor_proofs__is_excision_nbhd_self
  f_divisor_proofs__exists_excision_nbhd_adjoin_root --> concept_etale_ring_maps
  f_divisor_proofs__exists_excision_nbhd_adjoin_root --> concept_hensel_lifting
  f_divisor_proofs__exists_excision_nbhd_adjoin_root --> polynomials
  f_divisor_proofs__exists_pow_sub_mem_span_of_is_unit_mod_of_is_alg_closed --> f_divisor_proofs__is_excision_nbhd_self
  f_divisor_proofs__exists_pow_sub_mem_span_of_is_unit_mod_of_is_alg_closed --> concept_dedekind_domains
  f_divisor_proofs__exists_pow_sub_mem_span_of_is_unit_mod_of_is_alg_closed --> concept_hensel_lifting
  f_divisor_proofs__exists_pow_sub_mem_span_of_is_unit_mod_of_is_alg_closed --> algebraic_closure
  f_unit_power_on_excision_neighbourhood --> f_divisor_proofs__is_excision_nbhd_self
  f_unit_power_on_excision_neighbourhood --> f_divisor_proofs__is_excision_nbhd_away
  f_unit_power_on_excision_neighbourhood --> f_divisor_proofs__is_excision_nbhd_trans
  f_unit_power_on_excision_neighbourhood --> f_divisor_proofs__exists_excision_nbhd_adjoin_root
  f_unit_power_on_excision_neighbourhood --> f_divisor_proofs__exists_pow_sub_mem_span_of_is_unit_mod_of_is_alg_closed
  f_unit_power_on_excision_neighbourhood --> concept_prime_ideals_localization
  f_coprime_unit_etale_extension --> f_unit_power_on_excision_neighbourhood
  f_coprime_unit_etale_extension --> f_divisor_proofs__is_excision_nbhd_self
  f_is_integral_of_is_idempotent_elem --> concept_integral_closure_fraction_fields
  f_is_integral_of_is_idempotent_elem --> concept_tensor_product_of_algebras
  f_is_integral_of_is_idempotent_elem --> concept_smooth_morphisms
  f_exists_idempotent_tmul_one_eq_of_smooth_algebra --> f_is_integral_of_is_idempotent_elem
  f_range_comap_include_right_field --> concept_tensor_product_of_algebras
  f_range_comap_include_right_field --> concept_schemes_basics
  f_closure_generic_fibre_clopen_split --> f_exists_idempotent_tmul_one_eq_of_smooth_algebra
  f_closure_generic_fibre_clopen_split --> f_range_comap_include_right_field
  f_closure_generic_fibre_clopen_split --> concept_schemes_basics
  f_closure_generic_fibre_clopen_split --> concept_smooth_morphisms
  f_closure_generic_fibre_clopen_split --> concept_point_set_topology
  f_smooth_generic_fibre_closure_partition --> f_closure_generic_fibre_clopen_split
  f_smooth_generic_fibre_closure_partition --> concept_schemes_basics
  f_smooth_generic_fibre_closure_partition --> concept_smooth_morphisms
  f_is_open_connected_component_of_is_locally_noetherian --> concept_noetherian_and_irreducible_components
  f_is_open_connected_component_of_is_locally_noetherian --> concept_point_set_topology
  f_is_open_connected_component_of_is_locally_noetherian --> concept_schemes_basics
  f_section_mem_component_generic_of_closed_valuation --> f_is_open_connected_component_of_is_locally_noetherian
  f_section_mem_component_generic_of_closed_valuation --> f_smooth_generic_fibre_closure_partition
  f_section_mem_component_generic_of_closed_valuation --> concept_valuation_rings
  f_section_mem_component_generic_of_closed_valuation --> concept_smooth_morphisms
  f_adelic_hermitian_forms__adelic_pair --> concept_hermitian_unitary_matrices
  f_adelic_hermitian_forms__adelic_pair --> concept_group_representations
  f_adelic_hermitian_forms__adelic_pair --> groups
  f_adelic_hermitian_forms__adelic_pair --> polynomials
  f_adelic_hermitian_forms__adelic_pair --> p_adic_numbers
  f_adelic_hermitian_forms__adelic_pair --> linear_algebra
  f_exists_is_hermitian_log_of_pos_def_gram --> f_adelic_hermitian_forms__adelic_pair
  f_exists_is_hermitian_log_of_pos_def_gram --> concept_hermitian_unitary_matrices
  f_is_closed_is_hermitian_log_of_pos_def --> f_adelic_hermitian_forms__adelic_pair
  f_is_closed_is_hermitian_log_of_pos_def --> concept_hermitian_unitary_matrices
  f_is_closed_is_hermitian_log_of_pos_def --> concept_point_set_topology
  f_matrix_entries_bounded_of_hermitian_log_trace_sq_le --> f_adelic_hermitian_forms__adelic_pair
  f_matrix_entries_bounded_of_hermitian_log_trace_sq_le --> concept_hermitian_unitary_matrices
  f_entries_bounded_of_conj_spanning_bounded --> f_adelic_hermitian_forms__adelic_pair
  f_entries_bounded_of_conj_spanning_bounded --> linear_algebra
  f_exists_energy_min --> f_adelic_hermitian_forms__adelic_pair
  f_exists_energy_min --> f_exists_is_hermitian_log_of_pos_def_gram
  f_exists_energy_min --> f_is_closed_is_hermitian_log_of_pos_def
  f_exists_energy_min --> f_matrix_entries_bounded_of_hermitian_log_trace_sq_le
  f_exists_energy_min --> f_entries_bounded_of_conj_spanning_bounded
  f_exists_energy_min --> concept_point_set_topology
  f_exists_energy_min --> algebraic_closure
  f_foundations__pet_eq_rel_index_mul_pet_prod --> concept_modular_forms
  f_foundations__pet_eq_rel_index_mul_pet_prod --> concept_hecke_operators
  f_foundations__pet_eq_rel_index_mul_pet_prod --> concept_petersson_product
  f_foundations__pet_eq_rel_index_mul_pet_prod --> groups
  f_foundations__pet_eq_rel_index_mul_pet_prod --> modular_arithmetic
  f_cusp_form_gamma1_inter_gamma0_slash_rat_is_zero_at --> f_foundations__pet_eq_rel_index_mul_pet_prod
  f_cusp_form_gamma1_inter_gamma0_slash_rat_is_zero_at --> concept_modular_forms
  f_foundation_proofs__hecke_u_operator_explicit_eq_sum_slash --> f_foundations__pet_eq_rel_index_mul_pet_prod
  f_foundation_proofs__hecke_u_operator_explicit_eq_sum_slash --> concept_hecke_operators
  f_foundation_proofs__hecke_u_operator_explicit_eq_sum_slash --> concept_modular_forms
  f_foundation_proofs__hecke_u_operator_explicit_slash_invariant_gamma1_inter_g_statement --> f_foundation_proofs__hecke_u_operator_explicit_slash_invariant_gamma1_inter_gamma0
  f_foundation_proofs__hecke_u_operator_explicit_slash_invariant_gamma1_inter_g_statement --> f_foundations__pet_eq_rel_index_mul_pet_prod
  f_foundation_proofs__hecke_u_operator_explicit_slash_invariant_gamma1_inter_gamma0 --> f_foundations__pet_eq_rel_index_mul_pet_prod
  f_foundation_proofs__hecke_u_operator_explicit_slash_invariant_gamma1_inter_gamma0 --> concept_hecke_operators
  f_foundation_proofs__hecke_u_operator_explicit_slash_invariant_gamma1_inter_gamma0 --> concept_modular_forms
  f_foundation_proofs__hecke_u_operator_explicit_slash_invariant_gamma1_inter_gamma0 --> modular_arithmetic
  f_foundation_proofs__hecke_u_operator_explicit_slash_invariant_gamma1_inter_gamma0 --> primes_divisibility
  f_foundation_proofs__hecke_u_operator_explicit_slash_invariant_gamma1_inter_gamma0 --> counting
  f_is_zero_at_finset_sum --> f_foundation_proofs__hecke_u_operator_explicit_slash_invariant_gamma1_inter_g_statement
  f_is_zero_at_finset_sum --> f_foundation_proofs__hecke_u_operator_explicit_eq_sum_slash
  f_is_zero_at_finset_sum --> f_cusp_form_gamma1_inter_gamma0_slash_rat_is_zero_at
  f_is_zero_at_finset_sum --> f_foundation_proofs__mdifferentiable_hecke_operators_explicit
  f_is_zero_at_finset_sum --> f_foundations__pet_eq_rel_index_mul_pet_prod
  f_is_zero_at_finset_sum --> concept_modular_forms
  f_is_zero_at_finset_sum --> concept_hecke_operators
  f_foundation_proofs__mdifferentiable_hecke_operators_explicit --> f_foundations__pet_eq_rel_index_mul_pet_prod
  f_foundation_proofs__mdifferentiable_hecke_operators_explicit --> concept_hecke_operators
  f_foundation_proofs__mdifferentiable_hecke_operators_explicit --> concept_modular_forms
  f_foundation_proofs__mdifferentiable_hecke_operators_explicit --> complex_analysis
  f_exists_det_ne_zero_of_rows_separating --> linear_algebra
  f_mem_sq_localization_of_pderiv_mem --> concept_derivations_smoothness
  f_mem_sq_localization_of_pderiv_mem --> concept_prime_ideals_localization
  f_mem_sq_localization_of_pderiv_mem --> polynomials
  f_exists_mul_mem_of_forall --> concept_prime_ideals_localization
  f_exists_mul_mem_of_forall --> rings_fields
  f_exists_mul_mem_of_forall --> counting
  f_exists_minimal_local_generators --> f_exists_mul_mem_of_forall
  f_exists_minimal_local_generators --> concept_prime_ideals_localization
  f_exists_generic_jacobian_data_of_prime --> f_exists_minimal_local_generators
  f_exists_generic_jacobian_data_of_prime --> f_mem_sq_localization_of_pderiv_mem
  f_exists_generic_jacobian_data_of_prime --> f_exists_det_ne_zero_of_rows_separating
  f_exists_generic_jacobian_data_of_prime --> concept_derivations_smoothness
  f_exists_generic_jacobian_data_of_prime --> concept_prime_ideals_localization
  f_exists_generic_jacobian_data_iterated --> f_exists_generic_jacobian_data_of_prime
  f_exists_generic_jacobian_data_iterated --> concept_derivations_smoothness
  f_exists_generic_jacobian_data_iterated --> polynomials
  f_divisors__xi_mul_nu --> concept_witt_vectors_ainf
  f_divisors__xi_mul_nu --> p_adic_numbers
  f_divisors__xi_mul_nu --> linear_algebra
  f_divisors__xi_mul_nu --> polynomials
  f_divisor_base__sandwich_maps --> f_divisors__xi_mul_nu
  f_divisor_base__sandwich_maps --> concept_exterior_powers
  f_divisor_base__sandwich_maps --> concept_valuation_rings
  f_divisor_base__sandwich_maps --> concept_witt_vectors_ainf
  f_divisor_base__sandwich_maps --> linear_algebra
  f_determinant_lattice_principal --> f_divisor_proofs__eigen_projection_quotient_lattice
  f_determinant_lattice_principal --> f_divisor_proofs__exists_spanning_image_lattice
  f_determinant_lattice_principal --> f_exterior_power_span_of_lattice
  f_determinant_lattice_principal --> f_exterior_power_top_finrank_one
  f_determinant_lattice_principal --> f_rank_one_lattice_span_singleton
  f_determinant_lattice_principal --> f_divisor_base__sandwich_maps
  f_determinant_lattice_principal --> concept_exterior_powers
  f_determinant_lattice_principal --> concept_valuation_rings
  f_divisor_proofs__eigen_projection_quotient_lattice --> f_divisor_base__sandwich_maps
  f_divisor_proofs__eigen_projection_quotient_lattice --> linear_algebra
  f_divisor_proofs__exists_spanning_image_lattice --> f_divisor_base__sandwich_maps
  f_divisor_proofs__exists_spanning_image_lattice --> linear_algebra
  f_divisor_proofs__exists_spanning_image_lattice --> concept_valuation_rings
  f_exterior_power_span_of_lattice --> f_divisor_base__sandwich_maps
  f_exterior_power_span_of_lattice --> concept_exterior_powers
  f_exterior_power_span_of_lattice --> concept_valuation_rings
  f_exterior_power_top_finrank_one --> f_divisor_base__sandwich_maps
  f_exterior_power_top_finrank_one --> concept_exterior_powers
  f_exterior_power_top_finrank_one --> linear_algebra
  f_exterior_power_top_finrank_one --> counting
  f_rank_one_lattice_span_singleton --> f_divisor_base__sandwich_maps
  f_rank_one_lattice_span_singleton --> concept_valuation_rings
  f_rank_one_lattice_span_singleton --> concept_ultrametric_norm
  f_splits --> rings_fields
  f_splits --> polynomials
  f_splits --> concept_local_rings
  f_splits --> concept_ideals_and_discriminant
  f_absolutely_closed_polynomial_splits --> f_splits
  f_absolutely_closed_polynomial_splits --> polynomials
  f_absolutely_closed_polynomial_splits --> algebraic_closure
  f_absolutely_closed_polynomial_splits --> rings_fields
  f_absolutely_closed_unit_coefficient_root --> f_absolutely_closed_polynomial_splits
  f_absolutely_closed_unit_coefficient_root --> f_splits
  f_absolutely_closed_unit_coefficient_root --> concept_local_rings
  f_absolutely_closed_unit_coefficient_root --> polynomials
  f_polynomial_roots_of_closed_quotient --> f_splits
  f_polynomial_roots_of_closed_quotient --> concept_local_rings
  f_polynomial_roots_of_closed_quotient --> concept_ideals_and_discriminant
  f_polynomial_roots_of_closed_quotient --> polynomials
  f_newton_polygon_slope_existence --> f_splits
  f_newton_polygon_slope_existence --> concept_newton_polygon
  f_newton_polygon_slope_existence --> concept_ultrametric_norm
  f_newton_polygon_slope_existence --> rings_fields
  f_newton_polygon_slope_existence --> primes_divisibility
  f_newton_approximation_of_dichotomy --> f_polynomial_roots_of_closed_quotient
  f_newton_approximation_of_dichotomy --> f_absolutely_closed_unit_coefficient_root
  f_newton_approximation_of_dichotomy --> f_newton_polygon_slope_existence
  f_newton_approximation_of_dichotomy --> f_splits
  f_newton_approximation_of_dichotomy --> concept_newton_polygon
  f_newton_approximation_of_dichotomy --> concept_local_rings
  f_newton_approximation_of_dichotomy --> polynomials
  f_valuation_add_pow_sub_le --> concept_ultrametric_norm
  f_valuation_add_pow_sub_le --> counting
  f_valuation_add_pow_sub_le --> primes_divisibility
  f_valuation_add_pow_sub_le --> rings_fields
  f_valuation_sub_one_pow_eq_prime --> concept_ultrametric_norm
  f_valuation_sub_one_pow_eq_prime --> concept_roots_of_unity_kummer
  f_valuation_sub_one_pow_eq_prime --> primes_divisibility
  f_valuation_sub_one_pow_eq_prime --> complex_numbers
  f_exists_improved_approx_kummer_generator --> f_valuation_add_pow_sub_le
  f_exists_improved_approx_kummer_generator --> concept_ultrametric_norm
  f_exists_improved_approx_kummer_generator --> concept_roots_of_unity_kummer
  f_exists_improved_approx_kummer_generator --> rings_fields
  f_kummer_generator_approx_critical_radius --> f_exists_improved_approx_kummer_generator
  f_kummer_generator_approx_critical_radius --> f_foundations__coset_trace
  f_kummer_generator_approx_critical_radius --> concept_ultrametric_norm
  f_kummer_generator_approx_critical_radius --> concept_roots_of_unity_kummer
  f_kummer_automorphism_moves_integers_almost_unit --> f_kummer_generator_approx_critical_radius
  f_kummer_automorphism_moves_integers_almost_unit --> f_valuation_sub_one_pow_eq_prime
  f_kummer_automorphism_moves_integers_almost_unit --> f_foundation_proofs__exists_pth_power_scale_thin_shell
  f_kummer_automorphism_moves_integers_almost_unit --> f_foundations__coset_trace
  f_kummer_automorphism_moves_integers_almost_unit --> concept_group_actions
  f_kummer_automorphism_moves_integers_almost_unit --> concept_ultrametric_norm
  f_kummer_automorphism_moves_integers_almost_unit --> concept_roots_of_unity_kummer
  f_orbital_bounds_conclusion__sigma_star_uniq --> f_sigma_star_uniq_of
  f_orbital_bounds_conclusion__sigma_star_uniq --> f_orbital_bounds_conclusion__area_lat
  f_orbital_bounds_conclusion__sigma_star_uniq --> f_period_integrals__sigma_star_uniq
  f_period_integrals__sigma_star_uniq --> f_lat_defs
  f_period_integrals__sigma_star_uniq --> concept_lattices_in_the_plane
  f_period_integrals__sigma_star_uniq --> complex_analysis
  f_coef_shift --> f_complete
  f_coef_shift --> fourier_analysis
  f_coef_shift --> complex_numbers
  f_coef_shift --> calculus
  f_complete --> fourier_analysis
  f_complete --> complex_numbers
  f_complete --> calculus
  f_siegel_set_completeness --> f_complete
  f_siegel_set_completeness --> fourier_analysis
  f_siegel_set_completeness --> complex_analysis
  f_siegel_set_shift_invariance --> f_complete
  f_siegel_set_shift_invariance --> complex_analysis
  f_siegel_set_shift_invariance --> fourier_analysis
  f_sigma_star_uniq_of --> f_zero_of_coef
  f_sigma_star_uniq_of --> f_coef_shift
  f_sigma_star_uniq_of --> f_siegel_set_completeness
  f_sigma_star_uniq_of --> f_siegel_set_shift_invariance
  f_sigma_star_uniq_of --> f_period_integrals__area_lat
  f_sigma_star_uniq_of --> f_period_integrals__sigma_star_uniq
  f_zero_of_coef --> f_complete
  f_zero_of_coef --> f_period_integrals__sigma_star_uniq
  f_zero_of_coef --> f_period_integrals__area_lat
  f_zero_of_coef --> f_lat_defs
  f_zero_of_coef --> complex_analysis
  f_zero_of_coef --> complex_powers
  f_hecke_u_operator_preserves_modular_form_gamma1_inter_gam_statement --> f_hecke_u_operator_preserves_modular_form_gamma1_inter_gamma0
  f_hecke_u_operator_preserves_modular_form_gamma1_inter_gam_statement --> concept_modular_forms
  f_hecke_u_operator_preserves_modular_form_gamma1_inter_gam_statement --> concept_hecke_operators
  f_hecke_u_operator_preserves_modular_form_gamma1_inter_gamma0 --> f_foundation_proofs__hecke_u_operator_explicit_slash_invariant_gamma1_inter_gamma0
  f_hecke_u_operator_preserves_modular_form_gamma1_inter_gamma0 --> f_foundation_proofs__hecke_u_operator_explicit_eq_sum_slash
  f_hecke_u_operator_preserves_modular_form_gamma1_inter_gamma0 --> f_foundation_proofs__mdifferentiable_hecke_operators_explicit
  f_hecke_u_operator_preserves_modular_form_gamma1_inter_gamma0 --> f_slash_rat_is_bounded_at_gamma1_inter_gamma0_level
  f_hecke_u_operator_preserves_modular_form_gamma1_inter_gamma0 --> f_foundations__pet_eq_rel_index_mul_pet_prod
  f_hecke_u_operator_preserves_modular_form_gamma1_inter_gamma0 --> concept_modular_forms
  f_hecke_u_operator_preserves_modular_form_gamma1_inter_gamma0 --> concept_hecke_operators
  f_slash_rat_is_bounded_at_gamma1_inter_gamma0_level --> concept_modular_forms
  f_slash_rat_is_bounded_at_gamma1_inter_gamma0_level --> concept_group_actions
  f_slash_rat_is_bounded_at_gamma1_inter_gamma0_level --> linear_algebra
  f_unit_eq_mul_pow_on_etale_excision_nbhd_zero_locus --> f_divisor_proofs__is_excision_nbhd_self
  f_unit_eq_mul_pow_on_etale_excision_nbhd_zero_locus --> f_divisor_proofs__is_excision_nbhd_away
  f_unit_eq_mul_pow_on_etale_excision_nbhd_zero_locus --> f_divisor_proofs__is_excision_nbhd_trans
  f_unit_eq_mul_pow_on_etale_excision_nbhd_zero_locus --> f_divisor_proofs__exists_pow_sub_mem_span_of_is_unit_mod_of_is_alg_closed
  f_unit_eq_mul_pow_on_etale_excision_nbhd_zero_locus --> f_divisor_proofs__exists_excision_nbhd_adjoin_root
  f_unit_eq_mul_pow_on_etale_excision_nbhd_zero_locus --> concept_prime_ideals_localization
  f_unit_eq_mul_pow_on_etale_excision_nbhd_zero_locus --> concept_etale_ring_maps
  f_unit_eq_mul_pow_on_etale_excision_nbhd_zero_locus --> concept_hensel_lifting
  f_unit_eq_mul_pow_on_etale_excision_nbhd_zero_locus --> concept_dedekind_domains
  f_unit_eq_mul_pow_on_etale_excision_nbhd_zero_locus --> concept_finitely_generated_algebras
  f_unit_eq_mul_pow_on_etale_excision_nbhd_zero_locus --> algebraic_closure
  f_q_act_m_sub_algebra_map --> linear_algebra
  f_q_act_m_sub_algebra_map --> rings_fields
  f_q_act_m_sub_algebra_map --> concept_group_representations
  f_character_augmentation_subspace_top_eq_ker_smul --> f_q_act_m_sub_algebra_map
  f_character_augmentation_subspace_top_eq_ker_smul --> concept_tensor_product_of_algebras
  f_character_augmentation_subspace_top_eq_ker_smul --> linear_algebra
  f_character_augmentation_subspace_top_eq_ker_smul --> rings_fields
  f_character_augmentation_subspace_top_eq_ker_smul_statement --> f_character_augmentation_subspace_top_eq_ker_smul
  f_character_augmentation_subspace_top_eq_ker_smul_statement --> concept_tensor_product_of_algebras
  f_exists_idempotent_local_of_character --> rings_fields
  f_exists_idempotent_local_of_character --> linear_algebra
  f_exists_idempotent_local_of_character --> concept_local_rings
  f_exists_idempotent_local_of_character --> concept_prime_ideals_localization
  f_exists_idempotent_local_of_character_statement --> f_exists_idempotent_local_of_character
  f_exists_idempotent_local_of_character_statement --> rings_fields
  f_finrank_quot_one_sub_idempotent_eq_mul --> concept_local_rings
  f_finrank_quot_one_sub_idempotent_eq_mul --> concept_flat_modules
  f_finrank_quot_one_sub_idempotent_eq_mul --> concept_tensor_product_of_algebras
  f_finrank_quot_one_sub_idempotent_eq_mul --> linear_algebra
  f_finrank_quot_one_sub_idempotent_eq_mul --> rings_fields
  f_finrank_quot_one_sub_idempotent_eq_mul_statement --> f_finrank_quot_one_sub_idempotent_eq_mul
  f_finrank_quot_one_sub_idempotent_eq_mul_statement --> linear_algebra
  f_weight_space_iff_idempotent_fixed --> linear_algebra
  f_weight_space_iff_idempotent_fixed --> concept_tensor_product_of_algebras
  f_weight_space_iff_idempotent_fixed --> rings_fields
  f_weight_space_iff_idempotent_fixed_statement --> f_weight_space_iff_idempotent_fixed
  f_weight_space_iff_idempotent_fixed_statement --> linear_algebra
  f_finrank_weight_space_projective_tensor_eq --> f_exists_idempotent_local_of_character_statement
  f_finrank_weight_space_projective_tensor_eq --> f_finrank_quot_one_sub_idempotent_eq_mul_statement
  f_finrank_weight_space_projective_tensor_eq --> f_weight_space_iff_idempotent_fixed_statement
  f_finrank_weight_space_projective_tensor_eq --> f_character_augmentation_subspace_top_eq_ker_smul_statement
  f_finrank_weight_space_projective_tensor_eq --> f_q_act_m_sub_algebra_map
  f_finrank_weight_space_projective_tensor_eq --> concept_tensor_product_of_algebras
  f_finrank_weight_space_projective_tensor_eq --> concept_flat_modules
  f_finrank_weight_space_projective_tensor_eq --> linear_algebra
  f_finrank_weight_space_projective_tensor_eq --> algebraic_closure
  f_adjoin_inverse_is_localization_away --> concept_prime_ideals_localization
  f_adjoin_inverse_is_localization_away --> rings_fields
  f_adjoin_inverse_is_localization_away --> concept_integral_closure_fraction_fields
  f_kaehler_basis_tower --> concept_derivations_smoothness
  f_kaehler_basis_tower --> concept_smooth_morphisms
  f_kaehler_basis_tower --> concept_chain_complexes_homology
  f_kaehler_basis_tower --> linear_algebra
  f_kaehler_finrank_fraction_field --> concept_derivations_smoothness
  f_kaehler_finrank_fraction_field --> concept_etale_ring_maps
  f_kaehler_finrank_fraction_field --> concept_integral_closure_fraction_fields
  f_kaehler_finrank_fraction_field --> concept_prime_ideals_localization
  f_kaehler_finrank_fraction_field --> linear_algebra
  f_localization_kaehler_prime_ideal --> concept_prime_ideals_localization
  f_localization_kaehler_prime_ideal --> polynomials
  f_localization_kaehler_prime_ideal --> rings_fields
  f_localization_kaehler_prime_ideal --> concept_coordinate_rings_dimension
  f_kaehler_rank_localization_bound --> f_kaehler_finrank_fraction_field
  f_kaehler_rank_localization_bound --> f_kaehler_basis_tower
  f_kaehler_rank_localization_bound --> f_adjoin_inverse_is_localization_away
  f_kaehler_rank_localization_bound --> f_localization_kaehler_prime_ideal
  f_kaehler_rank_localization_bound --> concept_smooth_morphisms
  f_kaehler_rank_localization_bound --> concept_derivations_smoothness
  f_kaehler_rank_localization_bound --> concept_prime_ideals_localization
  f_kaehler_rank_localization_bound --> concept_integral_closure_fraction_fields
  f_exists_nat_mul_mem_range_pi_quotient_minimal_primes --> concept_prime_ideals_localization
  f_exists_nat_mul_mem_range_pi_quotient_minimal_primes --> concept_noetherian_and_irreducible_components
  f_exists_nat_mul_mem_range_pi_quotient_minimal_primes --> concept_integral_closure_fraction_fields
  f_exists_nat_mul_mem_range_pi_quotient_minimal_primes --> modular_arithmetic
  f_is_of_fin_order_of_is_of_fin_order_map_ring_hom --> concept_picard_group
  f_is_of_fin_order_of_is_of_fin_order_map_ring_hom --> concept_finitely_generated_abelian_groups
  f_is_of_fin_order_of_is_of_fin_order_map_ring_hom --> concept_flat_modules
  f_is_of_fin_order_of_is_of_fin_order_map_ring_hom --> groups
  f_pic_is_of_fin_order_of_finite_int --> f_is_of_fin_order_of_is_of_fin_order_map_ring_hom
  f_pic_is_of_fin_order_of_finite_int --> concept_picard_group
  f_pic_is_of_fin_order_of_finite_int --> number_fields
  f_pic_is_of_fin_order_of_finite_int --> concept_integral_closure_fraction_fields
  f_pic_is_of_fin_order_of_finite_int --> concept_ideals_and_discriminant
  f_pic_pi_is_of_fin_order --> concept_picard_group
  f_pic_pi_is_of_fin_order --> concept_tensor_product_of_algebras
  f_pic_pi_is_of_fin_order --> concept_flat_modules
  f_pic_pi_is_of_fin_order --> groups
  f_is_of_fin_order_pic_of_is_reduced_finite_int --> f_exists_nat_mul_mem_range_pi_quotient_minimal_primes
  f_is_of_fin_order_pic_of_is_reduced_finite_int --> f_is_of_fin_order_of_is_of_fin_order_map_ring_hom
  f_is_of_fin_order_pic_of_is_reduced_finite_int --> f_pic_is_of_fin_order_of_finite_int
  f_is_of_fin_order_pic_of_is_reduced_finite_int --> f_pic_pi_is_of_fin_order
  f_is_of_fin_order_pic_of_is_reduced_finite_int --> concept_picard_group
  f_is_of_fin_order_pic_of_is_reduced_finite_int --> concept_prime_ideals_localization
  f_toroidal_compactification__is_completed_strict_hens --> concept_schemes_basics
  f_toroidal_compactification__is_completed_strict_hens --> concept_local_rings
  f_toroidal_compactification__is_completed_strict_hens --> concept_flat_modules
  f_toroidal_compactification__is_completed_strict_hens --> concept_integral_closure_fraction_fields
  f_toroidal_compactification__is_completed_strict_hens --> concept_hensel_lifting
  f_toroidal_compactification__is_completed_strict_hens --> concept_etale_ring_maps
  f_represents_kill_ideal --> f_toroidal_compactification__is_completed_strict_hens
  f_represents_kill_ideal --> concept_schemes_basics
  f_represents_kill_ideal --> concept_prime_ideals_localization
  f_represents_kill_ideal --> concept_categorical_pullbacks
  f_ideal_represents_of_away_cover --> f_represents_kill_ideal
  f_ideal_represents_of_away_cover --> concept_prime_ideals_localization
  f_ideal_represents_of_away_cover --> concept_local_rings
  f_ideal_represents_of_away_cover_statement --> f_ideal_represents_of_away_cover
  f_exists_basic_open_cover_ideal_represents --> f_represents_kill_ideal
  f_exists_basic_open_cover_ideal_represents --> concept_schemes_basics
  f_exists_basic_open_cover_ideal_represents --> concept_prime_ideals_localization
  f_exists_basic_open_cover_ideal_represents --> concept_point_set_topology
  f_exists_basic_open_cover_ideal_represents_statement --> f_exists_basic_open_cover_ideal_represents
  f_ideal_killed_by_ring_maps_with_property_le_ker_app --> f_represents_kill_ideal
  f_ideal_killed_by_ring_maps_with_property_le_ker_app --> concept_schemes_basics
  f_ideal_killed_by_ring_maps_with_property_le_ker_app --> concept_point_set_topology
  f_ideal_killed_by_ring_maps_with_property_le_ker_app_statement --> f_ideal_killed_by_ring_maps_with_property_le_ker_app
  f_affine_point_property_of_le_ker_app --> f_represents_kill_ideal
  f_affine_point_property_of_le_ker_app --> concept_schemes_basics
  f_affine_point_property_of_le_ker_app --> concept_point_set_topology
  f_affine_point_property_of_le_ker_app --> concept_prime_ideals_localization
  f_is_closed_of_local_ideal_point_property --> f_ideal_represents_of_away_cover_statement
  f_is_closed_of_local_ideal_point_property --> f_exists_basic_open_cover_ideal_represents_statement
  f_is_closed_of_local_ideal_point_property --> f_ideal_killed_by_ring_maps_with_property_le_ker_app_statement
  f_is_closed_of_local_ideal_point_property --> f_affine_point_property_of_le_ker_app
  f_is_closed_of_local_ideal_point_property --> f_represents_kill_ideal
  f_is_closed_of_local_ideal_point_property --> concept_schemes_basics
  f_is_closed_of_local_ideal_point_property --> concept_categorical_pullbacks
  f_diamond_operator_of_matrix_modular_form_gamma1_inter_gam --> f_foundations__pet_eq_rel_index_mul_pet_prod
  f_diamond_operator_of_matrix_modular_form_gamma1_inter_gam --> concept_modular_forms
  f_diamond_operator_of_matrix_modular_form_gamma1_inter_gam --> concept_hecke_operators
  f_diamond_operator_of_matrix_modular_form_gamma1_inter_gam --> concept_normal_subgroups_quotients
  f_diamond_operator_of_matrix_modular_form_gamma1_inter_gam --> modular_arithmetic
  f_gamma1_inter_gamma0_modular_form_has_sum_q_expansion --> concept_modular_forms
  f_gamma1_inter_gamma0_modular_form_has_sum_q_expansion --> infinite_series
  f_gamma1_inter_gamma0_modular_form_has_sum_q_expansion --> fourier_analysis
  f_gamma1_inter_gamma0_modular_form_has_sum_q_expansion --> complex_numbers
  f_has_sum_hecke_u_operator_explicit --> concept_hecke_operators
  f_has_sum_hecke_u_operator_explicit --> concept_roots_of_unity_kummer
  f_has_sum_hecke_u_operator_explicit --> infinite_series
  f_has_sum_hecke_u_operator_explicit --> complex_numbers
  f_has_sum_hecke_v_operator_explicit --> concept_hecke_operators
  f_has_sum_hecke_v_operator_explicit --> infinite_series
  f_has_sum_hecke_v_operator_explicit --> complex_numbers
  f_q_expansion_coeff_period_one_eq_of_has_sum --> complex_analysis
  f_q_expansion_coeff_period_one_eq_of_has_sum --> infinite_series
  f_q_expansion_coeff_period_one_eq_of_has_sum --> concept_modular_forms
  f_q_expansion_coeff_period_one_eq_of_has_sum --> real_analysis
  f_q_expansion_coeff_hecke_t_operator_gamma1_inter_gamma0 --> f_diamond_operator_of_matrix_modular_form_gamma1_inter_gam
  f_q_expansion_coeff_hecke_t_operator_gamma1_inter_gamma0 --> f_gamma1_inter_gamma0_modular_form_has_sum_q_expansion
  f_q_expansion_coeff_hecke_t_operator_gamma1_inter_gamma0 --> f_has_sum_hecke_u_operator_explicit
  f_q_expansion_coeff_hecke_t_operator_gamma1_inter_gamma0 --> f_has_sum_hecke_v_operator_explicit
  f_q_expansion_coeff_hecke_t_operator_gamma1_inter_gamma0 --> f_q_expansion_coeff_period_one_eq_of_has_sum
  f_q_expansion_coeff_hecke_t_operator_gamma1_inter_gamma0 --> f_foundations__pet_eq_rel_index_mul_pet_prod
  f_q_expansion_coeff_hecke_t_operator_gamma1_inter_gamma0 --> concept_hecke_operators
  f_q_expansion_coeff_hecke_t_operator_gamma1_inter_gamma0 --> concept_modular_forms
  f_q_expansion_coeff_hecke_t_operator_gamma1_inter_gamma0 --> primes_divisibility
  f_adelic_hermitian_forms__is_herm_hyperbolic --> concept_hermitian_unitary_matrices
  f_adelic_hermitian_forms__is_herm_hyperbolic --> linear_algebra
  f_adelic_hermitian_forms__is_herm_hyperbolic --> complex_numbers
  f_existence_of_lattices__hat1 --> number_fields
  f_existence_of_lattices__hat1 --> p_adic_numbers
  f_existence_of_lattices__hat1 --> concept_tensor_product_of_algebras
  f_existence_of_lattices__hat1 --> concept_valuation_rings
  f_existence_of_lattices__hat1 --> concept_lattices_in_the_plane
  f_exists_nsmul_mul_vec_mem --> number_fields
  f_exists_nsmul_mul_vec_mem --> concept_integral_closure_fraction_fields
  f_exists_nsmul_mul_vec_mem --> linear_algebra
  f_exists_nsmul_mul_vec_mem --> concept_lattices_in_the_plane
  f_adelic_lattice_proofs__imports_ter --> number_fields
  f_adelic_lattice_proofs__imports_ter --> concept_integral_closure_fraction_fields
  f_adelic_lattice_proofs__imports_ter --> linear_algebra
  f_adelic_lattice_proofs__transvection_identities_unitary --> f_adelic_hermitian_forms__is_herm_hyperbolic
  f_adelic_lattice_proofs__transvection_identities_unitary --> concept_hermitian_unitary_matrices
  f_adelic_lattice_proofs__transvection_identities_unitary --> linear_algebra
  f_exists_trace_zero_adjustment_of_hermitian_lattice --> f_exists_nsmul_mul_vec_mem
  f_exists_trace_zero_adjustment_of_hermitian_lattice --> f_adelic_lattice_proofs__imports_ter
  f_exists_trace_zero_adjustment_of_hermitian_lattice --> f_adelic_hermitian_forms__is_herm_hyperbolic
  f_exists_trace_zero_adjustment_of_hermitian_lattice --> primes_divisibility
  f_exists_trace_zero_adjustment_of_hermitian_lattice --> modular_arithmetic
  f_exists_trace_zero_adjustment_of_hermitian_lattice --> concept_lattices_in_the_plane
  f_unitary_transvection_submonoid_adjust_integral_away --> f_exists_trace_zero_adjustment_of_hermitian_lattice
  f_unitary_transvection_submonoid_adjust_integral_away --> f_adelic_lattice_proofs__transvection_identities_unitary
  f_unitary_transvection_submonoid_adjust_integral_away --> f_adelic_hermitian_forms__is_herm_hyperbolic
  f_unitary_transvection_submonoid_adjust_integral_away --> concept_lattices_in_the_plane
  f_unitary_transvection_submonoid_adjust_integral_away --> groups
  f_homogeneous_ideals__exists_ring_equiv_of_is_transcendence_basis --> concept_field_extensions_transcendence
  f_homogeneous_ideals__exists_ring_equiv_of_is_transcendence_basis --> algebraic_closure
  f_homogeneous_ideals__exists_ring_equiv_of_is_transcendence_basis --> polynomials
  f_homogeneous_ideals__exists_ring_equiv_of_is_transcendence_basis --> concept_galois_fixed_fields
  f_adelic_lattice_proofs__exists_ring_equiv_apply_ne_of_is_algebraic --> f_homogeneous_ideals__exists_ring_equiv_of_is_transcendence_basis
  f_adelic_lattice_proofs__exists_ring_equiv_apply_ne_of_is_algebraic --> concept_galois_fixed_fields
  f_adelic_lattice_proofs__exists_ring_equiv_apply_ne_of_is_algebraic --> concept_field_extensions_transcendence
  f_adelic_lattice_proofs__exists_ring_equiv_apply_ne_of_is_algebraic --> complex_numbers
  f_adelic_lattice_proofs__exists_ring_equiv_ne_of_transcendental --> concept_field_extensions_transcendence
  f_adelic_lattice_proofs__exists_ring_equiv_ne_of_transcendental --> algebraic_closure
  f_adelic_lattice_proofs__exists_ring_equiv_ne_of_transcendental --> polynomials
  f_adelic_lattice_proofs__exists_ring_equiv_ne_of_transcendental --> complex_numbers
  f_adelic_lattice_proofs__exists_rat_of_forall_complex_ring_equiv_fixed --> f_adelic_lattice_proofs__exists_ring_equiv_apply_ne_of_is_algebraic
  f_adelic_lattice_proofs__exists_rat_of_forall_complex_ring_equiv_fixed --> f_adelic_lattice_proofs__exists_ring_equiv_ne_of_transcendental
  f_adelic_lattice_proofs__exists_rat_of_forall_complex_ring_equiv_fixed --> concept_field_extensions_transcendence
  f_adelic_lattice_proofs__exists_rat_of_forall_complex_ring_equiv_fixed --> concept_galois_fixed_fields
  f_adelic_lattice_proofs__galois_stable_submodule_le_span_rational --> f_adelic_lattice_proofs__exists_rat_of_forall_complex_ring_equiv_fixed
  f_adelic_lattice_proofs__galois_stable_submodule_le_span_rational --> linear_algebra
  f_adelic_lattice_proofs__galois_stable_submodule_le_span_rational --> concept_galois_fixed_fields
  f_adelic_lattice_proofs__galois_stable_submodule_le_span_rational --> proofs
  f_mem_span_rational_kronecker_invariants --> f_adelic_lattice_proofs__galois_stable_submodule_le_span_rational
  f_mem_span_rational_kronecker_invariants --> linear_algebra
  f_mem_span_rational_kronecker_invariants --> concept_group_actions
  f_mem_span_rational_kronecker_invariants --> concept_galois_fixed_fields
  f_convex_nerve_complexes__nerve_face_closed --> concept_chain_complexes_homology
  f_convex_nerve_complexes__nerve_face_closed --> counting
  f_convex_nerve_complexes__nerve_face_closed --> concept_point_set_topology
  f_alt_double_sum --> f_convex_nerve_complexes__nerve_face_closed
  f_alt_double_sum --> concept_chain_complexes_homology
  f_alt_double_sum --> counting
  f_bd_mem --> f_convex_nerve_complexes__nerve_face_closed
  f_bd_mem --> concept_chain_complexes_homology
  f_acyc_cone --> f_convex_nerve_complexes__nerve_face_closed
  f_acyc_cone --> concept_chain_complexes_homology
  f_acyc_directed --> f_convex_nerve_complexes__nerve_face_closed
  f_acyc_directed --> concept_chain_complexes_homology
  f_acyc_union --> f_convex_nerve_complexes__nerve_face_closed
  f_acyc_union --> f_bd_mem
  f_acyc_union --> f_alt_double_sum
  f_acyc_union --> concept_chain_complexes_homology
  f_nerve_cut --> f_convex_nerve_complexes__nerve_face_closed
  f_nerve_cut --> linear_algebra
  f_nerve_cut --> concept_point_set_topology
  f_nerve_sep --> f_convex_nerve_complexes__nerve_face_closed
  f_nerve_sep --> linear_algebra
  f_nerve_sep --> concept_point_set_topology
  f_nerve_sep --> counting
  f_nerve_compact --> f_acyc_cone
  f_nerve_compact --> f_acyc_union
  f_nerve_compact --> f_nerve_sep
  f_nerve_compact --> f_nerve_cut
  f_nerve_compact --> f_convex_nerve_complexes__nerve_face_closed
  f_nerve_compact --> concept_point_set_topology
  f_nerve_compact --> counting
  f_nerve_convex --> f_acyc_directed
  f_nerve_convex --> f_nerve_compact
  f_nerve_convex --> f_convex_nerve_complexes__nerve_face_closed
  f_nerve_convex --> concept_point_set_topology
  f_nerve_convex --> linear_algebra
  f_pow_form --> calculus
  f_pow_form --> real_analysis
  f_pow_form --> linear_algebra
  f_pow_form --> complex_numbers
  f_divisor_proofs__poly_mul_gaussian_bounded --> calculus
  f_divisor_proofs__poly_mul_gaussian_bounded --> real_analysis
  f_divisor_proofs__poly_mul_gaussian_bounded --> polynomials
  f_gaussian_iterated_f_deriv_weighted_exp_bounded --> f_divisor_proofs__poly_mul_gaussian_bounded
  f_gaussian_iterated_f_deriv_weighted_exp_bounded --> calculus
  f_gaussian_iterated_f_deriv_weighted_exp_bounded --> real_analysis
  f_gaussian_iterated_f_deriv_weighted_exp_bounded --> linear_algebra
  f_norm_gaussian_convolution_series_coefficient_le_integr --> f_pow_form
  f_norm_gaussian_convolution_series_coefficient_le_integr --> fourier_analysis
  f_norm_gaussian_convolution_series_coefficient_le_integr --> calculus
  f_norm_gaussian_convolution_series_coefficient_le_integr --> real_analysis
  f_norm_iterated_f_deriv_multilinear_diagonal_le --> calculus
  f_norm_iterated_f_deriv_multilinear_diagonal_le --> linear_algebra
  f_norm_iterated_f_deriv_multilinear_diagonal_le --> real_analysis
  f_gaussian_convolution_series_coefficient_desc_factoria --> f_pow_form
  f_gaussian_convolution_series_coefficient_desc_factoria --> calculus
  f_gaussian_convolution_series_coefficient_desc_factoria --> real_analysis
  f_gaussian_convolution_series_coefficient_desc_factoria --> infinite_series
  f_summable_seminorm_gaussian_convolution_series_term --> f_gaussian_iterated_f_deriv_weighted_exp_bounded
  f_summable_seminorm_gaussian_convolution_series_term --> f_norm_gaussian_convolution_series_coefficient_le_integr
  f_summable_seminorm_gaussian_convolution_series_term --> f_norm_iterated_f_deriv_multilinear_diagonal_le
  f_summable_seminorm_gaussian_convolution_series_term --> f_gaussian_convolution_series_coefficient_desc_factoria
  f_summable_seminorm_gaussian_convolution_series_term --> f_pow_form
  f_summable_seminorm_gaussian_convolution_series_term --> infinite_series
  f_summable_seminorm_gaussian_convolution_series_term --> real_analysis
  f_summable_seminorm_gaussian_convolution_series_term --> fourier_analysis
  f_nonempty_alg_hom_adjoin --> concept_prime_ideals_localization
  f_nonempty_alg_hom_adjoin --> rings_fields
  f_adjoin_hom_extend_of_denominator --> f_nonempty_alg_hom_adjoin
  f_adjoin_hom_extend_of_denominator --> rings_fields
  f_extend_alg_hom_adjoin_integral_root --> concept_integral_closure_fraction_fields
  f_extend_alg_hom_adjoin_integral_root --> polynomials
  f_extend_alg_hom_adjoin_integral_root --> rings_fields
  f_is_integrally_closed_adjoin --> concept_integral_closure_fraction_fields
  f_is_integrally_closed_adjoin --> concept_field_extensions_transcendence
  f_is_integrally_closed_adjoin --> polynomials
  f_is_integrally_closed_adjoin --> concept_separable_polynomials
  f_linear_indep_on_pow_of_is_domain_tensor_purely_inseparabl --> concept_tensor_product_of_algebras
  f_linear_indep_on_pow_of_is_domain_tensor_purely_inseparabl --> concept_flat_modules
  f_linear_indep_on_pow_of_is_domain_tensor_purely_inseparabl --> linear_algebra
  f_linear_indep_on_pow_of_is_domain_tensor_purely_inseparabl --> algebraic_closure
  f_linear_indep_on_pow_of_is_domain_tensor_purely_inseparabl --> concept_integral_closure_fraction_fields
  f_exists_primitive_element_separability_certificate --> f_is_integrally_closed_adjoin
  f_exists_primitive_element_separability_certificate --> concept_field_extensions_transcendence
  f_exists_primitive_element_separability_certificate --> concept_separable_polynomials
  f_exists_primitive_element_separability_certificate --> concept_integral_closure_fraction_fields
  f_exists_primitive_element_separability_certificate --> polynomials
  f_exists_finite_separable_point_of_separable_closure_poin --> concept_finitely_generated_algebras
  f_exists_finite_separable_point_of_separable_closure_poin --> concept_separable_polynomials
  f_exists_finite_separable_point_of_separable_closure_poin --> concept_field_extensions_transcendence
  f_exists_finite_separable_point_of_separable_closure_poin --> algebraic_closure
  f_exists_separable_point_of_geometrically_domain --> f_is_integrally_closed_adjoin
  f_exists_separable_point_of_geometrically_domain --> f_exists_primitive_element_separability_certificate
  f_exists_separable_point_of_geometrically_domain --> f_extend_alg_hom_adjoin_integral_root
  f_exists_separable_point_of_geometrically_domain --> f_adjoin_hom_extend_of_denominator
  f_exists_separable_point_of_geometrically_domain --> f_linear_indep_on_pow_of_is_domain_tensor_purely_inseparabl
  f_exists_separable_point_of_geometrically_domain --> f_exists_finite_separable_point_of_separable_closure_poin
  f_exists_separable_point_of_geometrically_domain --> concept_field_extensions_transcendence
  f_exists_separable_point_of_geometrically_domain --> concept_separable_polynomials
  f_exists_separable_point_of_geometrically_domain --> concept_tensor_product_of_algebras
  f_exists_separable_point_of_geometrically_domain --> concept_finitely_generated_algebras
  f_divisors__has_q_iff --> concept_modular_forms
  f_divisors__has_q_iff --> infinite_series
  f_divisors__has_q_iff --> complex_numbers
  f_divisors__has_q_iff --> concept_lattices_in_the_plane
  f_divisors__zeta_act_refl --> f_divisors__has_q_iff
  f_divisors__zeta_act_refl --> concept_modular_forms
  f_divisors__zeta_act_refl --> concept_roots_of_unity_kummer
  f_divisors__zeta_act_refl --> modular_arithmetic
  f_divisors__zeta_act_refl --> primes_divisibility
  f_divisors__zeta_act_refl --> concept_lattices_in_the_plane
  f_root_of_unity_exp_z_mod_additive_character_properties --> f_divisors__zeta_act_refl
  f_root_of_unity_exp_z_mod_additive_character_properties --> concept_roots_of_unity_kummer
  f_root_of_unity_exp_z_mod_additive_character_properties --> modular_arithmetic
  f_root_of_unity_exp_z_mod_additive_character_properties --> groups
  f_root_of_unity_exp_z_mod_additive_character_properties --> complex_numbers
  f_tsum_residue_class_split_by_sign --> infinite_series
  f_tsum_residue_class_split_by_sign --> modular_arithmetic
  f_tsum_residue_class_split_by_sign --> counting
  f_has_sum_lambert_double_series_divisors --> infinite_series
  f_has_sum_lambert_double_series_divisors --> primes_divisibility
  f_has_sum_lambert_double_series_divisors --> counting
  f_torsion_point_row_sum_eq_q_expansion_series --> f_root_of_unity_exp_z_mod_additive_character_properties
  f_torsion_point_row_sum_eq_q_expansion_series --> f_divisors__zeta_act_refl
  f_torsion_point_row_sum_eq_q_expansion_series --> concept_modular_forms
  f_torsion_point_row_sum_eq_q_expansion_series --> infinite_series
  f_torsion_point_row_sum_eq_q_expansion_series --> complex_analysis
  f_torsion_point_rows_sum_eq_divisor_series --> f_torsion_point_row_sum_eq_q_expansion_series
  f_torsion_point_rows_sum_eq_divisor_series --> f_tsum_residue_class_split_by_sign
  f_torsion_point_rows_sum_eq_divisor_series --> f_has_sum_lambert_double_series_divisors
  f_torsion_point_rows_sum_eq_divisor_series --> f_divisors__zeta_act_refl
  f_torsion_point_rows_sum_eq_divisor_series --> concept_modular_forms
  f_torsion_point_rows_sum_eq_divisor_series --> infinite_series
  f_torsion_point_rows_sum_eq_divisor_series --> primes_divisibility
  f_hermitian_local_continuous_congruence_section --> concept_dedekind_domains
  f_hermitian_local_continuous_congruence_section --> concept_prime_ideals_localization
  f_dedekind_power_localization --> f_hermitian_local_continuous_congruence_section
  f_dedekind_power_localization --> concept_dedekind_domains
  f_divisor_proofs__tensor_involution_algebra_properties --> concept_flat_modules
  f_divisor_proofs__tensor_involution_algebra_properties --> concept_local_rings
  f_divisor_proofs__tensor_involution_algebra_properties --> concept_prime_ideals_localization
  f_flat_localization_membership --> f_divisor_proofs__tensor_involution_algebra_properties
  f_flat_localization_membership --> concept_flat_modules
  f_flat_localization_membership --> concept_prime_ideals_localization
  f_gram_fiber_measures_unique_ae --> concept_prime_ideals_localization
  f_gram_fiber_measures_unique_ae --> concept_local_rings
  f_localization_inverse_mod_f --> f_gram_fiber_measures_unique_ae
  f_localization_inverse_mod_f --> concept_prime_ideals_localization
  f_primitive_vector_quadratic_level_measure --> concept_prime_ideals_localization
  f_primitive_vector_quadratic_level_measure --> concept_local_rings
  f_primitive_vector_quadratic_level_measure --> modular_arithmetic
  f_localization_residue_approximation --> f_primitive_vector_quadratic_level_measure
  f_localization_residue_approximation --> concept_prime_ideals_localization
  f_divisor_proofs__local_hermitian_diagonalization_units --> concept_prime_ideals_localization
  f_divisor_proofs__local_hermitian_diagonalization_units --> concept_hensel_lifting
  f_divisor_proofs__local_hermitian_diagonalization_units --> rings_fields
  f_nilpotent_approximation_surjective --> f_divisor_proofs__local_hermitian_diagonalization_units
  f_nilpotent_approximation_surjective --> concept_hensel_lifting
  f_etale_unique_prime_le_map_maximal --> concept_etale_ring_maps
  f_etale_unique_prime_le_map_maximal --> concept_prime_ideals_localization
  f_etale_unique_prime_le_map_maximal --> concept_local_rings
  f_isolate_maximal_among_primes_containing_etale --> concept_etale_ring_maps
  f_isolate_maximal_among_primes_containing_etale --> concept_dedekind_domains
  f_isolate_maximal_among_primes_containing_etale --> concept_prime_ideals_localization
  f_isolate_maximal_among_primes_containing_etale --> concept_noetherian_and_irreducible_components
  f_etale_away_quotient_eq_localization --> f_dedekind_power_localization
  f_etale_away_quotient_eq_localization --> f_isolate_maximal_among_primes_containing_etale
  f_etale_away_quotient_eq_localization --> f_localization_inverse_mod_f
  f_etale_away_quotient_eq_localization --> f_etale_unique_prime_le_map_maximal
  f_etale_away_quotient_eq_localization --> f_localization_residue_approximation
  f_etale_away_quotient_eq_localization --> f_nilpotent_approximation_surjective
  f_etale_away_quotient_eq_localization --> f_flat_localization_membership
  f_etale_away_quotient_eq_localization --> concept_etale_ring_maps
  f_etale_away_quotient_eq_localization --> concept_dedekind_domains
  f_etale_away_quotient_eq_localization --> concept_prime_ideals_localization
  f_commuting_semisimple_eigenspaces_span --> linear_algebra
  f_commuting_semisimple_eigenspaces_span --> algebraic_closure
  f_commuting_semisimple_eigenspaces_span --> polynomials
  f_commuting_semisimple_eigenspaces_span --> concept_separable_polynomials
  f_dvr_rep_eigenspaces_span_top --> f_commuting_semisimple_eigenspaces_span
  f_dvr_rep_eigenspaces_span_top --> f_exists_ring_hom_of_joint_eigenvalue
  f_dvr_rep_eigenspaces_span_top --> f_exists_separable_annihilating_poly
  f_dvr_rep_eigenspaces_span_top --> f_padic_ring_hom_unique_adic_complete
  f_dvr_rep_eigenspaces_span_top --> f_scalar_rep_commute_and_annihilate
  f_dvr_rep_eigenspaces_span_top --> f_divisor_base__sandwich_maps
  f_dvr_rep_eigenspaces_span_top --> concept_discrete_valuation_ring
  f_dvr_rep_eigenspaces_span_top --> concept_valuation_rings
  f_dvr_rep_eigenspaces_span_top --> p_adic_numbers
  f_dvr_rep_eigenspaces_span_top --> concept_group_representations
  f_exists_ring_hom_of_joint_eigenvalue --> linear_algebra
  f_exists_ring_hom_of_joint_eigenvalue --> concept_valuation_rings
  f_exists_ring_hom_of_joint_eigenvalue --> concept_ultrametric_norm
  f_exists_ring_hom_of_joint_eigenvalue --> rings_fields
  f_exists_separable_annihilating_poly --> p_adic_numbers
  f_exists_separable_annihilating_poly --> polynomials
  f_exists_separable_annihilating_poly --> concept_separable_polynomials
  f_exists_separable_annihilating_poly --> concept_integral_closure_fraction_fields
  f_exists_separable_annihilating_poly --> concept_field_extensions_transcendence
  f_padic_ring_hom_unique_adic_complete --> f_ring_hom_from_padic_unique_of_sep
  f_padic_ring_hom_unique_adic_complete --> p_adic_numbers
  f_padic_ring_hom_unique_adic_complete --> rings_fields
  f_padic_ring_hom_unique_adic_complete --> linear_algebra
  f_ring_hom_from_padic_unique_of_sep --> p_adic_numbers
  f_ring_hom_from_padic_unique_of_sep --> rings_fields
  f_ring_hom_from_padic_unique_of_sep --> modular_arithmetic
  f_scalar_rep_commute_and_annihilate --> linear_algebra
  f_scalar_rep_commute_and_annihilate --> polynomials
  f_scalar_rep_commute_and_annihilate --> rings_fields
  f_scalar_rep_commute_and_annihilate --> concept_group_representations
  f_period_integrals__add_int_g --> p_adic_numbers
  f_period_integrals__add_int_g --> concept_ultrametric_norm
  f_period_integrals__add_int_g --> concept_roots_of_unity_kummer
  f_period_integrals__add_int_g --> concept_witt_vectors_ainf
  f_period_integrals__add_int_g --> infinite_series
  f_period_integrals__add_int_g --> polynomials
  f_period_integrals__exp_int_w --> p_adic_numbers
  f_period_integrals__exp_int_w --> concept_ultrametric_norm
  f_period_integrals__exp_int_w --> concept_roots_of_unity_kummer
  f_period_integrals__exp_int_w --> concept_witt_vectors_ainf
  f_period_integrals__exp_int_w --> infinite_series
  f_period_integrals__exp_int_w --> calculus
  f_period_integrals__inv_ser_sub --> f_period_integrals__add_int_g
  f_period_integrals__inv_ser_sub --> f_period_integrals__exp_int_w
  f_period_integrals__inv_ser_sub --> polynomials
  f_period_integrals__inv_ser_sub --> rings_fields
  f_period_integrals__inv_ser_sub --> p_adic_numbers
  f_exponential_integrality__development --> f_period_integrals__exp_int_w
  f_exponential_integrality__development --> p_adic_numbers
  f_exponential_integrality__development --> concept_ultrametric_norm
  f_exponential_integrality__development --> concept_roots_of_unity_kummer
  f_exponential_integrality__inv_nat_cast_mem_witt_integers --> f_period_integrals__exp_int_w
  f_exponential_integrality__inv_nat_cast_mem_witt_integers --> p_adic_numbers
  f_exponential_integrality__inv_nat_cast_mem_witt_integers --> concept_ultrametric_norm
  f_exponential_integrality__inv_nat_cast_mem_witt_integers --> infinite_series
  f_exponential_integrality__inv_nat_cast_mem_witt_integers --> primes_divisibility
  f_exponential_integrality__inv_nat_cast_mem_witt_integers --> modular_arithmetic
  f_roots_of_unity_ring_le_witt_integers --> f_exponential_integrality__development
  f_roots_of_unity_ring_le_witt_integers --> f_period_integrals__exp_int_w
  f_roots_of_unity_ring_le_witt_integers --> concept_roots_of_unity_kummer
  f_roots_of_unity_ring_le_witt_integers --> concept_ultrametric_norm
  f_roots_of_unity_ring_le_witt_integers --> p_adic_numbers
  f_roots_of_unity_ring_le_witt_integers --> modular_arithmetic
  f_roots_of_unity_ring_le_witt_integers --> infinite_series
  f_step_i_i_i --> f_exponential_integrality__development
  f_step_i_i_i --> f_exponential_integrality__inv_nat_cast_mem_witt_integers
  f_step_i_i_i --> f_period_integrals__exp_int_w
  f_step_i_i_i --> p_adic_numbers
  f_step_i_i_i --> concept_ultrametric_norm
  f_step_i_i_i --> proofs
  f_flog_constant_coeff --> f_wf_ring
  f_flog_constant_coeff --> f_wf_subst
  f_flog_constant_coeff --> f_period_integrals__inv_ser_sub
  f_flog_constant_coeff --> f_w2pair
  f_flog_constant_coeff --> f_period_integrals__add_int_g
  f_flog_constant_coeff --> f_step_i_i_i
  f_flog_constant_coeff --> f_roots_of_unity_ring_le_witt_integers
  f_flog_constant_coeff --> p_adic_numbers
  f_w2pair --> f_period_integrals__add_int_g
  f_w2pair --> f_period_integrals__exp_int_w
  f_w2pair --> p_adic_numbers
  f_w2pair --> concept_roots_of_unity_kummer
  f_wf_ring --> f_period_integrals__exp_int_w
  f_wf_ring --> p_adic_numbers
  f_wf_ring --> rings_fields
  f_wf_ring --> polynomials
  f_wf_subst --> f_period_integrals__exp_int_w
  f_wf_subst --> p_adic_numbers
  f_wf_subst --> rings_fields
  f_wf_subst --> polynomials
  f_wf_subst --> infinite_series
  f_divisor_proofs__div_fractions_bilinear_formula --> f_divisor_proofs__h_poly_add_two
  f_divisor_proofs__div_fractions_bilinear_formula --> concept_hermitian_unitary_matrices
  f_divisor_proofs__div_fractions_bilinear_formula --> complex_numbers
  f_divisor_proofs__div_fractions_bilinear_formula --> calculus
  f_divisor_proofs__div_fractions_bilinear_formula --> real_analysis
  f_divisor_proofs__div_fractions_bilinear_formula --> linear_algebra
  f_fibre_cosine_explicit_formula --> f_divisor_proofs__fs_one
  f_fibre_cosine_explicit_formula --> concept_hermitian_unitary_matrices
  f_fibre_cosine_explicit_formula --> complex_numbers
  f_fibre_cosine_explicit_formula --> linear_algebra
  f_fibre_cosine_explicit_formula --> real_analysis
  f_fibre_cosine_pushforward_uniform --> f_fibre_cosine_explicit_formula
  f_fibre_cosine_pushforward_uniform --> f_divisor_proofs__mobius_change_of_variables
  f_fibre_cosine_pushforward_uniform --> f_divisor_proofs__stereographic_measure_change
  f_fibre_cosine_pushforward_uniform --> f_divisor_proofs__fs_one
  f_fibre_cosine_pushforward_uniform --> counting
  f_fibre_cosine_pushforward_uniform --> real_analysis
  f_fibre_cosine_pushforward_uniform --> calculus
  f_divisor_proofs__fs_one --> complex_numbers
  f_divisor_proofs__fs_one --> linear_algebra
  f_divisor_proofs__fs_one --> concept_hermitian_unitary_matrices
  f_divisor_proofs__fs_one --> trigonometry
  f_divisor_proofs__h_poly_add_two --> polynomials
  f_divisor_proofs__h_poly_add_two --> complex_numbers
  f_divisor_proofs__h_poly_add_two --> linear_algebra
  f_divisor_proofs__h_poly_add_two --> real_analysis
  f_divisor_proofs__mobius_change_of_variables --> f_divisor_proofs__div_fractions_bilinear_formula
  f_divisor_proofs__mobius_change_of_variables --> complex_numbers
  f_divisor_proofs__mobius_change_of_variables --> calculus
  f_divisor_proofs__mobius_change_of_variables --> real_analysis
  f_divisor_proofs__stereographic_measure_change --> calculus
  f_divisor_proofs__stereographic_measure_change --> real_analysis
  f_divisor_proofs__stereographic_measure_change --> complex_numbers
  f_divisor_proofs__stereographic_measure_change --> trigonometry
  f_period_integrals__primes_dyadic_r_s --> primes_divisibility
  f_period_integrals__primes_dyadic_r_s --> real_analysis
  f_period_integrals__primes_dyadic_r_s --> counting
  f_period_integrals__sqf_lab --> polynomials
  f_period_integrals__sqf_lab --> modular_arithmetic
  f_period_integrals__sqf_lab --> primes_divisibility
  f_period_integrals__sqf_lab --> algebraic_closure
  f_period_integrals__sqf_lab --> rings_fields
  f_period_integrals__sqf_lab --> groups
  f_sqf_prime_factor --> f_period_integrals__sqf_lab
  f_sqf_prime_factor --> polynomials
  f_sqf_prime_factor --> primes_divisibility
  f_sqf_prime_factor --> counting
  f_ana_core --> f_period_integrals__primes_dyadic_r_s
  f_ana_core --> real_analysis
  f_ana_core --> calculus
  f_ana_core --> primes_divisibility
  f_ana_core --> counting
  f_squarefree_prime_factor__analytic --> f_ana_core
  f_squarefree_prime_factor__analytic --> f_big_primes
  f_squarefree_prime_factor__analytic --> f_period_integrals__primes_dyadic_r_s
  f_big_primes --> f_period_integrals__sqf_lab
  f_big_primes --> polynomials
  f_big_primes --> counting
  f_big_primes --> primes_divisibility
  f_big_primes --> modular_arithmetic
  f_squarefree_prime_factor__claim_of --> f_big_primes
  f_squarefree_prime_factor__claim_of --> f_sqf_prime_factor
  f_squarefree_prime_factor__claim_of --> f_period_integrals__sqf_lab
  f_squarefree_prime_factor__claim_of --> real_analysis
  f_squarefree_prime_factor__claim_of --> counting
  f_irreducible_count_lower_bound --> f_big_primes
  f_irreducible_count_lower_bound --> rings_fields
  f_irreducible_count_lower_bound --> polynomials
  f_irreducible_count_lower_bound --> counting
  f_irreducible_count_lower_bound --> primes_divisibility
  f_irreducible_count_lower_bound --> concept_field_extensions_transcendence
  f_irreducible_count_lower_bound --> concept_galois_fixed_fields
  f_monic_deg_fn_nat_degree --> f_big_primes
  f_monic_deg_fn_nat_degree --> polynomials
  f_monic_deg_fn_nat_degree --> counting
  f_monic_deg_fn_nat_degree --> modular_arithmetic
  f_sqf_prime_factor_of --> f_squarefree_prime_factor__claim_of
  f_sqf_prime_factor_of --> f_squarefree_count_estimate
  f_sqf_prime_factor_of --> f_irreducible_count_lower_bound
  f_sqf_prime_factor_of --> f_squarefree_prime_factor__analytic
  f_sqf_prime_factor_of --> f_period_integrals__primes_dyadic_r_s
  f_sqf_prime_factor_of --> f_sqf_prime_factor
  f_squarefree_count_estimate --> f_big_primes
  f_squarefree_count_estimate --> f_monic_deg_fn_nat_degree
  f_squarefree_count_estimate --> f_period_integrals__sqf_lab
  f_squarefree_count_estimate --> polynomials
  f_squarefree_count_estimate --> counting
  f_squarefree_count_estimate --> primes_divisibility
  f_commutative_algebra__dual_order --> groups
  f_commutative_algebra__dual_order --> rings_fields
  f_commutative_algebra__dual_order --> linear_algebra
  f_commutative_algebra__dual_order --> concept_group_representations
  f_commutative_algebra__models --> f_p_adic_hodge__finite_flat
  f_commutative_algebra__models --> f_commutative_algebra__translate_mem_ind_order
  f_commutative_algebra__models --> groups
  f_commutative_algebra__models --> rings_fields
  f_commutative_algebra__models --> concept_schemes_basics
  f_commutative_algebra__translate_mem_ind_order --> groups
  f_commutative_algebra__translate_mem_ind_order --> rings_fields
  f_commutative_algebra__translate_mem_ind_order --> concept_flat_modules
  f_commutative_algebra__translate_mem_ind_order --> linear_algebra
  f_commutative_algebra__translate_mem_ind_order --> concept_normal_subgroups_quotients
  f_global_geometry__exists_unit_form_localization_etale_nbhd --> concept_schemes_basics
  f_global_geometry__exists_unit_form_localization_etale_nbhd --> concept_flat_modules
  f_global_geometry__exists_unit_form_localization_etale_nbhd --> concept_categorical_pullbacks
  f_global_geometry__exists_unit_form_localization_etale_nbhd --> concept_integral_closure_fraction_fields
  f_global_geometry__exists_unit_form_localization_etale_nbhd --> concept_local_rings
  f_global_geometry__exists_unit_form_localization_etale_nbhd --> groups
  f_base_change_points_compat --> f_global_geometry__exists_unit_form_localization_etale_nbhd
  f_base_change_points_compat --> concept_schemes_basics
  f_base_change_points_compat --> concept_categorical_pullbacks
  f_base_change_points_compat --> concept_integral_closure_fraction_fields
  f_base_change_points_compat --> rings_fields
  f_regular_at_base_change --> f_htat_bc_pull
  f_regular_at_base_change --> f_global_geometry__exists_unit_form_localization_etale_nbhd
  f_regular_at_base_change --> concept_schemes_basics
  f_htat_bc_pull --> f_base_change_points_compat
  f_htat_bc_pull --> f_global_geometry__exists_unit_form_localization_etale_nbhd
  f_htat_bc_pull --> concept_schemes_basics
  f_htat_bc_pull --> concept_categorical_pullbacks
  f_htat_bc_pull --> concept_local_rings
  f_p_adic_hodge__finite_flat --> concept_flat_modules
  f_p_adic_hodge__finite_flat --> concept_tensor_product_of_algebras
  f_p_adic_hodge__finite_flat --> groups
  f_p_adic_hodge__finite_flat --> rings_fields
  f_p_adic_hodge__finite_flat --> linear_algebra
  f_p_adic_hodge__finite_flat --> concept_schemes_basics
  f_global_twisting__perm_rep_single --> concept_group_actions
  f_global_twisting__perm_rep_single --> concept_group_representations
  f_global_twisting__perm_rep_single --> concept_group_homology
  f_exists_free_resolution_short_exact --> concept_group_representations
  f_exists_free_resolution_short_exact --> concept_chain_complexes_homology
  f_exists_free_resolution_short_exact --> concept_group_homology
  f_group_homology_dimension_shift_is_iso --> concept_group_homology
  f_group_homology_dimension_shift_is_iso --> concept_chain_complexes_homology
  f_group_homology_long_exact_maps_natural_of_res --> f_global_twisting__perm_rep_single
  f_group_homology_long_exact_maps_natural_of_res --> concept_group_homology
  f_group_homology_long_exact_maps_natural_of_res --> concept_chain_complexes_homology
  f_perm_coef_preserves_short_exact --> f_global_twisting__perm_rep_single
  f_perm_coef_preserves_short_exact --> concept_chain_complexes_homology
  f_perm_coef_preserves_short_exact --> concept_group_representations
  f_projective_perm_tensor_free --> f_global_twisting__perm_rep_single
  f_projective_perm_tensor_free --> concept_group_actions
  f_projective_perm_tensor_free --> concept_group_homology
  f_projective_rep_group_homology_pos_vanishes --> concept_group_homology
  f_projective_rep_group_homology_pos_vanishes --> concept_group_representations
  f_projective_res_free_rep_of_injective --> groups
  f_projective_res_free_rep_of_injective --> concept_group_representations
  f_projective_res_free_rep_of_injective --> concept_group_homology
  f_shapiro_is_iso_group_homology_zero --> f_global_twisting__perm_rep_single
  f_shapiro_is_iso_group_homology_zero --> concept_group_actions
  f_shapiro_is_iso_group_homology_zero --> concept_group_homology
  f_shapiro_lemma_transitive_group_homology --> f_shapiro_is_iso_group_homology_zero
  f_shapiro_lemma_transitive_group_homology --> f_exists_free_resolution_short_exact
  f_shapiro_lemma_transitive_group_homology --> f_group_homology_dimension_shift_is_iso
  f_shapiro_lemma_transitive_group_homology --> f_perm_coef_preserves_short_exact
  f_shapiro_lemma_transitive_group_homology --> f_projective_perm_tensor_free
  f_shapiro_lemma_transitive_group_homology --> f_projective_rep_group_homology_pos_vanishes
  f_shapiro_lemma_transitive_group_homology --> f_projective_res_free_rep_of_injective
  f_shapiro_lemma_transitive_group_homology --> f_global_twisting__perm_rep_single
  f_shapiro_lemma_transitive_group_homology --> concept_group_homology
  f_witt_exact_sequences__is_compl --> concept_frobenius_perfect_rings
  f_witt_exact_sequences__is_compl --> concept_tensor_product_of_algebras
  f_witt_exact_sequences__is_compl --> rings_fields
  f_cov_of_alg_hom --> f_witt_exact_sequences__is_compl
  f_cov_of_alg_hom --> concept_tensor_product_of_algebras
  f_block_decomposition__exists_fg_tmul_eq_zero --> concept_tensor_product_of_algebras
  f_block_decomposition__exists_fg_tmul_eq_zero --> concept_flat_modules
  f_block_decomposition__exists_fg_tmul_eq_zero --> linear_algebra
  f_block_decomposition__exists_perfect_radical --> concept_frobenius_perfect_rings
  f_block_decomposition__exists_perfect_radical --> concept_prime_ideals_localization
  f_block_decomposition__exists_perfect_radical --> rings_fields
  f_block_decomposition__exists_p_q --> f_block_decomposition__exists_perfect_radical
  f_block_decomposition__exists_p_q --> f_witt_exact_sequences__is_compl
  f_block_decomposition__exists_p_q --> concept_frobenius_perfect_rings
  f_block_decomposition__exists_ring_hom_pow_prime_pow --> concept_frobenius_perfect_rings
  f_block_decomposition__exists_ring_hom_pow_prime_pow --> rings_fields
  f_block_decomposition__pf_facts --> f_witt_exact_sequences__is_compl
  f_block_decomposition__pf_facts --> concept_frobenius_perfect_rings
  f_block_decomposition__perfect_frobenius_root_solution --> f_block_decomposition__pf_facts
  f_block_decomposition__perfect_frobenius_root_solution --> f_block_decomposition__exists_ring_hom_pow_prime_pow
  f_block_decomposition__perfect_frobenius_root_solution --> f_witt_exact_sequences__is_compl
  f_block_decomposition__frobenius_power_solution_lift --> f_witt_exact_sequences__is_compl
  f_block_decomposition__frobenius_power_solution_lift --> concept_frobenius_perfect_rings
  f_block_decomposition__frobenius_power_solution_lift --> concept_hensel_lifting
  f_block_decomposition__one_tmul_mem_range_iff --> f_block_decomposition__exists_fg_tmul_eq_zero
  f_block_decomposition__one_tmul_mem_range_iff --> f_witt_exact_sequences__is_compl
  f_block_decomposition__one_tmul_mem_range_iff --> concept_flat_modules
  f_block_decomposition__one_tmul_mem_range_iff --> concept_tensor_product_of_algebras
  f_exists_retraction --> f_block_decomposition__exists_p_q
  f_exists_retraction --> f_block_decomposition__frobenius_power_solution_lift
  f_exists_retraction --> f_block_decomposition__perfect_frobenius_root_solution
  f_exists_retraction --> f_cov_of_alg_hom
  f_exists_retraction --> f_block_decomposition__one_tmul_mem_range_iff
  f_exists_retraction --> f_witt_exact_sequences__is_compl
  f_exists_retraction --> concept_field_extensions_transcendence
  f_exists_retraction --> polynomials
  f_global_geometry__is_cpt_gen --> concept_schemes_basics
  f_global_geometry__is_cpt_gen --> concept_local_rings
  f_global_geometry__is_cpt_gen --> concept_point_set_topology
  f_global_geometry__coords_at --> f_global_geometry__is_cpt_gen
  f_global_geometry__coords_at --> concept_schemes_basics
  f_global_geometry__coords_at --> concept_local_rings
  f_global_geometry__etale_localization_at_prime_tensor_of_low_height --> f_global_geometry__is_cpt_gen
  f_global_geometry__etale_localization_at_prime_tensor_of_low_height --> concept_exterior_powers
  f_global_geometry__etale_localization_at_prime_tensor_of_low_height --> linear_algebra
  f_global_geometry__exists_gen_of_is_v_b_one --> f_global_geometry__is_cpt_gen
  f_global_geometry__exists_gen_of_is_v_b_one --> f_global_geometry__etale_localization_at_prime_tensor_of_low_height
  f_global_geometry__exists_gen_of_is_v_b_one --> concept_integral_closure_fraction_fields
  f_global_geometry__exists_gen_of_is_v_b_one --> concept_local_rings
  f_global_geometry__is_generic_flag --> f_global_geometry__etale_localization_at_prime_tensor_of_low_height
  f_global_geometry__is_generic_flag --> f_global_geometry__is_cpt_gen
  f_global_geometry__is_generic_flag --> linear_algebra
  f_global_geometry__is_generic_flag --> concept_field_extensions_transcendence
  f_global_geometry__is_line_gen_on --> f_global_geometry__etale_localization_at_prime_tensor_of_low_height
  f_global_geometry__is_line_gen_on --> concept_exterior_powers
  f_global_geometry__level_sections_exact_kernel_locus_open --> f_global_geometry__is_line_gen_on
  f_global_geometry__level_sections_exact_kernel_locus_open --> f_global_geometry__etale_localization_at_prime_tensor_of_low_height
  f_global_geometry__level_sections_exact_kernel_locus_open --> f_global_geometry__is_cpt_gen
  f_global_geometry__level_sections_exact_kernel_locus_open --> concept_field_extensions_transcendence
  f_geometry_proofs__gen_map_germ_eq_gen_map_germ --> f_global_geometry__is_cpt_gen
  f_geometry_proofs__gen_map_germ_eq_gen_map_germ --> concept_schemes_basics
  f_geometry_proofs__gen_map_germ_eq_gen_map_germ --> concept_point_set_topology
  f_frame_near_generic_point --> f_global_geometry__is_cpt_gen
  f_frame_near_generic_point --> f_global_geometry__etale_localization_at_prime_tensor_of_low_height
  f_frame_near_generic_point --> f_geometry_proofs__gen_map_germ_eq_gen_map_germ
  f_frame_near_generic_point --> linear_algebra
  f_additive_poly_taylor_coeff_sub_norm_le --> concept_ultrametric_norm
  f_additive_poly_taylor_coeff_sub_norm_le --> p_adic_numbers
  f_additive_poly_taylor_coeff_sub_norm_le --> polynomials
  f_few_roots_small_disc --> f_additive_poly_taylor_coeff_sub_norm_le
  f_few_roots_small_disc --> f_card_roots_closed_ball_bounds_ultrametric
  f_few_roots_small_disc --> concept_newton_polygon
  f_few_roots_small_disc --> concept_ultrametric_norm
  f_few_roots_small_disc --> p_adic_numbers
  f_multiset_many_separated_points --> counting
  f_multiset_many_separated_points --> proofs
  f_separated_roots_additive_poly --> f_few_roots_small_disc
  f_separated_roots_additive_poly --> f_multiset_many_separated_points
  f_separated_roots_additive_poly --> f_card_roots_closed_ball_bounds_ultrametric
  f_separated_roots_additive_poly --> concept_newton_polygon
  f_separated_roots_additive_poly --> p_adic_numbers
  f_commutative_algebra__invariant_subspace_mobius_inverse_rec_eq_of_finrank_lt --> linear_algebra
  f_commutative_algebra__invariant_subspace_mobius_inverse_rec_eq_of_finrank_lt --> polynomials
  f_commutative_algebra__invariant_subspace_mobius_inverse_rec_eq_of_finrank_lt --> concept_group_representations
  f_character_theory__charpoly_block_and_invariant_under_stabilizer_nilradic --> f_commutative_algebra__invariant_subspace_mobius_inverse_rec_eq_of_finrank_lt
  f_character_theory__charpoly_block_and_invariant_under_stabilizer_nilradic --> linear_algebra
  f_character_theory__charpoly_block_and_invariant_under_stabilizer_nilradic --> polynomials
  f_exists_perm_of_sum_min_eq_positive_family --> counting
  f_exists_perm_of_sum_min_eq_positive_family --> proofs
  f_primary_endomorphism_cyclic_decomposition_finrank_ker --> linear_algebra
  f_primary_endomorphism_cyclic_decomposition_finrank_ker --> polynomials
  f_primary_endomorphism_cyclic_decomposition_finrank_ker --> concept_finitely_generated_abelian_groups
  f_conj_of_primary_finrank_ker_pow_eq --> f_primary_endomorphism_cyclic_decomposition_finrank_ker
  f_conj_of_primary_finrank_ker_pow_eq --> f_exists_perm_of_sum_min_eq_positive_family
  f_conj_of_primary_finrank_ker_pow_eq --> linear_algebra
  f_conj_of_primary_finrank_ker_pow_eq --> polynomials
  f_ker_aeval_add_stabilizer_nilradical_socle --> f_commutative_algebra__invariant_subspace_mobius_inverse_rec_eq_of_finrank_lt
  f_ker_aeval_add_stabilizer_nilradical_socle --> linear_algebra
  f_ker_aeval_add_stabilizer_nilradical_socle --> polynomials
  f_primitive_end_class_function_eq_zero_of_primary --> f_commutative_algebra__invariant_subspace_mobius_inverse_rec_eq_of_finrank_lt
  f_primitive_end_class_function_eq_zero_of_primary --> f_character_theory__charpoly_block_and_invariant_under_stabilizer_nilradic
  f_primitive_end_class_function_eq_zero_of_primary --> f_ker_aeval_add_stabilizer_nilradical_socle
  f_primitive_end_class_function_eq_zero_of_primary --> f_conj_of_primary_finrank_ker_pow_eq
  f_primitive_end_class_function_eq_zero_of_primary --> linear_algebra
  f_primitive_end_class_function_eq_zero_of_primary --> polynomials
  f_primitive_end_class_function_eq_zero_of_primary --> concept_group_representations
  f_block_decomposition__perfect_tensor_product --> concept_tensor_product_of_algebras
  f_block_decomposition__perfect_tensor_product --> rings_fields
  f_block_decomposition__perfect_tensor_product --> primes_divisibility
  f_block_decomposition__perfect_tensor_product --> f_block_decomposition__pf_facts
  f_block_decomposition__pq_lift --> f_block_decomposition__pf_facts
  f_block_decomposition__pq_lift --> rings_fields
  f_block_decomposition__pq_lift --> primes_divisibility
  f_block_decomposition__pq_lift --> concept_categorical_pullbacks
  f_block_decomposition__perfect_tensor_generated_lift --> f_block_decomposition__perfect_tensor_product
  f_block_decomposition__perfect_tensor_generated_lift --> f_block_decomposition__pq_lift
  f_block_decomposition__perfect_tensor_generated_lift --> f_block_decomposition__exists_p_q
  f_block_decomposition__perfect_tensor_generated_lift --> f_block_decomposition__pf_facts
  f_block_decomposition__perfect_tensor_generated_lift --> concept_tensor_product_of_algebras
  f_pq_base_change_polynomial --> f_block_decomposition__perfect_tensor_generated_lift
  f_pq_base_change_polynomial --> polynomials
  f_pq_base_change_polynomial --> concept_tensor_product_of_algebras
  f_valuation_at_centre_order --> concept_schemes_basics
  f_valuation_at_centre_order --> concept_local_rings
  f_valuation_at_centre_order --> concept_valuation_rings
  f_valuation_at_centre_order --> f_global_geometry__is_cpt_gen
  f_valuation_at_centre_order --> f_global_geometry__is_line_gen_on
  f_valuation_at_centre_order --> f_global_geometry__coords_at
  f_order_valuation_compare --> f_valuation_at_centre_order
  f_order_valuation_compare --> concept_schemes_basics
  f_order_valuation_compare --> concept_valuation_rings
  f_character_theory__card_subspaces_of_finrank_mul_card_bases --> linear_algebra
  f_character_theory__card_subspaces_of_finrank_mul_card_bases --> counting
  f_card_subspaces_mul_general_linear_group_card --> f_character_theory__card_subspaces_of_finrank_mul_card_bases
  f_card_subspaces_mul_general_linear_group_card --> linear_algebra
  f_card_subspaces_mul_general_linear_group_card --> counting
  f_card_subspaces_mul_general_linear_group_card --> groups
  f_endomorphism_mass_eq_of_linear_equiv_invariant --> linear_algebra
  f_endomorphism_mass_eq_of_linear_equiv_invariant --> polynomials
  f_endomorphism_mass_eq_of_linear_equiv_invariant --> concept_group_representations
  f_finsum_subspace_stabilizer_mul_block_functions --> linear_algebra
  f_finsum_subspace_stabilizer_mul_block_functions --> counting
  f_finsum_subspace_stabilizer_mul_block_functions --> concept_normal_subgroups_quotients
  f_endomorphism_mass_mul_parabolic_induction_trivial --> f_card_subspaces_mul_general_linear_group_card
  f_endomorphism_mass_mul_parabolic_induction_trivial --> f_endomorphism_mass_eq_of_linear_equiv_invariant
  f_endomorphism_mass_mul_parabolic_induction_trivial --> f_finsum_subspace_stabilizer_mul_block_functions
  f_endomorphism_mass_mul_parabolic_induction_trivial --> f_character_theory__charpoly_block_and_invariant_under_stabilizer_nilradic
  f_endomorphism_mass_mul_parabolic_induction_trivial --> f_commutative_algebra__invariant_subspace_mobius_inverse_rec_eq_of_finrank_lt
  f_endomorphism_mass_mul_parabolic_induction_trivial --> linear_algebra
  f_endomorphism_mass_mul_parabolic_induction_trivial --> polynomials
  f_endomorphism_mass_mul_parabolic_induction_trivial --> counting
  f_real_place_analysis__statement_a --> concept_hermitian_unitary_matrices
  f_real_place_analysis__statement_a --> concept_group_representations
  f_real_place_analysis__statement_a --> linear_algebra
  f_real_place_analysis__statement_a --> concept_tensor_product_of_algebras
  f_real_place_analysis__statement_a --> complex_numbers
  f_real_place_analysis__statement_b --> f_real_place_analysis__statement_a
  f_real_place_analysis__statement_b --> linear_algebra
  f_real_place_analysis__statement_b --> polynomials
  f_real_place_analysis__statement_b --> complex_numbers
  f_real_place_analysis__statement_e --> f_real_place_analysis__statement_a
  f_real_place_analysis__statement_e --> f_real_place_analysis__statement_b
  f_real_place_analysis__statement_e --> concept_exterior_powers
  f_real_place_analysis__statement_e --> linear_algebra
  f_real_place_analysis__statement_e --> rings_fields
  f_is_top --> f_real_place_analysis__statement_e
  f_is_top --> concept_group_representations
  f_is_top --> polynomials
  f_is_top --> calculus
  f_is_top --> linear_algebra
  f_coef_diff --> f_is_top
  f_coef_diff --> polynomials
  f_coef_diff --> complex_analysis
  f_coef_diff --> calculus
  f_curve --> f_coef_diff
  f_curve --> f_is_top
  f_curve --> calculus
  f_curve --> complex_analysis
  f_inv_curve --> calculus
  f_inv_curve --> complex_numbers
  f_inv_curve --> linear_algebra
  f_line_deriv --> f_is_top
  f_line_deriv --> calculus
  f_line_deriv --> complex_analysis
  f_line_deriv --> linear_algebra
  f_bracket --> f_inv_curve
  f_bracket --> f_curve
  f_bracket --> f_line_deriv
  f_bracket --> f_is_top
  f_bracket --> calculus
  f_gl_rel --> f_bracket
  f_gl_rel --> f_real_place_analysis__statement_a
  f_gl_rel --> f_is_top
  f_gl_rel --> linear_algebra
  f_subsingleton_of_adic_completion_tensor --> concept_flat_modules
  f_subsingleton_of_adic_completion_tensor --> concept_tensor_product_of_algebras
  f_subsingleton_of_adic_completion_tensor --> concept_prime_ideals_localization
  f_subsingleton_of_adic_completion_tensor --> p_adic_numbers
  f_torsion_of_localization_flat --> concept_flat_modules
  f_torsion_of_localization_flat --> concept_prime_ideals_localization
  f_torsion_of_localization_flat --> concept_tensor_product_of_algebras
  f_quotient_flat_of_completion_flat --> concept_flat_modules
  f_quotient_flat_of_completion_flat --> concept_tensor_product_of_algebras
  f_quotient_flat_of_completion_flat --> concept_prime_ideals_localization
  f_smul_regular_tensor_of_quotient_flat --> concept_flat_modules
  f_smul_regular_tensor_of_quotient_flat --> concept_chain_complexes_homology
  f_smul_regular_tensor_of_quotient_flat --> concept_tensor_product_of_algebras
  f_localization_projective_kernel_finite --> concept_prime_ideals_localization
  f_localization_projective_kernel_finite --> concept_flat_modules
  f_localization_projective_kernel_finite --> concept_chain_complexes_homology
  f_completion_flat_kernel_finite --> concept_flat_modules
  f_completion_flat_kernel_finite --> concept_chain_complexes_homology
  f_completion_flat_kernel_finite --> concept_tensor_product_of_algebras
  f_finite_of_localization_and_completion --> concept_prime_ideals_localization
  f_finite_of_localization_and_completion --> concept_tensor_product_of_algebras
  f_finite_projective --> f_finite_of_localization_and_completion
  f_finite_projective --> f_subsingleton_of_adic_completion_tensor
  f_finite_projective --> f_quotient_flat_of_completion_flat
  f_finite_projective --> f_torsion_of_localization_flat
  f_finite_projective --> f_smul_regular_tensor_of_quotient_flat
  f_finite_projective --> f_localization_projective_kernel_finite
  f_finite_projective --> f_completion_flat_kernel_finite
  f_finite_projective --> concept_flat_modules
  f_finite_projective --> concept_prime_ideals_localization
  f_commute_image_abelian_by_prime_power_of_normal_central --> f_ab_by_p_of_comm
  f_commute_image_abelian_by_prime_power_of_normal_central --> groups
  f_commute_image_abelian_by_prime_power_of_normal_central --> concept_normal_subgroups_quotients
  f_commute_image_abelian_by_prime_power_of_normal_central --> concept_sylow_theorems
  f_exists_character_eigenvector_of_commuting_representat --> f_character_theory__imports
  f_exists_character_eigenvector_of_commuting_representat --> concept_group_representations
  f_exists_character_eigenvector_of_commuting_representat --> linear_algebra
  f_exists_character_eigenvector_of_commuting_representat --> algebraic_closure
  f_exists_monomial_basis_abelian_by_prime_power --> f_exists_monomial_basis_of_imprimitive
  f_exists_monomial_basis_abelian_by_prime_power --> f_invariant_eq_top_of_irreducible
  f_exists_monomial_basis_abelian_by_prime_power --> f_is_abelian_by_prime_power_group_subgroup
  f_exists_monomial_basis_abelian_by_prime_power --> f_ab_by_p_of_comm
  f_exists_monomial_basis_abelian_by_prime_power --> concept_group_representations
  f_exists_monomial_basis_abelian_by_prime_power --> linear_algebra
  f_exists_monomial_basis_of_imprimitive --> concept_group_representations
  f_exists_monomial_basis_of_imprimitive --> concept_normal_subgroups_quotients
  f_exists_monomial_basis_of_imprimitive --> concept_group_actions
  f_exists_monomial_basis_of_imprimitive --> linear_algebra
  f_character_theory__imports --> linear_algebra
  f_character_theory__imports --> algebraic_closure
  f_invariant_eq_top_of_irreducible --> f_commute_image_abelian_by_prime_power_of_normal_central
  f_invariant_eq_top_of_irreducible --> f_exists_character_eigenvector_of_commuting_representat
  f_invariant_eq_top_of_irreducible --> f_ab_by_p_of_comm
  f_invariant_eq_top_of_irreducible --> concept_group_representations
  f_invariant_eq_top_of_irreducible --> concept_normal_subgroups_quotients
  f_is_abelian_by_prime_power_group_subgroup --> f_ab_by_p_of_comm
  f_is_abelian_by_prime_power_group_subgroup --> groups
  f_is_abelian_by_prime_power_group_subgroup --> concept_normal_subgroups_quotients
  f_complex_analytic_sets__p_manifold_zeros_complement_connected --> f_st_manifold_zeros_complement_connected
  f_complex_analytic_sets__p_manifold_zeros_complement_connected --> f_regular_locus
  f_complex_analytic_sets__p_manifold_zeros_complement_connected --> concept_point_set_topology
  f_complex_analytic_sets__p_manifold_zeros_complement_connected --> concept_complex_analytic_sets
  f_complex_analytic_sets__p_manifold_zeros_complement_connected --> complex_analysis
  f_p_proper_open_projection_local_cover --> f_st_proper_open_projection_local_cover
  f_p_proper_open_projection_local_cover --> f_st_proper_open_projection_local_unbranched
  f_p_proper_open_projection_local_cover --> f_p_unbranched_proper_count_constant
  f_p_proper_open_projection_local_cover --> f_p_unbranched_proper_count_locally_constant
  f_p_proper_open_projection_local_cover --> f_complex_analytic_sets__p_manifold_zeros_complement_connected
  f_p_proper_open_projection_local_cover --> concept_complex_analytic_sets
  f_p_proper_open_projection_local_cover --> concept_point_set_topology
  f_p_unbranched_proper_count_constant --> f_complex_analytic_sets__st_unbranched_proper_count_constant
  f_p_unbranched_proper_count_constant --> f_st_unbranched_proper_count_locally_constant
  f_p_unbranched_proper_count_constant --> f_st_manifold_zeros_complement_connected
  f_p_unbranched_proper_count_constant --> f_regular_locus
  f_p_unbranched_proper_count_constant --> concept_point_set_topology
  f_p_unbranched_proper_count_locally_constant --> f_st_unbranched_proper_count_locally_constant
  f_p_unbranched_proper_count_locally_constant --> concept_point_set_topology
  f_st_proper_open_projection_local_cover --> concept_complex_analytic_sets
  f_st_proper_open_projection_local_cover --> concept_point_set_topology
  f_st_proper_open_projection_local_cover --> complex_analysis
  f_st_proper_open_projection_local_unbranched --> concept_complex_analytic_sets
  f_st_proper_open_projection_local_unbranched --> concept_point_set_topology
  f_st_proper_open_projection_local_unbranched --> complex_analysis
  f_st_unbranched_proper_count_locally_constant --> concept_point_set_topology
  f_st_unbranched_proper_count_locally_constant --> concept_complex_analytic_sets
  f_divisor_proofs__etale_localization_at_prime_tensor_of_low_height --> f_divisor_proofs__torsion_free_over
  f_divisor_proofs__etale_localization_at_prime_tensor_of_low_height --> concept_etale_ring_maps
  f_divisor_proofs__etale_localization_at_prime_tensor_of_low_height --> concept_prime_ideals_localization
  f_divisor_proofs__etale_localization_at_prime_tensor_of_low_height --> concept_tensor_product_of_algebras
  f_exists_smul_dvd_of_localization_at_prime_tensor --> concept_prime_ideals_localization
  f_exists_smul_dvd_of_localization_at_prime_tensor --> concept_tensor_product_of_algebras
  f_exists_smul_dvd_of_localization_at_prime_tensor --> concept_flat_modules
  f_finite_etale_of_galois_descent_hartogs --> f_finite_of_galois_trace_relation
  f_finite_etale_of_galois_descent_hartogs --> f_hart_tensor_of_flat
  f_finite_etale_of_galois_descent_hartogs --> f_divisor_proofs__etale_localization_at_prime_tensor_of_low_height
  f_finite_etale_of_galois_descent_hartogs --> f_galois_comparison_map_injective_of_flat
  f_finite_etale_of_galois_descent_hartogs --> f_galois_element_dvd_of_formally_unramified
  f_finite_etale_of_galois_descent_hartogs --> f_exists_smul_dvd_of_localization_at_prime_tensor
  f_finite_etale_of_galois_descent_hartogs --> f_gal_map_gal_elt
  f_finite_etale_of_galois_descent_hartogs --> f_divisor_proofs__torsion_free_over
  f_finite_etale_of_galois_descent_hartogs --> concept_etale_ring_maps
  f_finite_etale_of_galois_descent_hartogs --> concept_galois_fixed_fields
  f_finite_etale_of_galois_descent_hartogs --> concept_flat_modules
  f_finite_etale_of_galois_descent_hartogs --> concept_prime_ideals_localization
  f_finite_of_galois_trace_relation --> f_divisor_proofs__torsion_free_over
  f_finite_of_galois_trace_relation --> concept_galois_fixed_fields
  f_finite_of_galois_trace_relation --> rings_fields
  f_finite_of_galois_trace_relation --> linear_algebra
  f_gal_map_gal_elt --> concept_tensor_product_of_algebras
  f_gal_map_gal_elt --> concept_galois_fixed_fields
  f_gal_map_gal_elt --> groups
  f_galois_comparison_map_injective_of_flat --> f_gal_map_gal_elt
  f_galois_comparison_map_injective_of_flat --> f_divisor_proofs__torsion_free_over
  f_galois_comparison_map_injective_of_flat --> concept_flat_modules
  f_galois_comparison_map_injective_of_flat --> concept_tensor_product_of_algebras
  f_galois_comparison_map_injective_of_flat --> concept_galois_fixed_fields
  f_galois_element_dvd_of_formally_unramified --> f_gal_map_gal_elt
  f_galois_element_dvd_of_formally_unramified --> concept_etale_ring_maps
  f_galois_element_dvd_of_formally_unramified --> concept_tensor_product_of_algebras
  f_galois_element_dvd_of_formally_unramified --> concept_derivations_smoothness
  f_hart_tensor_of_flat --> f_divisor_proofs__torsion_free_over
  f_hart_tensor_of_flat --> concept_flat_modules
  f_hart_tensor_of_flat --> concept_tensor_product_of_algebras
  f_hart_tensor_of_flat --> concept_noetherian_and_irreducible_components
  f_hart_tensor_of_flat --> concept_chain_complexes_homology
  f_divisor_proofs__torsion_free_over --> concept_etale_ring_maps
  f_divisor_proofs__torsion_free_over --> concept_prime_ideals_localization
  f_divisor_proofs__torsion_free_over --> concept_coordinate_rings_dimension
  f_divisor_proofs__torsion_free_over --> concept_integral_closure_fraction_fields
  f_algebra_trace_map_of_cokernel_killed_by_scalar --> linear_algebra
  f_algebra_trace_map_of_cokernel_killed_by_scalar --> rings_fields
  f_algebra_trace_map_of_cokernel_killed_by_scalar --> concept_tensor_product_of_algebras
  f_discr_is_unit --> f_etale_of_etale_at_height_one_primes
  f_discr_is_unit --> concept_local_rings
  f_discr_is_unit --> concept_etale_ring_maps
  f_discr_is_unit --> concept_ideals_and_discriminant
  f_etale_of_etale_at_height_one_primes --> concept_etale_ring_maps
  f_etale_of_etale_at_height_one_primes --> concept_ideals_and_discriminant
  f_etale_of_etale_at_height_one_primes --> concept_integral_closure_fraction_fields
  f_etale_of_etale_at_height_one_primes --> concept_coordinate_rings_dimension
  f_etale_of_etale_at_height_one_primes --> concept_prime_ideals_localization
  f_etale_of_etale_at_height_one_primes --> concept_separable_polynomials
  f_exists_smul_mem_range_of_surjective_localized_map --> concept_prime_ideals_localization
  f_exists_smul_mem_range_of_surjective_localized_map --> concept_tensor_product_of_algebras
  f_exists_smul_mem_range_of_surjective_localized_map --> concept_flat_modules
  f_finite_length_coker_of_etale_punctured_spectrum --> f_smul_mem_of_maximal_ideal_pow_of_locally_surjective
  f_finite_length_coker_of_etale_punctured_spectrum --> f_localization_tensor_map_injective_coker_killed
  f_finite_length_coker_of_etale_punctured_spectrum --> f_algebra_trace_map_of_cokernel_killed_by_scalar
  f_finite_length_coker_of_etale_punctured_spectrum --> f_surjective_of_trace_of_smul_mem_range
  f_finite_length_coker_of_etale_punctured_spectrum --> f_exists_smul_mem_range_of_surjective_localized_map
  f_finite_length_coker_of_etale_punctured_spectrum --> concept_etale_ring_maps
  f_finite_length_coker_of_etale_punctured_spectrum --> concept_local_rings
  f_finite_length_coker_of_etale_punctured_spectrum --> concept_prime_ideals_localization
  f_localization_tensor_map_injective_coker_killed --> concept_flat_modules
  f_localization_tensor_map_injective_coker_killed --> concept_tensor_product_of_algebras
  f_localization_tensor_map_injective_coker_killed --> concept_prime_ideals_localization
  f_smul_mem_of_maximal_ideal_pow_of_locally_surjective --> concept_local_rings
  f_smul_mem_of_maximal_ideal_pow_of_locally_surjective --> concept_prime_ideals_localization
  f_smul_mem_of_maximal_ideal_pow_of_locally_surjective --> concept_noetherian_and_irreducible_components
  f_surjective_of_trace_of_smul_mem_range --> f_discr_is_unit
  f_surjective_of_trace_of_smul_mem_range --> concept_ideals_and_discriminant
  f_surjective_of_trace_of_smul_mem_range --> concept_etale_ring_maps
  f_surjective_of_trace_of_smul_mem_range --> concept_local_rings
  f_surjective_of_trace_of_smul_mem_range --> linear_algebra
  f_commutative_algebra__chain_conn_in_dim --> concept_coordinate_rings_dimension
  f_commutative_algebra__chain_conn_in_dim --> concept_point_set_topology
  f_commutative_algebra__chain_conn_in_dim --> concept_noetherian_and_irreducible_components
  f_commutative_algebra__chain_conn_in_dim --> concept_local_rings
  f_commutative_algebra__chain_conn_in_dim --> concept_prime_ideals_localization
  f_cohen_macaulay__mod_depth_g_e --> concept_local_rings
  f_cohen_macaulay__mod_depth_g_e --> concept_coordinate_rings_dimension
  f_cohen_macaulay__mod_depth_g_e --> concept_noetherian_and_irreducible_components
  f_exists_sq_zero_extend_localization_away_pow --> concept_finitely_generated_algebras
  f_exists_sq_zero_extend_localization_away_pow --> concept_prime_ideals_localization
  f_exists_sq_zero_extend_localization_away_pow --> concept_tensor_product_of_algebras
  f_exists_sq_zero_extend_localization_away_pow --> rings_fields
  f_exists_sq_zero_extend_localization_away_pow --> polynomials
  f_exists_square_zero_lift_basic_open_pair_agree --> f_exists_sq_zero_extend_localization_away_pow
  f_exists_square_zero_lift_basic_open_pair_agree --> f_divisor_proofs__is_affine_combination_in_chart_spec_map_comp
  f_exists_square_zero_lift_basic_open_pair_agree --> f_divisor_proofs__is_comb_in
  f_exists_square_zero_lift_basic_open_pair_agree --> f_divisor_proofs__preimage_eq_of_square_zero_thickening
  f_exists_square_zero_lift_basic_open_pair_agree --> concept_schemes_basics
  f_exists_square_zero_lift_basic_open_pair_agree --> concept_smooth_morphisms
  f_exists_square_zero_lift_basic_open_pair_agree --> concept_categorical_pullbacks
  f_exists_square_zero_lift_basic_open_pair_agree --> concept_prime_ideals_localization
  f_divisor_proofs__is_affine_combination_in_chart_spec_map_comp --> f_divisor_proofs__is_comb_in
  f_divisor_proofs__is_affine_combination_in_chart_spec_map_comp --> concept_schemes_basics
  f_divisor_proofs__is_affine_combination_in_chart_spec_map_comp --> concept_categorical_pullbacks
  f_divisor_proofs__is_comb_in --> concept_schemes_basics
  f_divisor_proofs__is_comb_in --> concept_categorical_pullbacks
  f_divisor_proofs__lift_at --> concept_schemes_basics
  f_divisor_proofs__lift_at --> concept_categorical_pullbacks
  f_divisor_proofs__lift_at --> concept_prime_ideals_localization
  f_divisor_proofs__preimage_eq_of_square_zero_thickening --> concept_schemes_basics
  f_divisor_proofs__preimage_eq_of_square_zero_thickening --> concept_prime_ideals_localization
  f_divisor_proofs__preimage_eq_of_square_zero_thickening --> concept_categorical_pullbacks
  f_adelic_hermitian_forms__mem_pow_sub --> groups
  f_adelic_hermitian_forms__mem_pow_sub --> rings_fields
  f_adelic_hermitian_forms__mem_pow_sub --> number_fields
  f_adelic_hermitian_forms__mem_pow_sub --> concept_roots_of_unity_kummer
  f_adelic_hermitian_forms__mem_pow_sub --> concept_dedekind_domains
  f_adelic_hermitian_forms__mem_pow_sub --> p_adic_numbers
  f_adelic_hermitian_forms__mem_pow_sub --> concept_normal_subgroups_quotients
  f_adelic_hermitian_forms__sq_sub_le_norm_sub --> groups
  f_adelic_hermitian_forms__sq_sub_le_norm_sub --> rings_fields
  f_adelic_hermitian_forms__sq_sub_le_norm_sub --> number_fields
  f_adelic_hermitian_forms__sq_sub_le_norm_sub --> concept_ultrametric_norm
  f_adelic_hermitian_forms__sq_sub_le_norm_sub --> concept_dedekind_domains
  f_adelic_hermitian_forms__sq_sub_le_norm_sub --> concept_valuation_rings
  f_adelic_lattice_proofs__pow_index_torsion_ker_range_mul --> f_adelic_hermitian_forms__mem_pow_sub
  f_adelic_lattice_proofs__pow_index_torsion_ker_range_mul --> groups
  f_adelic_lattice_proofs__pow_index_torsion_ker_range_mul --> concept_normal_subgroups_quotients
  f_adelic_lattice_proofs__pow_index_torsion_ker_range_mul --> concept_chain_complexes_homology
  f_adelic_lattice_proofs__pow_index_torsion_ker_range_mul --> counting
  f_rel_index_one_units_mul_eq_card_quotient --> f_adelic_hermitian_forms__mem_pow_sub
  f_rel_index_one_units_mul_eq_card_quotient --> rings_fields
  f_rel_index_one_units_mul_eq_card_quotient --> concept_local_rings
  f_rel_index_one_units_mul_eq_card_quotient --> concept_prime_ideals_localization
  f_rel_index_one_units_mul_eq_card_quotient --> concept_normal_subgroups_quotients
  f_rel_index_one_units_mul_eq_card_quotient --> groups
  f_subgroup_pow_image_units_congruent_one_mod_of_is_adic_comp --> f_adelic_hermitian_forms__mem_pow_sub
  f_subgroup_pow_image_units_congruent_one_mod_of_is_adic_comp --> concept_hensel_lifting
  f_subgroup_pow_image_units_congruent_one_mod_of_is_adic_comp --> concept_discrete_valuation_ring
  f_subgroup_pow_image_units_congruent_one_mod_of_is_adic_comp --> concept_local_rings
  f_subgroup_pow_image_units_congruent_one_mod_of_is_adic_comp --> p_adic_numbers
  f_subgroup_pow_image_units_congruent_one_mod_of_is_adic_comp --> polynomials
  f_subgroup_pow_image_units_congruent_one_mod_of_is_adic_comp --> rings_fields
  f_subgroup_pow_rel_index_units_of_is_adic_complete --> f_adelic_lattice_proofs__pow_index_torsion_ker_range_mul
  f_subgroup_pow_rel_index_units_of_is_adic_complete --> f_rel_index_one_units_mul_eq_card_quotient
  f_subgroup_pow_rel_index_units_of_is_adic_complete --> f_subgroup_pow_image_units_congruent_one_mod_of_is_adic_comp
  f_subgroup_pow_rel_index_units_of_is_adic_complete --> f_adelic_hermitian_forms__mem_pow_sub
  f_subgroup_pow_rel_index_units_of_is_adic_complete --> concept_normal_subgroups_quotients
  f_subgroup_pow_rel_index_units_of_is_adic_complete --> counting
  f_global_twisting__mem_split_seq_iff --> f_global_twisting__sub_closed
  f_global_twisting__mem_split_seq_iff --> f_global_twisting__perm_rep_single
  f_global_twisting__mem_split_seq_iff --> concept_group_actions
  f_global_twisting__mem_split_seq_iff --> concept_group_representations
  f_global_twisting__mem_split_seq_iff --> concept_chain_complexes_homology
  f_global_twisting__mem_split_seq_iff --> linear_algebra
  f_global_twisting__sub_closed --> concept_chain_complexes_homology
  f_global_twisting__sub_closed --> linear_algebra
  f_global_twisting__sub_closed --> counting
  f_link_exactness_stability__seq_chain_boundary_comp_boundary_apply --> f_global_twisting__sub_closed
  f_link_exactness_stability__seq_chain_boundary_comp_boundary_apply --> concept_chain_complexes_homology
  f_link_exactness_stability__seq_chain_boundary_comp_boundary_apply --> counting
  f_split_set_perm_rep_chains_iso_split_seq_chains --> f_global_twisting__mem_split_seq_iff
  f_split_set_perm_rep_chains_iso_split_seq_chains --> f_global_twisting__sub_closed
  f_split_set_perm_rep_chains_iso_split_seq_chains --> concept_chain_complexes_homology
  f_split_set_perm_rep_chains_iso_split_seq_chains --> concept_group_representations
  f_split_sequence_rep_complex_exact --> f_split_set_perm_rep_chains_iso_split_seq_chains
  f_split_sequence_rep_complex_exact --> f_link_exactness_stability__seq_chain_boundary_comp_boundary_apply
  f_split_sequence_rep_complex_exact --> f_global_twisting__mem_split_seq_iff
  f_split_sequence_rep_complex_exact --> f_global_twisting__sub_closed
  f_split_sequence_rep_complex_exact --> concept_chain_complexes_homology
  f_published_theorems__k_acyclic_homology --> f_tensor_hom_cubes__is_acyclic_space
  f_published_theorems__k_acyclic_homology --> f_tensor_hom_cubes__simplex_face
  f_published_theorems__k_acyclic_homology --> f_tensor_hom_cubes__stab_directed_system
  f_published_theorems__k_acyclic_homology --> concept_gl_infinity_homology_stability
  f_published_theorems__k_acyclic_homology --> concept_chain_complexes_homology
  f_tensor_hom_cubes__is_acyclic_space --> concept_gl_infinity_homology_stability
  f_tensor_hom_cubes__is_acyclic_space --> f_tensor_hom_cubes__stab_directed_system
  f_tensor_hom_cubes__is_acyclic_space --> concept_point_set_topology
  f_tensor_hom_cubes__is_acyclic_space --> concept_chain_complexes_homology
  f_tensor_hom_cubes__is_acyclic_space --> groups
  f_tensor_hom_cubes__simplex_face --> f_tensor_hom_cubes__is_acyclic_space
  f_tensor_hom_cubes__simplex_face --> concept_point_set_topology
  f_tensor_hom_cubes__simplex_face --> concept_chain_complexes_homology
  f_tensor_hom_cubes__simplex_face --> counting
  f_tensor_hom_cubes__simplex_face --> primes_divisibility
  f_tensor_hom_cubes__stab_directed_system --> concept_gl_infinity_homology_stability
  f_tensor_hom_cubes__stab_directed_system --> linear_algebra
  f_tensor_hom_cubes__stab_directed_system --> groups
  f_tensor_hom_cubes__stab_directed_system --> rings_fields
  f_tensor_hom_cubes__stab_directed_system --> concept_chain_complexes_homology
  f_period_integrals__minkowski --> groups
  f_period_integrals__minkowski --> linear_algebra
  f_period_integrals__minkowski --> primes_divisibility
  f_period_integrals__minkowski --> counting
  f_period_integrals__minkowski_q --> f_period_integrals__minkowski
  f_period_integrals__minkowski_q --> groups
  f_period_integrals__minkowski_q --> linear_algebra
  f_orbital_bounds_conclusion__minkowski --> f_period_integrals__minkowski
  f_orbital_bounds_conclusion__minkowski --> f_minkowski_bound_of_steps
  f_orbital_bounds_conclusion__minkowski --> f_charpoly_dvd_of_pow_eq_one
  f_orbital_bounds_conclusion__minkowski --> f_power_sum
  f_orbital_bounds_conclusion__minkowski_q --> f_period_integrals__minkowski_q
  f_orbital_bounds_conclusion__minkowski_q --> f_minkowski_torsion_free__lattice
  f_minkowski_bound__assemble --> f_power_sum_step
  f_minkowski_bound__assemble --> f_period_integrals__minkowski
  f_minkowski_bound__assemble --> concept_sylow_theorems
  f_minkowski_bound__assemble --> primes_divisibility
  f_minkowski_bound__assemble --> groups
  f_charpoly_dvd_of_pow_eq_one --> f_power_sum_step
  f_charpoly_dvd_of_pow_eq_one --> polynomials
  f_charpoly_dvd_of_pow_eq_one --> linear_algebra
  f_charpoly_dvd_of_pow_eq_one --> concept_roots_of_unity_kummer
  f_charpoly_dvd_of_pow_eq_one --> concept_field_extensions_transcendence
  f_charpoly_dvd_of_pow_eq_one --> primes_divisibility
  f_minkowski_bound_of_steps --> f_minkowski_bound__assemble
  f_minkowski_bound_of_steps --> f_power_sum_step
  f_minkowski_bound_of_steps --> polynomials
  f_minkowski_bound_of_steps --> counting
  f_minkowski_bound_of_steps --> groups
  f_power_sum --> f_power_sum_step
  f_power_sum --> linear_algebra
  f_power_sum --> concept_group_representations
  f_power_sum --> groups
  f_power_sum --> counting
  f_power_sum_step --> linear_algebra
  f_power_sum_step --> groups
  f_power_sum_step --> primes_divisibility
  f_power_sum_step --> counting
  f_minkowski_torsion_free__lattice --> f_orbital_bounds_conclusion__minkowski
  f_minkowski_torsion_free__lattice --> f_period_integrals__minkowski_q
  f_minkowski_torsion_free__lattice --> linear_algebra
  f_minkowski_torsion_free__lattice --> concept_finitely_generated_abelian_groups
  f_minkowski_torsion_free__lattice --> concept_lattices_in_the_plane
  f_minkowski_torsion_free__lattice --> groups
  f_unit_t_zpow --> f_block_decomposition__perfect_tensor_generated_lift
  f_unit_t_zpow --> f_block_decomposition__pf_facts
  f_unit_t_zpow --> concept_tensor_product_of_algebras
  f_unit_t_zpow --> polynomials
  f_unit_t_zpow --> rings_fields
  f_haar_transversals__fold_bound --> concept_haar_measure_fundamental_domain
  f_haar_transversals__fold_bound --> concept_normal_subgroups_quotients
  f_haar_transversals__fold_bound --> infinite_series
  f_haar_transversals__fold_bound --> real_analysis
  f_haar_transversals__poincare_series_square_integrable --> f_haar_transversals__fold_bound
  f_haar_transversals__poincare_series_square_integrable --> concept_haar_measure_fundamental_domain
  f_haar_transversals__poincare_series_square_integrable --> concept_normal_subgroups_quotients
  f_haar_transversals__poincare_series_square_integrable --> complex_numbers
  f_period_integrals__fold_mult --> f_haar_transversals__fold_bound
  f_period_integrals__fold_mult --> concept_haar_measure_fundamental_domain
  f_period_integrals__fold_mult --> concept_point_set_topology
  f_period_integrals__fold_unfold --> f_haar_transversals__fold_bound
  f_period_integrals__fold_unfold --> concept_haar_measure_fundamental_domain
  f_orbital_bounds_conclusion__fold_mult --> f_period_integrals__fold_mult
  f_orbital_bounds_conclusion__fold_mult --> f_measurable_mult
  f_orbital_bounds_conclusion__fold_unfold --> f_period_integrals__fold_unfold
  f_orbital_bounds_conclusion__fold_unfold --> f_unfolding_identity__fold_unfold_main
  f_poincare_series_mem_lp --> f_fold_l2_double_coset
  f_poincare_series_mem_lp --> f_haar_transversals__poincare_series_square_integrable
  f_measurable_mult --> f_haar_transversals__fold_bound
  f_measurable_mult --> concept_point_set_topology
  f_measurable_mult --> concept_haar_measure_fundamental_domain
  f_measurable_mult --> counting
  f_fold_l2_double_coset --> f_haar_transversals__fold_bound
  f_fold_l2_double_coset --> f_haar_transversals__poincare_series_square_integrable
  f_fold_l2_double_coset --> f_orbital_bounds_conclusion__fold_mult
  f_fold_l2_double_coset --> f_orbital_bounds_conclusion__fold_unfold
  f_fold_l2_double_coset --> concept_haar_measure_fundamental_domain
  f_fold_l2_double_coset --> infinite_series
  f_fold_l2_double_coset --> complex_numbers
  f_unfolding_identity__fold_unfold_main --> f_period_integrals__fold_unfold
  f_unfolding_identity__fold_unfold_main --> f_haar_transversals__fold_bound
  f_unfolding_identity__fold_unfold_main --> concept_haar_measure_fundamental_domain
  f_unfolding_identity__fold_unfold_main --> concept_normal_subgroups_quotients
  f_unfolding_identity__fold_unfold_main --> infinite_series
  f_character_theory__eq_zero_of_not_primary --> f_character_theory__exists_conj_eq_add_of_is_coprime
  f_character_theory__eq_zero_of_not_primary --> concept_group_representations
  f_character_theory__eq_zero_of_not_primary --> linear_algebra
  f_character_theory__eq_zero_of_not_primary --> polynomials
  f_character_theory__exists_conj_eq_add_of_is_coprime --> linear_algebra
  f_character_theory__exists_conj_eq_add_of_is_coprime --> polynomials
  f_finite_monic_nat_degree --> polynomials
  f_finite_monic_nat_degree --> algebraic_closure
  f_finite_monic_nat_degree --> rings_fields
  f_finite_monic_nat_degree --> counting
  f_finite_monic_nat_degree --> complex_numbers
  f_is_unit_iff_charpoly_coeff_zero_ne --> linear_algebra
  f_is_unit_iff_charpoly_coeff_zero_ne --> polynomials
  f_is_unit_iff_charpoly_coeff_zero_ne --> concept_group_representations
  f_is_unit_iff_charpoly_coeff_zero_ne --> counting
  f_invertible_end_inner_product_root_power_sum_eq_torus_sum --> f_finite_monic_nat_degree
  f_invertible_end_inner_product_root_power_sum_eq_torus_sum --> f_is_unit_iff_charpoly_coeff_zero_ne
  f_invertible_end_inner_product_root_power_sum_eq_torus_sum --> f_character_theory__eq_zero_of_not_primary
  f_invertible_end_inner_product_root_power_sum_eq_torus_sum --> polynomials
  f_invertible_end_inner_product_root_power_sum_eq_torus_sum --> complex_numbers
  f_inner_product_root_power_sum_eq_of_frobenius_mod_eq --> f_invertible_end_inner_product_root_power_sum_eq_torus_sum
  f_inner_product_root_power_sum_eq_of_frobenius_mod_eq --> algebraic_closure
  f_inner_product_root_power_sum_eq_of_frobenius_mod_eq --> modular_arithmetic
  f_inner_product_root_power_sum_eq_of_frobenius_mod_eq --> concept_galois_fixed_fields
  f_exists_integral_hecke_eigensystem_deligne_serre --> f_exists_matrices_intertwining_of_semilinear
  f_exists_integral_hecke_eigensystem_deligne_serre --> f_finite_joint_eigensystems
  f_exists_integral_hecke_eigensystem_deligne_serre --> f_matrix_exists_common_eigenvector_mem
  f_exists_integral_hecke_eigensystem_deligne_serre --> f_norm_eigenvalue_le_one_of_entries
  f_exists_integral_hecke_eigensystem_deligne_serre --> concept_discrete_valuation_ring
  f_exists_integral_hecke_eigensystem_deligne_serre --> concept_ultrametric_norm
  f_exists_integral_hecke_eigensystem_deligne_serre --> concept_hecke_operators
  f_exists_integral_hecke_eigensystem_deligne_serre --> p_adic_numbers
  f_exists_integral_hecke_eigensystem_deligne_serre --> concept_prime_ideals_localization
  f_exists_integral_hecke_eigensystem_deligne_serre --> linear_algebra
  f_exists_matrices_intertwining_of_semilinear --> concept_discrete_valuation_ring
  f_exists_matrices_intertwining_of_semilinear --> concept_valuation_rings
  f_exists_matrices_intertwining_of_semilinear --> linear_algebra
  f_finite_joint_eigensystems --> linear_algebra
  f_matrix_exists_common_eigenvector_mem --> f_dvd_trace_of_balanced_tensor
  f_matrix_exists_common_eigenvector_mem --> linear_algebra
  f_matrix_exists_common_eigenvector_mem --> algebraic_closure
  f_norm_eigenvalue_le_one_of_entries --> concept_ultrametric_norm
  f_norm_eigenvalue_le_one_of_entries --> p_adic_numbers
  f_norm_eigenvalue_le_one_of_entries --> linear_algebra
  f_dvd_trace_of_balanced_tensor --> concept_tensor_product_of_algebras
  f_dvd_trace_of_balanced_tensor --> concept_local_rings
  f_dvd_trace_of_balanced_tensor --> algebraic_closure
  f_dvd_trace_of_balanced_tensor --> linear_algebra
  f_finite_open_le_closed_fibre --> f_hodge_tate_points__val_at_restrict
  f_finite_open_le_closed_fibre --> concept_schemes_basics
  f_finite_open_le_closed_fibre --> concept_local_rings
  f_finite_open_le_closed_fibre --> concept_point_set_topology
  f_is_fin_open_sub_of_finite --> f_finite_open_le_closed_fibre
  f_is_fin_open_sub_of_finite --> f_p_adic_hodge__finite_flat
  f_is_fin_open_sub_of_finite --> concept_schemes_basics
  f_is_fin_open_sub_of_finite --> concept_categorical_pullbacks
  f_is_fin_open_sub_of_finite --> concept_local_rings
  f_is_fin_open_sub_of_finite --> groups
  f_hodge_tate_points__val_at_restrict --> concept_schemes_basics
  f_hodge_tate_points__val_at_restrict --> concept_local_rings
  f_hodge_tate_points__val_at_restrict --> concept_point_set_topology
  f_hodge_tate_points__val_at_restrict --> f_p_adic_hodge__finite_flat
  f_geometry_proofs__coord_tie_comp_equiv --> f_global_geometry__coords_at
  f_geometry_proofs__coord_tie_comp_equiv --> concept_schemes_basics
  f_geometry_proofs__coord_tie_comp_equiv --> linear_algebra
  f_geometry_proofs__germ_gen_pt_injective_range_reg_at --> f_global_geometry__is_cpt_gen
  f_geometry_proofs__germ_gen_pt_injective_range_reg_at --> concept_schemes_basics
  f_geometry_proofs__germ_gen_pt_injective_range_reg_at --> concept_local_rings
  f_geometry_proofs__germ_gen_pt_injective_range_reg_at --> concept_point_set_topology
  f_piece_localization_at_element --> f_geometry_proofs__germ_gen_pt_injective_range_reg_at
  f_piece_localization_at_element --> f_reg_at_is_local_ring_is_fraction_ring_stalk
  f_piece_localization_at_element --> f_geometry_proofs__prod_update_div
  f_piece_localization_at_element --> f_global_geometry__is_cpt_gen
  f_piece_localization_at_element --> concept_schemes_basics
  f_piece_localization_at_element --> concept_prime_ideals_localization
  f_geometry_proofs__prod_update_div --> rings_fields
  f_geometry_proofs__prod_update_div --> linear_algebra
  f_geometry_proofs__prod_update_div --> concept_schemes_basics
  f_geometry_proofs__prod_update_div --> f_global_geometry__coords_at
  f_reg_at_is_local_ring_is_fraction_ring_stalk --> f_global_geometry__is_cpt_gen
  f_reg_at_is_local_ring_is_fraction_ring_stalk --> concept_local_rings
  f_reg_at_is_local_ring_is_fraction_ring_stalk --> concept_integral_closure_fraction_fields
  f_reg_at_is_local_ring_is_fraction_ring_stalk --> concept_schemes_basics
  f_reg_at_is_local_ring_is_fraction_ring_stalk --> concept_prime_ideals_localization
  f_exists_kill --> f_block_decomposition__exists_p_q
  f_exists_kill --> f_block_decomposition__pq_lift
  f_exists_kill --> rings_fields
  f_exists_kill --> polynomials
  f_exists_kill --> concept_finitely_generated_algebras
  f_exists_kill --> concept_prime_ideals_localization
  f_c_m_moduli__projective_space_over_spec --> concept_schemes_basics
  f_c_m_moduli__projective_space_over_spec --> concept_etale_ring_maps
  f_c_m_moduli__projective_space_over_spec --> concept_hensel_lifting
  f_c_m_moduli__projective_space_over_spec --> concept_local_rings
  f_c_m_moduli__projective_space_over_spec --> concept_integral_closure_fraction_fields
  f_c_m_moduli__projective_space_over_spec --> algebraic_closure
  f_c_m_moduli__projective_space_over_spec --> complex_numbers
  f_c_m_moduli__projective_space_over_spec --> polynomials
  f_divisor_proofs__closure_finite_etale --> concept_integral_closure_fraction_fields
  f_divisor_proofs__closure_finite_etale --> concept_etale_ring_maps
  f_divisor_proofs__closure_finite_etale --> concept_tensor_product_of_algebras
  f_divisor_proofs__closure_finite_etale --> concept_prime_ideals_localization
  f_divisor_proofs__closure_finite_etale --> f_divisor_proofs__torsors_trivial
  f_etale_away_of_is_etale_at_off_submonoid --> concept_etale_ring_maps
  f_etale_away_of_is_etale_at_off_submonoid --> concept_prime_ideals_localization
  f_etale_away_of_is_etale_at_off_submonoid --> concept_schemes_basics
  f_divisor_proofs__etale_localization_at_prime_is_domain_is_integrally_clos --> f_homogeneous_ideals__is_domain_and_is_integrally_closed_at_prime_of_smooth_of_co
  f_divisor_proofs__etale_localization_at_prime_is_domain_is_integrally_clos --> concept_etale_ring_maps
  f_divisor_proofs__etale_localization_at_prime_is_domain_is_integrally_clos --> concept_integral_closure_fraction_fields
  f_divisor_proofs__etale_localization_at_prime_is_domain_is_integrally_clos --> concept_prime_ideals_localization
  f_divisor_proofs__good_iff_etale_at --> f_divisor_proofs__closure_finite_etale
  f_divisor_proofs__good_iff_etale_at --> f_divisor_proofs__point_at_zero
  f_divisor_proofs__good_iff_etale_at --> concept_etale_ring_maps
  f_divisor_proofs__origin_ideal --> concept_group_actions
  f_divisor_proofs__origin_ideal --> concept_flat_modules
  f_divisor_proofs__origin_ideal --> concept_tensor_product_of_algebras
  f_divisor_proofs__origin_ideal --> concept_local_rings
  f_divisor_proofs__origin_ideal --> concept_prime_ideals_localization
  f_divisor_proofs__origin_ideal --> modular_arithmetic
  f_divisor_proofs__origin_ideal --> polynomials
  f_divisor_proofs__point_at_zero --> f_divisor_proofs__origin_ideal
  f_divisor_proofs__point_at_zero --> f_divisor_proofs__closure_finite_etale
  f_divisor_proofs__point_at_zero --> f_divisor_proofs__torsors_trivial
  f_divisor_proofs__point_at_zero --> concept_prime_ideals_localization
  f_divisor_proofs__point_at_zero --> concept_local_rings
  f_divisor_proofs__point_at_zero --> polynomials
  f_divisor_proofs__torsors_trivial --> f_c_m_moduli__projective_space_over_spec
  f_divisor_proofs__torsors_trivial --> concept_group_actions
  f_divisor_proofs__torsors_trivial --> concept_flat_modules
  f_divisor_proofs__torsors_trivial --> concept_local_rings
  f_divisor_proofs__torsors_trivial --> concept_hensel_lifting
  f_divisor_proofs__torsors_trivial --> concept_prime_ideals_localization
  f_divisor_proofs__torsors_trivial --> algebraic_closure
  f_divisor_proofs__torsors_trivial --> polynomials
  f_divisor_proofs__zmod_torsor_exists_point_finite_separable --> f_divisor_proofs__origin_ideal
  f_divisor_proofs__zmod_torsor_exists_point_finite_separable --> concept_separable_polynomials
  f_divisor_proofs__zmod_torsor_exists_point_finite_separable --> concept_flat_modules
  f_divisor_proofs__zmod_torsor_exists_point_finite_separable --> concept_tensor_product_of_algebras
  f_divisor_proofs__zmod_torsor_exists_point_finite_separable --> concept_field_extensions_transcendence
  f_divisor_proofs__zmod_torsor_exists_point_finite_separable --> concept_prime_ideals_localization
  f_homogeneous_ideals__is_domain_and_is_integrally_closed_at_prime_of_smooth_of_co --> concept_smooth_morphisms
  f_homogeneous_ideals__is_domain_and_is_integrally_closed_at_prime_of_smooth_of_co --> concept_etale_ring_maps
  f_homogeneous_ideals__is_domain_and_is_integrally_closed_at_prime_of_smooth_of_co --> concept_integral_closure_fraction_fields
  f_homogeneous_ideals__is_domain_and_is_integrally_closed_at_prime_of_smooth_of_co --> concept_prime_ideals_localization
  f_homogeneous_ideals__is_domain_and_is_integrally_closed_at_prime_of_smooth_of_co --> concept_tensor_product_of_algebras
  f_homogeneous_ideals__is_domain_and_is_integrally_closed_at_prime_of_smooth_of_co --> concept_local_rings
  f_homogeneous_ideals__is_domain_and_is_integrally_closed_at_prime_of_smooth_of_co --> concept_schemes_basics
  f_homogeneous_ideals__is_domain_and_is_integrally_closed_at_prime_of_smooth_of_co --> polynomials
  f_eval_complex_poly_eq_zero_on_rat_zariski_closure --> concept_galois_fixed_fields
  f_eval_complex_poly_eq_zero_on_rat_zariski_closure --> concept_field_extensions_transcendence
  f_eval_complex_poly_eq_zero_on_rat_zariski_closure --> linear_algebra
  f_eval_complex_poly_eq_zero_on_rat_zariski_closure --> polynomials
  f_eval_complex_poly_eq_zero_on_rat_zariski_closure --> complex_numbers
  f_eval_complex_poly_eq_zero_on_rat_zariski_closure --> f_adelic_lattice_proofs__galois_stable_submodule_le_span_rational
  f_adelic_lattice_proofs__mem_span_rat_polys_vanishing_of_aut_stable --> f_adelic_lattice_proofs__galois_stable_submodule_le_span_rational
  f_adelic_lattice_proofs__mem_span_rat_polys_vanishing_of_aut_stable --> concept_galois_fixed_fields
  f_adelic_lattice_proofs__mem_span_rat_polys_vanishing_of_aut_stable --> concept_field_extensions_transcendence
  f_adelic_lattice_proofs__mem_span_rat_polys_vanishing_of_aut_stable --> linear_algebra
  f_adelic_lattice_proofs__mem_span_rat_polys_vanishing_of_aut_stable --> polynomials
  f_adelic_lattice_proofs__mem_span_rat_polys_vanishing_of_aut_stable --> complex_numbers
  f_coords_left_mul_matrix_const_base_change --> number_fields
  f_coords_left_mul_matrix_const_base_change --> linear_algebra
  f_coords_left_mul_matrix_const_base_change --> rings_fields
  f_exists_is_q_group_weil_restriction --> f_exists_rational_equations_weil_restriction
  f_exists_is_q_group_weil_restriction --> f_gl_free_algebra_to_special_linear_emb_injective_hom
  f_exists_is_q_group_weil_restriction --> f_mem_rat_zariski_closure_points_iff_of_is_reduced
  f_exists_is_q_group_weil_restriction --> f_adelic_hermitian_forms__adelic_pair
  f_exists_is_q_group_weil_restriction --> number_fields
  f_exists_is_q_group_weil_restriction --> groups
  f_exists_is_q_group_weil_restriction --> linear_algebra
  f_exists_is_q_group_weil_restriction --> polynomials
  f_exists_is_q_group_weil_restriction --> complex_numbers
  f_exists_rational_coord_polynomial_base_change --> number_fields
  f_exists_rational_coord_polynomial_base_change --> polynomials
  f_exists_rational_coord_polynomial_base_change --> linear_algebra
  f_exists_rational_coord_polynomial_base_change --> rings_fields
  f_exists_rational_equations_weil_restriction --> f_exists_rational_coord_polynomial_base_change
  f_exists_rational_equations_weil_restriction --> f_coords_left_mul_matrix_const_base_change
  f_exists_rational_equations_weil_restriction --> f_restrict_scalars_matrix_of_basis_hom_injective_is_unit
  f_exists_rational_equations_weil_restriction --> linear_algebra
  f_exists_rational_equations_weil_restriction --> polynomials
  f_exists_rational_equations_weil_restriction --> number_fields
  f_gl_free_algebra_to_special_linear_emb_injective_hom --> linear_algebra
  f_gl_free_algebra_to_special_linear_emb_injective_hom --> groups
  f_gl_free_algebra_to_special_linear_emb_injective_hom --> rings_fields
  f_mem_rat_zariski_closure_points_iff_of_is_reduced --> concept_finitely_generated_algebras
  f_mem_rat_zariski_closure_points_iff_of_is_reduced --> concept_coordinate_rings_dimension
  f_mem_rat_zariski_closure_points_iff_of_is_reduced --> rings_fields
  f_mem_rat_zariski_closure_points_iff_of_is_reduced --> polynomials
  f_mem_rat_zariski_closure_points_iff_of_is_reduced --> complex_numbers
  f_restrict_scalars_matrix_of_basis_hom_injective_is_unit --> linear_algebra
  f_restrict_scalars_matrix_of_basis_hom_injective_is_unit --> rings_fields
  f_foundations__curve_cl --> f_degree_formula__flag_deg_formula
  f_foundations__curve_cl --> polynomials
  f_foundations__curve_cl --> counting
  f_foundations__curve_cl --> concept_derivations_smoothness
  f_exists_class_degree_one --> f_degree_formula__flag_deg_formula
  f_exists_class_degree_one --> f_point_degree__perm_exp_inj
  f_exists_class_degree_one --> f_point_degree__pow_sum
  f_exists_class_degree_one --> f_foundations__curve_cl
  f_exists_class_degree_one --> polynomials
  f_limits_of_shift_functionals --> f_shift_functional_power_sum
  f_limits_of_shift_functionals --> f_exists_class_degree_one
  f_limits_of_shift_functionals --> f_foundations__curve_cl
  f_limits_of_shift_functionals --> f_degree_formula__flag_deg_formula
  f_limits_of_shift_functionals --> calculus
  f_limits_of_shift_functionals --> real_analysis
  f_shift_functional_power_sum --> f_point_degree__pow_sum
  f_shift_functional_power_sum --> f_foundations__curve_cl
  f_shift_functional_power_sum --> f_degree_formula__flag_deg_formula
  f_shift_functional_power_sum --> concept_derivations_smoothness
  f_shift_functional_power_sum --> polynomials
  f_degree_formula__flag_deg_formula --> groups
  f_degree_formula__flag_deg_formula --> polynomials
  f_degree_formula__flag_deg_formula --> counting
  f_degree_formula__flag_deg_formula --> linear_algebra
  f_point_degree__perm_exp_inj --> f_degree_formula__flag_deg_formula
  f_point_degree__perm_exp_inj --> groups
  f_point_degree__perm_exp_inj --> polynomials
  f_point_degree__perm_exp_inj --> counting
  f_point_degree__pow_sum --> f_degree_formula__flag_deg_formula
  f_point_degree__pow_sum --> f_point_degree__perm_exp_inj
  f_point_degree__pow_sum --> groups
  f_point_degree__pow_sum --> polynomials
  f_point_degree__pow_sum --> counting
  f_etale_localization_at_prime_tensor_of_etale_away --> concept_etale_ring_maps
  f_etale_localization_at_prime_tensor_of_etale_away --> concept_tensor_product_of_algebras
  f_etale_localization_at_prime_tensor_of_etale_away --> concept_prime_ideals_localization
  f_etale_localization_at_prime_tensor_of_etale_away --> concept_flat_modules
  f_corank_share__statement_f_r --> linear_algebra
  f_corank_share__statement_f_r --> concept_hermitian_unitary_matrices
  f_corank_share__statement_f_r --> counting
  f_eichler_equivalence_holds --> f_statement_e_i
  f_eichler_equivalence_holds --> linear_algebra
  f_eichler_equivalence_holds --> concept_hermitian_unitary_matrices
  f_eichler_equivalence_holds --> rings_fields
  f_has_deriv_at_sphere_chart_last --> f_statement_s_b
  f_has_deriv_at_sphere_chart_last --> counting
  f_has_deriv_at_sphere_chart_last --> calculus
  f_lf_prod --> f_statement_l_f
  f_lf_prod --> number_fields
  f_lf_prod --> concept_dedekind_domains
  f_lf_prod --> concept_ideals_and_discriminant
  f_lf_prod --> primes_divisibility
  f_neighbourhood_hilbert_schmidt_holds --> f_statement_f_u
  f_neighbourhood_hilbert_schmidt_holds --> f_corank_share__statement_f_r
  f_neighbourhood_hilbert_schmidt_holds --> linear_algebra
  f_neighbourhood_hilbert_schmidt_holds --> concept_hermitian_unitary_matrices
  f_kernel_bound_rel --> f_eichler_equivalence_holds
  f_kernel_bound_rel --> f_lf_prod
  f_kernel_bound_rel --> f_neighbourhood_hilbert_schmidt_holds
  f_kernel_bound_rel --> f_statement_e_i
  f_kernel_bound_rel --> f_statement_l_f
  f_kernel_bound_rel --> f_statement_f_u
  f_statement_c_s --> concept_group_representations
  f_statement_c_s --> concept_group_actions
  f_statement_c_s --> complex_numbers
  f_statement_c_s --> modular_arithmetic
  f_statement_c_s --> linear_algebra
  f_statement_e_i --> linear_algebra
  f_statement_e_i --> concept_hermitian_unitary_matrices
  f_statement_e_i --> rings_fields
  f_statement_f_u --> f_corank_share__statement_f_r
  f_statement_f_u --> linear_algebra
  f_statement_f_u --> concept_hermitian_unitary_matrices
  f_statement_f_u --> concept_group_representations
  f_statement_l_f --> number_fields
  f_statement_l_f --> concept_ideals_and_discriminant
  f_statement_l_f --> calculus
  f_statement_l_f --> real_analysis
  f_statement_l_f --> counting
  f_statement_m_v --> counting
  f_statement_m_v --> complex_numbers
  f_statement_m_v --> linear_algebra
  f_statement_n_c --> rings_fields
  f_statement_n_c --> counting
  f_statement_n_c --> modular_arithmetic
  f_statement_n_c --> concept_group_representations
  f_statement_s_b --> calculus
  f_statement_s_b --> real_analysis
  f_statement_s_b --> complex_numbers
  f_character_theory__character_coset_sum_eq_zero_of_subgroup_sum --> concept_group_representations
  f_character_theory__character_coset_sum_eq_zero_of_subgroup_sum --> concept_normal_subgroups_quotients
  f_character_theory__character_coset_sum_eq_zero_of_subgroup_sum --> groups
  f_character_theory__character_coset_sum_eq_zero_of_subgroup_sum --> linear_algebra
  f_exists_standard_unipotent_radical_bij_on_nilradical --> linear_algebra
  f_exists_standard_unipotent_radical_bij_on_nilradical --> groups
  f_exists_standard_unipotent_radical_bij_on_nilradical --> rings_fields
  f_general_linear_function_extend_zero_end_properties --> linear_algebra
  f_general_linear_function_extend_zero_end_properties --> groups
  f_general_linear_function_extend_zero_end_properties --> rings_fields
  f_is_primitive_extend_zero_of_sum_unipotent_radical --> f_character_theory__character_coset_sum_eq_zero_of_subgroup_sum
  f_is_primitive_extend_zero_of_sum_unipotent_radical --> f_exists_standard_unipotent_radical_bij_on_nilradical
  f_is_primitive_extend_zero_of_sum_unipotent_radical --> f_general_linear_function_extend_zero_end_properties
  f_is_primitive_extend_zero_of_sum_unipotent_radical --> f_character_theory__charpoly_block_and_invariant_under_stabilizer_nilradic
  f_is_primitive_extend_zero_of_sum_unipotent_radical --> f_is_character_over_subfield_restrict_class_function_one
  f_is_primitive_extend_zero_of_sum_unipotent_radical --> concept_group_representations
  f_is_primitive_extend_zero_of_sum_unipotent_radical --> linear_algebra
  f_p_number_field_box_count_x --> f_p_number_field_box_count
  f_p_number_field_box_count_x --> f_p_lattice_image_z_lattice
  f_p_number_field_box_count_x --> f_p_covolume_rel_index
  f_p_number_field_box_count_x --> f_p_embedding_sum_places
  f_p_number_field_box_count_x --> f_p_mixed_box_count
  f_p_number_field_box_count_x --> f_p_lattice_count_volume
  f_heights__kernels_lattice --> number_fields
  f_heights__kernels_lattice --> concept_hermitian_unitary_matrices
  f_heights__kernels_lattice --> concept_lattice_point_counting
  f_heights__kernels_lattice --> linear_algebra
  f_p_covolume_rel_index --> f_statements_covolume_rel_index
  f_p_covolume_rel_index --> concept_lattice_point_counting
  f_p_covolume_rel_index --> real_analysis
  f_p_embedding_sum_places --> f_statements_embedding_sum_places
  f_p_embedding_sum_places --> number_fields
  f_p_embedding_sum_places --> complex_numbers
  f_p_embedding_sum_places --> counting
  f_p_lattice_count_volume --> f_statements_lattice_count_volume
  f_p_lattice_count_volume --> concept_lattice_point_counting
  f_p_lattice_count_volume --> real_analysis
  f_p_lattice_image_z_lattice --> f_statements_lattice_image_z_lattice
  f_p_lattice_image_z_lattice --> number_fields
  f_p_lattice_image_z_lattice --> concept_lattice_point_counting
  f_p_lattice_image_z_lattice --> concept_integral_closure_fraction_fields
  f_p_mixed_box_count --> f_statements_mixed_box_count
  f_p_mixed_box_count --> f_statements_lattice_count_volume
  f_p_mixed_box_count --> number_fields
  f_p_mixed_box_count --> concept_lattice_point_counting
  f_p_number_field_box_count --> f_statements_number_field_box_count
  f_p_number_field_box_count --> f_statements_lattice_image_z_lattice
  f_p_number_field_box_count --> f_statements_covolume_rel_index
  f_p_number_field_box_count --> f_statements_embedding_sum_places
  f_p_number_field_box_count --> f_statements_mixed_box_count
  f_p_number_field_box_count --> f_heights__kernels_lattice
  f_p_number_field_box_count --> number_fields
  f_statements_covolume_rel_index --> concept_lattice_point_counting
  f_statements_covolume_rel_index --> real_analysis
  f_statements_embedding_sum_places --> number_fields
  f_statements_embedding_sum_places --> complex_numbers
  f_statements_lattice_count_volume --> concept_lattice_point_counting
  f_statements_lattice_count_volume --> real_analysis
  f_statements_lattice_image_z_lattice --> number_fields
  f_statements_lattice_image_z_lattice --> concept_lattice_point_counting
  f_statements_mixed_box_count --> number_fields
  f_statements_mixed_box_count --> concept_lattice_point_counting
  f_statements_number_field_box_count --> number_fields
  f_statements_number_field_box_count --> f_heights__kernels_lattice
  f_card_step --> f_torsion_bounds_chains__face_d_single
  f_card_step --> groups
  f_card_step --> concept_normal_subgroups_quotients
  f_card_step --> counting
  f_torsion_bounds_chains__face_d_single --> concept_group_homology
  f_torsion_bounds_chains__face_d_single --> concept_group_actions
  f_torsion_bounds_chains__face_d_single --> concept_chain_complexes_homology
  f_torsion_bounds_chains__face_d_single --> concept_finitely_generated_abelian_groups
  f_fin_group --> f_torsion_bounds_chains__imports_alt
  f_fin_group --> f_subquot
  f_fin_group --> f_torsion_bounds_chains__face_d_single
  f_fin_group --> concept_group_homology
  f_group_homology_long_exact --> concept_group_homology
  f_group_homology_long_exact --> concept_group_representations
  f_group_homology_long_exact --> f_torsion_bounds_chains__face_d_single
  f_torsion_bounds_chains__imports_alt --> f_map_nsmul
  f_torsion_bounds_chains__imports_alt --> f_torsion_bounds_chains__shapiro
  f_torsion_bounds_chains__imports_alt --> f_torsion_bounds_chains__face_d_single
  f_torsion_bounds_chains__imports_alt --> concept_group_homology
  f_ind_perm --> concept_group_actions
  f_ind_perm --> concept_group_representations
  f_ind_perm --> concept_normal_subgroups_quotients
  f_ind_perm --> f_torsion_bounds_chains__face_d_single
  f_map_nsmul --> concept_group_homology
  f_map_nsmul --> concept_chain_complexes_homology
  f_map_nsmul --> f_torsion_bounds_chains__face_d_single
  f_orb_step --> concept_group_actions
  f_orb_step --> f_torsion_bounds_chains__face_d_single
  f_orb_step --> counting
  f_perm_card --> f_orb_step
  f_perm_card --> f_perm_split
  f_perm_card --> f_group_homology_long_exact
  f_perm_card --> f_perm_trans
  f_perm_card --> f_card_step
  f_perm_card --> f_perm_empty
  f_perm_card --> f_torsion_bounds_chains__face_d_single
  f_perm_empty --> concept_group_homology
  f_perm_empty --> f_torsion_bounds_chains__face_d_single
  f_perm_split --> concept_group_actions
  f_perm_split --> concept_group_representations
  f_perm_split --> f_torsion_bounds_chains__face_d_single
  f_perm_trans --> f_torsion_bounds_chains__shapiro
  f_perm_trans --> f_fin_group
  f_perm_trans --> f_torsion_bounds_chains__transport
  f_perm_trans --> f_torsion_bounds_chains__face_d_single
  f_perm_trans --> concept_group_actions
  f_torsion_bounds_chains__shapiro --> f_ind_perm
  f_torsion_bounds_chains__shapiro --> concept_group_homology
  f_torsion_bounds_chains__shapiro --> concept_group_actions
  f_torsion_bounds_chains__shapiro --> f_torsion_bounds_chains__face_d_single
  f_subquot --> f_torsion_bounds_chains__face_d_single
  f_subquot --> concept_finitely_generated_abelian_groups
  f_subquot --> linear_algebra
  f_subquot --> modular_arithmetic
  f_torsion_bounds_chains__transport --> f_torsion_bounds_chains__face_d_single
  f_torsion_bounds_chains__transport --> concept_finitely_generated_abelian_groups
  f_torsion_bounds_chains__transport --> counting
  f_period_integrals__prime_count --> primes_divisibility
  f_period_integrals__prime_count --> real_analysis
  f_chebyshev_prime_bounds__log_factorial_eq_sum_of_le --> f_chebyshev_prime_bounds__prime_count_bound_of
  f_chebyshev_prime_bounds__log_factorial_eq_sum_of_le --> concept_chebyshev_functions
  f_chebyshev_prime_bounds__log_factorial_eq_sum_of_le --> primes_divisibility
  f_chebyshev_prime_bounds__log_factorial_eq_sum_of_le --> infinite_series
  f_chebyshev_prime_bounds__log_factorial_le --> f_chebyshev_prime_bounds__prime_count_bound_of
  f_chebyshev_prime_bounds__log_factorial_le --> calculus
  f_chebyshev_prime_bounds__log_factorial_le --> real_analysis
  f_chebyshev_prime_bounds__log_factorial_le --> infinite_series
  f_chebyshev_prime_bounds__prime_count_bound_of --> f_period_integrals__prime_count
  f_chebyshev_prime_bounds__prime_count_bound_of --> concept_chebyshev_functions
  f_chebyshev_prime_bounds__prime_count_bound_of --> real_analysis
  f_chebyshev_prime_bounds__psi_lower_bound_holds --> f_chebyshev_prime_bounds__psi_upper_bound_of_lt_thirty_mul_six_pow
  f_chebyshev_prime_bounds__psi_lower_bound_holds --> f_chebyshev_prime_bounds__log_factorial_le
  f_chebyshev_prime_bounds__psi_lower_bound_holds --> f_chebyshev_prime_bounds__log_factorial_eq_sum_of_le
  f_chebyshev_prime_bounds__psi_lower_bound_holds --> f_chebyshev_prime_bounds__prime_count_bound_of
  f_chebyshev_prime_bounds__psi_lower_bound_holds --> concept_chebyshev_functions
  f_chebyshev_prime_bounds__psi_upper_bound_of_lt_thirty_mul_six_pow --> f_chebyshev_prime_bounds__prime_count_bound_of
  f_chebyshev_prime_bounds__psi_upper_bound_of_lt_thirty_mul_six_pow --> concept_chebyshev_functions
  f_chebyshev_prime_bounds__psi_upper_bound_of_lt_thirty_mul_six_pow --> real_analysis
  f_chebyshev_prime_bounds__psi_upper_bound_of_lt_thirty_mul_six_pow --> proofs
  f_claim_of_two --> f_theta_diff
  f_claim_of_two --> f_floor_half
  f_claim_of_two --> f_period_integrals__primes_dyadic_r_s
  f_claim_of_two --> concept_chebyshev_functions
  f_floor_half --> f_theta_diff
  f_floor_half --> f_chebyshev_prime_bounds__psi_lower_bound_holds
  f_floor_half --> f_period_integrals__primes_dyadic_r_s
  f_floor_half --> concept_chebyshev_functions
  f_floor_half --> real_analysis
  f_theta_diff --> concept_chebyshev_functions
  f_theta_diff --> primes_divisibility
  f_theta_diff --> real_analysis
  f_wedge_line_lattice_vector_bundle --> f_line_lattice_vector_bundle
  f_wedge_line_lattice_vector_bundle --> concept_exterior_powers
  f_wedge_line_lattice_vector_bundle --> concept_schemes_basics
  f_wedge_line_lattice_vector_bundle --> linear_algebra
  f_line_lattice_vector_bundle --> concept_exterior_powers
  f_line_lattice_vector_bundle --> concept_valuation_rings
  f_line_lattice_vector_bundle --> concept_schemes_basics
  f_line_lattice_vector_bundle --> linear_algebra
  f_complex_analytic_sets__st_zariski_analytic_normality --> f_complex_analytic_sets__st_normal_model
  f_complex_analytic_sets__st_zariski_analytic_normality --> concept_complex_analytic_sets
  f_complex_analytic_sets__st_zariski_analytic_normality --> concept_integral_closure_fraction_fields
  f_complex_analytic_sets__st_zariski_analytic_normality --> concept_prime_ideals_localization
  f_complex_analytic_sets__st_analytic_germs_noetherian --> f_complex_analytic_sets__st_zariski_analytic_normality
  f_complex_analytic_sets__st_analytic_germs_noetherian --> concept_noetherian_and_irreducible_components
  f_complex_analytic_sets__st_analytic_germs_noetherian --> concept_complex_analytic_sets
  f_complex_analytic_sets__st_germ_weierstrass_division --> complex_analysis
  f_complex_analytic_sets__st_germ_weierstrass_division --> polynomials
  f_complex_analytic_sets__st_germ_weierstrass_division --> concept_complex_analytic_sets
  f_complex_analytic_sets__st_germ_general_coordinates --> f_complex_analytic_sets__st_germ_weierstrass_division
  f_complex_analytic_sets__st_germ_general_coordinates --> linear_algebra
  f_complex_analytic_sets__st_germ_general_coordinates --> complex_analysis
  f_complex_analytic_sets__p_analytic_germs_noetherian --> f_complex_analytic_sets__st_analytic_germs_noetherian
  f_complex_analytic_sets__p_analytic_germs_noetherian --> f_complex_analytic_sets__st_germ_weierstrass_division
  f_complex_analytic_sets__p_analytic_germs_noetherian --> f_complex_analytic_sets__st_germ_general_coordinates
  f_complex_analytic_sets__p_analytic_germs_noetherian --> f_complex_analytic_sets__st_zariski_analytic_normality
  f_complex_analytic_sets__p_analytic_germs_noetherian --> concept_noetherian_and_irreducible_components
  f_complex_analytic_sets__p_analytic_germs_noetherian --> concept_complex_analytic_sets
  f_complex_analytic_sets__st_prime_germ_nullstellensatz --> f_complex_analytic_sets__st_zariski_analytic_normality
  f_complex_analytic_sets__st_prime_germ_nullstellensatz --> concept_finitely_generated_algebras
  f_complex_analytic_sets__st_prime_germ_nullstellensatz --> concept_prime_ideals_localization
  f_complex_analytic_sets__st_prime_germ_nullstellensatz --> concept_complex_analytic_sets
  f_complex_analytic_sets__st_prime_germ_primitive_presentation --> f_complex_analytic_sets__st_prime_germ_nullstellensatz
  f_complex_analytic_sets__st_prime_germ_primitive_presentation --> concept_separable_polynomials
  f_complex_analytic_sets__st_prime_germ_primitive_presentation --> concept_field_extensions_transcendence
  f_complex_analytic_sets__st_prime_germ_primitive_presentation --> concept_complex_analytic_sets
  f_st_finite_germ_projection_objects --> f_complex_analytic_sets__p_analytic_germs_noetherian
  f_st_finite_germ_projection_objects --> f_complex_analytic_sets__st_zariski_analytic_normality
  f_st_finite_germ_projection_objects --> concept_complex_analytic_sets
  f_st_finite_germ_projection_objects --> concept_prime_ideals_localization
  f_st_prime_germ_projection_step --> f_st_finite_germ_projection_objects
  f_st_prime_germ_projection_step --> concept_prime_ideals_localization
  f_st_prime_germ_projection_step --> concept_complex_analytic_sets
  f_st_germ_projection_function_form --> f_st_finite_germ_projection_objects
  f_st_germ_projection_function_form --> f_complex_analytic_sets__st_prime_germ_nullstellensatz
  f_st_germ_projection_function_form --> f_complex_analytic_sets__st_prime_germ_primitive_presentation
  f_st_germ_projection_function_form --> concept_complex_analytic_sets
  f_complex_analytic_sets__st_prime_germ_finite_projection --> f_complex_analytic_sets__st_prime_germ_nullstellensatz
  f_complex_analytic_sets__st_prime_germ_finite_projection --> f_complex_analytic_sets__st_prime_germ_primitive_presentation
  f_complex_analytic_sets__st_prime_germ_finite_projection --> concept_coordinate_rings_dimension
  f_complex_analytic_sets__st_prime_germ_finite_projection --> concept_complex_analytic_sets
  f_p_prime_germ_finite_projection --> f_complex_analytic_sets__st_prime_germ_finite_projection
  f_p_prime_germ_finite_projection --> f_st_prime_germ_projection_step
  f_p_prime_germ_finite_projection --> f_st_germ_projection_function_form
  f_p_prime_germ_finite_projection --> f_st_finite_germ_projection_objects
  f_p_prime_germ_finite_projection --> concept_complex_analytic_sets
  f_real_place_analysis__complexify --> concept_hermitian_unitary_matrices
  f_real_place_analysis__complexify --> linear_algebra
  f_real_place_analysis__complexify --> complex_numbers
  f_pf_d --> polynomials
  f_pf_d --> counting
  f_pf_d --> real_analysis
  f_partial_fraction_diagonal_identity --> f_pf_d
  f_partial_fraction_diagonal_identity --> polynomials
  f_partial_fraction_diagonal_identity --> rings_fields
  f_partial_fraction_off_diagonal_identity --> f_partial_fraction_diagonal_identity
  f_partial_fraction_off_diagonal_identity --> f_pf_d
  f_partial_fraction_off_diagonal_identity --> polynomials
  f_partial_fraction_square_identity --> f_partial_fraction_diagonal_identity
  f_partial_fraction_square_identity --> f_pf_d
  f_partial_fraction_square_identity --> calculus
  f_partial_fraction_square_identity --> polynomials
  f_exists_unitary_interlacing_realization --> f_partial_fraction_diagonal_identity
  f_exists_unitary_interlacing_realization --> f_partial_fraction_off_diagonal_identity
  f_exists_unitary_interlacing_realization --> f_partial_fraction_square_identity
  f_exists_unitary_interlacing_realization --> f_pf_d
  f_exists_unitary_interlacing_realization --> f_real_place_analysis__complexify
  f_exists_unitary_interlacing_realization --> concept_hermitian_unitary_matrices
  f_exists_unitary_interlacing_realization --> linear_algebra
  f_smith_zp --> f_smith_exists
  f_smith_zp --> f_mahler_measure__statement_d
  f_smith_zp --> p_adic_numbers
  f_smith_zp --> concept_discrete_valuation_ring
  f_smith_zp --> linear_algebra
  f_mahler_measure__statement --> polynomials
  f_mahler_measure__statement --> p_adic_numbers
  f_mahler_measure__statement --> concept_ultrametric_norm
  f_mahler_measure__statement --> counting
  f_mahler_measure__statement_b --> polynomials
  f_mahler_measure__statement_b --> p_adic_numbers
  f_mahler_measure__statement_b --> concept_prime_ideals_localization
  f_mahler_measure__statement_b --> linear_algebra
  f_mahler_measure__statement_d --> f_mahler_measure__statement
  f_mahler_measure__statement_d --> polynomials
  f_mahler_measure__statement_d --> p_adic_numbers
  f_mahler_measure__statement_d --> concept_ultrametric_norm
  f_mahler_measure__statement_d --> concept_discrete_valuation_ring
  f_defs_d_v_r --> f_statement_d_v_r
  f_defs_d_v_r --> concept_discrete_valuation_ring
  f_defs_gram --> f_smith_determinants__statement_gram
  f_defs_gram --> linear_algebra
  f_defs_gram --> polynomials
  f_defs_gram --> concept_hermitian_unitary_matrices
  f_smith_exists --> f_statement_d_v_r
  f_smith_exists --> concept_discrete_valuation_ring
  f_smith_exists --> concept_finitely_generated_abelian_groups
  f_smith_exists --> linear_algebra
  f_statement_d_v_r --> concept_discrete_valuation_ring
  f_statement_d_v_r --> concept_valuation_rings
  f_statement_d_v_r --> linear_algebra
  f_statement_d_v_r --> concept_finitely_generated_abelian_groups
  f_smith_determinants__statement_gram --> polynomials
  f_smith_determinants__statement_gram --> linear_algebra
  f_smith_determinants__statement_gram --> primes_divisibility
  f_smith_determinants__statement_gram --> rings_fields
  f_truncation_chain_bound_nonneg_exponents --> f_smith_exists
  f_truncation_chain_bound_nonneg_exponents --> concept_discrete_valuation_ring
  f_closure_prime_regular_height --> f_counting_bound
  f_closure_prime_regular_height --> concept_etale_ring_maps
  f_closure_prime_regular_height --> concept_prime_ideals_localization
  f_closure_prime_regular_height --> concept_integral_closure_fraction_fields
  f_counting_bound --> concept_etale_ring_maps
  f_counting_bound --> concept_prime_ideals_localization
  f_counting_bound --> concept_tensor_product_of_algebras
  f_counting_bound --> concept_integral_closure_fraction_fields
  f_dixmier_schur_of_rank_le_aleph0 --> linear_algebra
  f_dixmier_schur_of_rank_le_aleph0 --> polynomials
  f_dixmier_schur_of_rank_le_aleph0 --> complex_numbers
  f_dixmier_schur_of_rank_le_aleph0 --> concept_group_representations
  f_dixmier_schur_of_rank_le_aleph0 --> counting
  f_operator_stable_pi_tensor_pure_kernel_span --> f_simple_over
  f_operator_stable_pi_tensor_pure_kernel_span --> concept_flat_modules
  f_operator_stable_pi_tensor_pure_kernel_span --> linear_algebra
  f_simple_over --> linear_algebra
  f_simple_over --> concept_flat_modules
  f_simple_over_stable_submodule_pi_tensor --> f_simple_over
  f_simple_over_stable_submodule_pi_tensor --> f_simple_over_stable_submodule_tensor_pure_kernel_span
  f_simple_over_stable_submodule_pi_tensor --> f_operator_stable_pi_tensor_pure_kernel_span
  f_simple_over_stable_submodule_pi_tensor --> linear_algebra
  f_simple_over_stable_submodule_pi_tensor --> counting
  f_simple_over_stable_submodule_tensor_pure_kernel_span --> f_simple_over
  f_simple_over_stable_submodule_tensor_pure_kernel_span --> f_simple_tensor_product_operator_stable_countable
  f_simple_over_stable_submodule_tensor_pure_kernel_span --> concept_normal_subgroups_quotients
  f_simple_over_stable_submodule_tensor_pure_kernel_span --> linear_algebra
  f_simple_tensor_product_operator_stable_countable --> f_dixmier_schur_of_rank_le_aleph0
  f_simple_tensor_product_operator_stable_countable --> f_simple_over
  f_simple_tensor_product_operator_stable_countable --> concept_group_representations
  f_simple_tensor_product_operator_stable_countable --> concept_tensor_product_of_algebras
  f_simple_tensor_product_operator_stable_countable --> linear_algebra
  f_coker_tors --> f_torsion_bounds_chains__max_indep
  f_coker_tors --> f_full_enum
  f_coker_tors --> f_index_le
  f_coker_tors --> f_tors_sat
  f_coker_tors --> concept_finitely_generated_abelian_groups
  f_coker_tors --> counting
  f_det_nat_abs_le_prod_l1_norms --> linear_algebra
  f_det_nat_abs_le_prod_l1_norms --> counting
  f_full_enum --> linear_algebra
  f_full_enum --> counting
  f_full_enum --> concept_finitely_generated_abelian_groups
  f_torsion_bounds_chains__imports --> f_quotients_equiv_of_ker_eq
  f_torsion_bounds_chains__imports --> f_l1_map_domain_le_and_l1_face_d_single_le
  f_torsion_bounds_chains__imports --> f_coker_tors
  f_torsion_bounds_chains__imports --> f_torsion_bounds_chains__transport
  f_torsion_bounds_chains__imports --> concept_group_actions
  f_torsion_bounds_chains__imports --> concept_chain_complexes_homology
  f_index_le --> f_det_nat_abs_le_prod_l1_norms
  f_index_le --> concept_finitely_generated_abelian_groups
  f_index_le --> linear_algebra
  f_ker_orb --> concept_group_actions
  f_ker_orb --> concept_group_representations
  f_ker_orb --> linear_algebra
  f_l1_map_domain_le_and_l1_face_d_single_le --> f_torsion_bounds_chains__face_d_single
  f_l1_map_domain_le_and_l1_face_d_single_le --> infinite_series
  f_l1_map_domain_le_and_l1_face_d_single_le --> counting
  f_torsion_bounds_chains__max_indep --> linear_algebra
  f_torsion_bounds_chains__max_indep --> concept_finitely_generated_abelian_groups
  f_quotients_equiv_of_ker_eq --> f_ker_orb
  f_quotients_equiv_of_ker_eq --> concept_group_actions
  f_quotients_equiv_of_ker_eq --> concept_chain_complexes_homology
  f_quotients_equiv_of_ker_eq --> concept_normal_subgroups_quotients
  f_tors_sat --> f_tors_sat_mult
  f_tors_sat --> concept_finitely_generated_abelian_groups
  f_tors_sat --> concept_normal_subgroups_quotients
  f_tors_sat_mult --> concept_finitely_generated_abelian_groups
  f_tors_sat_mult --> groups
  f_character_theory__virtual_characters_mul_comap_conj_ind_linear --> f_is_character_over_subfield_restrict_class_function_one
  f_character_theory__virtual_characters_mul_comap_conj_ind_linear --> f_is_character_over_subfield_induced_class_function
  f_character_theory__virtual_characters_mul_comap_conj_ind_linear --> f_is_character_over_subfield_of_representation
  f_character_theory__virtual_characters_mul_comap_conj_ind_linear --> f_induced_class_function_from_subgroup_eq_finsum_cosets
  f_character_theory__virtual_characters_mul_comap_conj_ind_linear --> concept_group_representations
  f_character_theory__virtual_characters_mul_comap_conj_ind_linear --> groups
  f_character_theory__virtual_characters_mul_comap_conj_ind_linear --> complex_numbers
  f_exists_lt_commutator_mem_of_ne_top --> concept_normal_subgroups_quotients
  f_exists_lt_commutator_mem_of_ne_top --> groups
  f_inertia_eigenvalues__ind_apply_one --> f_character_theory__virtual_characters_mul_comap_conj_ind_linear
  f_inertia_eigenvalues__ind_apply_one --> f_galois_cohomology₂__brauer_degree_zero
  f_inertia_eigenvalues__ind_apply_one --> f_induced_class_function_from_subgroup_eq_finsum_cosets
  f_inertia_eigenvalues__ind_apply_one --> concept_group_representations
  f_inertia_eigenvalues__ind_apply_one --> concept_normal_subgroups_quotients
  f_galois_cohomology₂__brauer_degree_zero --> concept_group_representations
  f_galois_cohomology₂__brauer_degree_zero --> groups
  f_galois_cohomology₂__brauer_degree_zero --> complex_numbers
  f_galois_cohomology₂__brauer_degree_zero --> linear_algebra
  f_analytic_forms__ma_int_empty --> calculus
  f_analytic_forms__ma_int_empty --> complex_analysis
  f_analytic_forms__ma_int_empty --> complex_numbers
  f_analytic_forms__ma_int_empty --> linear_algebra
  f_potential_theory__is_potential_of_fun --> f_analytic_forms__ma_int_empty
  f_potential_theory__is_potential_of_fun --> complex_analysis
  f_potential_theory__is_potential_of_fun --> concept_point_set_topology
  f_potential_theory__is_potential_of_fun --> calculus
  f_divisor_base__model_ddc_forms --> f_potential_theory__is_potential_of_fun
  f_divisor_base__model_ddc_forms --> f_analytic_forms__ma_int_empty
  f_divisor_base__model_ddc_forms --> complex_analysis
  f_divisor_base__model_ddc_forms --> real_analysis
  f_divisor_proofs__boundary_potential_smooth_off_divisor --> f_divisor_proofs__potential_smooth_in_chart
  f_divisor_proofs__boundary_potential_smooth_off_divisor --> f_divisor_base__model_ddc_forms
  f_divisor_proofs__boundary_potential_smooth_off_divisor --> complex_analysis
  f_divisor_proofs__boundary_potential_smooth_off_divisor --> calculus
  f_divisor_proofs__levi_form_log_potential_formula --> f_analytic_forms__ma_int_empty
  f_divisor_proofs__levi_form_log_potential_formula --> f_divisor_base__model_ddc_forms
  f_divisor_proofs__levi_form_log_potential_formula --> calculus
  f_divisor_proofs__levi_form_log_potential_formula --> complex_analysis
  f_divisor_proofs__potential_smooth_in_chart --> f_potential_theory__is_potential_of_fun
  f_divisor_proofs__potential_smooth_in_chart --> complex_analysis
  f_divisor_proofs__potential_smooth_in_chart --> calculus
  f_poincare_form_bound_of_ddc --> f_divisor_base__model_ddc_forms
  f_poincare_form_bound_of_ddc --> f_divisor_proofs__boundary_potential_smooth_off_divisor
  f_poincare_form_bound_of_ddc --> f_divisor_proofs__levi_form_log_potential_formula
  f_poincare_form_bound_of_ddc --> f_divisor_proofs__potential_smooth_in_chart
  f_poincare_form_bound_of_ddc --> real_analysis
  f_sup_meas --> concept_haar_measure_fundamental_domain
  f_sup_meas --> concept_normal_subgroups_quotients
  f_sup_meas --> groups
  f_semidirect_quotient_measure_conjugation_invariant --> f_sup_meas
  f_semidirect_quotient_measure_conjugation_invariant --> concept_haar_measure_fundamental_domain
  f_semidirect_quotient_measure_conjugation_invariant --> concept_normal_subgroups_quotients
  f_conjugation_measure_preserving_semidirect --> f_sup_meas
  f_conjugation_measure_preserving_semidirect --> concept_haar_measure_fundamental_domain
  f_conjugation_measure_preserving_semidirect --> concept_normal_subgroups_quotients
  f_semidirect_measure_restriction_normal_part --> f_sup_meas
  f_semidirect_measure_restriction_normal_part --> concept_haar_measure_fundamental_domain
  f_semidirect_measure_restriction_normal_part --> concept_normal_subgroups_quotients
  f_countable_transversal_measure_extension --> concept_haar_measure_fundamental_domain
  f_countable_transversal_measure_extension --> concept_normal_subgroups_quotients
  f_countable_transversal_measure_extension --> concept_point_set_topology
  f_normalizing_element_fundamental_domain_scaling --> concept_haar_measure_fundamental_domain
  f_normalizing_element_fundamental_domain_scaling --> concept_normal_subgroups_quotients
  f_normalizing_element_fundamental_domain_scaling --> groups
  f_quotient_measure_conjugation_invariant --> f_sup_meas
  f_quotient_measure_conjugation_invariant --> f_semidirect_quotient_measure_conjugation_invariant
  f_quotient_measure_conjugation_invariant --> f_conjugation_measure_preserving_semidirect
  f_quotient_measure_conjugation_invariant --> f_semidirect_measure_restriction_normal_part
  f_quotient_measure_conjugation_invariant --> f_countable_transversal_measure_extension
  f_quotient_measure_conjugation_invariant --> f_normalizing_element_fundamental_domain_scaling
  f_quotient_measure_conjugation_invariant --> concept_haar_measure_fundamental_domain
  f_quotient_measure_conjugation_invariant --> concept_normal_subgroups_quotients
  f_global_geometry__has_values --> f_global_geometry__lie_model
  f_global_geometry__has_values --> concept_dual_numbers
  f_global_geometry__has_values --> concept_group_schemes
  f_global_geometry__has_values --> concept_integral_closure_fraction_fields
  f_global_geometry__has_values --> groups
  f_global_geometry__lie_model --> concept_dual_numbers
  f_global_geometry__lie_model --> concept_group_schemes
  f_global_geometry__lie_model --> linear_algebra
  f_geometry_proofs__exists_unique_tangent_dual_number --> f_global_geometry__lie_model
  f_geometry_proofs__exists_unique_tangent_dual_number --> f_global_geometry__has_values
  f_geometry_proofs__exists_unique_tangent_dual_number --> concept_dual_numbers
  f_geometry_proofs__exists_unique_tangent_dual_number --> concept_group_schemes
  f_geometry_proofs__exists_unique_tangent_dual_number --> concept_categorical_pullbacks
  f_torsion_embedding_base_change --> f_htat_bc_tors
  f_torsion_embedding_base_change --> concept_group_schemes
  f_torsion_embedding_base_change --> concept_categorical_pullbacks
  f_htat_bc_tors --> f_htat_ht
  f_htat_bc_tors --> concept_group_schemes
  f_htat_bc_tors --> concept_categorical_pullbacks
  f_htat_bc_tors --> concept_schemes_basics
  f_htat_ht --> f_global_geometry__has_values
  f_htat_ht --> f_global_geometry__lie_model
  f_htat_ht --> f_geometry_proofs__exists_unique_tangent_dual_number
  f_htat_ht --> concept_dual_numbers
  f_abelian_scheme_quotients__is_abelian_scheme --> f_split_tori__split_torus_aff
  f_abelian_scheme_quotients__is_abelian_scheme --> concept_group_schemes
  f_abelian_scheme_quotients__is_abelian_scheme --> concept_smooth_morphisms
  f_abelian_scheme_quotients__is_abelian_scheme --> concept_schemes_basics
  f_split_tori__split_torus_aff --> concept_group_schemes
  f_split_tori__split_torus_aff --> rings_fields
  f_split_tori__split_torus_aff --> groups
  f_split_tori__split_torus_aff --> concept_categorical_pullbacks
  f_split_tori__split_torus_aff --> concept_finitely_generated_abelian_groups
  f_eq_of_sec_alg_top --> concept_schemes_basics
  f_eq_of_sec_alg_top --> concept_categorical_pullbacks
  f_eq_of_sec_alg_top --> concept_tensor_product_of_algebras
  f_kappa_apply_eq --> f_eq_of_sec_alg_top
  f_kappa_apply_eq --> concept_tensor_product_of_algebras
  f_kappa_apply_eq --> concept_schemes_basics
  f_kappa_apply_eq --> concept_categorical_pullbacks
  f_section_tensor_pullback_ring_hom_bijective --> f_kappa_apply_eq
  f_section_tensor_pullback_ring_hom_bijective --> concept_tensor_product_of_algebras
  f_section_tensor_pullback_ring_hom_bijective --> concept_categorical_pullbacks
  f_section_tensor_pullback_ring_hom_bijective --> concept_schemes_basics
  f_ideal_sheaf_comap_ideal_affine_open_of_is_affine --> f_divisor_proofs__ideal_sheaf_data_comap_ideal_top_of_is_affine
  f_ideal_sheaf_comap_ideal_affine_open_of_is_affine --> concept_schemes_basics
  f_ideal_sheaf_comap_ideal_affine_open_of_is_affine --> concept_prime_ideals_localization
  f_divisor_proofs__affine_hilbert_ideal_sheaf_of_quotient_ideal_top --> f_kappa_apply_eq
  f_divisor_proofs__affine_hilbert_ideal_sheaf_of_quotient_ideal_top --> f_eq_of_sec_alg_top
  f_divisor_proofs__affine_hilbert_ideal_sheaf_of_quotient_ideal_top --> concept_tensor_product_of_algebras
  f_divisor_proofs__affine_hilbert_ideal_sheaf_of_quotient_ideal_top --> concept_prime_ideals_localization
  f_divisor_proofs__affine_hilbert_ideal_sheaf_of_quotient_ideal_top --> concept_schemes_basics
  f_affine_hilbert_base_change_app_l_e_comp_spec_tensor --> f_kappa_apply_eq
  f_affine_hilbert_base_change_app_l_e_comp_spec_tensor --> f_eq_of_sec_alg_top
  f_affine_hilbert_base_change_app_l_e_comp_spec_tensor --> f_divisor_proofs__comap_bc_comp
  f_affine_hilbert_base_change_app_l_e_comp_spec_tensor --> concept_tensor_product_of_algebras
  f_affine_hilbert_base_change_app_l_e_comp_spec_tensor --> concept_categorical_pullbacks
  f_ker_affine_hilbert_tensor_pullback_eq_map --> f_ideal_sheaf_comap_ideal_affine_open_of_is_affine
  f_ker_affine_hilbert_tensor_pullback_eq_map --> f_divisor_proofs__affine_hilbert_ideal_sheaf_of_quotient_ideal_top
  f_ker_affine_hilbert_tensor_pullback_eq_map --> f_affine_hilbert_base_change_app_l_e_comp_spec_tensor
  f_ker_affine_hilbert_tensor_pullback_eq_map --> f_section_tensor_pullback_ring_hom_bijective
  f_ker_affine_hilbert_tensor_pullback_eq_map --> f_kappa_apply_eq
  f_ker_affine_hilbert_tensor_pullback_eq_map --> f_eq_of_sec_alg_top
  f_ker_affine_hilbert_tensor_pullback_eq_map --> concept_tensor_product_of_algebras
  f_foundation_proofs__finite_index_of_gamma_le --> concept_modular_forms
  f_foundation_proofs__finite_index_of_gamma_le --> concept_normal_subgroups_quotients
  f_foundation_proofs__finite_index_of_gamma_le --> linear_algebra
  f_foundation_proofs__finite_index_of_gamma_le --> complex_analysis
  f_slash_q_expansion_coeff_width_transform --> f_foundation_proofs__finite_index_of_gamma_le
  f_slash_q_expansion_coeff_width_transform --> concept_modular_forms
  f_slash_q_expansion_coeff_width_transform --> concept_roots_of_unity_kummer
  f_slash_q_expansion_coeff_width_transform --> infinite_series
  f_slash_q_expansion_coeff_width_transform --> complex_analysis
  f_slash_sub_q_expansion_partial_sum_is_big_o --> f_foundation_proofs__finite_index_of_gamma_le
  f_slash_sub_q_expansion_partial_sum_is_big_o --> concept_modular_forms
  f_slash_sub_q_expansion_partial_sum_is_big_o --> infinite_series
  f_slash_sub_q_expansion_partial_sum_is_big_o --> complex_analysis
  f_coeff_eq_zero_of_sum_plus_minus_reps_eq_zero --> f_foundation_proofs__finite_index_of_gamma_le
  f_coeff_eq_zero_of_sum_plus_minus_reps_eq_zero --> concept_roots_of_unity_kummer
  f_coeff_eq_zero_of_sum_plus_minus_reps_eq_zero --> linear_algebra
  f_coeff_eq_zero_of_sum_plus_minus_reps_eq_zero --> complex_numbers
  f_exists_level_one_form_one_add_exp_decay --> f_foundation_proofs__finite_index_of_gamma_le
  f_exists_level_one_form_one_add_exp_decay --> concept_modular_forms
  f_exists_level_one_form_one_add_exp_decay --> infinite_series
  f_exists_eq_discriminant_mul_of_exp_decay_cusps --> f_foundation_proofs__finite_index_of_gamma_le
  f_exists_eq_discriminant_mul_of_exp_decay_cusps --> concept_modular_forms
  f_exists_eq_discriminant_mul_of_exp_decay_cusps --> complex_analysis
  f_reduces_to_smaller_odd_weight_of_leading_coeff_matrix_det --> f_slash_q_expansion_coeff_width_transform
  f_reduces_to_smaller_odd_weight_of_leading_coeff_matrix_det --> f_slash_sub_q_expansion_partial_sum_is_big_o
  f_reduces_to_smaller_odd_weight_of_leading_coeff_matrix_det --> f_coeff_eq_zero_of_sum_plus_minus_reps_eq_zero
  f_reduces_to_smaller_odd_weight_of_leading_coeff_matrix_det --> f_exists_level_one_form_one_add_exp_decay
  f_reduces_to_smaller_odd_weight_of_leading_coeff_matrix_det --> f_exists_eq_discriminant_mul_of_exp_decay_cusps
  f_reduces_to_smaller_odd_weight_of_leading_coeff_matrix_det --> f_foundation_proofs__finite_index_of_gamma_le
  f_reduces_to_smaller_odd_weight_of_leading_coeff_matrix_det --> linear_algebra
  f_reduces_to_smaller_odd_weight_of_leading_coeff_matrix_det --> concept_modular_forms
  f_one_add_smul_mem_of_sq_zero --> polynomials
  f_one_add_smul_mem_of_sq_zero --> linear_algebra
  f_one_add_smul_mem_of_sq_zero --> groups
  f_exists_rat_projector_of_aut_stable_matrices --> f_adelic_lattice_proofs__galois_stable_submodule_le_span_rational
  f_exists_rat_projector_of_aut_stable_matrices --> concept_galois_fixed_fields
  f_exists_rat_projector_of_aut_stable_matrices --> linear_algebra
  f_exists_rat_linear_param_block_diag_kernel --> f_exists_rat_projector_of_aut_stable_matrices
  f_exists_rat_linear_param_block_diag_kernel --> f_one_add_smul_mem_of_sq_zero
  f_exists_rat_linear_param_block_diag_kernel --> linear_algebra
  f_exists_rat_linear_param_block_diag_kernel --> concept_galois_fixed_fields
  f_uniformization_proofs__exists_graded_ring_kernel_lift --> concept_adic_completion
  f_uniformization_proofs__exists_graded_ring_kernel_lift --> concept_noetherian_and_irreducible_components
  f_uniformization_proofs__exists_graded_ring_kernel_lift --> polynomials
  f_uniformization_proofs__exists_graded_ring_kernel_lift --> linear_algebra
  f_moduli_proofs__is_noetherian_ring_of_is_adic_complete --> f_uniformization_proofs__exists_graded_ring_kernel_lift
  f_moduli_proofs__is_noetherian_ring_of_is_adic_complete --> concept_adic_completion
  f_moduli_proofs__is_noetherian_ring_of_is_adic_complete --> concept_noetherian_and_irreducible_components
  f_moduli_proofs__is_noetherian_ring_of_is_adic_complete --> concept_finitely_generated_algebras
  f_iwasawa_decomposition__is_noetherian_ring_adic_completion_of_noetherian --> f_moduli_proofs__is_noetherian_ring_of_is_adic_complete
  f_iwasawa_decomposition__is_noetherian_ring_adic_completion_of_noetherian --> concept_adic_completion
  f_iwasawa_decomposition__is_noetherian_ring_adic_completion_of_noetherian --> concept_noetherian_and_irreducible_components
  f_algebra_tools__is_cpl_at_self --> concept_adic_completion
  f_algebra_tools__is_cpl_at_self --> concept_local_rings
  f_algebra_tools__is_cpl_at_self --> concept_prime_ideals_localization
  f_algebra_tools__is_cpl_at_self --> concept_noetherian_and_irreducible_components
  f_algebra_tools__ca_cpl_ex --> f_algebra_tools__is_cpl_at_self
  f_algebra_tools__ca_cpl_ex --> f_iwasawa_decomposition__is_noetherian_ring_adic_completion_of_noetherian
  f_algebra_tools__ca_cpl_ex --> concept_adic_completion
  f_algebra_tools__ca_cpl_ex --> concept_prime_ideals_localization
  f_algebra_tools__ca_cpl_ex --> concept_local_rings
  f_algebra_tools__ca_cpl_map --> f_algebra_tools__is_cpl_at_self
  f_algebra_tools__ca_cpl_map --> concept_local_rings
  f_algebra_tools__ca_cpl_map --> concept_noetherian_and_irreducible_components
  f_algebra_tools__ca_cpl_lift --> f_algebra_tools__ca_cpl_map
  f_algebra_tools__ca_cpl_lift --> f_algebra_tools__is_cpl_at_self
  f_algebra_tools__ca_cpl_lift --> concept_adic_completion
  f_algebra_tools__ca_cpl_lift --> concept_local_rings
  f_algebra_tools__ca_cpl_lift --> concept_hensel_lifting
  f_algebra_tools__ca_cpl_uniq --> f_algebra_tools__ca_cpl_lift
  f_algebra_tools__ca_cpl_uniq --> f_algebra_tools__is_cpl_at_self
  f_algebra_tools__ca_cpl_uniq --> concept_adic_completion
  f_algebra_tools__ca_cpl_flat --> f_algebra_tools__ca_cpl_uniq
  f_algebra_tools__ca_cpl_flat --> f_algebra_tools__ca_cpl_ex
  f_algebra_tools__ca_cpl_flat --> concept_flat_modules
  f_algebra_tools__ca_cpl_flat --> concept_adic_completion
  f_ca_cpl_spec --> f_algebra_tools__ca_cpl_flat
  f_ca_cpl_spec --> f_algebra_tools__is_cpl_at_self
  f_ca_cpl_spec --> concept_prime_ideals_localization
  f_ca_cpl_spec --> concept_local_rings
  f_ca_cpl_spec --> concept_flat_modules
  f_global_geometry__eig_lat --> f_global_geometry__lie_model
  f_global_geometry__eig_lat --> f_global_geometry__coords_at
  f_global_geometry__eig_lat --> concept_schemes_basics
  f_global_geometry__eig_lat --> concept_valuation_rings
  f_global_geometry__eig_lat --> linear_algebra
  f_quadratic_character_prescribed_places --> f_toric_varieties__krull_domain
  f_quadratic_character_prescribed_places --> concept_integral_closure_fraction_fields
  f_quadratic_character_prescribed_places --> concept_coordinate_rings_dimension
  f_quadratic_character_prescribed_places --> linear_algebra
  f_exists_point_localization_prime --> f_global_geometry__is_cpt_gen
  f_exists_point_localization_prime --> concept_prime_ideals_localization
  f_exists_point_localization_prime --> concept_schemes_basics
  f_exists_point_localization_prime --> concept_local_rings
  f_lattice_eq_of_codim_one_eq --> f_lattices_agree_of_height_one
  f_geometry_proofs__reg_at_fraction_noetherian_closed --> f_global_geometry__is_cpt_gen
  f_geometry_proofs__reg_at_fraction_noetherian_closed --> f_global_geometry__coords_at
  f_geometry_proofs__reg_at_fraction_noetherian_closed --> concept_integral_closure_fraction_fields
  f_geometry_proofs__reg_at_fraction_noetherian_closed --> concept_prime_ideals_localization
  f_geometry_proofs__reg_at_fraction_noetherian_closed --> concept_noetherian_and_irreducible_components
  f_lattices_agree_of_height_one --> f_geometry_proofs__reg_at_fraction_noetherian_closed
  f_lattices_agree_of_height_one --> f_exists_point_localization_prime
  f_lattices_agree_of_height_one --> f_quadratic_character_prescribed_places
  f_lattices_agree_of_height_one --> f_global_geometry__is_cpt_gen
  f_lattices_agree_of_height_one --> f_global_geometry__coords_at
  f_lattices_agree_of_height_one --> concept_integral_closure_fraction_fields
  f_lattices_agree_of_height_one --> concept_coordinate_rings_dimension
  f_toric_varieties__krull_domain --> concept_integral_closure_fraction_fields
  f_toric_varieties__krull_domain --> concept_coordinate_rings_dimension
  f_toric_varieties__krull_domain --> concept_prime_ideals_localization
  f_toric_varieties__krull_domain --> concept_noetherian_and_irreducible_components
  f_class_number_bounds__totally_real_roots --> primes_divisibility
  f_class_number_bounds__totally_real_roots --> modular_arithmetic
  f_gal_abelian --> f_totally_real_roots__gal_aut
  f_gal_abelian --> f_totally_real_roots__gal_defs
  f_gal_abelian --> f_gal_roots
  f_gal_abelian --> f_level_lift
  f_gal_abelian --> f_princ_top
  f_gal_abelian --> f_totally_real_roots__le_nu_iff_pow_mem_princ
  f_gal_abelian --> concept_roots_of_unity_kummer
  f_gal_abelian --> concept_galois_fixed_fields
  f_gal_abelian --> p_adic_numbers
  f_totally_real_roots__gal_aut --> concept_roots_of_unity_kummer
  f_totally_real_roots__gal_aut --> concept_galois_fixed_fields
  f_totally_real_roots__gal_aut --> algebraic_closure
  f_totally_real_roots__gal_aut --> number_fields
  f_totally_real_roots__gal_aut --> modular_arithmetic
  f_totally_real_roots__gal_defs --> f_class_number_bounds__totally_real_roots
  f_totally_real_roots__gal_defs --> f_totally_real_roots__le_nu_iff_pow_mem_princ
  f_totally_real_roots__gal_defs --> concept_roots_of_unity_kummer
  f_totally_real_roots__gal_defs --> concept_galois_fixed_fields
  f_totally_real_roots__gal_defs --> p_adic_numbers
  f_gal_roots --> f_totally_real_roots__gal_defs
  f_gal_roots --> f_totally_real_roots__le_nu_iff_pow_mem_princ
  f_gal_roots --> concept_roots_of_unity_kummer
  f_gal_roots --> p_adic_numbers
  f_gal_roots --> concept_point_set_topology
  f_totally_real_roots__le_nu_iff_pow_mem_princ --> f_class_number_bounds__totally_real_roots
  f_totally_real_roots__le_nu_iff_pow_mem_princ --> p_adic_numbers
  f_totally_real_roots__le_nu_iff_pow_mem_princ --> modular_arithmetic
  f_totally_real_roots__le_nu_iff_pow_mem_princ --> groups
  f_level_group_sup_level_inertia --> f_totally_real_roots__le_nu_iff_pow_mem_princ
  f_level_group_sup_level_inertia --> f_princ_top
  f_level_group_sup_level_inertia --> p_adic_numbers
  f_level_group_sup_level_inertia --> modular_arithmetic
  f_level_lift --> f_totally_real_roots__le_nu_iff_pow_mem_princ
  f_level_lift --> modular_arithmetic
  f_level_lift --> primes_divisibility
  f_nu_basic --> f_totally_real_roots__le_nu_iff_pow_mem_princ
  f_nu_basic --> f_class_number_bounds__totally_real_roots
  f_nu_basic --> p_adic_numbers
  f_nu_basic --> groups
  f_nu_basic --> modular_arithmetic
  f_princ_top --> f_totally_real_roots__le_nu_iff_pow_mem_princ
  f_princ_top --> concept_ultrametric_norm
  f_princ_top --> concept_point_set_topology
  f_princ_top --> p_adic_numbers
  f_princ_top --> groups
  f_units_map_surj_of_zmod --> f_totally_real_roots__le_nu_iff_pow_mem_princ
  f_units_map_surj_of_zmod --> concept_local_rings
  f_units_map_surj_of_zmod --> p_adic_numbers
  f_units_map_surj_of_zmod --> modular_arithmetic
  f_line_lattice_generic_sections --> f_regular_everywhere_is_integral
  f_line_lattice_generic_sections --> f_global_geometry__is_cpt_gen
  f_line_lattice_generic_sections --> f_global_geometry__is_line_gen_on
  f_line_lattice_generic_sections --> concept_integral_closure_fraction_fields
  f_regular_everywhere_is_integral --> f_valuation_centre_regular_unit
  f_regular_everywhere_is_integral --> f_global_geometry__is_cpt_gen
  f_regular_everywhere_is_integral --> concept_valuation_rings
  f_regular_everywhere_is_integral --> concept_integral_closure_fraction_fields
  f_regular_everywhere_is_integral --> concept_schemes_basics
  f_valuation_centre_regular_unit --> f_valuation_centre_exists
  f_valuation_centre_regular_unit --> concept_valuation_rings
  f_valuation_centre_regular_unit --> concept_schemes_basics
  f_valuation_centre_regular_unit --> concept_local_rings
  f_valuation_centre_exists --> f_global_geometry__is_cpt_gen
  f_valuation_centre_exists --> f_global_geometry__coords_at
  f_valuation_centre_exists --> concept_valuation_rings
  f_valuation_centre_exists --> concept_schemes_basics
  f_valuation_centre_exists --> concept_local_rings
  f_exists_basis_of_lattice_span --> concept_valuation_rings
  f_exists_basis_of_lattice_span --> concept_flat_modules
  f_exists_basis_of_lattice_span --> concept_local_rings
  f_exists_basis_of_lattice_span --> linear_algebra
  f_exists_basis_quotient_lattice_eigen --> f_divisor_proofs__eigen_projection_quotient_lattice
  f_exists_basis_quotient_lattice_eigen --> f_divisor_proofs__exists_spanning_image_lattice
  f_exists_basis_quotient_lattice_eigen --> f_exists_basis_of_lattice_span
  f_exists_basis_quotient_lattice_eigen --> f_exterior_power_basis_lattice_principal
  f_exists_basis_quotient_lattice_eigen --> f_divisor_base__sandwich_maps
  f_exists_basis_quotient_lattice_eigen --> concept_exterior_powers
  f_exists_basis_quotient_lattice_eigen --> concept_valuation_rings
  f_exterior_power_basis_lattice_principal --> f_wedge_ne_zero_of_linear_independent
  f_exterior_power_basis_lattice_principal --> concept_exterior_powers
  f_exterior_power_basis_lattice_principal --> linear_algebra
  f_dual_lattices__small_level_class_set --> concept_exterior_powers
  f_dual_lattices__small_level_class_set --> concept_valuation_rings
  f_dual_lattices__small_level_class_set --> concept_discrete_valuation_ring
  f_dual_lattices__small_level_class_set --> concept_hensel_lifting
  f_dual_lattices__small_level_class_set --> linear_algebra
  f_dual_lattices__small_level_class_set --> polynomials
  f_wedge_ne_zero_of_linear_independent --> f_dual_lattices__small_level_class_set
  f_wedge_ne_zero_of_linear_independent --> concept_exterior_powers
  f_wedge_ne_zero_of_linear_independent --> linear_algebra
  f_induced_class_function_from_subgroup_trans --> f_induced_class_function_from_subgroup_eq_finsum_cosets
  f_induced_class_function_from_subgroup_trans --> concept_group_representations
  f_induced_class_function_from_subgroup_trans --> concept_normal_subgroups_quotients
  f_induced_class_function_from_subgroup_trans --> groups
  f_divisors__orth_subrepresentation --> concept_group_representations
  f_divisors__orth_subrepresentation --> linear_algebra
  f_divisors__orth_subrepresentation --> groups
  f_divisors__orth_subrepresentation --> modular_arithmetic
  f_alpha_kernel_derivative_vanishes --> f_divisors__orth_subrepresentation
  f_alpha_kernel_derivative_vanishes --> modular_arithmetic
  f_alpha_kernel_derivative_vanishes --> primes_divisibility
  f_alpha_kernel_derivative_vanishes --> infinite_series
  f_exists_formal_germ_open_affine --> f_lift_l_deg_reg
  f_exists_formal_germ_open_affine --> f_regular_pair_lift_to_prime_power_field
  f_exists_formal_germ_open_affine --> f_divisors__orth_subrepresentation
  f_exists_formal_germ_open_affine --> counting
  f_exists_formal_germ_open_affine --> primes_divisibility
  f_lift_all_preserves_degree_and_regularity --> f_exists_formal_germ_open_affine
  f_lift_l_deg_reg --> f_not_mod_eq_of_lt
  f_lift_l_deg_reg --> f_divisors__orth_subrepresentation
  f_lift_l_deg_reg --> counting
  f_lift_l_deg_reg --> primes_divisibility
  f_not_mod_eq_of_lt --> f_divisors__orth_subrepresentation
  f_not_mod_eq_of_lt --> modular_arithmetic
  f_not_mod_eq_of_lt --> primes_divisibility
  f_regular_pair_lift_to_prime_power_field --> f_alpha_kernel_derivative_vanishes
  f_capelli_identities__det_mul_expand --> linear_algebra
  f_capelli_identities__det_mul_expand --> rings_fields
  f_algebraic_independent_of_adjoin --> concept_field_extensions_transcendence
  f_algebraic_independent_of_adjoin --> rings_fields
  f_algebraic_independent_of_adjoin --> counting
  f_geometry_proofs__exists_unit_of_sum_eq_one --> f_capelli_identities__det_mul_expand
  f_geometry_proofs__exists_unit_of_sum_eq_one --> concept_local_rings
  f_geometry_proofs__exists_unit_of_sum_eq_one --> linear_algebra
  f_geometry_proofs__exists_unit_of_sum_eq_one --> rings_fields
  f_contour_shift_gaussian_decay --> complex_analysis
  f_contour_shift_gaussian_decay --> calculus
  f_contour_shift_gaussian_decay --> real_analysis
  f_gauss_tube_of_tube_good --> f_siegel_eisenstein_continuation__strip_entire
  f_gauss_tube_of_tube_good --> complex_analysis
  f_gauss_tube_of_tube_good --> real_analysis
  f_tube_transform_horizontal_invariance --> f_contour_shift_gaussian_decay
  f_tube_transform_horizontal_invariance --> f_gauss_tube_of_tube_good
  f_tube_transform_horizontal_invariance --> f_siegel_eisenstein_continuation__strip_entire
  f_tube_transform_horizontal_invariance --> complex_analysis
  f_tube_transform_vertical_invariance --> f_contour_shift_gaussian_decay
  f_tube_transform_vertical_invariance --> f_gauss_tube_of_tube_good
  f_tube_transform_vertical_invariance --> f_siegel_eisenstein_continuation__strip_entire
  f_tube_transform_vertical_invariance --> complex_analysis
  f_tube_transform_independent_of_base --> f_tube_transform_horizontal_invariance
  f_tube_transform_independent_of_base --> f_tube_transform_vertical_invariance
  f_tube_transform_independent_of_base --> concept_point_set_topology
  f_tube_transform_independent_of_base --> real_analysis
  f_siegel_eisenstein_continuation__strip_entire --> analytic_continuation
  f_siegel_eisenstein_continuation__strip_entire --> complex_analysis
  f_siegel_eisenstein_continuation__strip_entire --> concept_group_representations
  f_siegel_eisenstein_continuation__strip_entire --> concept_point_set_topology
  f_exists_derivations_dual_to_family_of_nilpotent_aug --> concept_derivations_smoothness
  f_exists_derivations_dual_to_family_of_nilpotent_aug --> linear_algebra
  f_exists_derivations_dual_to_family_of_nilpotent_aug --> rings_fields
  f_exists_generators_dual_point_derivations_augmented --> concept_derivations_smoothness
  f_exists_generators_dual_point_derivations_augmented --> concept_finitely_generated_algebras
  f_exists_generators_dual_point_derivations_augmented --> linear_algebra
  f_exists_generators_dual_point_derivations_augmented --> rings_fields
  f_exists_invariant_derivation_of_counital_comul --> concept_tensor_product_of_algebras
  f_exists_invariant_derivation_of_counital_comul --> concept_derivations_smoothness
  f_exists_invariant_derivation_of_counital_comul --> rings_fields
  f_exists_square_presentation_of_tower --> polynomials
  f_exists_square_presentation_of_tower --> concept_finitely_generated_algebras
  f_exists_square_presentation_of_tower --> rings_fields
  f_frobenius_subalgebra_counital_comul --> concept_tensor_product_of_algebras
  f_frobenius_subalgebra_counital_comul --> concept_flat_modules
  f_frobenius_subalgebra_counital_comul --> rings_fields
  f_frobenius_subalgebra_counital_comul --> modular_arithmetic
  f_ker_aeval_truncated_polynomial_presentation --> polynomials
  f_ker_aeval_truncated_polynomial_presentation --> linear_algebra
  f_ker_aeval_truncated_polynomial_presentation --> rings_fields
  f_ker_aeval_truncated_polynomial_presentation --> concept_prime_ideals_localization
  f_square_presentation_of_counital_comul --> f_exists_generators_dual_point_derivations_augmented
  f_square_presentation_of_counital_comul --> f_exists_invariant_derivation_of_counital_comul
  f_square_presentation_of_counital_comul --> f_exists_derivations_dual_to_family_of_nilpotent_aug
  f_square_presentation_of_counital_comul --> f_frobenius_subalgebra_counital_comul
  f_square_presentation_of_counital_comul --> f_truncated_monomials_linear_independent_over_constants
  f_square_presentation_of_counital_comul --> f_ker_aeval_truncated_polynomial_presentation
  f_square_presentation_of_counital_comul --> f_exists_square_presentation_of_tower
  f_square_presentation_of_counital_comul --> concept_derivations_smoothness
  f_square_presentation_of_counital_comul --> proofs
  f_truncated_monomials_linear_independent_over_constants --> concept_derivations_smoothness
  f_truncated_monomials_linear_independent_over_constants --> polynomials
  f_truncated_monomials_linear_independent_over_constants --> linear_algebra
  f_truncated_monomials_linear_independent_over_constants --> modular_arithmetic
  f_localization_closure_equal --> concept_prime_ideals_localization
  f_localization_closure_equal --> concept_integral_closure_fraction_fields
  f_localization_closure_equal --> rings_fields
  f_lu_decomposition_of_minors --> linear_algebra
  f_lu_decomposition_of_minors --> rings_fields
  f_finite_point_extends_section --> concept_schemes_basics
  f_finite_point_extends_section --> concept_integral_closure_fraction_fields
  f_finite_point_extends_section --> concept_categorical_pullbacks
  f_finite_point_extends_section --> rings_fields
  f_regular_at_translate --> concept_schemes_basics
  f_regular_at_translate --> groups
  f_regular_at_translate --> concept_categorical_pullbacks
  f_translate_into_smaller_open --> f_finite_point_extends_section
  f_translate_into_smaller_open --> f_p_adic_hodge__finite_flat
  f_translate_into_smaller_open --> concept_schemes_basics
  f_translate_into_smaller_open --> concept_flat_modules
  f_translate_into_smaller_open --> concept_point_set_topology
  f_translate_into_smaller_open --> groups
  f_bt_order_eq_of_le --> f_translate_into_smaller_open
  f_bt_order_eq_of_le --> f_regular_at_translate
  f_bt_order_eq_of_le --> concept_schemes_basics
  f_bt_order_eq_of_le --> counting
  f_bt_order_eq_of_le --> groups
  f_foundations__alt_coeff_rho --> f_degree_formula__flag_deg_formula
  f_foundations__alt_coeff_rho --> polynomials
  f_foundations__alt_coeff_rho --> counting
  f_foundations__alt_coeff_rho --> linear_algebra
  f_flag_degree_formula --> f_degree_formula__flag_deg_formula
  f_flag_degree_formula --> f_point_degree__pow_sum
  f_flag_degree_formula --> f_point_degree__perm_exp_inj
  f_flag_degree_formula --> polynomials
  f_flag_degree_formula --> linear_algebra
  f_flag_degree_formula --> counting
  f_flag_degree_eq_discriminant_multiple --> f_flag_degree_formula
  f_flag_degree_eq_discriminant_multiple --> polynomials
  f_flag_degree_eq_discriminant_multiple --> counting
  f_divisor_proofs__flag_degree_vandermonde --> f_foundations__alt_coeff_rho
  f_divisor_proofs__flag_degree_vandermonde --> f_degree_formula__flag_deg_formula
  f_divisor_proofs__flag_degree_vandermonde --> polynomials
  f_divisor_proofs__flag_degree_vandermonde --> linear_algebra
  f_divisor_proofs__flag_degree_vandermonde --> counting
  f_coarse_lipschitz_exponential_estimate --> infinite_series
  f_coarse_lipschitz_exponential_estimate --> real_analysis
  f_coarse_lipschitz_exponential_estimate --> complex_analysis
  f_coarse_lipschitz_exponential_estimate --> concept_point_set_topology
  f_coarse_lipschitz_exponential_estimate --> concept_normal_subgroups_quotients
  f_coarse_lipschitz_exponential_estimate --> groups
  f_coset_series_summable_shifted --> infinite_series
  f_coset_series_summable_shifted --> concept_normal_subgroups_quotients
  f_coset_series_summable_shifted --> groups
  f_coset_series_summable_shifted --> real_analysis
  f_holomorphic_series_uniform_tube --> complex_analysis
  f_holomorphic_series_uniform_tube --> infinite_series
  f_holomorphic_series_uniform_tube --> concept_point_set_topology
  f_holomorphic_series_uniform_tube --> real_analysis
  f_section_invariance_coset_sum --> infinite_series
  f_section_invariance_coset_sum --> concept_normal_subgroups_quotients
  f_section_invariance_coset_sum --> groups
  f_section_invariance_coset_sum --> complex_analysis
  f_crossing_of_walls_and_heights --> f_coarse_lipschitz_exponential_estimate
  f_crossing_of_walls_and_heights --> f_coset_series_summable_shifted
  f_crossing_of_walls_and_heights --> f_holomorphic_series_uniform_tube
  f_crossing_of_walls_and_heights --> f_section_invariance_coset_sum
  f_crossing_of_walls_and_heights --> complex_analysis
  f_crossing_of_walls_and_heights --> infinite_series
  f_crossing_of_walls_and_heights --> concept_point_set_topology
  f_crossing_of_walls_and_heights --> groups
  f_expansion_coeff_valuation_ge --> p_adic_numbers
  f_expansion_coeff_valuation_ge --> concept_ultrametric_norm
  f_expansion_coeff_valuation_ge --> polynomials
  f_expansion_coeff_valuation_ge --> linear_algebra
  f_expansion_coeff_valuation_ge --> concept_exterior_powers
  f_minor_prod_span_has_compl --> f_expansion_coeff_valuation_ge
  f_minor_prod_span_has_compl --> polynomials
  f_minor_prod_span_has_compl --> linear_algebra
  f_minor_prod_span_has_compl --> rings_fields
  f_minor_prod_span_has_compl --> concept_exterior_powers
  f_nabla_span_c --> f_expansion_coeff_valuation_ge
  f_nabla_span_c --> f_minor_prod_span_has_compl
  f_nabla_span_c --> p_adic_numbers
  f_nabla_span_c --> polynomials
  f_nabla_span_c --> linear_algebra
  f_step_back --> f_nabla_span_c
  f_step_back --> f_expansion_coeff_valuation_ge
  f_step_back --> concept_ultrametric_norm
  f_step_back --> p_adic_numbers
  f_monomial_frame_span__det_submatrix_fun --> linear_algebra
  f_monomial_frame_span__det_submatrix_fun --> counting
  f_basis_monomials_apply --> f_monomial_frame_span__det_submatrix_fun
  f_basis_monomials_apply --> f_nabla_span_c
  f_basis_monomials_apply --> f_expansion_coeff_valuation_ge
  f_basis_monomials_apply --> polynomials
  f_basis_monomials_apply --> linear_algebra
  f_sat_defs --> f_minor_prod_span_has_compl
  f_sat_defs --> f_nabla_span_c
  f_sat_defs --> polynomials
  f_sat_defs --> linear_algebra
  f_sat_proj --> f_sat_defs
  f_sat_proj --> f_minor_prod_span_has_compl
  f_sat_proj --> f_expansion_coeff_valuation_ge
  f_sat_proj --> polynomials
  f_sat_proj --> linear_algebra
  f_sat_fin --> f_sat_defs
  f_sat_fin --> f_nabla_span_c
  f_sat_fin --> concept_ultrametric_norm
  f_sat_fin --> p_adic_numbers
  f_sat_fin --> polynomials
  f_sat_fin --> linear_algebra
  f_gen_frame_s_b_of --> f_nabla_span_c
  f_gen_frame_s_b_of --> f_expansion_coeff_valuation_ge
  f_gen_frame_s_b_of --> f_minor_prod_span_has_compl
  f_gen_frame_s_b_of_span --> f_gen_frame_s_b_of
  f_gen_frame_s_b_of_span --> f_step_back
  f_gen_frame_s_b_of_span --> f_sat_fin
  f_gen_frame_s_b_of_span --> f_sat_proj
  f_gen_frame_s_b --> f_gen_frame_s_b_of_span
  f_gen_frame_s_b --> f_basis_monomials_apply
  f_gen_frame_s_b --> f_minor_prod_span_has_compl
  f_dominating_pieces_smooth --> f_gen_map_stalk_map
  f_dominating_pieces_smooth --> f_geometry_proofs__germ_gen_pt_injective_range_reg_at
  f_dominating_pieces_smooth --> f_global_geometry__is_cpt_gen
  f_dominating_pieces_smooth --> concept_smooth_morphisms
  f_dominating_pieces_smooth --> concept_schemes_basics
  f_dominating_pieces_smooth --> concept_local_rings
  f_gen_map_stalk_map --> f_geometry_proofs__gen_map_stalk_specializes
  f_gen_map_stalk_map --> f_global_geometry__is_cpt_gen
  f_gen_map_stalk_map --> concept_schemes_basics
  f_gen_map_stalk_map --> concept_local_rings
  f_gen_map_stalk_map --> concept_categorical_pullbacks
  f_geometry_proofs__gen_map_stalk_specializes --> f_global_geometry__is_cpt_gen
  f_geometry_proofs__gen_map_stalk_specializes --> concept_schemes_basics
  f_geometry_proofs__gen_map_stalk_specializes --> concept_local_rings
  f_geometry_proofs__gen_map_stalk_specializes --> concept_prime_ideals_localization
  f_holomorphic_continuation__is_sing_test --> concept_hermitian_unitary_matrices
  f_holomorphic_continuation__is_sing_test --> linear_algebra
  f_holomorphic_continuation__is_sing_test --> fourier_analysis
  f_holomorphic_continuation__is_sing_test --> concept_group_representations
  f_holomorphic_continuation__null_sec --> polynomials
  f_holomorphic_continuation__null_sec --> concept_hermitian_unitary_matrices
  f_holomorphic_continuation__null_sec --> calculus
  f_holomorphic_continuation__null_sec --> complex_numbers
  f_polynomial_derivatives__fock_mono --> f_holomorphic_continuation__null_sec
  f_polynomial_derivatives__fock_mono --> polynomials
  f_polynomial_derivatives__fock_mono --> concept_derivations_smoothness
  f_polynomial_derivatives__fock_mono --> linear_algebra
  f_polynomial_derivatives__core_st --> f_holomorphic_continuation__null_sec
  f_polynomial_derivatives__core_st --> f_polynomial_derivatives__fock_mono
  f_polynomial_derivatives__core_st --> polynomials
  f_polynomial_derivatives__core_st --> linear_algebra
  f_polynomial_derivatives__core_st --> concept_derivations_smoothness
  f_polynomial_derivatives__equiv_lift --> f_polynomial_derivatives__core_st
  f_polynomial_derivatives__equiv_lift --> f_polynomial_derivatives__fock_mono
  f_polynomial_derivatives__equiv_lift --> polynomials
  f_polynomial_derivatives__equiv_lift --> linear_algebra
  f_fform_smul_right --> f_polynomial_derivatives__core_st
  f_fform_smul_right --> f_polynomial_derivatives__fock_mono
  f_fform_smul_right --> polynomials
  f_fform_smul_right --> linear_algebra
  f_monomial_mem_supported --> f_polynomial_derivatives__core_st
  f_monomial_mem_supported --> polynomials
  f_monomial_mem_supported --> linear_algebra
  f_monomial_mem_supported --> counting
  f_adjoin_first_operators_preserves_family --> f_polynomial_derivatives__core_st
  f_adjoin_first_operators_preserves_family --> f_polynomial_derivatives__fock_mono
  f_adjoin_first_operators_preserves_family --> concept_derivations_smoothness
  f_adjoin_first_operators_preserves_family --> polynomials
  f_polynomial_derivatives__null_stable_alt --> f_polynomial_derivatives__fock_mono
  f_polynomial_derivatives__null_stable_alt --> f_holomorphic_continuation__null_sec
  f_polynomial_derivatives__null_stable_alt --> polynomials
  f_polynomial_derivatives__null_stable_alt --> linear_algebra
  f_k_alg_of_adjoin_restrict --> f_polynomial_derivatives__null_stable_alt
  f_k_alg_of_adjoin_restrict --> f_polynomial_derivatives__core_st
  f_k_alg_of_adjoin_restrict --> f_polynomial_derivatives__equiv_lift
  f_k_alg_of_adjoin_restrict --> f_fform_smul_right
  f_k_alg_of_adjoin_restrict --> f_monomial_mem_supported
  f_k_alg_of_adjoin_restrict --> f_adjoin_first_operators_preserves_family
  f_k_alg_of_adjoin_restrict --> f_polynomial_derivatives__fock_mono
  f_k_alg_of_adjoin_restrict --> linear_algebra
  f_metric_periods__in_flag_domain_one --> concept_hermitian_unitary_matrices
  f_metric_periods__in_flag_domain_one --> linear_algebra
  f_metric_periods__in_flag_domain_one --> complex_numbers
  f_metric_proofs__cont_diff_at_frame_entry --> f_metric_periods__in_flag_domain_one
  f_metric_proofs__cont_diff_at_frame_entry --> f_analytic_charts__osgood
  f_metric_proofs__cont_diff_at_frame_entry --> complex_analysis
  f_metric_proofs__cont_diff_at_frame_entry --> calculus
  f_exists_holomorphic_normal_frame --> f_metric_periods__in_flag_domain_one
  f_exists_holomorphic_normal_frame --> concept_hermitian_unitary_matrices
  f_exists_holomorphic_normal_frame --> trigonometry
  f_weighted_polynomial_homogeneous_coeff_bound --> f_projective_line_normal_frame
  f_weighted_polynomial_homogeneous_coeff_bound --> concept_hermitian_unitary_matrices
  f_weighted_polynomial_homogeneous_coeff_bound --> complex_analysis
  f_projective_line_normal_frame --> f_triple_deriv
  f_projective_line_normal_frame --> concept_hermitian_unitary_matrices
  f_projective_line_normal_frame --> linear_algebra
  f_projective_line_normal_frame --> calculus
  f_projective_line_normal_frame --> complex_analysis
  f_triple_deriv --> calculus
  f_triple_deriv --> linear_algebra
  f_triple_deriv --> complex_numbers
  f_local_unitary_normal_frame2x2 --> f_weighted_polynomial_homogeneous_coeff_bound
  f_local_unitary_normal_frame2x2 --> f_exists_holomorphic_normal_frame
  f_local_unitary_normal_frame2x2 --> f_metric_proofs__cont_diff_at_frame_entry
  f_local_unitary_normal_frame2x2 --> concept_hermitian_unitary_matrices
  f_local_unitary_normal_frame2x2 --> calculus
  f_analytic_charts__osgood --> f_analytic_charts__osgood_a
  f_analytic_charts__osgood --> complex_analysis
  f_analytic_charts__osgood --> calculus
  f_analytic_charts__osgood_a --> complex_analysis
  f_analytic_charts__osgood_a --> calculus
  f_analytic_charts__osgood_a --> complex_numbers
  f_formalism__statement_o_c --> rh_statement
  f_formalism__statement_o_c --> dirichlet_l_function
  f_formalism__statement_o_c --> dirichlet_characters
  f_formalism__statement_o_c --> primes_divisibility
  f_formalism__statement_o_c --> zeta_series
  f_formalism__statement --> rh_statement
  f_formalism__statement --> dirichlet_l_function
  f_formalism__statement --> dirichlet_characters
  f_formalism__statement --> zeta_series
  f_zero_free_region__statement --> f_formalism__statement_o_c
  f_zero_free_region__statement --> rh_statement
  f_zero_free_region__statement --> zeta_series
  f_zero_free_region__statement --> complex_analysis
  f_zero_free_region__small_height_log_deriv --> f_zero_free_region__statement
  f_zero_free_region__small_height_log_deriv --> f_formalism__statement_o_c
  f_zero_free_region__small_height_log_deriv --> zeta_series
  f_zero_free_region__small_height_log_deriv --> complex_analysis
  f_zero_free_region__small_height_log_deriv --> analytic_continuation
  f_norm_log_deriv_le_lam_f --> zeta_series
  f_norm_log_deriv_le_lam_f --> infinite_series
  f_norm_log_deriv_le_lam_f --> complex_powers
  f_norm_log_deriv_le_lam_f --> primes_divisibility
  f_log_deriv_right --> f_norm_log_deriv_le_lam_f
  f_log_deriv_right --> f_zero_free_region__small_height_log_deriv
  f_log_deriv_right --> zeta_series
  f_log_deriv_right --> analytic_continuation
  f_log_deriv_right --> complex_analysis
  f_zeta_inv_bound --> f_zero_free_region__small_height_log_deriv
  f_zeta_inv_bound --> zeta_series
  f_zeta_inv_bound --> infinite_series
  f_zeta_inv_bound --> primes_divisibility
  f_zeta_inv_bound --> complex_powers
  f_landau_zero_free_bounds__statement --> dirichlet_l_function
  f_landau_zero_free_bounds__statement --> dirichlet_characters
  f_landau_zero_free_bounds__statement --> primitive_characters
  f_landau_zero_free_bounds__statement --> zeta_series
  f_landau_zero_free_bounds__no_zero_complex_of --> f_landau_zero_free_bounds__statement
  f_landau_zero_free_bounds__no_zero_complex_of --> f_zero_free_region__statement
  f_landau_zero_free_bounds__no_zero_complex_of --> dirichlet_l_function
  f_landau_zero_free_bounds__no_zero_complex_of --> dirichlet_characters
  f_landau_zero_free_bounds__no_zero_complex_of --> functional_equation_dirichlet
  f_l_right --> f_landau_zero_free_bounds__no_zero_complex_of
  f_l_right --> f_zeta_inv_bound
  f_l_right --> f_norm_log_deriv_le_lam_f
  f_l_right --> f_log_deriv_right
  f_l_right --> dirichlet_l_function
  f_l_right --> dirichlet_characters
  f_l_right --> infinite_series
  f_l_right --> primes_divisibility
  f_divisor_proofs__exists_mul_mem_integral_closure_over_generic_fibre --> concept_integral_closure_fraction_fields
  f_divisor_proofs__exists_mul_mem_integral_closure_over_generic_fibre --> concept_prime_ideals_localization
  f_divisor_proofs__exists_mul_mem_integral_closure_over_generic_fibre --> rings_fields
  f_injective_trace_galois_data --> concept_galois_fixed_fields
  f_injective_trace_galois_data --> concept_group_actions
  f_injective_trace_galois_data --> concept_flat_modules
  f_injective_trace_galois_data --> concept_tensor_product_of_algebras
  f_integral_closure_over_generic_fibre_hartogs --> concept_integral_closure_fraction_fields
  f_integral_closure_over_generic_fibre_hartogs --> concept_prime_ideals_localization
  f_integral_closure_over_generic_fibre_hartogs --> concept_dedekind_domains
  f_integral_closure_over_generic_fibre_hartogs --> concept_noetherian_and_irreducible_components
  f_integral_closure_zmod_torsor_generic_fibre_data --> f_divisor_proofs__exists_mul_mem_integral_closure_over_generic_fibre
  f_integral_closure_zmod_torsor_generic_fibre_data --> f_injective_trace_galois_data
  f_integral_closure_zmod_torsor_generic_fibre_data --> f_integral_closure_over_generic_fibre_hartogs
  f_integral_closure_zmod_torsor_generic_fibre_data --> f_divisor_proofs__torsion_free_over
  f_integral_closure_zmod_torsor_generic_fibre_data --> concept_integral_closure_fraction_fields
  f_integral_closure_zmod_torsor_generic_fibre_data --> concept_flat_modules
  f_integral_closure_zmod_torsor_generic_fibre_data --> concept_galois_fixed_fields
  f_divisor_proofs__loc_hom_algebra_map --> concept_integral_closure_fraction_fields
  f_divisor_proofs__loc_hom_algebra_map --> concept_tensor_product_of_algebras
  f_divisor_proofs__loc_hom_algebra_map --> concept_prime_ideals_localization
  f_algebra_map_integral_closure_tensor_eq --> f_divisor_proofs__loc_hom_algebra_map
  f_algebra_map_integral_closure_tensor_eq --> concept_integral_closure_fraction_fields
  f_algebra_map_integral_closure_tensor_eq --> concept_tensor_product_of_algebras
  f_etale_adjoin_root_x_pow_sub_c --> concept_etale_ring_maps
  f_etale_adjoin_root_x_pow_sub_c --> concept_separable_polynomials
  f_etale_adjoin_root_x_pow_sub_c --> polynomials
  f_etale_adjoin_root_x_pow_sub_c --> concept_roots_of_unity_kummer
  f_finite_integral_closure_of_formally_unramified --> f_etale_adjoin_root_x_pow_sub_c
  f_finite_integral_closure_of_formally_unramified --> concept_etale_ring_maps
  f_finite_integral_closure_of_formally_unramified --> concept_integral_closure_fraction_fields
  f_finite_integral_closure_of_formally_unramified --> concept_tensor_product_of_algebras
  f_finite_integral_closure_of_formally_unramified --> concept_discrete_valuation_ring
  f_finite_integral_closure_of_formally_unramified --> concept_separable_polynomials
  f_finite_integral_closure_of_formally_unramified --> linear_algebra
  f_kummer_uniformiser_adjoin_root_tensor_is_reduced --> concept_discrete_valuation_ring
  f_kummer_uniformiser_adjoin_root_tensor_is_reduced --> concept_roots_of_unity_kummer
  f_kummer_uniformiser_adjoin_root_tensor_is_reduced --> concept_separable_polynomials
  f_kummer_uniformiser_adjoin_root_tensor_is_reduced --> concept_tensor_product_of_algebras
  f_kummer_uniformiser_adjoin_root_tensor_is_reduced --> polynomials
  f_localization_integral_closure_artinian_reduced_domain --> concept_integral_closure_fraction_fields
  f_localization_integral_closure_artinian_reduced_domain --> concept_prime_ideals_localization
  f_localization_integral_closure_artinian_reduced_domain --> concept_local_rings
  f_localization_integral_closure_artinian_reduced_domain --> concept_coordinate_rings_dimension
  f_normalisation_dvr_tensor_separable_finite --> f_finite_integral_closure_of_formally_unramified
  f_normalisation_dvr_tensor_separable_finite --> concept_discrete_valuation_ring
  f_normalisation_dvr_tensor_separable_finite --> concept_flat_modules
  f_normalisation_dvr_tensor_separable_finite --> concept_tensor_product_of_algebras
  f_normalisation_dvr_tensor_separable_finite --> concept_integral_closure_fraction_fields
  f_localization_normalization_root_adjoin_is_d_v_r --> f_normalisation_dvr_tensor_separable_finite
  f_localization_normalization_root_adjoin_is_d_v_r --> f_kummer_uniformiser_adjoin_root_tensor_is_reduced
  f_localization_normalization_root_adjoin_is_d_v_r --> f_localization_integral_closure_artinian_reduced_domain
  f_localization_normalization_root_adjoin_is_d_v_r --> concept_discrete_valuation_ring
  f_localization_normalization_root_adjoin_is_d_v_r --> concept_flat_modules
  f_localization_normalization_root_adjoin_is_d_v_r --> concept_local_rings
  f_localization_normalization_root_adjoin_is_d_v_r --> concept_prime_ideals_localization
  f_period_integrals__zeros_window --> dirichlet_l_function
  f_period_integrals__zeros_window --> primitive_characters
  f_period_integrals__zeros_window --> dirichlet_characters
  f_period_integrals__zeros_window --> rh_statement
  f_period_integrals__zeros_window --> complex_analysis
  f_period_integrals__zeros_window_in --> dirichlet_l_function
  f_period_integrals__zeros_window_in --> zeta_series
  f_period_integrals__zeros_window_in --> analytic_continuation
  f_period_integrals__zeros_window_in --> dirichlet_characters
  f_right_half_with --> f_period_integrals__zeros_window
  f_right_half_with --> f_period_integrals__zeros_window_in
  f_right_half_with --> dirichlet_l_function
  f_right_half_with --> complex_analysis
  f_right_half_with --> primitive_characters
  f_jensen --> f_right_half_with
  f_jensen --> complex_analysis
  f_jensen --> real_analysis
  f_jensen --> calculus
  f_right_chi --> f_right_half_with
  f_right_chi --> f_period_integrals__zeros_window_in
  f_right_chi --> dirichlet_l_function
  f_right_chi --> complex_analysis
  f_right_chi --> real_analysis
  f_right_one --> f_right_half_with
  f_right_one --> f_period_integrals__zeros_window_in
  f_right_one --> zeta_series
  f_right_one --> analytic_continuation
  f_right_one --> complex_analysis
  f_zero_window__transfer --> f_right_half_with
  f_zero_window__transfer --> functional_equation_dirichlet
  f_zero_window__transfer --> primitive_characters
  f_zero_window__transfer --> factors_nonzero
  f_zero_window__transfer --> gamma_function
  f_zero_window__transfer --> complex_powers
  f_zero_window__transfer --> complex_analysis
  f_finsum_mem_le_finsum_mem --> f_right_half_with
  f_finsum_mem_le_finsum_mem --> f_period_integrals__zeros_window
  f_finsum_mem_le_finsum_mem --> primitive_characters
  f_finsum_mem_le_finsum_mem --> dirichlet_l_function
  f_finsum_mem_le_finsum_mem --> counting
  f_zero_window__assemble --> f_right_chi
  f_zero_window__assemble --> f_right_one
  f_zero_window__assemble --> f_jensen
  f_zero_window__assemble --> f_finsum_mem_le_finsum_mem
  f_zero_window__assemble --> f_right_half_with
  f_zero_window__assemble --> f_period_integrals__zeros_window
  f_zero_window__assemble --> f_period_integrals__zeros_window_in
  f_orbital_bounds_conclusion__zeros_window --> f_zero_window__assemble
  f_orbital_bounds_conclusion__zeros_window --> f_zero_window__transfer
  f_orbital_bounds_conclusion__zeros_window --> f_period_integrals__zeros_window
  f_orbital_bounds_conclusion__zeros_window --> f_period_integrals__zeros_window_in
  f_is_h_t_form_over --> f_global_geometry__lie_model
  f_is_h_t_form_over --> concept_schemes_basics
  f_is_h_t_form_over --> linear_algebra
  f_is_h_t_form_over --> concept_categorical_pullbacks
  f_geometry_proofs__std_smooth_mv_polynomial --> f_global_geometry__lie_model
  f_geometry_proofs__std_smooth_mv_polynomial --> concept_smooth_morphisms
  f_geometry_proofs__std_smooth_mv_polynomial --> concept_derivations_smoothness
  f_geometry_proofs__std_smooth_mv_polynomial --> concept_schemes_basics
  f_geometry_proofs__std_smooth_mv_polynomial --> concept_categorical_pullbacks
  f_geometry_proofs__std_smooth_mv_polynomial --> polynomials
  f_ga_is_h_t_form_over --> f_is_h_t_form_over
  f_ga_is_h_t_form_over --> f_geometry_proofs__std_smooth_mv_polynomial
  f_ga_is_h_t_form_over --> f_global_geometry__lie_model
  f_ga_is_h_t_form_over --> concept_schemes_basics
  f_ga_is_h_t_form_over --> concept_local_rings
  f_localization_closure_smooth --> concept_smooth_morphisms
  f_localization_closure_smooth --> concept_field_extensions_transcendence
  f_localization_closure_smooth --> concept_prime_ideals_localization
  f_localization_closure_smooth --> concept_finitely_generated_algebras
  f_localization_closure_smooth --> polynomials
  f_localization_closure_smooth --> rings_fields
  f_induced_one_sub_index_mem_degree_one_character_diff --> f_galois_cohomology₂__brauer_degree_zero
  f_induced_one_sub_index_mem_degree_one_character_diff --> f_inertia_eigenvalues__ind_apply_one
  f_induced_one_sub_index_mem_degree_one_character_diff --> f_ab_by_p_of_comm
  f_induced_one_sub_index_mem_degree_one_character_diff --> concept_group_representations
  f_induced_one_sub_index_mem_degree_one_character_diff --> concept_normal_subgroups_quotients
  f_induced_one_sub_index_mem_degree_one_character_diff --> groups
  f_lattice_generator_invert_constant --> f_line_lattice_spread
  f_lattice_generator_invert_constant --> f_global_geometry__is_cpt_gen
  f_lattice_generator_invert_constant --> concept_schemes_basics
  f_geometry_proofs__stalk_closed_point_to_germ_top --> f_geometry_proofs__zmod_torsor_base_change_transport_point
  f_geometry_proofs__stalk_closed_point_to_germ_top --> f_global_geometry__is_cpt_gen
  f_geometry_proofs__stalk_closed_point_to_germ_top --> concept_schemes_basics
  f_geometry_proofs__stalk_closed_point_to_germ_top --> concept_local_rings
  f_geometry_proofs__stalk_closed_point_to_germ_top --> concept_prime_ideals_localization
  f_geometry_proofs__zmod_torsor_base_change_transport_point --> f_global_geometry__is_cpt_gen
  f_geometry_proofs__zmod_torsor_base_change_transport_point --> concept_local_rings
  f_geometry_proofs__zmod_torsor_base_change_transport_point --> rings_fields
  f_line_lattice_spread --> f_geometry_proofs__stalk_closed_point_to_germ_top
  f_line_lattice_spread --> f_geometry_proofs__zmod_torsor_base_change_transport_point
  f_line_lattice_spread --> f_global_geometry__is_cpt_gen
  f_line_lattice_spread --> f_global_geometry__is_line_gen_on
  f_line_lattice_spread --> concept_noetherian_and_irreducible_components
  f_line_lattice_spread --> concept_schemes_basics
  f_line_lattice_spread --> concept_point_set_topology
  f_line_lattice_spread --> concept_prime_ideals_localization
  f_gaussian_polynomial_density --> f_schwartz_tendsto_of_pointwise_uniform_bounds
  f_gaussian_polynomial_density --> f_schwartz_taylor_series_converges
  f_gaussian_polynomial_density --> f_schwartz_taylor_partial_sum_deriv_bound
  f_gaussian_polynomial_density --> f_gaussian_quadratic_form_schwartz_bounds
  f_gaussian_polynomial_density --> concept_schwartz_functions
  f_gaussian_polynomial_density --> concept_point_set_topology
  f_gaussian_polynomial_density --> infinite_series
  f_gaussian_quadratic_form_schwartz_bounds --> f_norm_iterated_f_deriv_trunc_exp_i_comp_le
  f_gaussian_quadratic_form_schwartz_bounds --> f_divisor_proofs__poly_mul_gaussian_bounded
  f_gaussian_quadratic_form_schwartz_bounds --> concept_schwartz_functions
  f_gaussian_quadratic_form_schwartz_bounds --> calculus
  f_norm_iterated_f_deriv_trunc_exp_i_comp_le --> f_divisor_proofs__poly_mul_gaussian_bounded
  f_norm_iterated_f_deriv_trunc_exp_i_comp_le --> calculus
  f_norm_iterated_f_deriv_trunc_exp_i_comp_le --> real_analysis
  f_divisor_proofs__schwartz_continuous_at_of_pointwise_of_bounded --> concept_schwartz_functions
  f_divisor_proofs__schwartz_continuous_at_of_pointwise_of_bounded --> concept_point_set_topology
  f_divisor_proofs__schwartz_continuous_at_of_pointwise_of_bounded --> real_analysis
  f_divisor_proofs__schwartz_continuous_at_of_pointwise_of_bounded --> calculus
  f_schwartz_taylor_partial_sum_deriv_bound --> concept_schwartz_functions
  f_schwartz_taylor_partial_sum_deriv_bound --> calculus
  f_schwartz_taylor_partial_sum_deriv_bound --> infinite_series
  f_schwartz_taylor_partial_sum_deriv_bound --> counting
  f_schwartz_taylor_series_converges --> concept_schwartz_functions
  f_schwartz_taylor_series_converges --> calculus
  f_schwartz_taylor_series_converges --> infinite_series
  f_schwartz_tendsto_of_pointwise_uniform_bounds --> f_divisor_proofs__schwartz_continuous_at_of_pointwise_of_bounded
  f_schwartz_tendsto_of_pointwise_uniform_bounds --> concept_schwartz_functions
  f_schwartz_tendsto_of_pointwise_uniform_bounds --> concept_point_set_topology
  f_aeval_sum_elim_eq_zero_of_mem_pts --> f_eq_zero_of_contractions
  f_aeval_sum_elim_eq_zero_of_mem_pts --> f_rat_component_mem_rat_polys_vanishing_on_matrix_set
  f_aeval_sum_elim_eq_zero_of_mem_pts --> f_adelic_hermitian_forms__adelic_pair
  f_aeval_sum_elim_eq_zero_of_mem_pts --> concept_tensor_product_of_algebras
  f_aeval_sum_elim_eq_zero_of_mem_pts --> polynomials
  f_aeval_sum_elim_eq_zero_of_mem_pts --> linear_algebra
  f_eq_zero_of_contractions --> linear_algebra
  f_eq_zero_of_contractions --> concept_tensor_product_of_algebras
  f_rat_component_mem_rat_polys_vanishing_on_matrix_set --> f_adelic_lattice_proofs__mem_span_rat_polys_vanishing_of_aut_stable
  f_rat_component_mem_rat_polys_vanishing_on_matrix_set --> f_adelic_hermitian_forms__adelic_pair
  f_rat_component_mem_rat_polys_vanishing_on_matrix_set --> polynomials
  f_rat_component_mem_rat_polys_vanishing_on_matrix_set --> linear_algebra
  f_rat_component_mem_rat_polys_vanishing_on_matrix_set --> concept_galois_fixed_fields
  f_fourier_modulated_schwartz_bounds --> concept_schwartz_functions
  f_fourier_modulated_schwartz_bounds --> calculus
  f_fourier_modulated_schwartz_bounds --> complex_numbers
  f_fourier_modulated_schwartz_bounds --> trigonometry
  f_iterated_f_deriv_weighted_integral --> concept_schwartz_functions
  f_iterated_f_deriv_weighted_integral --> calculus
  f_iterated_f_deriv_weighted_integral --> real_analysis
  f_schwartz_family_pairing_integral_commute --> concept_schwartz_functions
  f_schwartz_family_pairing_integral_commute --> real_analysis
  f_schwartz_family_pairing_integral_commute --> linear_algebra
  f_schwartz_fourier_superposition --> fourier_analysis
  f_schwartz_fourier_superposition --> concept_schwartz_functions
  f_schwartz_fourier_superposition --> complex_numbers
  f_tempered_functional_vanish_mul --> f_fourier_modulated_schwartz_bounds
  f_tempered_functional_vanish_mul --> f_iterated_f_deriv_weighted_integral
  f_tempered_functional_vanish_mul --> f_schwartz_family_pairing_integral_commute
  f_tempered_functional_vanish_mul --> f_schwartz_fourier_superposition
  f_tempered_functional_vanish_mul --> f_divisor_proofs__schwartz_continuous_at_of_pointwise_of_bounded
  f_tempered_functional_vanish_mul --> concept_schwartz_functions
  f_tempered_functional_vanish_mul --> fourier_analysis
  f_exists_rat_idempotent_block_diag_part_kills_span --> f_invariant_subspace_not_semisimple
  f_exists_rat_idempotent_block_diag_part_kills_span --> f_exists_rat_idempotent_of_aut_stable_subspace
  f_exists_rat_idempotent_block_diag_part_kills_span --> f_adelic_hermitian_forms__adelic_pair
  f_exists_rat_idempotent_block_diag_part_kills_span --> concept_semisimple_algebras_radical
  f_exists_rat_idempotent_block_diag_part_kills_span --> linear_algebra
  f_exists_rat_idempotent_of_aut_stable_subspace --> f_adelic_lattice_proofs__galois_stable_submodule_le_span_rational
  f_exists_rat_idempotent_of_aut_stable_subspace --> concept_galois_fixed_fields
  f_exists_rat_idempotent_of_aut_stable_subspace --> linear_algebra
  f_invariant_subspace_not_semisimple --> concept_semisimple_algebras_radical
  f_invariant_subspace_not_semisimple --> f_adelic_hermitian_forms__adelic_pair
  f_invariant_subspace_not_semisimple --> linear_algebra
  f_invariant_subspace_not_semisimple --> rings_fields
  f_invariant_subspace_not_semisimple --> concept_galois_fixed_fields
  f_normalized_minor_extends --> f_capelli_identities__det_mul_expand
  f_normalized_minor_extends --> f_geometry_proofs__exists_unit_of_sum_eq_one
  f_normalized_minor_extends --> concept_local_rings
  f_normalized_minor_extends --> linear_algebra
  f_period_integrals__weil_quot_meas --> concept_haar_measure_fundamental_domain
  f_period_integrals__weil_quot_meas --> concept_normal_subgroups_quotients
  f_period_integrals__weil_quot_meas --> concept_point_set_topology
  f_weil_quotient_measure__step_bruhat --> concept_haar_measure_fundamental_domain
  f_weil_quotient_measure__step_bruhat --> concept_point_set_topology
  f_weil_quotient_measure__lintegral_mul_avg_comm --> f_period_integrals__weil_quot_meas
  f_weil_quotient_measure__lintegral_mul_avg_comm --> f_weil_quotient_measure__step_bruhat
  f_weil_quotient_measure__lintegral_mul_avg_comm --> concept_haar_measure_fundamental_domain
  f_weil_quotient_measure__lintegral_mul_avg_comm --> concept_normal_subgroups_quotients
  f_weil_quotient_measure__bruhat --> f_weil_quotient_measure__step_bruhat
  f_weil_quotient_measure__bruhat --> f_weil_quotient_measure__lintegral_mul_avg_comm
  f_weil_quotient_measure__bruhat --> concept_point_set_topology
  f_weil_quotient_measure__bruhat --> concept_haar_measure_fundamental_domain
  f_closed_subgroup_quotient_measure --> f_weil_quotient_measure__bruhat
  f_closed_subgroup_quotient_measure --> concept_haar_measure_fundamental_domain
  f_closed_subgroup_quotient_measure --> concept_point_set_topology
  f_finite_covolume_unimodular --> concept_haar_measure_fundamental_domain
  f_finite_covolume_unimodular --> concept_group_actions
  f_quotient_measure_tower --> f_closed_subgroup_quotient_measure
  f_quotient_measure_tower --> f_finite_covolume_unimodular
  f_quotient_measure_tower --> concept_haar_measure_fundamental_domain
  f_quotient_measure_tower --> concept_lattice_point_counting
  f_modular_character_trivial_finite_covolume --> f_finite_covolume_unimodular
  f_modular_character_trivial_finite_covolume --> f_quotient_measure_tower
  f_modular_character_trivial_finite_covolume --> concept_haar_measure_fundamental_domain
  f_l2_dbar_estimates__is_local_homeomorph --> complex_analysis
  f_l2_dbar_estimates__is_local_homeomorph --> concept_point_set_topology
  f_l2_dbar_estimates__is_local_homeomorph --> calculus
  f_holo_section_statement --> f_l2_dbar_estimates__is_local_homeomorph
  f_holo_section_statement --> complex_analysis
  f_holo_section_statement --> polynomials
  f_esymm_zero --> f_holo_section_statement
  f_esymm_zero --> polynomials
  f_line_finite --> f_holo_section_statement
  f_line_finite --> polynomials
  f_removable_finset --> f_holo_section_statement
  f_removable_finset --> complex_analysis
  f_symmetric_sections__section --> f_holo_section_statement
  f_symmetric_sections__section --> f_l2_dbar_estimates__is_local_homeomorph
  f_symmetric_sections__section --> complex_analysis
  f_sheets --> f_holo_section_statement
  f_sheets --> concept_point_set_topology
  f_symm_diff --> f_sheets
  f_symm_diff --> f_holo_section_statement
  f_symm_diff --> complex_analysis
  f_symm_growth --> f_holo_section_statement
  f_symm_growth --> counting
  f_symm_vanish --> f_sheets
  f_symm_vanish --> f_holo_section_statement
  f_symm_vanish --> real_analysis
  f_norm_vanish_of_parts --> f_holo_section_statement
  f_norm_vanish_of_holo_section --> f_norm_vanish_of_parts
  f_norm_vanish_of_holo_section --> f_symmetric_sections__section
  f_norm_vanish_of_holo_section --> f_symm_diff
  f_norm_vanish_of_holo_section --> f_symm_vanish
  f_norm_vanish_of_holo_section --> f_symm_growth
  f_norm_vanish_of_holo_section --> f_line_finite
  f_norm_vanish_of_holo_section --> f_esymm_zero
  f_norm_vanish_of_holo_section --> f_removable_finset
  f_norm_vanish_of_holo_section --> f_holo_section_statement
  f_jets__sum_io_pr --> concept_group_representations
  f_jets__sum_io_pr --> concept_hermitian_unitary_matrices
  f_jets__sum_io_pr --> linear_algebra
  f_jets__sum_io_pr --> f_real_place_analysis__statement_a
  f_real_place_analysis__statement_k_t --> f_real_place_analysis__statement_a
  f_real_place_analysis__statement_k_t --> concept_group_representations
  f_real_place_analysis__statement_k_t --> concept_hermitian_unitary_matrices
  f_formal_degree_bessel__statement_d_s --> f_real_place_analysis__statement_a
  f_formal_degree_bessel__statement_d_s --> f_real_place_analysis__statement_b
  f_formal_degree_bessel__statement_d_s --> f_real_place_analysis__statement_e
  f_formal_degree_bessel__statement_d_s --> polynomials
  f_wt_near_orth_decomp --> f_jets__sum_io_pr
  f_wt_near_orth_decomp --> f_real_place_analysis__statement_k_t
  f_wt_near_orth_decomp --> concept_hermitian_unitary_matrices
  f_wt_near_orth_decomp --> linear_algebra
  f_weight_near_diagonal_operators_bounds --> f_wt_near_orth_decomp
  f_weight_near_diagonal_operators_bounds --> f_jets__sum_io_pr
  f_weight_near_diagonal_operators_bounds --> concept_hermitian_unitary_matrices
  f_weight_near_diagonal_operators_bounds --> linear_algebra
  f_spec_hom_ext_of_localization_away_span_eq_top --> concept_schemes_basics
  f_spec_hom_ext_of_localization_away_span_eq_top --> concept_prime_ideals_localization
  f_is_affine_combination_in_chart_unique --> f_divisor_proofs__is_comb_in
  f_is_affine_combination_in_chart_unique --> concept_schemes_basics
  f_is_affine_combination_in_chart_unique --> concept_categorical_pullbacks
  f_is_affine_combination_independent_of_chart --> f_is_affine_combination_in_chart_unique
  f_is_affine_combination_independent_of_chart --> f_divisor_proofs__is_comb_in
  f_is_affine_combination_independent_of_chart --> f_divisor_proofs__is_affine_combination_in_chart_spec_map_comp
  f_is_affine_combination_independent_of_chart --> f_divisor_proofs__preimage_eq_of_square_zero_thickening
  f_is_affine_combination_independent_of_chart --> concept_dual_numbers
  f_is_affine_combination_independent_of_chart --> concept_prime_ideals_localization
  f_is_affine_combination_independent_of_chart --> concept_schemes_basics
  f_exists_affine_combination_square_zero_lifts_chart --> f_divisor_proofs__is_comb_in
  f_exists_affine_combination_square_zero_lifts_chart --> f_divisor_proofs__preimage_eq_of_square_zero_thickening
  f_exists_affine_combination_square_zero_lifts_chart --> concept_dual_numbers
  f_exists_affine_combination_square_zero_lifts_chart --> concept_schemes_basics
  f_exists_affine_combination_square_zero_lifts_chart --> concept_categorical_pullbacks
  f_exists_lifts_agree_of_cocycle --> f_exists_affine_combination_square_zero_lifts_chart
  f_exists_lifts_agree_of_cocycle --> f_is_affine_combination_independent_of_chart
  f_exists_lifts_agree_of_cocycle --> f_is_affine_combination_in_chart_unique
  f_exists_lifts_agree_of_cocycle --> f_spec_hom_ext_of_localization_away_span_eq_top
  f_exists_lifts_agree_of_cocycle --> f_divisor_proofs__is_comb_in
  f_exists_lifts_agree_of_cocycle --> f_divisor_proofs__lift_at
  f_exists_lifts_agree_of_cocycle --> f_divisor_proofs__is_affine_combination_in_chart_spec_map_comp
  f_exists_lifts_agree_of_cocycle --> concept_dual_numbers
  f_exists_lifts_agree_of_cocycle --> concept_prime_ideals_localization
  f_exists_lifts_agree_of_cocycle --> concept_schemes_basics
  f_orbital_bounds_conclusion__sqf_root_shift --> f_period_integrals__sqf_root_shift
  f_orbital_bounds_conclusion__sqf_root_shift --> f_squarefree_root_shift__development
  f_orbital_bounds_conclusion__sqf_root_shift --> f_count_d
  f_orbital_bounds_conclusion__sqf_root_shift --> f_arith_p
  f_orbital_bounds_conclusion__sqf_root_shift --> counting
  f_period_integrals__sqf_root_shift --> f_period_integrals__sqf_lab
  f_period_integrals__sqf_root_shift --> polynomials
  f_period_integrals__sqf_root_shift --> modular_arithmetic
  f_period_integrals__sqf_root_shift --> primes_divisibility
  f_period_integrals__sqf_root_shift --> counting
  f_arith_p --> f_squarefree_root_shift__development
  f_arith_p --> f_sum_le_prod_of_two_le
  f_arith_p --> infinite_series
  f_arith_p --> primes_divisibility
  f_arith_p --> modular_arithmetic
  f_count_a --> f_period_integrals__sqf_lab
  f_count_a --> f_squarefree_root_shift__development
  f_count_a --> polynomials
  f_count_a --> primes_divisibility
  f_count_a --> modular_arithmetic
  f_count_a --> groups
  f_count_b --> f_period_integrals__sqf_lab
  f_count_b --> algebraic_closure
  f_count_b --> polynomials
  f_count_b --> rings_fields
  f_count_b --> modular_arithmetic
  f_count_b --> concept_frobenius_perfect_rings
  f_count_c --> f_count_a
  f_count_c --> f_count_b
  f_count_c --> f_period_integrals__sqf_lab
  f_count_c --> f_squarefree_root_shift__development
  f_count_c --> concept_separable_polynomials
  f_count_c --> counting
  f_count_c --> polynomials
  f_count_d --> f_count_a
  f_count_d --> f_count_b
  f_count_d --> f_count_c
  f_count_d --> f_period_integrals__sqf_lab
  f_count_d --> f_squarefree_root_shift__development
  f_count_d --> polynomials
  f_count_d --> counting
  f_squarefree_root_shift__development --> f_period_integrals__sqf_root_shift
  f_squarefree_root_shift__development --> f_period_integrals__sqf_lab
  f_squarefree_root_shift__development --> primes_divisibility
  f_squarefree_root_shift__development --> counting
  f_sum_le_prod_of_two_le --> f_squarefree_root_shift__development
  f_sum_le_prod_of_two_le --> primes_divisibility
  f_sum_le_prod_of_two_le --> modular_arithmetic
  f_sum_le_prod_of_two_le --> p_adic_numbers
  f_sum_le_prod_of_two_le --> counting
  f_in_p_apply_eq_zero --> linear_algebra
  f_in_p_apply_eq_zero --> concept_hermitian_unitary_matrices
  f_in_p_apply_eq_zero --> complex_numbers
  f_closure_k --> f_bochner_inequality__layer_basic
  f_closure_k --> f_iterated_deriv_orbit
  f_closure_k --> f_analytic_vectors__taylor
  f_closure_k --> f_conj_transpose_eq_of_in_g
  f_closure_k --> f_discrete_series__defs_rep
  f_closure_k --> f_discrete_series__is_inf_unitary
  f_closure_k --> concept_hermitian_unitary_matrices
  f_closure_k --> linear_algebra
  f_closure_k --> infinite_series
  f_conj_transpose_eq_of_in_g --> f_discrete_series__defs_rep
  f_conj_transpose_eq_of_in_g --> f_in_p_apply_eq_zero
  f_conj_transpose_eq_of_in_g --> concept_hermitian_unitary_matrices
  f_conj_transpose_eq_of_in_g --> linear_algebra
  f_iterated_deriv_orbit --> f_discrete_series__defs_rep
  f_iterated_deriv_orbit --> f_conj_transpose_eq_of_in_g
  f_iterated_deriv_orbit --> concept_group_representations
  f_iterated_deriv_orbit --> calculus
  f_analytic_vectors__taylor --> f_iterated_deriv_orbit
  f_analytic_vectors__taylor --> f_discrete_series__defs_rep
  f_analytic_vectors__taylor --> calculus
  f_analytic_vectors__taylor --> infinite_series
  f_analytic_vectors__taylor --> real_analysis
  f_bochner_inequality__cas_val_k --> f_discrete_series__is_inf_unitary
  f_bochner_inequality__cas_val_k --> linear_algebra
  f_bochner_inequality__cas_val_k --> concept_group_representations
  f_bochner_inequality__layer_basic --> f_bochner_inequality__cas_val_k
  f_bochner_inequality__layer_basic --> f_discrete_series__is_inf_unitary
  f_bochner_inequality__layer_basic --> f_casimir_algebra__mul_mul_sub_mul_mul_eq_add
  f_bochner_inequality__layer_basic --> linear_algebra
  f_casimir_algebra__mul_mul_sub_mul_mul_eq_add --> f_discrete_series__is_inf_unitary
  f_casimir_algebra__mul_mul_sub_mul_mul_eq_add --> linear_algebra
  f_casimir_algebra__mul_mul_sub_mul_mul_eq_add --> rings_fields
  f_discrete_series__defs_rep --> concept_hermitian_unitary_matrices
  f_discrete_series__defs_rep --> concept_group_representations
  f_discrete_series__defs_rep --> linear_algebra
  f_discrete_series__defs_rep --> groups
  f_discrete_series__is_inf_unitary --> concept_group_representations
  f_discrete_series__is_inf_unitary --> linear_algebra
  f_ca_cpl_quot --> f_algebra_tools__is_cpl_at_self
  f_ca_cpl_quot --> concept_adic_completion
  f_ca_cpl_quot --> concept_local_rings
  f_ca_cpl_quot --> concept_prime_ideals_localization
  f_ca_cpl_quot --> rings_fields
  f_one_mom --> complex_numbers
  f_one_mom --> gamma_function
  f_one_mom --> real_analysis
  f_integrable_rpow_gauss --> f_one_mom
  f_integrable_rpow_gauss --> gamma_function
  f_integrable_rpow_gauss --> complex_numbers
  f_integrable_rpow_gauss --> trigonometry
  f_integrable_rpow_gauss --> calculus
  f_integrable_rpow_gauss --> real_analysis
  f_integrable_monomial --> f_one_mom
  f_integrable_monomial --> f_holomorphic_continuation__null_sec
  f_integrable_monomial --> polynomials
  f_integrable_monomial --> complex_numbers
  f_integrable_monomial --> real_analysis
  f_gaussian_moment_recurrence --> f_integrable_monomial
  f_gaussian_moment_recurrence --> f_one_mom
  f_gaussian_moment_recurrence --> f_polynomial_derivatives__fock_mono
  f_gaussian_moment_recurrence --> concept_derivations_smoothness
  f_gaussian_moment_recurrence --> polynomials
  f_contr_eq_of_subset --> f_polynomial_derivatives__fock_mono
  f_contr_eq_of_subset --> polynomials
  f_contr_eq_of_subset --> concept_derivations_smoothness
  f_contr_eq_of_subset --> counting
  f_fock_mom_of_basic --> f_polynomial_derivatives__fock_mono
  f_fock_mom_of_basic --> f_polynomial_derivatives__null_stable_alt
  f_fock_mom_of_basic --> f_contr_eq_of_subset
  f_fock_mom_of_basic --> f_gaussian_moment_recurrence
  f_fock_mom_of_basic --> f_integrable_monomial
  f_fock_mom_of_basic --> f_integrable_rpow_gauss
  f_fock_mom_of_basic --> f_one_mom
  f_fock_mom_of_basic --> polynomials
  f_fock_mom_of_basic --> proofs
  f_affine_hilbert_scheme_functor_is_sheaf_zariski --> f_divisor_proofs__comap_bc_comp
  f_affine_hilbert_scheme_functor_is_sheaf_zariski --> f_exists_ideal_sheaf_comap_eq_of_open_cover_statement
  f_affine_hilbert_scheme_functor_is_sheaf_zariski --> f_ideal_sheaf_data_ext_of_open_cover_statement
  f_affine_hilbert_scheme_functor_is_sheaf_zariski --> f_is_finite_flat_rank_closed_subscheme_of_open_cover_statement
  f_affine_hilbert_scheme_functor_is_sheaf_zariski --> concept_schemes_basics
  f_affine_hilbert_scheme_functor_is_sheaf_zariski --> concept_categorical_pullbacks
  f_affine_hilbert_scheme_functor_is_sheaf_zariski --> concept_flat_modules
  f_exists_ideal_sheaf_comap_eq_of_open_cover_statement --> f_exists_ideal_sheaf_comap_eq_of_open_cover
  f_exists_ideal_sheaf_comap_eq_of_open_cover_statement --> concept_schemes_basics
  f_exists_ideal_sheaf_comap_eq_of_open_cover_statement --> concept_categorical_pullbacks
  f_exists_ideal_sheaf_comap_eq_of_open_cover --> f_ideal_sheaf_glue_of_open_immersions
  f_exists_ideal_sheaf_comap_eq_of_open_cover --> f_exists_ideal_sheaf_data_of_compatible
  f_exists_ideal_sheaf_comap_eq_of_open_cover --> concept_schemes_basics
  f_exists_ideal_sheaf_data_of_compatible --> concept_schemes_basics
  f_exists_ideal_sheaf_data_of_compatible --> concept_prime_ideals_localization
  f_exists_ideal_sheaf_data_of_compatible --> concept_point_set_topology
  f_exists_ideal_sheaf_data_of_compatible --> concept_noetherian_and_irreducible_components
  f_ideal_sheaf_data_ext_of_open_cover --> concept_schemes_basics
  f_ideal_sheaf_data_ext_of_open_cover --> concept_point_set_topology
  f_ideal_sheaf_data_ext_of_open_cover_statement --> f_ideal_sheaf_data_ext_of_open_cover
  f_ideal_sheaf_data_ext_of_open_cover_statement --> concept_schemes_basics
  f_ideal_sheaf_glue_of_open_immersions --> concept_schemes_basics
  f_ideal_sheaf_glue_of_open_immersions --> concept_categorical_pullbacks
  f_ideal_sheaf_glue_of_open_immersions --> concept_point_set_topology
  f_is_finite_flat_rank_closed_subscheme_of_open_cover --> f_divisor_proofs__comap_bc_comp
  f_is_finite_flat_rank_closed_subscheme_of_open_cover --> concept_schemes_basics
  f_is_finite_flat_rank_closed_subscheme_of_open_cover --> concept_categorical_pullbacks
  f_is_finite_flat_rank_closed_subscheme_of_open_cover --> concept_flat_modules
  f_is_finite_flat_rank_closed_subscheme_of_open_cover_statement --> f_is_finite_flat_rank_closed_subscheme_of_open_cover
  f_is_finite_flat_rank_closed_subscheme_of_open_cover_statement --> concept_schemes_basics
  f_is_finite_flat_rank_closed_subscheme_of_open_cover_statement --> concept_flat_modules
  f_noether_normalization_chart --> polynomials
  f_noether_normalization_chart --> rings_fields
  f_proof_simp --> f_noether_normalization_chart
  f_proof_simp --> f_pseudo_division
  f_proof_simp --> f_st_generic_noether_normalisation
  f_proof_simp --> concept_prime_ideals_localization
  f_proof_simp --> concept_finitely_generated_algebras
  f_pseudo_division --> polynomials
  f_pseudo_division --> rings_fields
  f_sum_r_mul_ne --> polynomials
  f_sum_r_mul_ne --> counting
  f_p_generic_freeness --> f_st_generic_freeness
  f_p_generic_freeness --> f_st_generic_noether_normalisation
  f_p_generic_freeness --> f_p_generic_freeness_loc
  f_p_generic_freeness --> concept_flat_modules
  f_p_generic_freeness --> concept_prime_ideals_localization
  f_p_generic_freeness --> concept_finitely_generated_algebras
  f_p_generic_freeness --> concept_noetherian_and_irreducible_components
  f_p_generic_freeness_closed --> f_p_generic_freeness
  f_p_generic_freeness_closed --> f_p_generic_noether_normalisation
  f_p_generic_freeness_loc --> concept_prime_ideals_localization
  f_p_generic_freeness_loc --> concept_flat_modules
  f_p_generic_freeness_loc --> rings_fields
  f_p_generic_noether_normalisation --> f_proof_simp
  f_p_generic_noether_normalisation --> f_sum_r_mul_ne
  f_p_generic_noether_normalisation --> f_st_generic_noether_normalisation
  f_p_generic_noether_normalisation --> polynomials
  f_st_generic_freeness --> concept_prime_ideals_localization
  f_st_generic_freeness --> concept_flat_modules
  f_st_generic_freeness --> concept_finitely_generated_algebras
  f_st_generic_noether_normalisation --> concept_prime_ideals_localization
  f_st_generic_noether_normalisation --> concept_finitely_generated_algebras
  f_st_generic_noether_normalisation --> polynomials
  f_high_degree_in_power_sum_ideal --> f_polynomial_reduction_mod_elementary
  f_high_degree_in_power_sum_ideal --> f_span_psum_eq_span_esymm
  f_high_degree_in_power_sum_ideal --> polynomials
  f_high_degree_in_power_sum_ideal --> rings_fields
  f_polynomial_reduction_mod_elementary --> polynomials
  f_polynomial_reduction_mod_elementary --> rings_fields
  f_polynomial_reduction_mod_elementary --> concept_prime_ideals_localization
  f_power_sum_decomposition_homogeneous --> f_high_degree_in_power_sum_ideal
  f_power_sum_decomposition_homogeneous --> f_foundations__curve_cl
  f_power_sum_decomposition_homogeneous --> polynomials
  f_span_psum_eq_span_esymm --> polynomials
  f_span_psum_eq_span_esymm --> rings_fields
  f_exists_perm_normalized_minors --> linear_algebra
  f_exists_perm_normalized_minors --> rings_fields
  f_exists_perm_normalized_minors --> groups
  f_exists_perm_normalized_minors --> concept_valuation_rings
  f_covolume_bounds__linear_independent_real_of_int_of_discrete --> linear_algebra
  f_covolume_bounds__linear_independent_real_of_int_of_discrete --> concept_lattice_point_counting
  f_covolume_bounds__linear_independent_real_of_int_of_discrete --> concept_finitely_generated_abelian_groups
  f_covolume_bounds__linear_independent_real_of_int_of_discrete --> concept_point_set_topology
  f_covolume_bounds__linear_independent_real_of_int_of_discrete --> concept_hermitian_unitary_matrices
  f_norm_det_mul_prod_sq_le_of_entry_le --> concept_etale_ring_maps
  f_norm_det_mul_prod_sq_le_of_entry_le --> concept_tensor_product_of_algebras
  f_norm_det_mul_prod_sq_le_of_entry_le --> algebraic_closure
  f_norm_det_mul_prod_sq_le_of_entry_le --> linear_algebra
  f_norm_det_mul_prod_sq_le_of_entry_le --> rings_fields
  f_integral_closure_fg_finite_etale_dvr --> f_norm_det_mul_prod_sq_le_of_entry_le
  f_integral_closure_fg_finite_etale_dvr --> concept_discrete_valuation_ring
  f_integral_closure_fg_finite_etale_dvr --> concept_etale_ring_maps
  f_integral_closure_fg_finite_etale_dvr --> concept_integral_closure_fraction_fields
  f_period_integrals__unimod_loc_std --> complex_numbers
  f_period_integrals__unimod_loc_std --> concept_lattices_in_the_plane
  f_period_integrals__unimod_loc_std --> concept_hermitian_unitary_matrices
  f_period_integrals__unimod_loc_std --> concept_lattice_point_counting
  f_period_integrals__unimod_loc_std --> linear_algebra
  f_unimodular_local_standard__key_def --> f_period_integrals__unimod_loc_std
  f_unimodular_local_standard__key_def --> concept_prime_ideals_localization
  f_key_exact --> f_unimodular_local_standard__rep_defs
  f_key_exact --> f_unimodular_local_standard__rep_basic
  f_key_exact --> f_unimodular_local_standard__rep_arith
  f_key_exact --> f_unimodular_local_standard__key_def
  f_key_exact --> f_period_integrals__unimod_loc_std
  f_key_exact --> concept_hensel_lifting
  f_key_exact --> primes_divisibility
  f_key_newton --> f_unimodular_local_standard__rep_newton
  f_key_newton --> f_unimodular_local_standard__rep_basic
  f_key_newton --> f_unimodular_local_standard__rep_defs
  f_key_newton --> concept_hensel_lifting
  f_key_newton --> complex_numbers
  f_unimodular_local_standard__rep_arith --> f_period_integrals__unimod_loc_std
  f_unimodular_local_standard__rep_arith --> f_unimodular_local_standard__rep_basic
  f_unimodular_local_standard__rep_arith --> f_unimodular_local_standard__rep_defs
  f_unimodular_local_standard__rep_arith --> complex_numbers
  f_unimodular_local_standard__rep_arith --> concept_ideals_and_discriminant
  f_unimodular_local_standard__rep_basic --> f_unimodular_local_standard__key_def
  f_unimodular_local_standard__rep_basic --> f_period_integrals__unimod_loc_std
  f_unimodular_local_standard__rep_basic --> complex_numbers
  f_unimodular_local_standard__rep_basic --> concept_prime_ideals_localization
  f_unimodular_local_standard__rep_defs --> f_unimodular_local_standard__key_def
  f_unimodular_local_standard__rep_defs --> f_period_integrals__unimod_loc_std
  f_unimodular_local_standard__rep_defs --> proofs
  f_unimodular_local_standard__rep_exact --> f_period_integrals__unimod_loc_std
  f_rep_key --> f_unimodular_local_standard__rep_defs
  f_rep_key --> f_key_newton
  f_rep_key --> f_key_exact
  f_rep_key --> f_unimodular_local_standard__key_def
  f_unimodular_local_standard__rep_newton --> f_unimodular_local_standard__rep_arith
  f_unimodular_local_standard__rep_newton --> f_unimodular_local_standard__key_def
  f_unimodular_local_standard__rep_newton --> f_period_integrals__unimod_loc_std
  f_unimodular_local_standard__rep_newton --> modular_arithmetic
  f_unimodular_local_standard__rep_newton --> complex_numbers
  f_mollified_integrability__cls_bound_alt --> f_holomorphic_continuation__null_sec
  f_mollified_integrability__cls_bound_alt --> f_holomorphic_continuation__is_sing_test
  f_mollified_integrability__cls_bound_alt --> concept_hermitian_unitary_matrices
  f_mollified_integrability__cls_bound_alt --> real_analysis
  f_mollified_integrability__cls_bound_alt --> complex_analysis
  f_continuous_cexp_ip --> f_dens_defs
  f_continuous_cexp_ip --> f_moll_id
  f_continuous_cexp_ip --> f_moll_id_a
  f_continuous_cexp_ip --> f_exp_combine
  f_continuous_cexp_ip --> f_step_b
  f_continuous_cexp_ip --> f_step_c
  f_continuous_cexp_ip --> fourier_analysis
  f_continuous_cexp_ip --> real_analysis
  f_dens_defs --> f_holomorphic_continuation__null_sec
  f_dens_defs --> fourier_analysis
  f_dens_defs --> real_analysis
  f_dens_defs --> polynomials
  f_exp_combine --> f_moll_id
  f_exp_combine --> f_moll_id_a
  f_exp_combine --> f_dens_defs
  f_exp_combine --> fourier_analysis
  f_exp_combine --> complex_numbers
  f_moll_id --> f_moll_id_a
  f_moll_id --> f_dens_defs
  f_moll_id --> real_analysis
  f_moll_id --> fourier_analysis
  f_moll_id --> complex_numbers
  f_moll_id_a --> f_dens_defs
  f_moll_id_a --> fourier_analysis
  f_moll_id_a --> real_analysis
  f_moll_id_a --> concept_schwartz_functions
  f_step_b --> f_moll_id
  f_step_b --> f_moll_id_a
  f_step_b --> real_analysis
  f_step_c --> f_moll_id
  f_step_c --> f_moll_id_a
  f_step_c --> real_analysis
  f_step_c --> linear_algebra
  f_poincare_form_two_sided_bound --> f_divisor_base__model_ddc_forms
  f_poincare_form_two_sided_bound --> f_divisor_proofs__boundary_potential_smooth_off_divisor
  f_poincare_form_two_sided_bound --> f_divisor_proofs__levi_form_log_potential_formula
  f_poincare_form_two_sided_bound --> f_divisor_proofs__potential_smooth_in_chart
  f_poincare_form_two_sided_bound --> f_analytic_forms__ma_int_empty
  f_poincare_form_two_sided_bound --> f_potential_theory__is_potential_of_fun
  f_poincare_form_two_sided_bound --> complex_analysis
  f_poincare_form_two_sided_bound --> calculus
  f_poincare_form_two_sided_bound --> real_analysis
  f_square_norm_bound --> real_analysis
  f_square_norm_bound --> counting
  f_has_f_deriv_at_ev_x --> f_holomorphic_continuation__null_sec
  f_has_f_deriv_at_ev_x --> polynomials
  f_has_f_deriv_at_ev_x --> concept_derivations_smoothness
  f_has_f_deriv_at_ev_x --> calculus
  f_has_f_deriv_at_ev_x --> complex_numbers
  f_null_operator_evaluation --> f_has_f_deriv_at_ev_x
  f_null_operator_evaluation --> f_poly_exp_bound
  f_null_operator_evaluation --> f_holomorphic_continuation__null_sec
  f_null_operator_evaluation --> real_analysis
  f_null_operator_evaluation --> calculus
  f_null_stable --> f_sum_pderiv_x_mem
  f_null_stable --> f_polynomial_derivatives__null_stable_alt
  f_null_stable --> f_holomorphic_continuation__null_sec
  f_partial_deriv_quadratic_pairing --> f_holomorphic_continuation__null_sec
  f_partial_deriv_quadratic_pairing --> polynomials
  f_partial_deriv_quadratic_pairing --> concept_derivations_smoothness
  f_partial_deriv_quadratic_pairing --> rings_fields
  f_poly_exp_bound --> f_square_norm_bound
  f_poly_exp_bound --> f_has_f_deriv_at_ev_x
  f_poly_exp_bound --> f_holomorphic_continuation__null_sec
  f_poly_exp_bound --> real_analysis
  f_poly_exp_bound --> polynomials
  f_sum_pderiv_x_mem --> f_null_operator_evaluation
  f_sum_pderiv_x_mem --> f_partial_deriv_quadratic_pairing
  f_sum_pderiv_x_mem --> f_poly_exp_bound
  f_sum_pderiv_x_mem --> f_polynomial_derivatives__null_stable_alt
  f_sum_pderiv_x_mem --> f_holomorphic_continuation__null_sec
  f_sum_pderiv_x_mem --> polynomials
  f_sum_pderiv_x_mem --> concept_derivations_smoothness
  f_abstract --> f_kills_of_idem
  f_abstract --> f_conv_assoc
  f_abstract --> f_conv_eig
  f_abstract --> f_band_cc
  f_abstract --> f_band_kill
  f_abstract --> f_eq_zero_of_test
  f_abstract --> f_unfold
  f_abstract --> f_is_band
  f_abstract --> concept_haar_measure_fundamental_domain
  f_band_cc --> f_is_band
  f_band_cc --> concept_haar_measure_fundamental_domain
  f_band_cc --> concept_point_set_topology
  f_band_cc --> real_analysis
  f_band_kill --> f_is_band
  f_band_kill --> f_eig_band
  f_band_kill --> f_fourier
  f_band_kill --> fourier_analysis
  f_band_kill --> concept_haar_measure_fundamental_domain
  f_conv_assoc --> f_is_band
  f_conv_assoc --> concept_haar_measure_fundamental_domain
  f_conv_assoc --> real_analysis
  f_conv_eig --> f_is_band
  f_conv_eig --> concept_haar_measure_fundamental_domain
  f_conv_eig --> real_analysis
  f_eig_band --> f_is_band
  f_eig_band --> fourier_analysis
  f_eig_band --> real_analysis
  f_eig_band --> complex_numbers
  f_eq_zero_of_test --> concept_haar_measure_fundamental_domain
  f_eq_zero_of_test --> concept_point_set_topology
  f_eq_zero_of_test --> real_analysis
  f_eq_zero_of_test --> complex_numbers
  f_exists_compact_tail --> f_is_band
  f_exists_compact_tail --> concept_haar_measure_fundamental_domain
  f_exists_compact_tail --> concept_point_set_topology
  f_exists_compact_tail --> real_analysis
  f_fourier --> fourier_analysis
  f_fourier --> real_analysis
  f_fourier --> complex_numbers
  f_is_band --> groups
  f_is_band --> concept_haar_measure_fundamental_domain
  f_is_band --> concept_point_set_topology
  f_kills_of_idem --> f_exists_compact_tail
  f_kills_of_idem --> f_op_le_half
  f_kills_of_idem --> f_conv_eig
  f_kills_of_idem --> f_conv_assoc
  f_kills_of_idem --> f_is_band
  f_kills_of_idem --> real_analysis
  f_op_le_half --> f_real_bands__transl
  f_op_le_half --> f_is_band
  f_op_le_half --> concept_haar_measure_fundamental_domain
  f_op_le_half --> real_analysis
  f_real_bands__transl --> concept_haar_measure_fundamental_domain
  f_real_bands__transl --> concept_point_set_topology
  f_real_bands__transl --> real_analysis
  f_unfold --> f_band_cc
  f_unfold --> f_is_band
  f_unfold --> concept_haar_measure_fundamental_domain
  f_unfold --> real_analysis
  f_foundations__is_d_c_reps --> concept_modular_forms
  f_foundations__is_d_c_reps --> concept_hecke_operators
  f_foundations__is_d_c_reps --> concept_group_homology
  f_foundations__is_d_c_reps --> polynomials
  f_foundations__is_d_c_reps --> complex_analysis
  f_coeff_eq_zero_of_exp_decay_of_integral_identity --> real_analysis
  f_coeff_eq_zero_of_exp_decay_of_integral_identity --> calculus
  f_cusp_form_eq_zero_of_periodic_of_bound --> f_coeff_eq_zero_of_exp_decay_of_integral_identity
  f_cusp_form_eq_zero_of_periodic_of_bound --> f_green_formula_periodic_rectangle_upper_half_plane
  f_cusp_form_eq_zero_of_periodic_of_bound --> f_integral_conj_mul_exp_eq_conj_q_expansion_coeff
  f_cusp_form_eq_zero_of_periodic_of_bound --> f_wirtinger_eichler
  f_cusp_form_eq_zero_of_periodic_of_bound --> f_foundations__is_d_c_reps
  f_cusp_form_eq_zero_of_periodic_of_bound --> concept_modular_forms
  f_cusp_form_eq_zero_of_periodic_of_bound --> concept_petersson_product
  f_cusp_form_eq_zero_of_periodic_of_bound --> fourier_analysis
  f_cusp_form_eq_zero_of_periodic_of_bound --> complex_analysis
  f_foundation_proofs__eichler_integral_from_i_slash_change_of_variables --> f_foundations__is_d_c_reps
  f_foundation_proofs__eichler_integral_from_i_slash_change_of_variables --> concept_modular_forms
  f_foundation_proofs__eichler_integral_from_i_slash_change_of_variables --> complex_analysis
  f_foundation_proofs__eichler_integral_from_i_slash_change_of_variables --> calculus
  f_foundation_proofs__eichler_integral_from_i_slash_change_of_variables --> polynomials
  f_green_formula_periodic_rectangle_upper_half_plane --> complex_analysis
  f_green_formula_periodic_rectangle_upper_half_plane --> calculus
  f_green_formula_periodic_rectangle_upper_half_plane --> real_analysis
  f_integral_conj_mul_exp_eq_conj_q_expansion_coeff --> concept_modular_forms
  f_integral_conj_mul_exp_eq_conj_q_expansion_coeff --> fourier_analysis
  f_integral_conj_mul_exp_eq_conj_q_expansion_coeff --> complex_analysis
  f_integral_conj_mul_exp_eq_conj_q_expansion_coeff --> complex_numbers
  f_wirtinger_eichler --> f_foundation_proofs__eichler_integral_from_i_slash_change_of_variables
  f_wirtinger_eichler --> f_foundations__is_d_c_reps
  f_wirtinger_eichler --> complex_analysis
  f_wirtinger_eichler --> calculus
  f_wirtinger_eichler --> polynomials
  f_st_sandwich --> concept_ultrametric_norm
  f_st_sandwich --> concept_valuation_rings
  f_st_sandwich --> concept_hermitian_unitary_matrices
  f_st_sandwich --> linear_algebra
  f_st_sandwich --> p_adic_numbers
  f_witt_statement --> f_st_sandwich
  f_witt_statement --> f_witt_extension_theorem
  f_witt_statement --> concept_hermitian_unitary_matrices
  f_witt_statement --> linear_algebra
  f_witt_extension_theorem --> f_witt_of
  f_witt_extension_theorem --> f_one_vector
  f_witt_extension_theorem --> f_anisotropic_holds
  f_witt_extension_theorem --> f_witt_extension
  f_anisotropic --> concept_hermitian_unitary_matrices
  f_anisotropic --> linear_algebra
  f_anisotropic --> rings_fields
  f_anisotropic_holds --> f_anisotropic
  f_anisotropic_holds --> concept_hermitian_unitary_matrices
  f_anisotropic_holds --> rings_fields
  f_enlarge_step --> f_witt_decomposition__imports
  f_enlarge_step --> concept_hermitian_unitary_matrices
  f_enlarge_step --> linear_algebra
  f_witt_decomposition__imports --> linear_algebra
  f_witt_decomposition__imports --> concept_hermitian_unitary_matrices
  f_witt_decomposition__nondeg --> f_anisotropic
  f_witt_decomposition__nondeg --> linear_algebra
  f_witt_decomposition__nondeg --> concept_hermitian_unitary_matrices
  f_one_vector --> f_anisotropic
  f_one_vector --> concept_hermitian_unitary_matrices
  f_one_vector --> linear_algebra
  f_witt_of --> f_witt_extension
  f_witt_of --> f_anisotropic
  f_witt_of --> f_witt_decomposition__nondeg
  f_witt_of --> f_enlarge_step
  f_witt_of --> linear_algebra
  f_witt_extension --> concept_hermitian_unitary_matrices
  f_witt_extension --> linear_algebra
  f_adic_completion_principal_perfect --> concept_adic_completion
  f_adic_completion_principal_perfect --> concept_frobenius_perfect_rings
  f_adic_completion_principal_perfect --> rings_fields
  f_adic_completion_valuation_ring_complete_valuation_doma --> concept_adic_completion
  f_adic_completion_valuation_ring_complete_valuation_doma --> concept_valuation_rings
  f_adic_completion_valuation_ring_complete_valuation_doma --> rings_fields
  f_bounded_powers_or_exists_valuation_subring_dvd --> f_exists_valuation_subring_alg_closed_not_is_unit
  f_bounded_powers_or_exists_valuation_subring_dvd --> concept_valuation_rings
  f_bounded_powers_or_exists_valuation_subring_dvd --> concept_prime_ideals_localization
  f_bounded_powers_or_exists_valuation_subring_dvd --> algebraic_closure
  f_bounded_powers_or_exists_valuation_subring_dvd --> polynomials
  f_descent_of_points_killed --> f_dvd_all_pow_of_frobenius_eq_killed_by_perfect_points
  f_descent_of_points_killed --> concept_flat_modules
  f_descent_of_points_killed --> concept_tensor_product_of_algebras
  f_descent_of_points_killed --> concept_adic_completion
  f_descent_of_points_killed --> concept_frobenius_perfect_rings
  f_dvd_all_pow_of_frobenius_eq_killed_by_perfect_points --> f_pow_dvd_of_vanishing_at_perfect_valuation_points
  f_dvd_all_pow_of_frobenius_eq_killed_by_perfect_points --> f_frobenius_pow_equation_dvd_all_pow
  f_dvd_all_pow_of_frobenius_eq_killed_by_perfect_points --> concept_prime_ideals_localization
  f_dvd_all_pow_of_frobenius_eq_killed_by_perfect_points --> concept_frobenius_perfect_rings
  f_dvd_all_pow_of_frobenius_eq_killed_by_perfect_points --> concept_valuation_rings
  f_exists_valuation_subring_alg_closed_not_is_unit --> concept_valuation_rings
  f_exists_valuation_subring_alg_closed_not_is_unit --> concept_prime_ideals_localization
  f_exists_valuation_subring_alg_closed_not_is_unit --> algebraic_closure
  f_exists_valuation_subring_alg_closed_not_is_unit --> concept_local_rings
  f_frobenius_pow_equation_dvd_all_pow --> concept_frobenius_perfect_rings
  f_frobenius_pow_equation_dvd_all_pow --> primes_divisibility
  f_frobenius_pow_equation_dvd_all_pow --> rings_fields
  f_pow_dvd_of_vanishing_at_perfect_valuation_points --> f_bounded_powers_or_exists_valuation_subring_dvd
  f_pow_dvd_of_vanishing_at_perfect_valuation_points --> f_adic_completion_valuation_ring_complete_valuation_doma
  f_pow_dvd_of_vanishing_at_perfect_valuation_points --> f_adic_completion_principal_perfect
  f_pow_dvd_of_vanishing_at_perfect_valuation_points --> concept_frobenius_perfect_rings
  f_pow_dvd_of_vanishing_at_perfect_valuation_points --> concept_valuation_rings
  f_pow_dvd_of_vanishing_at_perfect_valuation_points --> algebraic_closure
  f_period_integrals__unitary_approx --> concept_hermitian_unitary_matrices
  f_period_integrals__unitary_approx --> number_fields
  f_period_integrals__unitary_approx --> p_adic_numbers
  f_period_integrals__unitary_approx --> concept_tensor_product_of_algebras
  f_period_integrals__unitary_approx --> concept_dedekind_domains
  f_period_integrals__unitary_approx --> groups
  f_unitary_approx_fin --> f_period_integrals__unitary_approx
  f_unitary_approx_fin --> concept_hermitian_unitary_matrices
  f_unitary_approx_fin --> number_fields
  f_unitary_approx_fin --> p_adic_numbers
  f_unitary_approximation__assembly --> f_unitary_approximation__cayley
  f_unitary_approximation__assembly --> f_skew_approx
  f_unitary_approximation__assembly --> f_weak_approx_f
  f_unitary_approximation__assembly --> f_mem_int_o_e_of_is_integral
  f_unitary_approximation__assembly --> f_sigma_mem_int_o_e
  f_unitary_approximation__assembly --> f_unitary_approximation__development
  f_unitary_approximation__assembly --> f_general_b_fact_right_ter__imports
  f_unitary_approximation__assembly --> f_period_integrals__unitary_approx
  f_unitary_approximation__assembly --> concept_hermitian_unitary_matrices
  f_unitary_approximation__cayley --> f_period_integrals__unitary_approx
  f_unitary_approximation__cayley --> concept_hermitian_unitary_matrices
  f_unitary_approximation__cayley --> linear_algebra
  f_unitary_approximation__development --> f_unitary_approx_fin
  f_unitary_approximation__development --> f_weak_approx_f
  f_mem_int_o_e_of_is_integral --> f_weak_approx_f
  f_mem_int_o_e_of_is_integral --> f_period_integrals__unitary_approx
  f_mem_int_o_e_of_is_integral --> number_fields
  f_mem_int_o_e_of_is_integral --> concept_integral_closure_fraction_fields
  f_sigma_mem_int_o_e --> f_weak_approx_f
  f_sigma_mem_int_o_e --> f_mem_int_o_e_of_is_integral
  f_sigma_mem_int_o_e --> f_period_integrals__unitary_approx
  f_sigma_mem_int_o_e --> linear_algebra
  f_sigma_mem_int_o_e --> concept_tensor_product_of_algebras
  f_skew_approx --> f_weak_approx_f
  f_skew_approx --> f_sigma_mem_int_o_e
  f_skew_approx --> f_mem_int_o_e_of_is_integral
  f_skew_approx --> concept_hermitian_unitary_matrices
  f_skew_approx --> number_fields
  f_weak_approx_f --> f_period_integrals__unitary_approx
  f_weak_approx_f --> number_fields
  f_weak_approx_f --> p_adic_numbers
  f_weak_approx_f --> concept_dedekind_domains
  f_weak_approx_f --> concept_tensor_product_of_algebras
  f_general_b_fact_right_ter__imports --> number_fields
  f_general_b_fact_right_ter__imports --> counting
  f_complex_analytic_sets__osgood_separate --> f_regularisation__p_riemann_extension_slices
  f_complex_analytic_sets__osgood_separate --> f_analytic_charts__osgood
  f_complex_analytic_sets__osgood_separate --> f_analytic_charts__osgood_a
  f_complex_analytic_sets__osgood_separate --> complex_analysis
  f_complex_analytic_sets__osgood_separate --> concept_point_set_topology
  f_p_non_isolated_fibre_curve --> f_st_analytic_germ_components
  f_p_non_isolated_fibre_curve --> f_st_irreducible_germ_curve
  f_p_non_isolated_fibre_curve --> f_st_non_isolated_fibre_curve
  f_p_non_isolated_fibre_curve --> f_complex_analytic_sets__osgood_separate
  f_p_non_isolated_fibre_curve --> f_analytic_germ
  f_p_non_isolated_fibre_curve --> concept_complex_analytic_sets
  f_p_non_isolated_fibre_curve --> complex_analysis
  f_st_analytic_germ_components --> concept_complex_analytic_sets
  f_st_analytic_germ_components --> f_analytic_germ
  f_st_analytic_germ_components --> concept_noetherian_and_irreducible_components
  f_st_irreducible_germ_curve --> concept_complex_analytic_sets
  f_st_irreducible_germ_curve --> f_analytic_germ
  f_st_irreducible_germ_curve --> complex_analysis
  f_st_non_isolated_fibre_curve --> concept_complex_analytic_sets
  f_st_non_isolated_fibre_curve --> complex_analysis
  f_regularisation__p_riemann_extension_slices --> f_regularisation__st_riemann_slices
  f_regularisation__p_riemann_extension_slices --> f_analytic_charts__osgood
  f_regularisation__p_riemann_extension_slices --> f_analytic_charts__osgood_a
  f_regularisation__p_riemann_extension_slices --> complex_analysis
  f_regularisation__p_riemann_extension_slices --> concept_point_set_topology
  f_regularisation__st_riemann_slices --> complex_analysis
  f_regularisation__st_riemann_slices --> concept_point_set_topology
  f_alpha_uniqueness__statement --> groups
  f_alpha_uniqueness__statement --> modular_arithmetic
  f_alpha_uniqueness__statement --> concept_finitely_generated_abelian_groups
  f_alpha_uniqueness__statement --> concept_hermitian_unitary_matrices
  f_alpha_uniqueness__statement --> complex_numbers
  f_fock_gram__statement_herm --> f_fock_gram__statement_lat
  f_fock_gram__statement_herm --> concept_hermitian_unitary_matrices
  f_fock_gram__statement_herm --> concept_lattice_point_counting
  f_fock_gram__statement_herm --> number_fields
  f_fock_gram__statement_herm --> linear_algebra
  f_fock_gram__statement_lat --> linear_algebra
  f_fock_gram__statement_lat --> concept_lattice_point_counting
  f_fock_gram__statement_lat --> concept_hermitian_unitary_matrices
  f_fock_gram__statement_lat --> concept_tensor_product_of_algebras
  f_hermitian_lattices__defs_c_s --> f_hermitian_lattices__statement_lat
  f_hermitian_lattices__defs_c_s --> number_fields
  f_hermitian_lattices__defs_c_s --> concept_lattice_point_counting
  f_hermitian_lattices__defs_c_s --> concept_hermitian_unitary_matrices
  f_discr_finite --> f_hermitian_lattices__genus_covol_bound
  f_discr_finite --> f_hermitian_lattices__statement_theta
  f_discr_finite --> f_alpha_uniqueness__statement
  f_discr_finite --> concept_modular_forms
  f_discr_finite --> concept_lattice_point_counting
  f_discr_finite --> number_fields
  f_hermitian_lattices__genus_covol_bound --> f_hermitian_lattices__statement_lat
  f_hermitian_lattices__genus_covol_bound --> f_hermitian_lattices__defs_c_s
  f_hermitian_lattices__genus_covol_bound --> number_fields
  f_hermitian_lattices__genus_covol_bound --> concept_lattice_point_counting
  f_hermitian_lattices__statement_lat --> f_fock_gram__statement_herm
  f_hermitian_lattices__statement_lat --> concept_hermitian_unitary_matrices
  f_hermitian_lattices__statement_lat --> concept_dedekind_domains
  f_hermitian_lattices__statement_lat --> concept_prime_ideals_localization
  f_hermitian_lattices__statement_lat --> concept_lattice_point_counting
  f_hermitian_lattices__statement_lat --> concept_group_actions
  f_hermitian_lattices__statement_theta --> f_alpha_uniqueness__statement
  f_hermitian_lattices__statement_theta --> f_hermitian_lattices__statement_lat
  f_hermitian_lattices__statement_theta --> f_lattice_theta__statement
  f_hermitian_lattices__statement_theta --> fourier_analysis
  f_hermitian_lattices__statement_theta --> concept_modular_forms
  f_hermitian_lattices__statement_theta --> complex_numbers
  f_hermitian_lattices__statement_theta --> infinite_series
  f_theta_l_euclid --> f_hermitian_lattices__statement_theta
  f_theta_l_euclid --> f_hermitian_lattices__defs_c_s
  f_theta_l_euclid --> f_hermitian_lattices__genus_covol_bound
  f_theta_l_euclid --> fourier_analysis
  f_theta_l_euclid --> concept_lattice_point_counting
  f_lattice_theta__statement --> fourier_analysis
  f_lattice_theta__statement --> concept_schwartz_functions
  f_lattice_theta__statement --> concept_lattice_point_counting
  f_lattice_theta__statement --> concept_lattices_in_the_plane
  f_lattice_theta__statement --> infinite_series
  f_card_nonregular_residues_mod_pow_sub_one_le --> modular_arithmetic
  f_card_nonregular_residues_mod_pow_sub_one_le --> primes_divisibility
  f_card_nonregular_residues_mod_pow_sub_one_le --> counting
  f_no_norm_eight_of_fourier_vanishing_order_fifteen --> concept_roots_of_unity_kummer
  f_no_norm_eight_of_fourier_vanishing_order_fifteen --> fourier_analysis
  f_no_norm_eight_of_fourier_vanishing_order_fifteen --> complex_numbers
  f_no_norm_eight_of_fourier_vanishing_order_fifteen --> linear_algebra
  f_no_norm_eight_of_fourier_vanishing_order_fifteen --> modular_arithmetic
  f_no_norm_twelve_order_sixtythree --> concept_roots_of_unity_kummer
  f_no_norm_twelve_order_sixtythree --> fourier_analysis
  f_no_norm_twelve_order_sixtythree --> complex_numbers
  f_no_norm_twelve_order_sixtythree --> modular_arithmetic
  f_no_norm_twelve_order_sixtythree --> linear_algebra
  f_orthogonal_int_vectors_not_agree_on_regular --> f_card_nonregular_residues_mod_pow_sub_one_le
  f_orthogonal_int_vectors_not_agree_on_regular --> f_no_norm_eight_of_fourier_vanishing_order_fifteen
  f_orthogonal_int_vectors_not_agree_on_regular --> f_no_norm_twelve_order_sixtythree
  f_orthogonal_int_vectors_not_agree_on_regular --> f_parseval_bound_integer_vector_small_fourier_support
  f_orthogonal_int_vectors_not_agree_on_regular --> f_separation_numerical_ineq_cuspidal_g_l
  f_orthogonal_int_vectors_not_agree_on_regular --> fourier_analysis
  f_orthogonal_int_vectors_not_agree_on_regular --> concept_roots_of_unity_kummer
  f_parseval_bound_integer_vector_small_fourier_support --> fourier_analysis
  f_parseval_bound_integer_vector_small_fourier_support --> concept_roots_of_unity_kummer
  f_parseval_bound_integer_vector_small_fourier_support --> complex_numbers
  f_parseval_bound_integer_vector_small_fourier_support --> infinite_series
  f_separation_numerical_ineq_cuspidal_g_l --> primes_divisibility
  f_separation_numerical_ineq_cuspidal_g_l --> infinite_series
  f_separation_numerical_ineq_cuspidal_g_l --> counting
  f_mahler_measure__level_sum --> polynomials
  f_mahler_measure__level_sum --> counting
  f_mahler_measure__level_sum --> rings_fields
  f_mahler_measure__good_count --> f_mahler_measure__level_sum
  f_mahler_measure__good_count --> p_adic_numbers
  f_mahler_measure__good_count --> polynomials
  f_mahler_measure__good_count --> linear_algebra
  f_mahler_measure__good_count --> concept_valuation_rings
  f_mahler_measure__is_frozen_inv --> f_mahler_measure__good_count
  f_mahler_measure__is_frozen_inv --> p_adic_numbers
  f_mahler_measure__is_frozen_inv --> polynomials
  f_mahler_measure__has_order --> f_mahler_measure__is_frozen_inv
  f_mahler_measure__has_order --> f_mahler_measure__good_count
  f_mahler_measure__has_order --> f_mahler_measure__level_sum
  f_mahler_measure__has_order --> p_adic_numbers
  f_mahler_measure__has_order --> polynomials
  f_mahler_measure__cs_saturated --> f_mahler_measure__good_count
  f_mahler_measure__cs_saturated --> f_mahler_measure__has_order
  f_mahler_measure__cs_saturated --> p_adic_numbers
  f_mahler_measure__cs_saturated --> linear_algebra
  f_mahler_measure__cs_saturated --> concept_group_representations
  f_mahler_measure__quotient_upper_bounds_of_power_bounds --> f_mahler_measure__statement
  f_mahler_measure__quotient_upper_bounds_of_power_bounds --> f_mahler_measure__statement_b
  f_mahler_measure__quotient_upper_bounds_of_power_bounds --> f_mahler_measure__statement_d
  f_mahler_measure__quotient_upper_bounds_of_power_bounds --> p_adic_numbers
  f_mahler_measure__quotient_upper_bounds_of_power_bounds --> concept_ultrametric_norm
  f_mahler_measure__quotient_upper_bounds_of_power_bounds --> polynomials
  f_mahler_measure__quotient_upper_bounds_of_power_bounds --> linear_algebra
  f_mahler_measure__statement_t --> f_mahler_measure__cs_saturated
  f_mahler_measure__statement_t --> f_mahler_measure__good_count
  f_mahler_measure__statement_t --> p_adic_numbers
  f_mahler_measure__statement_t --> linear_algebra
  f_mahler_measure__statement_t --> concept_group_representations
  f_mahler_measure__statement_t_m --> f_mahler_measure__statement_t
  f_mahler_measure__statement_t_m --> f_mahler_measure__quotient_upper_bounds_of_power_bounds
  f_mahler_measure__statement_t_m --> f_mahler_measure__cs_saturated
  f_mahler_measure__statement_t_m --> f_mahler_measure__good_count
  f_mahler_measure__statement_t_m --> f_mahler_measure__is_frozen_inv
  f_mahler_measure__statement_t_m --> f_mahler_measure__has_order
  f_mahler_measure__statement_t_m --> p_adic_numbers
  f_fock_resolution_onto__shift_last_letter_thresholds --> f_mahler_measure__cs_saturated
  f_fock_resolution_onto__shift_last_letter_thresholds --> f_mahler_measure__good_count
  f_fock_resolution_onto__shift_last_letter_thresholds --> f_mahler_measure__has_order
  f_fock_resolution_onto__shift_last_letter_thresholds --> p_adic_numbers
  f_fock_resolution_onto__statement_a --> f_fock_resolution_onto__shift_last_letter_thresholds
  f_fock_resolution_onto__statement_a --> f_mahler_measure__cs_saturated
  f_fock_resolution_onto__statement_a --> f_mahler_measure__good_count
  f_fock_resolution_onto__statement_a --> p_adic_numbers
  f_fock_resolution_onto__statement_a --> linear_algebra
  f_fock_resolution_onto__statement_a --> concept_lattice_point_counting
  f_meets_open_cosets --> concept_group_representations
  f_meets_open_cosets --> concept_semisimple_algebras_radical
  f_meets_open_cosets --> concept_separable_polynomials
  f_meets_open_cosets --> concept_derivations_smoothness
  f_meets_open_cosets --> polynomials
  f_meets_open_cosets --> linear_algebra
  f_div_w_core_lac_use_type --> f_meets_open_cosets
  f_div_w_core_lac_use_type --> concept_group_representations
  f_div_w_core_lac_use_type --> concept_separable_polynomials
  f_div_w_core_lac_use_type --> concept_point_set_topology
  f_div_w_core_lac_use_type --> polynomials
  f_div_w_core_lac_use_type --> linear_algebra
  f_open_coset --> f_meets_open_cosets
  f_open_coset --> f_div_w_core_lac_use_type
  f_open_coset --> concept_group_representations
  f_open_coset --> concept_separable_polynomials
  f_open_coset --> concept_normal_subgroups_quotients
  f_open_coset --> concept_point_set_topology
  f_open_coset --> polynomials
  f_open_coset --> linear_algebra
  f_chain_pf --> f_open_coset
  f_chain_pf --> polynomials
  f_chain_pf --> linear_algebra
  f_chain_pf --> concept_derivations_smoothness
  f_sep_poly_proof --> f_open_coset
  f_sep_poly_proof --> concept_separable_polynomials
  f_sep_poly_proof --> polynomials
  f_sep_poly_proof --> linear_algebra
  f_coset_of_cover --> concept_noetherian_and_irreducible_components
  f_coset_of_cover --> concept_group_actions
  f_coset_of_cover --> concept_normal_subgroups_quotients
  f_coset_of_cover --> concept_point_set_topology
  f_coset_of_cover --> concept_prime_ideals_localization
  f_coset_of_cover --> concept_schemes_basics
  f_coset_of_cover --> concept_group_representations
  f_coset_of_cover --> polynomials
  f_open_coset_pf --> f_coset_of_cover
  f_open_coset_pf --> f_open_coset
  f_open_coset_pf --> concept_prime_ideals_localization
  f_cycle_count --> f_open_coset
  f_cycle_count --> f_div_w_core_lac_use_type
  f_cycle_count --> f_meets_open_cosets
  f_cycle_count --> concept_group_representations
  f_cycle_count --> concept_semisimple_algebras_radical
  f_cycle_count --> concept_separable_polynomials
  f_cycle_count --> concept_point_set_topology
  f_cycle_count --> linear_algebra
  f_fin_dense_pf --> f_cycle_count
  f_fin_dense_pf --> f_open_coset
  f_fin_dense_pf --> concept_separable_polynomials
  f_fin_dense_pf --> concept_point_set_topology
  f_fin_dense_pf --> concept_normal_subgroups_quotients
  f_fin_fin_dense --> f_sep_poly_proof
  f_fin_fin_dense --> f_chain_pf
  f_fin_fin_dense --> f_open_coset_pf
  f_fin_fin_dense --> f_fin_dense_pf
  f_geometry_proofs__section_eq_zero_of_values --> f_hodge_tate_points__val_at_restrict
  f_geometry_proofs__section_eq_zero_of_values --> f_p_adic_hodge__finite_flat
  f_geometry_proofs__section_eq_zero_of_values --> concept_group_schemes
  f_geometry_proofs__section_eq_zero_of_values --> concept_schemes_basics
  f_hodge_tate_functional_unique --> f_geometry_proofs__section_eq_zero_of_values
  f_hodge_tate_functional_unique --> f_geometry_proofs__exists_unique_tangent_dual_number
  f_hodge_tate_functional_unique --> f_global_geometry__lie_model
  f_hodge_tate_functional_unique --> f_global_geometry__has_values
  f_hodge_tate_functional_unique --> f_hodge_tate_points__val_at_restrict
  f_hodge_tate_functional_unique --> f_p_adic_hodge__finite_flat
  f_hodge_tate_functional_unique --> concept_dual_numbers
  f_hodge_tate_functional_unique --> concept_group_schemes
  f_hodge_tate_functional_unique --> concept_flat_modules
  f_archimedean_orbit_measures__upq --> groups
  f_archimedean_orbit_measures__upq --> linear_algebra
  f_archimedean_orbit_measures__upq --> complex_numbers
  f_archimedean_orbit_measures__upq --> concept_hermitian_unitary_matrices
  f_archimedean_orbit_measures__omega_density --> f_archimedean_orbit_measures__upq
  f_archimedean_orbit_measures__omega_density --> concept_haar_measure_fundamental_domain
  f_archimedean_orbit_measures__omega_density --> concept_hermitian_unitary_matrices
  f_archimedean_orbit_measures__omega_density --> concept_point_set_topology
  f_archimedean_orbit_measures__omega_density --> calculus
  f_cay_dens_ex_om --> f_archimedean_orbit_measures__omega_density
  f_cay_dens_ex_om --> f_archimedean_orbit_measures__upq
  f_cay_dens_ex_om --> concept_point_set_topology
  f_cay_dens_ex_om --> concept_hermitian_unitary_matrices
  f_archimedean_orbit_measures__imports --> linear_algebra
  f_archimedean_orbit_measures__imports --> rings_fields
  f_archimedean_orbit_measures__imports --> concept_lattice_point_counting
  f_archimedean_orbit_measures__imports --> concept_hermitian_unitary_matrices
  f_archimedean_orbit_measures__is_unimodular --> f_archimedean_orbit_measures__imports
  f_archimedean_orbit_measures__is_unimodular --> groups
  f_archimedean_orbit_measures__is_unimodular --> linear_algebra
  f_archimedean_orbit_measures__is_unimodular --> concept_hermitian_unitary_matrices
  f_archimedean_orbit_measures__is_c_m_unram --> number_fields
  f_archimedean_orbit_measures__is_c_m_unram --> concept_ideals_and_discriminant
  f_archimedean_orbit_measures__is_c_m_unram --> complex_numbers
  f_archimedean_orbit_measures__base_lattice_is_unimodular --> f_archimedean_orbit_measures__is_c_m_unram
  f_archimedean_orbit_measures__base_lattice_is_unimodular --> f_archimedean_orbit_measures__is_unimodular
  f_archimedean_orbit_measures__base_lattice_is_unimodular --> number_fields
  f_archimedean_orbit_measures__base_lattice_is_unimodular --> linear_algebra
  f_archimedean_orbit_measures__base_lattice_is_unimodular --> concept_hermitian_unitary_matrices
  f_archimedean_orbit_measures__inst_topological_space_h_a --> f_archimedean_orbit_measures__upq
  f_archimedean_orbit_measures__inst_topological_space_h_a --> number_fields
  f_archimedean_orbit_measures__inst_topological_space_h_a --> concept_tensor_product_of_algebras
  f_archimedean_orbit_measures__inst_topological_space_h_a --> concept_haar_measure_fundamental_domain
  f_archimedean_orbit_measures__inst_topological_space_h_a --> fourier_analysis
  f_archimedean_orbit_measures__inst_topological_space_h_a --> p_adic_numbers
  f_archimedean_orbit_measures__is_inf_emb --> f_archimedean_orbit_measures__inst_topological_space_h_a
  f_archimedean_orbit_measures__is_inf_emb --> number_fields
  f_archimedean_orbit_measures__is_inf_emb --> concept_tensor_product_of_algebras
  f_archimedean_orbit_measures__is_inf_emb --> complex_numbers
  f_archimedean_orbit_measures__meas_lie --> f_archimedean_orbit_measures__inst_topological_space_h_a
  f_archimedean_orbit_measures__meas_lie --> f_archimedean_orbit_measures__upq
  f_archimedean_orbit_measures__meas_lie --> concept_haar_measure_fundamental_domain
  f_archimedean_orbit_measures__meas_lie --> concept_hermitian_unitary_matrices
  f_archimedean_orbit_measures__meas_lie --> fourier_analysis
  f_archimedean_orbit_measures__one_per_place --> f_archimedean_orbit_measures__base_lattice_is_unimodular
  f_archimedean_orbit_measures__one_per_place --> f_archimedean_orbit_measures__inst_topological_space_h_a
  f_archimedean_orbit_measures__one_per_place --> f_archimedean_orbit_measures__is_inf_emb
  f_archimedean_orbit_measures__one_per_place --> f_archimedean_orbit_measures__meas_lie
  f_archimedean_orbit_measures__one_per_place --> f_archimedean_orbit_measures__omega_density
  f_archimedean_orbit_measures__one_per_place --> concept_haar_measure_fundamental_domain
  f_archimedean_orbit_measures__one_per_place --> number_fields
  f_archimedean_orbit_measures__cay_dens_ex_sk --> f_archimedean_orbit_measures__one_per_place
  f_archimedean_orbit_measures__cay_dens_ex_sk --> f_archimedean_orbit_measures__meas_lie
  f_archimedean_orbit_measures__cay_dens_ex_sk --> f_archimedean_orbit_measures__is_inf_emb
  f_archimedean_orbit_measures__cay_dens_ex_sk --> f_archimedean_orbit_measures__omega_density
  f_archimedean_orbit_measures__cay_dens_ex_sk --> f_archimedean_orbit_measures__inst_topological_space_h_a
  f_archimedean_orbit_measures__cay_dens_ex_sk --> f_archimedean_orbit_measures__base_lattice_is_unimodular
  f_archimedean_orbit_measures__cay_dens_ex_sk --> concept_haar_measure_fundamental_domain
  f_archimedean_orbit_measures__cay_dens_ex_top --> f_archimedean_orbit_measures__cay_dens_ex_sk
  f_archimedean_orbit_measures__cay_dens_ex_top --> f_archimedean_orbit_measures__omega_density
  f_archimedean_orbit_measures__cay_dens_ex_top --> f_archimedean_orbit_measures__upq
  f_archimedean_orbit_measures__cay_dens_ex_top --> concept_haar_measure_fundamental_domain
  f_archimedean_orbit_measures__cay_dens_ex_top --> concept_point_set_topology
  f_archimedean_orbit_measures__cay_dens_ex_top --> concept_hermitian_unitary_matrices
  f_diamond_diag_mul_eq_mul_of_dvd_lower_left_gamma1_inter_gamm --> concept_modular_forms
  f_diamond_diag_mul_eq_mul_of_dvd_lower_left_gamma1_inter_gamm --> concept_hecke_operators
  f_diamond_diag_mul_eq_mul_of_dvd_lower_left_gamma1_inter_gamm --> modular_arithmetic
  f_diamond_diag_mul_eq_mul_of_dvd_lower_left_gamma1_inter_gamm --> linear_algebra
  f_diamond_diag_mul_eq_mul_of_dvd_lower_left_gamma1_inter_gamm --> f_foundations__is_d_c_reps
  f_diamond_diag_mul_eq_mul_upper_triangular_of_not_dvd_lower_l --> concept_modular_forms
  f_diamond_diag_mul_eq_mul_upper_triangular_of_not_dvd_lower_l --> concept_hecke_operators
  f_diamond_diag_mul_eq_mul_upper_triangular_of_not_dvd_lower_l --> modular_arithmetic
  f_diamond_diag_mul_eq_mul_upper_triangular_of_not_dvd_lower_l --> primes_divisibility
  f_diamond_diag_mul_eq_mul_upper_triangular_of_not_dvd_lower_l --> f_foundations__is_d_c_reps
  f_hecke_operators_on_half_plane_functions_agree_explicit --> concept_modular_forms
  f_hecke_operators_on_half_plane_functions_agree_explicit --> concept_hecke_operators
  f_hecke_operators_on_half_plane_functions_agree_explicit --> complex_numbers
  f_hecke_operators_on_half_plane_functions_agree_explicit --> f_foundations__is_d_c_reps
  f_hecke_t_slash_invariant --> concept_modular_forms
  f_hecke_t_slash_invariant --> concept_hecke_operators
  f_hecke_t_slash_invariant --> concept_group_actions
  f_hecke_t_slash_invariant --> f_hecke_tq_representatives_cosets_distinct
  f_hecke_t_slash_invariant --> f_upper_mul_eq_mul_diamond_diag_gamma1_inter_gamma0
  f_hecke_t_slash_invariant --> f_upper_triangular_mul_eq_mul_upper_triangular_gamma1_inte
  f_hecke_t_slash_invariant --> f_diamond_diag_mul_eq_mul_of_dvd_lower_left_gamma1_inter_gamm
  f_hecke_t_slash_invariant --> f_diamond_diag_mul_eq_mul_upper_triangular_of_not_dvd_lower_l
  f_hecke_t_slash_invariant --> f_hecke_operators_on_half_plane_functions_agree_explicit
  f_hecke_t_slash_invariant --> f_foundations__is_d_c_reps
  f_hecke_tq_representatives_cosets_distinct --> concept_hecke_operators
  f_hecke_tq_representatives_cosets_distinct --> concept_normal_subgroups_quotients
  f_hecke_tq_representatives_cosets_distinct --> primes_divisibility
  f_hecke_tq_representatives_cosets_distinct --> linear_algebra
  f_upper_mul_eq_mul_diamond_diag_gamma1_inter_gamma0 --> concept_modular_forms
  f_upper_mul_eq_mul_diamond_diag_gamma1_inter_gamma0 --> concept_hecke_operators
  f_upper_mul_eq_mul_diamond_diag_gamma1_inter_gamma0 --> modular_arithmetic
  f_upper_mul_eq_mul_diamond_diag_gamma1_inter_gamma0 --> f_foundations__is_d_c_reps
  f_upper_triangular_mul_eq_mul_upper_triangular_gamma1_inte --> concept_modular_forms
  f_upper_triangular_mul_eq_mul_upper_triangular_gamma1_inte --> concept_hecke_operators
  f_upper_triangular_mul_eq_mul_upper_triangular_gamma1_inte --> modular_arithmetic
  f_upper_triangular_mul_eq_mul_upper_triangular_gamma1_inte --> primes_divisibility
  f_upper_triangular_mul_eq_mul_upper_triangular_gamma1_inte --> f_foundations__is_d_c_reps
  f_has_fderiv_at_schwartz_operator_first --> concept_schwartz_functions
  f_has_fderiv_at_schwartz_operator_first --> calculus
  f_has_fderiv_at_schwartz_operator_first --> real_analysis
  f_has_fderiv_at_schwartz_operator_first --> f_has_temperate_growth_prod_mk_const
  f_has_fderiv_at_schwartz_operator_first --> f_schwartz_translate_taylor_second_order
  f_has_temperate_growth_prod_mk_const --> concept_schwartz_functions
  f_has_temperate_growth_prod_mk_const --> linear_algebra
  f_has_temperate_growth_prod_mk_const --> calculus
  f_schwartz_operator_parametric_extension --> concept_schwartz_functions
  f_schwartz_operator_parametric_extension --> calculus
  f_schwartz_operator_parametric_extension --> real_analysis
  f_schwartz_operator_parametric_extension --> f_has_fderiv_at_schwartz_operator_first
  f_schwartz_operator_parametric_extension --> f_schwartz_slice_seminorm_le
  f_schwartz_operator_parametric_extension --> f_has_temperate_growth_prod_mk_const
  f_divisor_proofs__schwartz_seminorm_translate_sub_line_deriv_le --> concept_schwartz_functions
  f_divisor_proofs__schwartz_seminorm_translate_sub_line_deriv_le --> calculus
  f_divisor_proofs__schwartz_seminorm_translate_sub_line_deriv_le --> real_analysis
  f_schwartz_slice_seminorm_le --> concept_schwartz_functions
  f_schwartz_slice_seminorm_le --> calculus
  f_schwartz_slice_seminorm_le --> f_has_temperate_growth_prod_mk_const
  f_schwartz_translate_taylor_second_order --> concept_schwartz_functions
  f_schwartz_translate_taylor_second_order --> calculus
  f_schwartz_translate_taylor_second_order --> real_analysis
  f_schwartz_translate_taylor_second_order --> f_divisor_proofs__schwartz_seminorm_translate_sub_line_deriv_le
  f_adelic_hermitian_forms__is_herm_form --> number_fields
  f_adelic_hermitian_forms__is_herm_form --> concept_hermitian_unitary_matrices
  f_adelic_hermitian_forms__is_herm_form --> concept_dedekind_domains
  f_adelic_hermitian_forms__is_herm_form --> concept_ideals_and_discriminant
  f_adelic_hermitian_forms__is_herm_form --> linear_algebra
  f_adelic_hermitian_forms__is_herm_form --> f_existence_of_lattices__hat1
  f_exists_denominator_primes_prescribed --> number_fields
  f_exists_denominator_primes_prescribed --> concept_dedekind_domains
  f_exists_denominator_primes_prescribed --> concept_ideals_and_discriminant
  f_exists_denominator_primes_prescribed --> concept_valuation_rings
  f_exists_denominator_primes_prescribed --> concept_prime_ideals_localization
  f_exists_nat_smul_mem --> number_fields
  f_exists_nat_smul_mem --> linear_algebra
  f_exists_nat_smul_mem --> concept_integral_closure_fraction_fields
  f_exists_norm_one_reflection_correction_at_level --> number_fields
  f_exists_norm_one_reflection_correction_at_level --> concept_hermitian_unitary_matrices
  f_exists_norm_one_reflection_correction_at_level --> linear_algebra
  f_exists_norm_one_reflection_correction_at_level --> f_adelic_hermitian_forms__is_herm_form
  f_exists_norm_one_reflection_correction_at_level --> f_norm_one_approximation_at_level_primes
  f_exists_norm_one_reflection_correction_at_level --> f_adelic_lattice_proofs__unitary_quasi_reflection_laws
  f_exists_norm_one_reflection_correction_at_level --> f_exists_pos_nat_mul_mem_ring_of_integers
  f_exists_norm_one_reflection_correction_at_level --> f_exists_nat_smul_mem
  f_exists_pos_nat_mul_mem_ring_of_integers --> number_fields
  f_exists_pos_nat_mul_mem_ring_of_integers --> concept_integral_closure_fraction_fields
  f_exists_pos_nat_mul_mem_ring_of_integers --> polynomials
  f_norm_one_approximation_at_level_primes --> number_fields
  f_norm_one_approximation_at_level_primes --> concept_ideals_and_discriminant
  f_norm_one_approximation_at_level_primes --> concept_valuation_rings
  f_norm_one_approximation_at_level_primes --> modular_arithmetic
  f_norm_one_approximation_at_level_primes --> f_exists_denominator_primes_prescribed
  f_norm_one_approximation_at_level_primes --> f_valuation_eq_one_of_norm_one_of_not_moved
  f_norm_one_approximation_at_level_primes --> f_adelic_hermitian_forms__is_herm_form
  f_adelic_lattice_proofs__unitary_quasi_reflection_laws --> linear_algebra
  f_adelic_lattice_proofs__unitary_quasi_reflection_laws --> concept_hermitian_unitary_matrices
  f_adelic_lattice_proofs__unitary_quasi_reflection_laws --> f_adelic_hermitian_forms__is_herm_form
  f_valuation_eq_one_of_norm_one_of_not_moved --> number_fields
  f_valuation_eq_one_of_norm_one_of_not_moved --> concept_dedekind_domains
  f_valuation_eq_one_of_norm_one_of_not_moved --> concept_valuation_rings
  f_valuation_eq_one_of_norm_one_of_not_moved --> concept_ultrametric_norm
  f_valuation_eq_one_of_norm_one_of_not_moved --> f_adelic_hermitian_forms__is_herm_form
  f_foundations__same_part_iff_of_ne_zero --> polynomials
  f_foundations__same_part_iff_of_ne_zero --> algebraic_closure
  f_foundations__same_part_iff_of_ne_zero --> modular_arithmetic
  f_foundations__same_part_iff_of_ne_zero --> primes_divisibility
  f_foundations__same_part_iff_of_ne_zero --> counting
  f_foundations__same_part_iff_of_ne_zero --> f_cyclotomic_norms__statement_i
  f_foundations__same_part_iff_of_ne_zero --> f_cyclotomic_norms__statement_t
  f_card_monic_squarefree_unit_const_polys_ge --> polynomials
  f_card_monic_squarefree_unit_const_polys_ge --> counting
  f_card_monic_squarefree_unit_const_polys_ge --> modular_arithmetic
  f_card_monic_squarefree_unit_const_polys_ge --> f_foundations__same_part_iff_of_ne_zero
  f_foundation_proofs__mem_monic_squarefree_unit_const_polys_iff_monic_squarefr --> polynomials
  f_foundation_proofs__mem_monic_squarefree_unit_const_polys_iff_monic_squarefr --> counting
  f_foundation_proofs__mem_monic_squarefree_unit_const_polys_iff_monic_squarefr --> f_foundations__same_part_iff_of_ne_zero
  f_one_sub_two_div_le_squarefree_label_mass --> polynomials
  f_one_sub_two_div_le_squarefree_label_mass --> counting
  f_one_sub_two_div_le_squarefree_label_mass --> real_analysis
  f_one_sub_two_div_le_squarefree_label_mass --> f_foundations__same_part_iff_of_ne_zero
  f_one_sub_two_div_le_squarefree_label_mass --> f_foundation_proofs__squarefree_label_torus_card_bounds_and_mul
  f_one_sub_two_div_le_squarefree_label_mass --> f_card_monic_squarefree_unit_const_polys_ge
  f_one_sub_two_div_le_squarefree_label_mass --> f_foundation_proofs__mem_monic_squarefree_unit_const_polys_iff_monic_squarefr
  f_foundation_proofs__squarefree_label_torus_card_bounds_and_mul --> polynomials
  f_foundation_proofs__squarefree_label_torus_card_bounds_and_mul --> counting
  f_foundation_proofs__squarefree_label_torus_card_bounds_and_mul --> primes_divisibility
  f_foundation_proofs__squarefree_label_torus_card_bounds_and_mul --> f_foundations__same_part_iff_of_ne_zero
  f_cyclotomic_norms__statement_i --> primes_divisibility
  f_cyclotomic_norms__statement_i --> modular_arithmetic
  f_cyclotomic_norms__statement_i --> polynomials
  f_cyclotomic_norms__statement_i --> concept_group_actions
  f_cyclotomic_norms__statement_i --> concept_group_representations
  f_cyclotomic_norms__statement_i --> concept_hermitian_unitary_matrices
  f_cyclotomic_norms__statement_i --> linear_algebra
  f_cyclotomic_norms__statement_i --> counting
  f_cyclotomic_norms__statement_t --> polynomials
  f_cyclotomic_norms__statement_t --> algebraic_closure
  f_cyclotomic_norms__statement_t --> concept_group_representations
  f_cyclotomic_norms__statement_t --> concept_group_actions
  f_cyclotomic_norms__statement_t --> concept_normal_subgroups_quotients
  f_cyclotomic_norms__statement_t --> linear_algebra
  f_cyclotomic_norms__statement_t --> f_cyclotomic_norms__statement_i
  f_orbital_bounds_conclusion__sigma_star_ex --> f_period_integrals__sigma_star_ex
  f_orbital_bounds_conclusion__sigma_star_ex --> f_theta_series_existence__sigma_star_ex
  f_period_integrals__sigma_star_ex --> concept_lattices_in_the_plane
  f_period_integrals__sigma_star_ex --> complex_analysis
  f_period_integrals__sigma_star_ex --> complex_numbers
  f_period_integrals__sigma_star_ex --> f_lat_defs
  f_theta_series_existence__development --> complex_analysis
  f_theta_series_existence__development --> concept_lattices_in_the_plane
  f_theta_series_existence__development --> f_period_integrals__sigma_star_ex
  f_theta_series_existence__development --> f_theta_deriv_ne
  f_theta_series_existence__development --> f_period_integrals__area_lat
  f_theta_series_existence__development --> f_orbital_bounds_conclusion__area_lat
  f_theta_series_existence__development --> f_im_conj_mul_combo
  f_gen_eq_of --> complex_analysis
  f_gen_eq_of --> complex_powers
  f_gen_eq_of --> fourier_analysis
  f_gen_eq_of --> calculus
  f_gen_eq_of --> f_theta_a
  f_gen_eq_of --> f_theta_deriv_ne
  f_gen_eq_of --> f_theta_series_existence__development
  f_lat_ext --> concept_lattices_in_the_plane
  f_lat_ext --> complex_analysis
  f_lat_ext --> complex_numbers
  f_lat_ext --> f_theta_series_existence__development
  f_theta_series_existence__reduce --> concept_lattices_in_the_plane
  f_theta_series_existence__reduce --> concept_modular_forms
  f_theta_series_existence__reduce --> complex_numbers
  f_theta_series_existence__reduce --> linear_algebra
  f_theta_series_existence__reduce --> f_theta_deriv_ne
  f_theta_series_existence__sigma_star_ex --> f_theta_series_existence__development
  f_theta_series_existence__sigma_star_ex --> f_theta_a
  f_theta_series_existence__sigma_star_ex --> f_theta_nz
  f_theta_series_existence__sigma_star_ex --> f_theta_series_existence__reduce
  f_theta_series_existence__sigma_star_ex --> f_gen_eq_of
  f_theta_series_existence__sigma_star_ex --> f_lat_ext
  f_theta_series_existence__sigma_star_ex --> f_period_integrals__sigma_star_ex
  f_theta_a --> complex_analysis
  f_theta_a --> fourier_analysis
  f_theta_a --> complex_numbers
  f_theta_a --> f_theta_deriv_ne
  f_theta_deriv_ne --> complex_analysis
  f_theta_deriv_ne --> fourier_analysis
  f_theta_deriv_ne --> concept_lattices_in_the_plane
  f_theta_nz --> infinite_series
  f_theta_nz --> complex_analysis
  f_theta_nz --> fourier_analysis
  f_theta_nz --> real_analysis
  f_theta_nz --> f_theta_deriv_ne
  f_commutative_algebra__is_tight --> f_dual_lattices__tensor_span
  f_commutative_algebra__is_tight --> f_dual_lattices__cotangent_surjective
  f_commutative_algebra__is_tight --> concept_valuation_rings
  f_commutative_algebra__is_tight --> concept_ultrametric_norm
  f_commutative_algebra__is_tight --> rings_fields
  f_commutative_algebra__is_tight --> linear_algebra
  f_commutative_algebra__step_order_res --> f_commutative_algebra__is_tight
  f_commutative_algebra__step_order_res --> f_dual_lattices__tensor_span
  f_commutative_algebra__step_order_res --> f_dual_lattices__cotangent_surjective
  f_commutative_algebra__step_order_res --> dirichlet_characters
  f_commutative_algebra__step_order_res --> concept_group_actions
  f_commutative_algebra__step_order_res --> linear_algebra
  f_commutative_algebra__step_order_res --> rings_fields
  f_hopf_order_contains_add_characters --> f_hodge_tate_points__ra_char
  f_hopf_order_contains_add_characters --> f_dual_lattices__tensor_span
  f_hopf_order_contains_add_characters --> groups
  f_hopf_order_contains_add_characters --> concept_valuation_rings
  f_hodge_tate_points__ra_char --> f_dual_lattices__valuation_fourier_le_one
  f_hodge_tate_points__ra_char --> f_dual_lattices__valuation_det_eq_of_span_eq
  f_hodge_tate_points__ra_char --> f_dual_lattices__tensor_span
  f_hodge_tate_points__ra_char --> fourier_analysis
  f_hodge_tate_points__ra_char --> concept_valuation_rings
  f_dual_lattices__cotangent_surjective --> f_dual_lattices__tensor_span
  f_dual_lattices__cotangent_surjective --> p_adic_numbers
  f_dual_lattices__cotangent_surjective --> linear_algebra
  f_dual_lattices__cotangent_surjective --> concept_valuation_rings
  f_dual_lattices__cotangent_surjective --> concept_derivations_smoothness
  f_dual_lattices__cotangent_surjective --> concept_schemes_basics
  f_dual_lattices__tensor_span --> linear_algebra
  f_dual_lattices__tensor_span --> rings_fields
  f_dual_lattices__tensor_span --> groups
  f_dual_lattices__tensor_span --> fourier_analysis
  f_dual_lattices__tensor_span --> concept_normal_subgroups_quotients
  f_dual_lattices__tensor_span --> concept_valuation_rings
  f_dual_lattices__valuation_det_eq_of_span_eq --> f_dual_lattices__tensor_span
  f_dual_lattices__valuation_det_eq_of_span_eq --> linear_algebra
  f_dual_lattices__valuation_det_eq_of_span_eq --> concept_valuation_rings
  f_dual_lattices__valuation_det_eq_of_span_eq --> concept_ultrametric_norm
  f_dual_lattices__valuation_fourier_le_one --> f_dual_lattices__tensor_span
  f_dual_lattices__valuation_fourier_le_one --> f_dual_lattices__valuation_det_eq_of_span_eq
  f_dual_lattices__valuation_fourier_le_one --> fourier_analysis
  f_dual_lattices__valuation_fourier_le_one --> concept_ultrametric_norm
  f_dual_lattices__valuation_fourier_le_one --> concept_valuation_rings
  f_dual_lattices__valuation_fourier_le_one --> infinite_series
  f_fock_resolution_onto__statement_b --> f_fock_resolution_onto__shift_last_letter_thresholds
  f_fock_resolution_onto__statement_b --> f_mahler_measure__good_count
  f_fock_resolution_onto__statement_b --> f_mahler_measure__cs_saturated
  f_fock_resolution_onto__statement_b --> p_adic_numbers
  f_fock_resolution_onto__statement_b --> polynomials
  f_fock_resolution_onto__statement_b --> concept_valuation_rings
  f_non_galois_descent__fourier_match --> concept_hermitian_unitary_matrices
  f_non_galois_descent__fourier_match --> concept_haar_measure_fundamental_domain
  f_non_galois_descent__fourier_match --> concept_ultrametric_norm
  f_non_galois_descent__fourier_match --> p_adic_numbers
  f_non_galois_descent__fourier_match --> fourier_analysis
  f_non_galois_descent__fourier_match --> linear_algebra
  f_non_galois_descent__fourier_match --> concept_group_actions
  f_non_galois_descent__fourier_match --> concept_field_extensions_transcendence
  f_non_galois_descent__linear_descent --> f_non_galois_descent__unit_lemma_group
  f_non_galois_descent__linear_descent --> concept_discrete_valuation_ring
  f_non_galois_descent__linear_descent --> concept_valuation_rings
  f_non_galois_descent__linear_descent --> concept_lattice_point_counting
  f_non_galois_descent__linear_descent --> concept_separable_polynomials
  f_non_galois_descent__linear_descent --> linear_algebra
  f_non_galois_descent__linear_descent --> calculus
  f_non_galois_descent__unit_lemma_group --> concept_discrete_valuation_ring
  f_non_galois_descent__unit_lemma_group --> concept_integral_closure_fraction_fields
  f_non_galois_descent__unit_lemma_group --> concept_separable_polynomials
  f_non_galois_descent__unit_lemma_group --> concept_local_rings
  f_non_galois_descent__unit_lemma_group --> concept_adic_completion
  f_non_galois_descent__unit_lemma_group --> concept_group_actions
  f_non_galois_descent__unit_lemma_group --> groups
  f_non_galois_descent__unit_lemma_group --> linear_algebra
  f_exists_finset_cosets_integral_norm_units --> f_fg_units_quot_integral_units_reduced_finite_algebra
  f_exists_finset_cosets_integral_norm_units --> f_fg_units_quot_integral_units_finite_field_ext
  f_exists_finset_cosets_integral_norm_units --> f_is_reduced_of_separable_marked_charpoly
  f_exists_finset_cosets_integral_norm_units --> f_non_galois_descent__unit_lemma_group
  f_exists_finset_cosets_integral_norm_units --> concept_finitely_generated_abelian_groups
  f_exists_finset_cosets_integral_norm_units --> concept_normal_subgroups_quotients
  f_exists_finset_cosets_integral_norm_units --> groups
  f_inertia_eigenvalues__exists_power_basis_of_charpoly_separable --> f_non_galois_descent__unit_lemma_group
  f_inertia_eigenvalues__exists_power_basis_of_charpoly_separable --> concept_separable_polynomials
  f_inertia_eigenvalues__exists_power_basis_of_charpoly_separable --> algebraic_closure
  f_inertia_eigenvalues__exists_power_basis_of_charpoly_separable --> polynomials
  f_inertia_eigenvalues__exists_power_basis_of_charpoly_separable --> linear_algebra
  f_fg_units_quot_integral_units_finite_field_ext --> f_non_galois_descent__unit_lemma_group
  f_fg_units_quot_integral_units_finite_field_ext --> concept_dedekind_domains
  f_fg_units_quot_integral_units_finite_field_ext --> concept_discrete_valuation_ring
  f_fg_units_quot_integral_units_finite_field_ext --> concept_integral_closure_fraction_fields
  f_fg_units_quot_integral_units_finite_field_ext --> concept_finitely_generated_abelian_groups
  f_fg_units_quot_integral_units_finite_field_ext --> concept_normal_subgroups_quotients
  f_fg_units_quot_integral_units_finite_field_ext --> number_fields
  f_fg_units_quot_integral_units_reduced_finite_algebra --> f_non_galois_descent__unit_lemma_group
  f_fg_units_quot_integral_units_reduced_finite_algebra --> concept_prime_ideals_localization
  f_fg_units_quot_integral_units_reduced_finite_algebra --> concept_integral_closure_fraction_fields
  f_fg_units_quot_integral_units_reduced_finite_algebra --> concept_finitely_generated_abelian_groups
  f_fg_units_quot_integral_units_reduced_finite_algebra --> concept_normal_subgroups_quotients
  f_fg_units_quot_integral_units_reduced_finite_algebra --> rings_fields
  f_is_reduced_of_separable_marked_charpoly --> f_inertia_eigenvalues__exists_power_basis_of_charpoly_separable
  f_is_reduced_of_separable_marked_charpoly --> f_non_galois_descent__unit_lemma_group
  f_is_reduced_of_separable_marked_charpoly --> concept_separable_polynomials
  f_is_reduced_of_separable_marked_charpoly --> polynomials
  f_is_reduced_of_separable_marked_charpoly --> rings_fields
  f_complex_witt_basis_normal_form --> f_exists_levi_element_isotropic_orthogonal_complex
  f_complex_witt_basis_normal_form --> f_radical_elt_moving_dual_to_majorant
  f_complex_witt_basis_normal_form --> f_hermitian_flag_unipotent_matrix_exists_sparse
  f_complex_witt_basis_normal_form --> f_hermitian_flag_complement_pos_def_factorization
  f_complex_witt_basis_normal_form --> f_pos_def_exists_conj_transpose_mul_mul_eq_one
  f_complex_witt_basis_normal_form --> f_conj_transpose_mul_mul_self_of_unitary_conj
  f_complex_witt_basis_normal_form --> concept_hermitian_unitary_matrices
  f_complex_witt_basis_normal_form --> linear_algebra
  f_complex_witt_basis_normal_form --> complex_numbers
  f_conj_transpose_mul_mul_self_of_unitary_conj --> concept_hermitian_unitary_matrices
  f_conj_transpose_mul_mul_self_of_unitary_conj --> linear_algebra
  f_conj_transpose_mul_mul_self_of_unitary_conj --> complex_numbers
  f_exists_levi_element_isotropic_orthogonal_complex --> concept_hermitian_unitary_matrices
  f_exists_levi_element_isotropic_orthogonal_complex --> linear_algebra
  f_exists_levi_element_isotropic_orthogonal_complex --> complex_numbers
  f_hermitian_flag_complement_pos_def_factorization --> concept_hermitian_unitary_matrices
  f_hermitian_flag_complement_pos_def_factorization --> linear_algebra
  f_hermitian_flag_complement_pos_def_factorization --> complex_numbers
  f_hermitian_flag_unipotent_matrix_exists_sparse --> linear_algebra
  f_hermitian_flag_unipotent_matrix_exists_sparse --> concept_hermitian_unitary_matrices
  f_hermitian_flag_unipotent_matrix_exists_sparse --> complex_numbers
  f_pos_def_exists_conj_transpose_mul_mul_eq_one --> concept_hermitian_unitary_matrices
  f_pos_def_exists_conj_transpose_mul_mul_eq_one --> linear_algebra
  f_pos_def_exists_conj_transpose_mul_mul_eq_one --> complex_numbers
  f_radical_elt_moving_dual_to_majorant --> concept_hermitian_unitary_matrices
  f_radical_elt_moving_dual_to_majorant --> linear_algebra
  f_radical_elt_moving_dual_to_majorant --> complex_numbers
  f_min_weight_sum_add_cost_abs_bound --> f_gauss_jet_bounds__statement_n
  f_min_weight_sum_add_cost_abs_bound --> f_gauss_jet_bounds__statement_i
  f_min_weight_sum_add_cost_abs_bound --> f_gauss_jet_bounds__statement_h
  f_min_weight_sum_add_cost_abs_bound --> concept_ultrametric_norm
  f_min_weight_sum_add_cost_abs_bound --> polynomials
  f_min_weight_sum_add_cost_abs_bound --> counting
  f_min_weight_sum_add_cost_abs_bound --> linear_algebra
  f_sizes_rows7 --> real_analysis
  f_sizes_rows7 --> counting
  f_sizes_rows7 --> infinite_series
  f_gauss_jet_bounds__statement --> f_incoming_bounds__incoming_bound
  f_gauss_jet_bounds__statement --> concept_ultrametric_norm
  f_gauss_jet_bounds__statement --> p_adic_numbers
  f_gauss_jet_bounds__statement --> concept_roots_of_unity_kummer
  f_gauss_jet_bounds__statement --> polynomials
  f_gauss_jet_bounds__statement --> modular_arithmetic
  f_gauss_jet_bounds__statement --> infinite_series
  f_gauss_jet_bounds__statement_a --> f_incoming_bounds__incoming_bound
  f_gauss_jet_bounds__statement_a --> f_gauss_jet_bounds__statement
  f_gauss_jet_bounds__statement_a --> modular_arithmetic
  f_gauss_jet_bounds__statement_a --> real_analysis
  f_gauss_jet_bounds__statement_a --> counting
  f_gauss_jet_bounds__statement_c --> f_gauss_jet_bounds__statement
  f_gauss_jet_bounds__statement_c --> concept_ultrametric_norm
  f_gauss_jet_bounds__statement_c --> polynomials
  f_gauss_jet_bounds__statement_c --> linear_algebra
  f_gauss_jet_bounds__statement_c --> modular_arithmetic
  f_gauss_jet_bounds__statement_e --> f_gauss_jet_bounds__statement
  f_gauss_jet_bounds__statement_e --> f_gauss_jet_bounds__statement_c
  f_gauss_jet_bounds__statement_e --> f_gauss_jet_bounds__statement_a
  f_gauss_jet_bounds__statement_e --> f_incoming_bounds__incoming_bound
  f_gauss_jet_bounds__statement_e --> concept_ultrametric_norm
  f_gauss_jet_bounds__statement_e --> p_adic_numbers
  f_gauss_jet_bounds__statement_g --> f_gauss_jet_bounds__statement
  f_gauss_jet_bounds__statement_g --> f_gauss_jet_bounds__statement_e
  f_gauss_jet_bounds__statement_g --> f_incoming_bounds__incoming_bound
  f_gauss_jet_bounds__statement_g --> concept_ultrametric_norm
  f_gauss_jet_bounds__statement_g --> p_adic_numbers
  f_gauss_jet_bounds__statement_h --> polynomials
  f_gauss_jet_bounds__statement_h --> linear_algebra
  f_gauss_jet_bounds__statement_h --> counting
  f_gauss_jet_bounds__statement_i --> f_gauss_jet_bounds__statement_h
  f_gauss_jet_bounds__statement_i --> f_gauss_jet_bounds__statement_g
  f_gauss_jet_bounds__statement_i --> f_gauss_jet_bounds__statement
  f_gauss_jet_bounds__statement_i --> f_incoming_bounds__incoming_bound
  f_gauss_jet_bounds__statement_i --> concept_ultrametric_norm
  f_gauss_jet_bounds__statement_i --> polynomials
  f_gauss_jet_bounds__statement_n --> f_gauss_jet_bounds__statement_i
  f_gauss_jet_bounds__statement_n --> f_gauss_jet_bounds__statement_h
  f_gauss_jet_bounds__statement_n --> f_gauss_jet_bounds__statement
  f_gauss_jet_bounds__statement_n --> concept_ultrametric_norm
  f_gauss_jet_bounds__statement_n --> linear_algebra
  f_gauss_jet_bounds__statement_n --> polynomials
  f_gauss_jet_bounds__statement_n --> counting
  f_statement_q --> f_gauss_jet_bounds__statement_n
  f_statement_q --> f_gauss_jet_bounds__statement_i
  f_statement_q --> concept_ultrametric_norm
  f_statement_q --> polynomials
  f_incoming_bounds__incoming_bound --> counting
  f_incoming_bounds__incoming_bound --> modular_arithmetic
  f_incoming_bounds__incoming_bound --> real_analysis
  f_incoming_bounds__incoming_bound --> infinite_series
  f_incoming_bounds__incoming_bound --> primes_divisibility
  f_incoming_bounds__incoming_bound --> linear_algebra
  f_quot_meas_uniq --> f_wq_unique_of
  f_quot_meas_uniq --> f_weight
  f_quot_meas_uniq --> f_q_lift_is_mul_left_invariant
  f_quot_meas_uniq --> f_qmu_weight
  f_quot_meas_uniq --> f_period_integrals__weil_quot_meas
  f_quot_meas_uniq --> concept_haar_measure_fundamental_domain
  f_orbital_bounds_conclusion__weil_quot_meas --> f_weil_quotient_measure__step_bruhat
  f_orbital_bounds_conclusion__weil_quot_meas --> f_inv_inv
  f_orbital_bounds_conclusion__weil_quot_meas --> f_quot_meas_uniq
  f_orbital_bounds_conclusion__weil_quot_meas --> f_weil_quotient_measure__bruhat
  f_orbital_bounds_conclusion__weil_quot_meas --> f_weil_quotient_measure__lintegral_mul_avg_comm
  f_orbital_bounds_conclusion__weil_quot_meas --> f_period_integrals__weil_quot_meas
  f_orbital_bounds_conclusion__weil_quot_meas --> concept_haar_measure_fundamental_domain
  f_q_lift_is_mul_left_invariant --> f_qmu_weight
  f_q_lift_is_mul_left_invariant --> concept_haar_measure_fundamental_domain
  f_q_lift_is_mul_left_invariant --> concept_normal_subgroups_quotients
  f_q_lift_is_mul_left_invariant --> concept_point_set_topology
  f_q_lift_is_mul_left_invariant --> groups
  f_qmu_weight --> concept_haar_measure_fundamental_domain
  f_qmu_weight --> concept_normal_subgroups_quotients
  f_qmu_weight --> concept_point_set_topology
  f_weight --> f_qmu_weight
  f_weight --> f_q_lift_is_mul_left_invariant
  f_weight --> concept_haar_measure_fundamental_domain
  f_weight --> concept_point_set_topology
  f_weight --> infinite_series
  f_wq_unique_of --> f_qmu_weight
  f_wq_unique_of --> f_period_integrals__weil_quot_meas
  f_wq_unique_of --> concept_haar_measure_fundamental_domain
  f_wq_unique_of --> concept_normal_subgroups_quotients
  f_inv_inv --> f_weil_quotient_measure__step_bruhat
  f_inv_inv --> concept_haar_measure_fundamental_domain
  f_inv_inv --> groups
  f_box_le_first_family --> f_polynomial_derivatives__equiv_lift
  f_box_le_first_family --> f_sym_k_eq_zero_of_om
  f_box_le_first_family --> f_symbol_first_family_of_mem
  f_box_le_first_family --> f_polynomial_derivatives__core_st
  f_box_le_first_family --> f_polynomial_derivatives__fock_mono
  f_box_le_first_family --> f_polynomial_derivatives__null_stable_alt
  f_box_le_first_family --> polynomials
  f_box_le_first_family --> linear_algebra
  f_sym_k_eq_zero_of_om --> f_symbol_first_family_of_mem
  f_sym_k_eq_zero_of_om --> f_zero_right
  f_sym_k_eq_zero_of_om --> f_polynomial_derivatives__core_st
  f_sym_k_eq_zero_of_om --> polynomials
  f_sym_k_eq_zero_of_om --> linear_algebra
  f_sym_k_eq_zero_of_om --> complex_numbers
  f_symbol_first_family_of_mem --> f_polynomial_derivatives__core_st
  f_symbol_first_family_of_mem --> f_polynomial_derivatives__fock_mono
  f_symbol_first_family_of_mem --> polynomials
  f_symbol_first_family_of_mem --> concept_derivations_smoothness
  f_symbol_first_family_of_mem --> linear_algebra
  f_zero_right --> linear_algebra
  f_zero_right --> complex_numbers
  f_lattice_theorem_of_discharge --> f_mahler_measure__statement_t_m
  f_lattice_theorem_of_discharge --> f_trace_isometry_weights__statement_f
  f_lattice_theorem_of_discharge --> f_trace_isometry_weights__statement_g
  f_lattice_theorem_of_discharge --> f_mahler_measure__good_count
  f_lattice_theorem_of_discharge --> f_mahler_measure__statement_t
  f_trace_isometry_weights__statement_c --> f_mahler_measure__cs_saturated
  f_trace_isometry_weights__statement_c --> f_mahler_measure__good_count
  f_trace_isometry_weights__statement_c --> f_mahler_measure__statement
  f_trace_isometry_weights__statement_c --> p_adic_numbers
  f_trace_isometry_weights__statement_c --> polynomials
  f_trace_isometry_weights__statement_f --> f_trace_isometry_weights__statement_c
  f_trace_isometry_weights__statement_f --> f_mahler_measure__good_count
  f_trace_isometry_weights__statement_f --> f_mahler_measure__statement_t
  f_trace_isometry_weights__statement_f --> p_adic_numbers
  f_trace_isometry_weights__statement_g --> f_mahler_measure__statement_t_m
  f_trace_isometry_weights__statement_g --> f_mahler_measure__good_count
  f_trace_isometry_weights__statement_g --> f_mahler_measure__statement_t
  f_trace_isometry_weights__statement_g --> f_mahler_measure__has_order
  f_trace_isometry_weights__statement_g --> p_adic_numbers
  f_trace_isometry_weights__statement_g --> counting
  f_adelic_lattice_proofs__is_quadratic_sqrt_extension_basic_facts --> rings_fields
  f_adelic_lattice_proofs__is_quadratic_sqrt_extension_basic_facts --> linear_algebra
  f_adelic_lattice_proofs__is_quadratic_sqrt_extension_basic_facts --> number_fields
  f_adelic_lattice_proofs__height_one_spectrum_places_over_finite_set --> concept_dedekind_domains
  f_adelic_lattice_proofs__height_one_spectrum_places_over_finite_set --> number_fields
  f_adelic_lattice_proofs__height_one_spectrum_places_over_finite_set --> concept_ideals_and_discriminant
  f_adelic_lattice_proofs__height_one_spectrum_places_over_finite_set --> concept_ultrametric_norm
  f_two_places_of_embeddings --> f_adelic_lattice_proofs__exists_two_places_over_of_is_square_local
  f_two_places_of_embeddings --> concept_ultrametric_norm
  f_two_places_of_embeddings --> p_adic_numbers
  f_two_places_of_embeddings --> concept_dedekind_domains
  f_two_places_of_embeddings --> number_fields
  f_adelic_lattice_proofs__exists_two_places_over_of_is_square_local --> f_adelic_lattice_proofs__is_quadratic_sqrt_extension_basic_facts
  f_adelic_lattice_proofs__exists_two_places_over_of_is_square_local --> f_adelic_hermitian_forms__sq_sub_le_norm_sub
  f_adelic_lattice_proofs__exists_two_places_over_of_is_square_local --> concept_ultrametric_norm
  f_adelic_lattice_proofs__exists_two_places_over_of_is_square_local --> p_adic_numbers
  f_adelic_lattice_proofs__exists_two_places_over_of_is_square_local --> concept_dedekind_domains
  f_adelic_lattice_proofs__exists_two_places_over_of_is_square_local --> number_fields
  f_adelic_lattice_proofs__kummer_galois --> concept_roots_of_unity_kummer
  f_adelic_lattice_proofs__kummer_galois --> concept_galois_fixed_fields
  f_adelic_lattice_proofs__kummer_galois --> concept_field_extensions_transcendence
  f_adelic_lattice_proofs__kummer_galois --> polynomials
  f_adelic_lattice_proofs__kummer_galois --> groups
  f_ncard_places_over_eq_of_prime_degree --> concept_dedekind_domains
  f_ncard_places_over_eq_of_prime_degree --> concept_galois_fixed_fields
  f_ncard_places_over_eq_of_prime_degree --> primes_divisibility
  f_ncard_places_over_eq_of_prime_degree --> number_fields
  f_prime_mul_card_places_le_card_over_kummer --> f_adelic_lattice_proofs__kummer_galois
  f_prime_mul_card_places_le_card_over_kummer --> f_ncard_places_over_eq_of_prime_degree
  f_prime_mul_card_places_le_card_over_kummer --> f_two_places_of_embeddings
  f_prime_mul_card_places_le_card_over_kummer --> f_adelic_lattice_proofs__height_one_spectrum_places_over_finite_set
  f_prime_mul_card_places_le_card_over_kummer --> f_adelic_hermitian_forms__mem_pow_sub
  f_prime_mul_card_places_le_card_over_kummer --> concept_roots_of_unity_kummer
  f_prime_mul_card_places_le_card_over_kummer --> counting
  f_parabolic_induction_trivial_preserves_virtual_charact --> f_character_theory__virtual_characters_mul_comap_conj_ind_linear
  f_parabolic_induction_trivial_preserves_virtual_charact --> f_induced_class_function_from_subgroup_eq_finsum_cosets
  f_parabolic_induction_trivial_preserves_virtual_charact --> f_is_character_finsum_conj_subgroup_function_extend_by_zer
  f_parabolic_induction_trivial_preserves_virtual_charact --> concept_group_representations
  f_parabolic_induction_trivial_preserves_virtual_charact --> concept_group_actions
  f_parabolic_induction_trivial_preserves_virtual_charact --> concept_normal_subgroups_quotients
  f_parabolic_induction_trivial_preserves_virtual_charact --> linear_algebra
  f_parabolic_induction_trivial_preserves_virtual_charact --> counting
  f_statement_p_w --> f_mahler_measure__good_count
  f_statement_p_w --> f_mahler_measure__statement_t
  f_statement_p_w --> f_mahler_measure__level_sum
  f_statement_p_w --> p_adic_numbers
  f_statement_p_w --> real_analysis
  f_dedekind_finite_type_ideal_codimension --> concept_dedekind_domains
  f_dedekind_finite_type_ideal_codimension --> concept_finitely_generated_algebras
  f_dedekind_finite_type_ideal_codimension --> concept_prime_ideals_localization
  f_dedekind_finite_type_ideal_codimension --> linear_algebra
  f_dedekind_finite_type_ideal_codimension --> algebraic_closure
  f_exists_degree_lt_two_correction_simple_zero --> f_dedekind_finite_type_ideal_codimension
  f_exists_degree_lt_two_correction_simple_zero --> concept_dedekind_domains
  f_exists_degree_lt_two_correction_simple_zero --> polynomials
  f_exists_degree_lt_two_correction_simple_zero --> concept_prime_ideals_localization
  f_exists_linear_system_maximal_degree_factorization --> f_norm_degree_bound_polynomial_combination
  f_exists_linear_system_maximal_degree_factorization --> f_exists_degree_lt_two_correction_simple_zero
  f_exists_linear_system_maximal_degree_factorization --> f_exists_squarefree_poly_distinct_zeros_on_curve
  f_exists_linear_system_maximal_degree_factorization --> f_exists_low_degree_coords_mod_mul
  f_exists_linear_system_maximal_degree_factorization --> concept_dedekind_domains
  f_exists_linear_system_maximal_degree_factorization --> linear_algebra
  f_exists_low_degree_coords_mod_mul --> linear_algebra
  f_exists_low_degree_coords_mod_mul --> polynomials
  f_exists_low_degree_coords_mod_mul --> rings_fields
  f_exists_norm_form --> polynomials
  f_exists_norm_form --> linear_algebra
  f_exists_norm_form --> rings_fields
  f_exists_norm_form --> counting
  f_exists_squarefree_poly_distinct_zeros_on_curve --> f_reduced_fibres_almost_all
  f_exists_squarefree_poly_distinct_zeros_on_curve --> concept_dedekind_domains
  f_exists_squarefree_poly_distinct_zeros_on_curve --> concept_separable_polynomials
  f_exists_squarefree_poly_distinct_zeros_on_curve --> algebraic_closure
  f_exists_squarefree_poly_distinct_zeros_on_curve --> polynomials
  f_norm_degree_bound_polynomial_combination --> f_exists_norm_form
  f_norm_degree_bound_polynomial_combination --> polynomials
  f_norm_degree_bound_polynomial_combination --> linear_algebra
  f_reduced_fibres_almost_all --> concept_dedekind_domains
  f_reduced_fibres_almost_all --> concept_separable_polynomials
  f_reduced_fibres_almost_all --> concept_integral_closure_fraction_fields
  f_reduced_fibres_almost_all --> concept_etale_ring_maps
  f_reduced_fibres_almost_all --> polynomials
  f_bad_crit --> f_mahler_measure__good_count
  f_bad_crit --> p_adic_numbers
  f_bad_crit --> concept_valuation_rings
  f_bad_crit --> concept_finitely_generated_abelian_groups
  f_bad_crit --> linear_algebra
  f_jet_harmonics__cas_k_is_symmetric_and_form --> f_jets__sum_io_pr
  f_jet_harmonics__cas_k_is_symmetric_and_form --> f_real_place_analysis__statement_a
  f_jet_harmonics__cas_k_is_symmetric_and_form --> concept_hermitian_unitary_matrices
  f_jet_harmonics__cas_k_is_symmetric_and_form --> linear_algebra
  f_compact_casimir_le_subspace_monotone --> f_jet_harmonics__cas_k_is_symmetric_and_form
  f_compact_casimir_le_subspace_monotone --> f_jet_harmonics__re_inner_le_on_image_of_intertwining
  f_compact_casimir_le_subspace_monotone --> f_jets__sum_io_pr
  f_compact_casimir_le_subspace_monotone --> linear_algebra
  f_lev_subspace_mono --> f_compact_casimir_le_subspace_monotone
  f_lev_subspace_mono --> f_wt_near_le_of_add_dist_le
  f_lev_subspace_mono --> f_jets__sum_io_pr
  f_lev_subspace_mono --> linear_algebra
  f_jet_harmonics__re_inner_le_on_image_of_intertwining --> concept_hermitian_unitary_matrices
  f_jet_harmonics__re_inner_le_on_image_of_intertwining --> linear_algebra
  f_jet_harmonics__re_inner_le_on_image_of_intertwining --> complex_numbers
  f_wt_near_le_of_add_dist_le --> f_jets__sum_io_pr
  f_wt_near_le_of_add_dist_le --> linear_algebra
  f_wt_near_le_of_add_dist_le --> real_analysis
  f_hypersurface_diff_is_preirreducible_of_no_splitting --> concept_schemes_basics
  f_hypersurface_diff_is_preirreducible_of_no_splitting --> concept_point_set_topology
  f_hypersurface_diff_is_preirreducible_of_no_splitting --> concept_finitely_generated_algebras
  f_hypersurface_diff_is_preirreducible_of_no_splitting --> concept_prime_ideals_localization
  f_hypersurface_diff_is_preirreducible_of_no_splitting --> concept_noetherian_and_irreducible_components
  f_hypersurface_part_geometric_irreducible_spreads --> f_no_splitting_factorisation_of_pderiv_ne_zero
  f_hypersurface_part_geometric_irreducible_spreads --> f_splitting_absence_spreads
  f_hypersurface_part_geometric_irreducible_spreads --> f_hypersurface_diff_is_preirreducible_of_no_splitting
  f_hypersurface_part_geometric_irreducible_spreads --> concept_derivations_smoothness
  f_hypersurface_part_geometric_irreducible_spreads --> concept_schemes_basics
  f_no_common_zero_spreads_constructible_nbhd --> concept_finitely_generated_algebras
  f_no_common_zero_spreads_constructible_nbhd --> algebraic_closure
  f_no_common_zero_spreads_constructible_nbhd --> concept_integral_closure_fraction_fields
  f_no_common_zero_spreads_constructible_nbhd --> polynomials
  f_no_splitting_factorisation_of_pderiv_ne_zero --> concept_derivations_smoothness
  f_no_splitting_factorisation_of_pderiv_ne_zero --> concept_schemes_basics
  f_no_splitting_factorisation_of_pderiv_ne_zero --> concept_point_set_topology
  f_no_splitting_factorisation_of_pderiv_ne_zero --> concept_separable_polynomials
  f_preirreducible_fibre_standard_etale_spreads --> f_standard_etale_mv_polynomial_hypersurface
  f_preirreducible_fibre_standard_etale_spreads --> f_preirreducible_space_fibre_hypersurface_spectrum_iff
  f_preirreducible_fibre_standard_etale_spreads --> f_hypersurface_part_geometric_irreducible_spreads
  f_preirreducible_fibre_standard_etale_spreads --> concept_etale_ring_maps
  f_preirreducible_fibre_standard_etale_spreads --> concept_tensor_product_of_algebras
  f_preirreducible_fibre_standard_etale_spreads --> concept_schemes_basics
  f_preirreducible_space_fibre_hypersurface_spectrum_iff --> concept_tensor_product_of_algebras
  f_preirreducible_space_fibre_hypersurface_spectrum_iff --> concept_prime_ideals_localization
  f_preirreducible_space_fibre_hypersurface_spectrum_iff --> concept_schemes_basics
  f_preirreducible_space_fibre_hypersurface_spectrum_iff --> concept_point_set_topology
  f_splitting_absence_spreads --> f_no_common_zero_spreads_constructible_nbhd
  f_splitting_absence_spreads --> polynomials
  f_splitting_absence_spreads --> concept_finitely_generated_algebras
  f_standard_etale_mv_polynomial_hypersurface --> concept_etale_ring_maps
  f_standard_etale_mv_polynomial_hypersurface --> concept_derivations_smoothness
  f_standard_etale_mv_polynomial_hypersurface --> concept_prime_ideals_localization
  f_standard_etale_mv_polynomial_hypersurface --> polynomials
  f_fock_gram_proofs__covol_gram --> concept_lattice_point_counting
  f_fock_gram_proofs__covol_gram --> linear_algebra
  f_fock_gram_proofs__covol_gram --> concept_haar_measure_fundamental_domain
  f_det_sym_pow --> polynomials
  f_det_sym_pow --> linear_algebra
  f_det_sym_pow --> f_statement_fock
  f_fock_herm --> f_statement_fock
  f_fock_herm --> polynomials
  f_fock_herm --> complex_numbers
  f_fock_perm --> f_statement_fock
  f_fock_perm --> polynomials
  f_fock_perm --> counting
  f_fock_sesq --> f_statement_fock
  f_fock_sesq --> polynomials
  f_fock_sesq --> complex_numbers
  f_herm_dual_of --> f_fock_gram__statement_herm
  f_herm_dual_of --> concept_hermitian_unitary_matrices
  f_herm_dual_of --> linear_algebra
  f_herm_dual_of --> concept_lattice_point_counting
  f_hermitian_tensor_mul_hermitian --> f_statement_tensor
  f_hermitian_tensor_mul_hermitian --> f_fock_gram__statement_lat
  f_hermitian_tensor_mul_hermitian --> linear_algebra
  f_hermitian_tensor_mul_hermitian --> concept_flat_modules
  f_sub_index_norm --> concept_lattice_point_counting
  f_sub_index_norm --> linear_algebra
  f_sub_index_norm --> concept_finitely_generated_abelian_groups
  f_statement_fock --> polynomials
  f_statement_fock --> linear_algebra
  f_statement_fock --> complex_numbers
  f_statement_fock --> counting
  f_statement_sym_pos --> f_statement_fock
  f_statement_sym_pos --> concept_hermitian_unitary_matrices
  f_statement_sym_pos --> linear_algebra
  f_statement_tensor --> linear_algebra
  f_statement_tensor --> concept_flat_modules
  f_statement_tensor --> f_fock_gram__statement_lat
  f_sym_gram_pos_semidef --> f_fock_herm
  f_sym_gram_pos_semidef --> f_sub_index_norm
  f_sym_gram_pos_semidef --> f_herm_dual_of
  f_sym_gram_pos_semidef --> f_statement_fock
  f_sym_gram_pos_semidef --> f_statement_sym_pos
  f_sym_gram_pos_semidef --> f_fock_gram__statement_herm
  f_orbital_fiber_card_formula --> f_fib_abs
  f_orbital_fiber_card_formula --> concept_normal_subgroups_quotients
  f_orbital_fiber_card_formula --> groups
  f_orbital_fiber_card_formula --> counting
  f_orbital_fiber_decomposition --> f_fib_abs
  f_orbital_fiber_decomposition --> f_trace_formula_eigenvalues__is_gen_eig
  f_orbital_fiber_decomposition --> concept_group_actions
  f_orbital_fiber_decomposition --> concept_normal_subgroups_quotients
  f_orbital_fiber_of_bot --> f_fib_abs
  f_orbital_fiber_of_bot --> f_trace_formula_eigenvalues__is_gen_eig
  f_orbital_fiber_of_bot --> concept_group_actions
  f_orbital_fiber_pushforward --> f_orbital_fiber_decomposition
  f_orbital_fiber_pushforward --> f_orbital_fiber_pushforward_eq_zero
  f_orbital_fiber_pushforward --> f_fib_abs
  f_orbital_fiber_pushforward --> f_trace_formula_eigenvalues__is_gen_eig
  f_orbital_fiber_pushforward --> concept_group_actions
  f_orbital_fiber_pushforward_eq_zero --> f_fib_abs
  f_orbital_fiber_pushforward_eq_zero --> f_trace_formula_eigenvalues__is_gen_eig
  f_orbital_fiber_pushforward_eq_zero --> concept_group_actions
  f_orbital_fiber_pushforward_eq_zero --> counting
  f_symmetric_fiber_covering --> f_orbital_fiber_card_formula
  f_symmetric_fiber_covering --> f_orbital_fiber_pushforward
  f_symmetric_fiber_covering --> f_orbital_fiber_of_bot
  f_symmetric_fiber_covering --> f_fib_abs
  f_symmetric_fiber_covering --> f_trace_formula_eigenvalues__is_gen_eig
  f_symmetric_fiber_covering --> concept_group_actions
  f_symmetric_fiber_covering --> concept_normal_subgroups_quotients
  f_fib_abs --> f_trace_formula_eigenvalues__is_gen_eig
  f_fib_abs --> concept_group_actions
  f_fib_abs --> concept_normal_subgroups_quotients
  f_fib_abs --> concept_modular_forms
  f_trace_formula_eigenvalues__forms_fin --> f_trace_formula_eigenvalues__is_gen_eig
  f_trace_formula_eigenvalues__forms_fin --> f_symmetric_power_transfer__wcount
  f_trace_formula_eigenvalues__forms_fin --> concept_modular_forms
  f_trace_formula_eigenvalues__forms_fin --> concept_group_actions
  f_trace_formula_eigenvalues__forms_fin --> linear_algebra
  f_trace_formula_eigenvalues__is_gen_eig --> concept_group_actions
  f_trace_formula_eigenvalues__is_gen_eig --> concept_group_representations
  f_trace_formula_eigenvalues__is_gen_eig --> concept_modular_forms
  f_trace_formula_eigenvalues__is_gen_eig --> linear_algebra
  f_trace_formula_eigenvalues__is_gen_eig --> concept_normal_subgroups_quotients
  f_symmetric_power_transfer__wcount --> concept_group_actions
  f_symmetric_power_transfer__wcount --> concept_normal_subgroups_quotients
  f_symmetric_power_transfer__wcount --> rings_fields
  f_global_signature__invariant_radon_fibre --> concept_haar_measure_fundamental_domain
  f_global_signature__invariant_radon_fibre --> concept_normal_subgroups_quotients
  f_global_signature__invariant_radon_fibre --> concept_point_set_topology
  f_global_signature__invariant_radon_fibre --> concept_group_actions
  f_global_signature__invariant_radon_fibre --> real_analysis
  f_exists_bruhat_function_closed_subgroup --> f_global_signature__invariant_radon_fibre
  f_exists_bruhat_function_closed_subgroup --> concept_haar_measure_fundamental_domain
  f_exists_bruhat_function_closed_subgroup --> concept_point_set_topology
  f_exists_bruhat_function_closed_subgroup --> real_analysis
  f_global_interpolation__exists_unique_haar_of_invariant_radon_on_cosets --> f_global_signature__invariant_radon_fibre
  f_global_interpolation__exists_unique_haar_of_invariant_radon_on_cosets --> concept_haar_measure_fundamental_domain
  f_global_interpolation__exists_unique_haar_of_invariant_radon_on_cosets --> concept_point_set_topology
  f_global_interpolation__exists_unique_haar_of_invariant_radon_on_cosets --> real_analysis
  f_quotient_invariant_measure_exists_unique_unimodular --> f_weil_criterion_invariant_measure_homogeneous_space
  f_quotient_invariant_measure_exists_unique_unimodular --> f_global_signature__invariant_radon_fibre
  f_quotient_invariant_measure_exists_unique_unimodular --> concept_haar_measure_fundamental_domain
  f_quotient_invariant_measure_exists_unique_unimodular --> groups
  f_quotient_measure_normalised_by_haar_unique --> f_quotient_invariant_measure_exists_unique_unimodular
  f_quotient_measure_normalised_by_haar_unique --> f_global_interpolation__exists_unique_haar_of_invariant_radon_on_cosets
  f_quotient_measure_normalised_by_haar_unique --> f_global_signature__invariant_radon_fibre
  f_quotient_measure_normalised_by_haar_unique --> concept_haar_measure_fundamental_domain
  f_weil_criterion_invariant_measure_homogeneous_space --> f_exists_bruhat_function_closed_subgroup
  f_weil_criterion_invariant_measure_homogeneous_space --> f_global_interpolation__exists_unique_haar_of_invariant_radon_on_cosets
  f_weil_criterion_invariant_measure_homogeneous_space --> f_global_signature__invariant_radon_fibre
  f_weil_criterion_invariant_measure_homogeneous_space --> concept_haar_measure_fundamental_domain
  f_weil_criterion_invariant_measure_homogeneous_space --> real_analysis
  f_content_distance_bounds --> f_pieri_block_ideals__statement
  f_content_distance_bounds --> primes_divisibility
  f_content_distance_bounds --> counting
  f_content_distance_bounds --> concept_chebyshev_functions
  f_params_window --> f_rank_gap_bounds__cloud_min_false
  f_params_window --> primes_divisibility
  f_params_window --> counting
  f_params_window --> real_analysis
  f_joint_exact_exponent_stop_high --> f_pieri_block_ideals__statement_j
  f_joint_exact_exponent_stop_high --> f_rank_gap_bounds__large_prime_factor
  f_local_component_g_l --> f_content_distance_bounds
  f_local_component_g_l --> f_pieri_block_ideals__statement
  f_local_component_g_l --> modular_arithmetic
  f_local_component_g_l --> primes_divisibility
  f_max_val_eq_zero_of_lt --> f_rank_gap_bounds__cloud_min_false
  f_max_val_eq_zero_of_lt --> primes_divisibility
  f_max_val_eq_zero_of_lt --> counting
  f_pieri_block_ideals__statement --> primes_divisibility
  f_pieri_block_ideals__statement --> counting
  f_pieri_block_ideals__statement --> modular_arithmetic
  f_pieri_block_ideals__statement --> polynomials
  f_pieri_block_ideals__statement --> concept_lattice_point_counting
  f_pieri_block_ideals__statement --> concept_chebyshev_functions
  f_pieri_block_ideals__statement_c --> f_rank_gap_bounds__large_prime_factor
  f_pieri_block_ideals__statement_c --> primes_divisibility
  f_pieri_block_ideals__statement_c --> concept_chebyshev_functions
  f_pieri_block_ideals__statement_j --> f_pieri_block_ideals__statement_c
  f_pieri_block_ideals__statement_j --> f_rank_gap_bounds__large_prime_factor
  f_pieri_block_ideals__statement_j --> f_rank_gap_bounds__cloud_min_false
  f_pieri_block_ideals__statement_j --> f_pieri_block_ideals__statement
  f_rank_gap_bounds__cloud_min_false --> primes_divisibility
  f_rank_gap_bounds__cloud_min_false --> counting
  f_rank_gap_bounds__cloud_min_false --> concept_chebyshev_functions
  f_rank_gap_bounds__large_prime_factor --> concept_chebyshev_functions
  f_rank_gap_bounds__large_prime_factor --> primes_divisibility
  f_rank_gap_bounds__large_prime_factor --> modular_arithmetic
  f_rank_gap_bounds__large_prime_factor --> counting
  f_rank_gap_bounds__large_prime_factor --> infinite_series
  f_card_large_prime_factors_le_one_holds --> f_rank_gap_bounds__large_prime_factor
  f_card_large_prime_factors_le_one_holds --> concept_chebyshev_functions
  f_card_large_prime_factors_le_one_holds --> primes_divisibility
  f_card_large_prime_factors_le_one_holds --> modular_arithmetic
  f_card_large_prime_factors_le_one_holds --> infinite_series
  f_card_large_prime_factors_le_one_holds --> real_analysis
  f_one_letter_gauss_jets__odd_level_gain_sum --> f_incoming_bounds__incoming_bound
  f_one_letter_gauss_jets__odd_level_gain_sum --> modular_arithmetic
  f_one_letter_gauss_jets__odd_level_gain_sum --> infinite_series
  f_one_letter_gauss_jets__odd_level_gain_sum --> primes_divisibility
  f_one_letter_gauss_jets__statement_j --> f_one_letter_gauss_jets__odd_level_gain_sum
  f_one_letter_gauss_jets__statement_j --> f_gauss_jet_bounds__statement_j
  f_one_letter_gauss_jets__statement_j --> f_incoming_bounds__incoming_bound
  f_one_letter_gauss_jets__statement_j --> concept_ultrametric_norm
  f_one_letter_gauss_jets__statement_j --> p_adic_numbers
  f_one_letter_gauss_jets__statement_j --> concept_roots_of_unity_kummer
  f_one_letter_gauss_jets__statement_j --> polynomials
  f_gauss_jet_bounds__statement_j --> f_incoming_bounds__incoming_bound
  f_gauss_jet_bounds__statement_j --> f_gauss_jet_bounds__statement
  f_gauss_jet_bounds__statement_j --> f_gauss_jet_bounds__statement_i
  f_gauss_jet_bounds__statement_j --> concept_ultrametric_norm
  f_gauss_jet_bounds__statement_j --> p_adic_numbers
  f_gauss_jet_bounds__statement_j --> concept_roots_of_unity_kummer
  f_gauss_jet_bounds__statement_j --> polynomials
  f_descend --> f_weil_group_characters__rep_alg
  f_descend --> f_determinant_representations__map_api
  f_descend --> f_determinant_representations__gen_span
  f_descend --> f_determinant_representations__gen_eval
  f_descend --> f_extend_poly
  f_descend --> f_determinant_representations__ext_gen
  f_descend --> f_determinant_representations__inj_test
  f_descend --> rings_fields
  f_descend --> polynomials
  f_determinant_representations__ext_gen --> f_weil_group_characters__rep_alg
  f_determinant_representations__ext_gen --> f_determinant_representations__gen_span
  f_determinant_representations__ext_gen --> f_determinant_representations__gen_eval
  f_determinant_representations__ext_gen --> polynomials
  f_extend_poly --> f_weil_group_characters__rep_alg
  f_extend_poly --> f_lift_indep
  f_extend_poly --> polynomials
  f_extend_poly --> rings_fields
  f_determinant_representations__gen_eval --> f_weil_group_characters__rep_alg
  f_determinant_representations__gen_eval --> polynomials
  f_determinant_representations__gen_span --> f_weil_group_characters__rep_alg
  f_determinant_representations__gen_span --> groups
  f_determinant_representations__gen_span --> rings_fields
  f_determinant_representations__inj_test --> f_weil_group_characters__rep_alg
  f_determinant_representations__inj_test --> f_determinant_representations__ext_gen
  f_determinant_representations__inj_test --> f_determinant_representations__gen_span
  f_determinant_representations__inj_test --> f_determinant_representations__map_api
  f_determinant_representations__inj_test --> polynomials
  f_lift_indep --> f_weil_group_characters__rep_alg
  f_lift_indep --> polynomials
  f_determinant_representations__map_api --> f_weil_group_characters__rep_alg
  f_determinant_representations__map_api --> polynomials
  f_determinant_representations__map_api --> rings_fields
  f_commutative_algebra__res_map_bijective --> concept_local_rings
  f_commutative_algebra__res_map_bijective --> concept_adic_completion
  f_commutative_algebra__res_map_bijective --> concept_group_representations
  f_commutative_algebra__res_map_bijective --> concept_dual_numbers
  f_commutative_algebra__res_map_bijective --> rings_fields
  f_weil_group_characters__rep_alg --> f_commutative_algebra__res_map_bijective
  f_weil_group_characters__rep_alg --> concept_group_representations
  f_weil_group_characters__rep_alg --> concept_tensor_product_of_algebras
  f_weil_group_characters__rep_alg --> groups
  f_weil_group_characters__rep_alg --> linear_algebra
  f_weil_group_characters__rep_alg --> polynomials
  f_metric_periods__has_multiplier --> f_birational_geometry__arithmetic_hilbert_samuel_lower_bound
  f_metric_periods__has_multiplier --> f_birational_geometry__is_intersection_family
  f_metric_periods__has_multiplier --> f_birational_geometry__is_semipositive_on
  f_metric_periods__has_multiplier --> f_birational_geometry__pen_host
  f_metric_periods__has_multiplier --> number_fields
  f_metric_periods__has_multiplier --> p_adic_numbers
  f_metric_periods__has_multiplier --> algebraic_closure
  f_metric_proofs__hermitian_line_shift_properties --> f_rational_sup_metrics__hermitian_line_shift_properties
  f_metric_proofs__hermitian_line_shift_properties --> f_metric_periods__has_multiplier
  f_metric_proofs__hermitian_line_shift_properties --> f_birational_geometry__is_intersection_family
  f_aeval_eq_zero_of_mem --> concept_point_set_topology
  f_aeval_eq_zero_of_mem --> complex_numbers
  f_rational_sup_metrics__hermitian_line_shift_properties --> f_aeval_eq_zero_of_mem
  f_rational_sup_metrics__hermitian_line_shift_properties --> f_metric_periods__has_multiplier
  f_rational_sup_metrics__hermitian_line_shift_properties --> f_birational_geometry__is_semipositive_on
  f_rational_sup_metrics__hermitian_line_shift_properties --> f_birational_geometry__is_intersection_family
  f_rational_sup_metrics__hermitian_line_shift_properties --> calculus
  f_birational_geometry__arithmetic_hilbert_samuel_lower_bound --> f_birational_geometry__is_intersection_family
  f_birational_geometry__arithmetic_hilbert_samuel_lower_bound --> f_birational_geometry__is_semipositive_on
  f_birational_geometry__arithmetic_hilbert_samuel_lower_bound --> f_birational_geometry__pen_vol
  f_birational_geometry__arithmetic_hilbert_samuel_lower_bound --> concept_lattice_point_counting
  f_birational_geometry__arithmetic_hilbert_samuel_lower_bound --> concept_integral_closure_fraction_fields
  f_birational_geometry__is_intersection_family --> concept_coordinate_rings_dimension
  f_birational_geometry__is_intersection_family --> concept_prime_ideals_localization
  f_birational_geometry__is_intersection_family --> concept_noetherian_and_irreducible_components
  f_birational_geometry__is_intersection_family --> polynomials
  f_birational_geometry__is_intersection_family --> complex_numbers
  f_birational_geometry__is_semipositive_on --> concept_hermitian_unitary_matrices
  f_birational_geometry__is_semipositive_on --> number_fields
  f_birational_geometry__is_semipositive_on --> calculus
  f_birational_geometry__is_semipositive_on --> complex_numbers
  f_birational_geometry__is_semipositive_on --> linear_algebra
  f_birational_geometry__pen_host --> f_birational_geometry__arithmetic_hilbert_samuel_lower_bound
  f_birational_geometry__pen_host --> f_birational_geometry__is_intersection_family
  f_birational_geometry__pen_host --> f_birational_geometry__is_semipositive_on
  f_birational_geometry__pen_host --> number_fields
  f_birational_geometry__pen_vol --> f_birational_geometry__is_semipositive_on
  f_birational_geometry__pen_vol --> concept_lattice_point_counting
  f_birational_geometry__pen_vol --> polynomials
  f_p_hol_germs_domain --> concept_complex_analytic_sets
  f_p_hol_germs_domain --> complex_analysis
  f_p_hol_germs_domain --> rings_fields
  f_st_germ_weierstrass_preparation --> concept_complex_analytic_sets
  f_st_germ_weierstrass_preparation --> complex_analysis
  f_st_germ_weierstrass_preparation --> polynomials
  f_weierstrass_polynomial_ring --> f_st_germ_weierstrass_preparation
  f_weierstrass_polynomial_ring --> f_weierstrass_remainder_unique
  f_weierstrass_polynomial_ring --> f_p_hol_germs_domain
  f_weierstrass_polynomial_ring --> concept_complex_analytic_sets
  f_weierstrass_polynomial_ring --> polynomials
  f_weierstrass_polynomial_ring --> concept_local_rings
  f_weierstrass_remainder_unique --> f_st_germ_weierstrass_preparation
  f_weierstrass_remainder_unique --> concept_complex_analytic_sets
  f_weierstrass_remainder_unique --> polynomials
  f_weierstrass_remainder_unique --> complex_analysis
  f_weierstrass_remainder_unique --> real_analysis
  f_exists_value_basis --> f_formally_smooth_section_stalk
  f_exists_value_basis --> f_formally_smooth_surjective_derivation
  f_exists_value_basis --> f_one_left_congr
  f_exists_value_basis --> f_span_linear_independent_base
  f_exists_value_basis --> f_global_geometry__lie_model
  f_exists_value_basis --> f_global_geometry__is_cpt_gen
  f_exists_value_basis --> f_global_geometry__etale_localization_at_prime_tensor_of_low_height
  f_exists_value_basis --> f_global_geometry__eig_lat
  f_exists_value_basis --> concept_group_schemes
  f_exists_value_basis --> concept_dual_numbers
  f_exists_value_basis --> concept_schemes_basics
  f_formally_smooth_section_stalk --> concept_smooth_morphisms
  f_formally_smooth_section_stalk --> concept_schemes_basics
  f_formally_smooth_section_stalk --> concept_local_rings
  f_formally_smooth_section_stalk --> concept_dual_numbers
  f_formally_smooth_surjective_derivation --> concept_derivations_smoothness
  f_formally_smooth_surjective_derivation --> concept_dual_numbers
  f_formally_smooth_surjective_derivation --> concept_flat_modules
  f_formally_smooth_surjective_derivation --> concept_local_rings
  f_formally_smooth_surjective_derivation --> concept_smooth_morphisms
  f_formally_smooth_surjective_derivation --> linear_algebra
  f_one_left_congr --> concept_group_schemes
  f_one_left_congr --> concept_dual_numbers
  f_one_left_congr --> concept_schemes_basics
  f_one_left_congr --> concept_categorical_pullbacks
  f_span_linear_independent_base --> linear_algebra
  f_span_linear_independent_base --> rings_fields
  f_norm_iterated_f_deriv_rem_comp_le --> concept_schwartz_functions
  f_norm_iterated_f_deriv_rem_comp_le --> calculus
  f_norm_iterated_f_deriv_rem_comp_le --> real_analysis
  f_norm_iterated_f_deriv_rem_comp_le --> complex_numbers
  f_norm_iterated_f_deriv_rem_comp_le --> linear_algebra
  f_schwartz_family_phase_bound --> f_norm_iterated_f_deriv_rem_comp_le
  f_schwartz_family_phase_bound --> concept_schwartz_functions
  f_schwartz_family_phase_bound --> real_analysis
  f_schwartz_family_phase_bound --> calculus
  f_schwartz_fourier_representation --> fourier_analysis
  f_schwartz_fourier_representation --> concept_schwartz_functions
  f_schwartz_fourier_representation --> linear_algebra
  f_schwartz_inner_product_continuous --> concept_schwartz_functions
  f_schwartz_inner_product_continuous --> concept_haar_measure_fundamental_domain
  f_schwartz_inner_product_continuous --> real_analysis
  f_schwartz_integral_superposition --> concept_schwartz_functions
  f_schwartz_integral_superposition --> calculus
  f_schwartz_integral_superposition --> real_analysis
  f_schwartz_integral_superposition --> linear_algebra
  f_translation_character_invariant_form --> f_schwartz_fourier_representation
  f_translation_character_invariant_form --> f_schwartz_family_phase_bound
  f_translation_character_invariant_form --> f_schwartz_inner_product_continuous
  f_translation_character_invariant_form --> f_schwartz_integral_superposition
  f_translation_character_invariant_form --> concept_schwartz_functions
  f_translation_character_invariant_form --> fourier_analysis
  f_translation_character_invariant_form --> concept_haar_measure_fundamental_domain
  f_first_lemma_f --> f_jets_ph_w
  f_first_lemma_f --> concept_ultrametric_norm
  f_first_lemma_f --> p_adic_numbers
  f_first_lemma_f --> polynomials
  f_first_lemma_g --> f_jets_ph_w
  f_first_lemma_g --> concept_ultrametric_norm
  f_first_lemma_g --> p_adic_numbers
  f_first_lemma_g --> calculus
  f_imports_ter_alt --> concept_ultrametric_norm
  f_imports_ter_alt --> p_adic_numbers
  f_imports_ter_alt --> rings_fields
  f_int_mv_pderiv --> concept_ultrametric_norm
  f_int_mv_pderiv --> p_adic_numbers
  f_int_mv_pderiv --> calculus
  f_capelli_identities__integral_mv --> concept_ultrametric_norm
  f_capelli_identities__integral_mv --> p_adic_numbers
  f_integral_polynomial_fifth --> concept_ultrametric_norm
  f_integral_polynomial_fifth --> p_adic_numbers
  f_integral_polynomial_fifth --> algebraic_closure
  f_integral_polynomial_fifth --> polynomials
  f_integral_polynomial_first --> concept_ultrametric_norm
  f_integral_polynomial_first --> p_adic_numbers
  f_integral_polynomial_fourth --> concept_ultrametric_norm
  f_integral_polynomial_fourth --> p_adic_numbers
  f_integral_polynomial_second --> concept_ultrametric_norm
  f_integral_polynomial_second --> p_adic_numbers
  f_integral_polynomial_sixth --> concept_ultrametric_norm
  f_integral_polynomial_sixth --> p_adic_numbers
  f_integral_polynomial_third --> concept_ultrametric_norm
  f_integral_polynomial_third --> p_adic_numbers
  f_capelli_identities__is_integral_nat_cast --> concept_ultrametric_norm
  f_capelli_identities__is_integral_nat_cast --> p_adic_numbers
  f_unit_ball --> concept_ultrametric_norm
  f_unit_ball --> p_adic_numbers
  f_unit_ball --> rings_fields
  f_jets_ph_w --> concept_ultrametric_norm
  f_jets_ph_w --> p_adic_numbers
  f_jets_ph_w --> polynomials
  f_jets_ph_w --> infinite_series
  f_jets_ph_w --> calculus
  f_jet_integrality__exp_log --> f_jets_ph_w
  f_jet_integrality__exp_log --> f_imports_ter_alt
  f_jet_integrality__exp_log --> f_capelli_identities__is_integral_nat_cast
  f_jet_integrality__exp_log --> f_integral_polynomial_sixth
  f_jet_integrality__exp_log --> f_capelli_identities__integral_mv
  f_jet_integrality__exp_log --> f_integral_polynomial_first
  f_jet_integrality__exp_log --> f_integral_polynomial_fourth
  f_jet_integrality__exp_log --> f_integral_polynomial_second
  f_jet_integrality__exp_log --> f_integral_polynomial_third
  f_jet_integrality__exp_log --> f_integral_polynomial_fifth
  f_jet_integrality__exp_log --> f_int_mv_pderiv
  f_jet_integrality__exp_log --> f_unit_ball
  f_jet_integrality__exp_log --> calculus
  f_period_integrals__fold_d_c_unfold --> concept_haar_measure_fundamental_domain
  f_period_integrals__fold_d_c_unfold --> concept_normal_subgroups_quotients
  f_period_integrals__fold_d_c_unfold --> concept_group_actions
  f_period_integrals__fold_d_c_unfold --> f_haar_transversals__fold_bound
  f_period_integrals__fold_d_c_unfold --> f_haar_transversals__poincare_series_square_integrable
  f_orbital_bounds_conclusion__fold_d_c_unfold --> f_period_integrals__fold_d_c_unfold
  f_orbital_bounds_conclusion__fold_d_c_unfold --> f_fold_d_c_unfold_of
  f_orbital_bounds_conclusion__fold_d_c_unfold --> f_translation_independent
  f_orbital_bounds_conclusion__fold_d_c_unfold --> f_double_coset_translation
  f_orbital_bounds_conclusion__fold_d_c_unfold --> f_trans_exists
  f_orbital_bounds_conclusion__fold_d_c_unfold --> f_orbital_bounds_conclusion__fold_unfold
  f_orbital_bounds_conclusion__fold_d_c_unfold --> concept_haar_measure_fundamental_domain
  f_complex_double_coset --> f_cplx_d_c
  f_complex_double_coset --> f_orbital_bounds_conclusion__fold_d_c_unfold
  f_complex_double_coset --> concept_haar_measure_fundamental_domain
  f_complex_double_coset --> complex_numbers
  f_complex_double_coset --> infinite_series
  f_complex_double_coset --> real_analysis
  f_cplx_d_c --> concept_haar_measure_fundamental_domain
  f_cplx_d_c --> concept_normal_subgroups_quotients
  f_cplx_d_c --> f_haar_transversals__fold_bound
  f_cplx_d_c --> f_haar_transversals__poincare_series_square_integrable
  f_cplx_d_c --> complex_numbers
  f_double_coset_translation --> f_trans_exists
  f_double_coset_translation --> f_haar_transversals__fold_bound
  f_double_coset_translation --> f_haar_transversals__poincare_series_square_integrable
  f_double_coset_translation --> concept_normal_subgroups_quotients
  f_double_coset_translation --> groups
  f_fold_d_c_unfold_of --> f_trans_exists
  f_fold_d_c_unfold_of --> f_period_integrals__fold_unfold
  f_fold_d_c_unfold_of --> f_period_integrals__fold_d_c_unfold
  f_fold_d_c_unfold_of --> concept_haar_measure_fundamental_domain
  f_fold_d_c_unfold_of --> concept_normal_subgroups_quotients
  f_trans_exists --> concept_normal_subgroups_quotients
  f_trans_exists --> concept_group_actions
  f_trans_exists --> f_haar_transversals__fold_bound
  f_trans_exists --> f_haar_transversals__poincare_series_square_integrable
  f_translation_independent --> f_trans_exists
  f_translation_independent --> concept_normal_subgroups_quotients
  f_translation_independent --> concept_group_actions
  f_translation_independent --> groups
  f_translation_independent --> infinite_series
  f_global_geometry__is_cochar_lie --> f_global_geometry__lie_model
  f_global_geometry__is_cochar_lie --> f_split_tori__split_torus_aff
  f_global_geometry__is_cochar_lie --> concept_group_schemes
  f_global_geometry__is_cochar_lie --> concept_dual_numbers
  f_global_geometry__is_cochar_lie --> concept_schemes_basics
  f_global_geometry__is_cochar_lie --> concept_categorical_pullbacks
  f_lie_chart --> f_global_geometry__lie_model
  f_lie_chart --> concept_group_schemes
  f_lie_chart --> concept_schemes_basics
  f_lie_chart --> concept_flat_modules
  f_lie_chart --> concept_prime_ideals_localization
  f_lie_chart --> concept_dual_numbers
  f_toroidal_compactification__is_grp_pullback --> f_cubical_structures__cube_symmetric_swap_first
  f_toroidal_compactification__is_grp_pullback --> f_abelian_scheme_quotients__is_abelian_scheme
  f_toroidal_compactification__is_grp_pullback --> concept_group_schemes
  f_toroidal_compactification__is_grp_pullback --> concept_categorical_pullbacks
  f_toroidal_compactification__is_grp_pullback --> concept_schemes_basics
  f_toroidal_compactification__is_grp_pullback --> concept_picard_group
  f_cubical_structures__cube_symmetric_swap_first --> concept_schemes_basics
  f_cubical_structures__cube_symmetric_swap_first --> concept_group_schemes
  f_cubical_structures__cube_symmetric_swap_first --> concept_picard_group
  f_cubical_structures__cube_symmetric_swap_first --> concept_categorical_pullbacks
  f_cubical_structures__cubical_pull_base_change_st --> f_cubical_structures__cube_symmetric_swap_first
  f_cubical_structures__cubical_pull_base_change_st --> concept_group_schemes
  f_cubical_structures__cubical_pull_base_change_st --> concept_picard_group
  f_cubical_structures__cubical_pull_base_change_st --> concept_categorical_pullbacks
  f_eventually_finite_base_change_filtered_colimit --> concept_filtered_colimits
  f_eventually_finite_base_change_filtered_colimit --> concept_tensor_product_of_algebras
  f_eventually_finite_base_change_filtered_colimit --> concept_finitely_generated_algebras
  f_eventually_finite_base_change_filtered_colimit --> concept_integral_closure_fraction_fields
  f_eventually_finite_base_change_filtered_colimit --> polynomials
  f_exists_presentation_matrix_of_projective_base_change --> concept_projective_modules
  f_exists_presentation_matrix_of_projective_base_change --> concept_flat_modules
  f_exists_presentation_matrix_of_projective_base_change --> concept_tensor_product_of_algebras
  f_exists_presentation_matrix_of_projective_base_change --> linear_algebra
  f_gen_fib_map_algebra_map --> concept_prime_ideals_localization
  f_gen_fib_map_algebra_map --> rings_fields
  f_is_z_mod_torsor_iff --> concept_filtered_colimits
  f_is_z_mod_torsor_iff --> concept_group_actions
  f_is_z_mod_torsor_iff --> concept_tensor_product_of_algebras
  f_is_z_mod_torsor_iff --> modular_arithmetic
  f_polynomial_system_eventually_solvable_colimit --> f_is_z_mod_torsor_iff
  f_polynomial_system_eventually_solvable_colimit --> concept_filtered_colimits
  f_polynomial_system_eventually_solvable_colimit --> polynomials
  f_polynomial_system_eventually_solvable_colimit --> rings_fields
  f_projective_base_change_of_presentation_matrix_split --> concept_projective_modules
  f_projective_base_change_of_presentation_matrix_split --> concept_tensor_product_of_algebras
  f_projective_base_change_of_presentation_matrix_split --> linear_algebra
  f_projective_eventually_filtered_colimit_algebra --> f_eventually_finite_base_change_filtered_colimit
  f_projective_eventually_filtered_colimit_algebra --> f_exists_presentation_matrix_of_projective_base_change
  f_projective_eventually_filtered_colimit_algebra --> f_polynomial_system_eventually_solvable_colimit
  f_projective_eventually_filtered_colimit_algebra --> f_projective_base_change_of_presentation_matrix_split
  f_projective_eventually_filtered_colimit_algebra --> concept_filtered_colimits
  f_projective_eventually_filtered_colimit_algebra --> concept_projective_modules
  f_projective_eventually_filtered_colimit_algebra --> concept_tensor_product_of_algebras
  f_divisor_proofs__torsors_trivial_iff --> f_divisor_proofs__torsors_trivial
  f_divisor_proofs__torsors_trivial_iff --> concept_etale_ring_maps
  f_divisor_proofs__torsors_trivial_iff --> concept_flat_modules
  f_divisor_proofs__torsors_trivial_iff --> concept_group_actions
  f_divisor_proofs__torsors_trivial_iff --> concept_prime_ideals_localization
  f_divisor_proofs__torsors_trivial_iff --> concept_projective_modules
  f_k_h_free_bad_finite_st --> f_kleiman_ampleness__k_h_free_obj
  f_k_h_free_bad_finite_st --> counting
  f_kleiman_ampleness__k_h_free_obj --> f_kleiman_nefness__alg_defs
  f_kleiman_ampleness__k_h_free_obj --> concept_chain_complexes_homology
  f_kleiman_ampleness__k_h_free_obj --> concept_prime_ideals_localization
  f_kleiman_ampleness__k_h_free_obj --> polynomials
  f_p_k_h_free_bad_finite --> f_k_h_free_bad_finite_st
  f_p_k_h_free_bad_finite --> f_kleiman_ampleness__k_h_free_obj
  f_p_k_h_free_bad_finite --> counting
  f_kleiman_nefness__alg_defs --> concept_chain_complexes_homology
  f_kleiman_nefness__alg_defs --> concept_prime_ideals_localization
  f_kleiman_nefness__alg_defs --> polynomials
  f_kleiman_nefness__alg_defs --> concept_flat_modules
  f_kleiman_nefness__alg_s_free_st --> f_kleiman_nefness__alg_defs
  f_kleiman_nefness__alg_s_free_st --> f_kleiman_nefness__ample_st
  f_kleiman_nefness__alg_s_free_st --> concept_chain_complexes_homology
  f_kleiman_nefness__alg_s_free_st --> concept_ample_nef_line_bundles
  f_kleiman_nefness__alg_s_free_st --> concept_finitely_generated_algebras
  f_kleiman_nefness__ample_st --> f_kleiman_nefness__alg_defs
  f_kleiman_nefness__ample_st --> f_kleiman_nefness__kleiman_st
  f_kleiman_nefness__ample_st --> f_multihomogeneous_ideals__is_field_intersection
  f_kleiman_nefness__ample_st --> concept_ample_nef_line_bundles
  f_kleiman_nefness__ample_st --> concept_chain_complexes_homology
  f_kleiman_nefness__kleiman_st --> f_multihomogeneous_ideals__is_field_intersection
  f_kleiman_nefness__kleiman_st --> f_birational_geometry__is_intersection_family
  f_kleiman_nefness__kleiman_st --> concept_ample_nef_line_bundles
  f_kleiman_nefness__kleiman_st --> concept_coordinate_rings_dimension
  f_multihomogeneous_ideals__is_field_intersection --> f_birational_geometry__is_intersection_family
  f_multihomogeneous_ideals__is_field_intersection --> concept_coordinate_rings_dimension
  f_multihomogeneous_ideals__is_field_intersection --> concept_prime_ideals_localization
  f_multihomogeneous_ideals__is_field_intersection --> concept_ample_nef_line_bundles
  f_multihomogeneous_ideals__is_field_intersection --> polynomials
  f_period_integrals__explicit_formula --> dirichlet_characters
  f_period_integrals__explicit_formula --> dirichlet_l_function
  f_period_integrals__explicit_formula --> primitive_characters
  f_period_integrals__explicit_formula --> complex_powers
  f_period_integrals__explicit_formula --> rh_statement
  f_explicit_formula__good_height_exists --> f_period_integrals__explicit_formula
  f_explicit_formula__good_height_exists --> dirichlet_l_function
  f_explicit_formula__good_height_exists --> primitive_characters
  f_explicit_formula__good_height_exists --> complex_analysis
  f_explicit_formula__good_height_exists --> complex_powers
  f_l_growth_defs --> zeta_series
  f_l_growth_defs --> analytic_continuation
  f_l_growth_defs --> complex_analysis
  f_l_growth_gamma --> gamma_function
  f_l_growth_gamma --> complex_analysis
  f_l_growth_gamma --> trigonometry
  f_l_growth_gamma --> real_analysis
  f_l_growth_f_e --> f_l_growth_gamma
  f_l_growth_f_e --> functional_equation_dirichlet
  f_l_growth_f_e --> gamma_function
  f_l_growth_f_e --> primitive_characters
  f_l_growth_f_e --> dirichlet_l_function
  f_l_growth_f_e --> complex_powers
  f_l_growth_zeta --> f_l_growth_f_e
  f_l_growth_zeta --> f_l_growth_defs
  f_l_growth_zeta --> zeta_series
  f_l_growth_zeta --> analytic_continuation
  f_l_growth_zeta --> functional_equation_zeta
  f_l_growth_zeta --> complex_analysis
  f_l_growth_zeta --> f_period_integrals__zeros_window_in
  f_l_growth_main --> f_l_growth_f_e
  f_l_growth_main --> f_l_growth_defs
  f_l_growth_main --> f_explicit_formula__good_height_exists
  f_l_growth_main --> f_period_integrals__zeros_window_in
  f_l_growth_main --> dirichlet_l_function
  f_l_growth_main --> primitive_characters
  f_l_growth_final --> f_l_growth_main
  f_l_growth_final --> f_l_growth_zeta
  f_l_growth_final --> f_explicit_formula__good_height_exists
  f_l_growth_final --> f_period_integrals__zeros_window_in
  f_foundations__not_coboundary_constant_one --> concept_adic_completion
  f_foundations__not_coboundary_constant_one --> p_adic_numbers
  f_foundations__not_coboundary_constant_one --> concept_roots_of_unity_kummer
  f_foundations__not_coboundary_constant_one --> concept_galois_fixed_fields
  f_foundations__not_coboundary_constant_one --> algebraic_closure
  f_foundations__not_coboundary_constant_one --> concept_integral_closure_fraction_fields
  f_foundations__not_coboundary_constant_one --> concept_derivations_smoothness
  f_laurent_series_eq_sum_single_mul_pow --> concept_frobenius_perfect_rings
  f_laurent_series_eq_sum_single_mul_pow --> modular_arithmetic
  f_laurent_series_eq_sum_single_mul_pow --> infinite_series
  f_laurent_series_eq_sum_single_mul_pow --> rings_fields
  f_laurent_series_padic_exists_pth_power_combination --> f_laurent_series_eq_sum_single_mul_pow
  f_laurent_series_padic_exists_pth_power_combination --> f_foundations__not_coboundary_constant_one
  f_laurent_series_padic_exists_pth_power_combination --> p_adic_numbers
  f_laurent_series_padic_exists_pth_power_combination --> modular_arithmetic
  f_p_adic_completion_laurent_eq_sum_pth_powers_mod_p --> f_laurent_series_padic_exists_pth_power_combination
  f_p_adic_completion_laurent_eq_sum_pth_powers_mod_p --> f_foundations__not_coboundary_constant_one
  f_p_adic_completion_laurent_eq_sum_pth_powers_mod_p --> concept_adic_completion
  f_frobenius_surjective_mod_prime_cyclotomic_kummer_tower --> f_foundations__not_coboundary_constant_one
  f_frobenius_surjective_mod_prime_cyclotomic_kummer_tower --> f_p_adic_completion_laurent_eq_sum_pth_powers_mod_p
  f_frobenius_surjective_mod_prime_cyclotomic_kummer_tower --> concept_frobenius_perfect_rings
  f_frobenius_surjective_mod_prime_cyclotomic_kummer_tower --> concept_roots_of_unity_kummer
  f_cusp_span_norm_bounds__psi_e_def --> number_fields
  f_cusp_span_norm_bounds__psi_e_def --> p_adic_numbers
  f_cusp_span_norm_bounds__psi_e_def --> concept_dedekind_domains
  f_cusp_span_norm_bounds__psi_e_def --> concept_valuation_rings
  f_cusp_span_norm_bounds__psi_e_def --> concept_ultrametric_norm
  f_cusp_span_norm_bounds__psi_e_def --> concept_integral_closure_fraction_fields
  f_period_integrals__tr_dual_loc --> f_cusp_span_norm_bounds__psi_e_def
  f_period_integrals__tr_dual_loc --> number_fields
  f_period_integrals__tr_dual_loc --> p_adic_numbers
  f_period_integrals__tr_dual_loc --> concept_ultrametric_norm
  f_period_integrals__tr_dual_loc --> concept_valuation_rings
  f_period_integrals__tr_dual_loc --> concept_ideals_and_discriminant
  f_period_integrals__tr_dual_loc --> concept_dedekind_domains
  f_d_surj_def --> concept_tensor_product_of_algebras
  f_d_surj_def --> number_fields
  f_d_surj_def --> p_adic_numbers
  f_d_surj_def --> concept_ultrametric_norm
  f_t2_space_of_nonarchimedean_local_field --> f_d_surj_def
  f_t2_space_of_nonarchimedean_local_field --> concept_point_set_topology
  f_t2_space_of_nonarchimedean_local_field --> linear_algebra
  f_t2_space_of_nonarchimedean_local_field --> concept_tensor_product_of_algebras
  f_t2_space_of_nonarchimedean_local_field --> concept_ultrametric_norm
  f_trace_of_ker --> linear_algebra
  f_trace_of_ker --> rings_fields
  f_trace_of_ker --> concept_tensor_product_of_algebras
  f_is_integral_of_tmul_mem --> number_fields
  f_is_integral_of_tmul_mem --> p_adic_numbers
  f_is_integral_of_tmul_mem --> concept_integral_closure_fraction_fields
  f_is_integral_of_tmul_mem --> concept_tensor_product_of_algebras
  f_is_integral_of_tmul_mem --> concept_finitely_generated_abelian_groups
  f_trace_dual_local__is_integral_nat_cast --> f_is_integral_of_tmul_mem
  f_trace_dual_local__is_integral_nat_cast --> number_fields
  f_trace_dual_local__is_integral_nat_cast --> p_adic_numbers
  f_trace_dual_local__is_integral_nat_cast --> concept_integral_closure_fraction_fields
  f_trace_dual_local__imports --> f_trace_of_ker
  f_trace_dual_local__imports --> f_d_surj_def
  f_trace_dual_local__imports --> f_is_integral_of_tmul_mem
  f_trace_dual_local__imports --> f_trace_dual_local__is_integral_nat_cast
  f_trace_dual_local__imports --> f_t2_space_of_nonarchimedean_local_field
  f_trace_dual_local__imports --> number_fields
  f_trace_dual_local__imports --> concept_ideals_and_discriminant
  f_trace_dual_local__imports --> concept_point_set_topology
  f_trace_dual_local__imports --> linear_algebra
  f_orbital_bounds_conclusion__tr_dual_loc --> f_period_integrals__tr_dual_loc
  f_orbital_bounds_conclusion__tr_dual_loc --> f_trace_dual_local__imports
  f_orbital_bounds_conclusion__tr_dual_loc --> f_t2_space_of_nonarchimedean_local_field
  f_orbital_bounds_conclusion__tr_dual_loc --> f_d_surj_def
  f_orbital_bounds_conclusion__tr_dual_loc --> f_cusp_span_norm_bounds__psi_e_def
  f_cusp_span_norm_bounds__point --> linear_algebra
  f_cusp_span_norm_bounds__fraction_field_to_generic_stalk_algebra_map_eq --> f_cusp_span_norm_bounds__point
  f_cusp_span_norm_bounds__fraction_field_to_generic_stalk_algebra_map_eq --> p_adic_numbers
  f_cusp_span_norm_bounds__fraction_field_to_generic_stalk_algebra_map_eq --> concept_haar_measure_fundamental_domain
  f_cusp_span_norm_bounds__fraction_field_to_generic_stalk_algebra_map_eq --> concept_valuation_rings
  f_cusp_span_norm_bounds__fraction_field_to_generic_stalk_algebra_map_eq --> linear_algebra
  f_cusp_span_norm_bounds__fraction_field_to_generic_stalk_algebra_map_eq --> concept_ultrametric_norm
  f_twisted_trace_formula__inverse_chamber_map --> linear_algebra
  f_twisted_trace_formula__inverse_chamber_map --> concept_point_set_topology
  f_twisted_trace_formula__inverse_chamber_map --> concept_hermitian_unitary_matrices
  f_root_decompose_orthogonal --> f_twisted_trace_formula__inverse_chamber_map
  f_root_decompose_orthogonal --> linear_algebra
  f_gram_det_option_formula --> linear_algebra
  f_projection_erase_root_formula --> f_twisted_trace_formula__inverse_chamber_map
  f_projection_erase_root_formula --> linear_algebra
  f_exists_root_involution_parabolic --> f_twisted_trace_formula__inverse_chamber_map
  f_exists_root_involution_parabolic --> counting
  f_gram_root_determinant_erase --> f_root_decompose_orthogonal
  f_gram_root_determinant_erase --> f_gram_det_option_formula
  f_gram_root_determinant_erase --> f_twisted_trace_formula__inverse_chamber_map
  f_gram_root_determinant_erase --> linear_algebra
  f_parabolic_residue_sum_zero --> f_exists_root_involution_parabolic
  f_parabolic_residue_sum_zero --> f_gram_root_determinant_erase
  f_parabolic_residue_sum_zero --> f_projection_erase_root_formula
  f_parabolic_residue_sum_zero --> f_twisted_trace_formula__inverse_chamber_map
  f_parabolic_residue_sum_zero --> counting
  f_parabolic_residue_sum_zero --> linear_algebra
  f_commutative_algebra__flag_minor --> linear_algebra
  f_commutative_algebra__flag_minor --> concept_prime_ideals_localization
  f_commutative_algebra__flag_minor --> concept_valuation_rings
  f_commutative_algebra__flag_minor --> rings_fields
  f_commutative_algebra__lie_lattice_data --> f_commutative_algebra__flag_minor
  f_commutative_algebra__lie_lattice_data --> linear_algebra
  f_commutative_algebra__lie_lattice_data --> concept_valuation_rings
  f_commutative_algebra__lie_lattice_data --> concept_adic_completion
  f_commutative_algebra__lie_lattice_data --> algebraic_closure
  f_x_pt_seq_lin --> f_commutative_algebra__lie_lattice_data
  f_x_pt_seq_lin --> f_commutative_algebra__flag_minor
  f_x_pt_seq_lin --> linear_algebra
  f_hodge_kernel_image_lattice --> f_x_pt_seq_lin
  f_hodge_kernel_image_lattice --> f_commutative_algebra__lie_lattice_data
  f_hodge_kernel_image_lattice --> f_commutative_algebra__flag_minor
  f_algebra_statements__polarised_flag_statement --> f_commutative_algebra__is_tight
  f_algebra_statements__polarised_flag_statement --> f_commutative_algebra__step_order_res
  f_algebra_statements__polarised_flag_statement --> f_dual_lattices__tensor_span
  f_algebra_statements__polarised_flag_statement --> f_dual_lattices__cotangent_surjective
  f_algebra_statements__polarised_flag_statement --> concept_valuation_rings
  f_algebra_statements__polarised_flag_statement --> concept_frobenius_perfect_rings
  f_algebra_statements__polarised_flag_statement --> dirichlet_characters
  f_herbrand_prime_order --> f_index_range_ker_iterate_endomorphism
  f_herbrand_prime_order --> f_norm_difference_index_identity
  f_herbrand_prime_order --> f_pow_index_torsion_finite_ker_range
  f_herbrand_prime_order --> f_pow_prime_range_eq_iterated_difference
  f_herbrand_prime_order --> f_adelic_lattice_proofs__pow_index_torsion_ker_range_mul
  f_herbrand_prime_order --> f_adelic_hermitian_forms__mem_pow_sub
  f_herbrand_prime_order --> f_adelic_hermitian_forms__sq_sub_le_norm_sub
  f_herbrand_prime_order --> groups
  f_herbrand_prime_order --> concept_normal_subgroups_quotients
  f_herbrand_prime_order --> primes_divisibility
  f_index_range_ker_iterate_endomorphism --> groups
  f_index_range_ker_iterate_endomorphism --> concept_normal_subgroups_quotients
  f_index_range_ker_iterate_endomorphism --> counting
  f_norm_difference_index_identity --> groups
  f_norm_difference_index_identity --> concept_normal_subgroups_quotients
  f_norm_difference_index_identity --> f_adelic_hermitian_forms__mem_pow_sub
  f_norm_difference_index_identity --> counting
  f_pow_index_torsion_finite_ker_range --> groups
  f_pow_index_torsion_finite_ker_range --> concept_normal_subgroups_quotients
  f_pow_index_torsion_finite_ker_range --> f_adelic_hermitian_forms__mem_pow_sub
  f_pow_index_torsion_finite_ker_range --> counting
  f_pow_prime_range_eq_iterated_difference --> groups
  f_pow_prime_range_eq_iterated_difference --> polynomials
  f_pow_prime_range_eq_iterated_difference --> primes_divisibility
  f_pow_prime_range_eq_iterated_difference --> rings_fields
  f_aff_char --> polynomials
  f_aff_char --> complex_numbers
  f_aff_char --> rings_fields
  f_aff_char --> linear_algebra
  f_generators --> f_aff_char
  f_generators --> concept_symmetric_polynomials
  f_generators --> polynomials
  f_generators --> infinite_series
  f_matrix_entry_abs_sum_unitary_lie_coordinates_split --> polynomials
  f_matrix_entry_abs_sum_unitary_lie_coordinates_split --> complex_numbers
  f_matrix_entry_abs_sum_unitary_lie_coordinates_split --> real_analysis
  f_int_mv_polynomial_coeff_abs_sum_add_le --> f_aff_char
  f_int_mv_polynomial_coeff_abs_sum_add_le --> f_piece_add
  f_int_mv_polynomial_coeff_abs_sum_add_le --> f_matrix_entry_abs_sum_unitary_lie_coordinates_split
  f_int_mv_polynomial_coeff_abs_sum_add_le --> polynomials
  f_int_mv_polynomial_coeff_abs_sum_add_le --> calculus
  f_piece_add --> f_aff_char
  f_piece_add --> polynomials
  f_piece_hom --> f_aff_char
  f_piece_hom --> polynomials
  f_aeval_single_zero --> f_aff_char
  f_aeval_single_zero --> f_piece_add
  f_aeval_single_zero --> polynomials
  f_gen_fund --> concept_symmetric_polynomials
  f_gen_fund --> polynomials
  f_gen_fund --> groups
  f_gen_red --> concept_symmetric_polynomials
  f_gen_red --> f_matrix_entry_abs_sum_unitary_lie_coordinates_split
  f_gen_red --> polynomials
  f_gen_trunc --> concept_symmetric_polynomials
  f_gen_trunc --> polynomials
  f_coeff_l1_norm_nonneg --> f_gen_red
  f_coeff_l1_norm_nonneg --> f_gen_fund
  f_coeff_l1_norm_nonneg --> f_gen_trunc
  f_coeff_l1_norm_nonneg --> f_matrix_entry_abs_sum_unitary_lie_coordinates_split
  f_coeff_l1_norm_nonneg --> concept_symmetric_polynomials
  f_coeff_l1_norm_nonneg --> polynomials
  f_gen_pieces --> f_coeff_l1_norm_nonneg
  f_gen_pieces --> f_int_mv_polynomial_coeff_abs_sum_add_le
  f_gen_pieces --> f_piece_hom
  f_gen_pieces --> f_aeval_single_zero
  f_gen_pieces --> f_generators
  f_gen_pieces --> f_aff_char
  f_gen_pieces --> concept_symmetric_polynomials
  f_gen_pieces_k --> f_gen_pieces
  f_gen_pieces_k --> f_aff_char
  f_gen_pieces_k --> concept_symmetric_polynomials
  f_gen_pieces_k --> polynomials
  f_discharge --> f_trace_isometry_weights__statement_f
  f_discharge --> f_trace_isometry_weights__statement_c
  f_discharge --> p_adic_numbers
  f_discharge --> polynomials
  f_discharge --> primes_divisibility
  f_discharge --> real_analysis
  f_gauss_jet_bounds__statement_k --> f_gauss_jet_bounds__statement
  f_gauss_jet_bounds__statement_k --> f_gauss_jet_bounds__statement_a
  f_gauss_jet_bounds__statement_k --> f_gauss_jet_bounds__statement_g
  f_gauss_jet_bounds__statement_k --> f_incoming_bounds__incoming_bound
  f_gauss_jet_bounds__statement_k --> concept_ultrametric_norm
  f_gauss_jet_bounds__statement_k --> p_adic_numbers
  f_gauss_jet_bounds__statement_k --> concept_roots_of_unity_kummer
  f_gauss_jet_bounds__statement_k --> polynomials
  f_gauss_jet_bounds__statement_m --> f_gauss_jet_bounds__statement_k
  f_gauss_jet_bounds__statement_m --> f_gauss_jet_bounds__statement
  f_gauss_jet_bounds__statement_m --> f_incoming_bounds__incoming_bound
  f_gauss_jet_bounds__statement_m --> concept_ultrametric_norm
  f_gauss_jet_bounds__statement_m --> p_adic_numbers
  f_gauss_jet_bounds__statement_m --> polynomials
  f_gauss_jet_bounds__statement_p --> f_gauss_jet_bounds__statement_k
  f_gauss_jet_bounds__statement_p --> f_gauss_jet_bounds__statement_e
  f_gauss_jet_bounds__statement_p --> f_gauss_jet_bounds__statement_i
  f_gauss_jet_bounds__statement_p --> f_incoming_bounds__incoming_bound
  f_gauss_jet_bounds__statement_p --> p_adic_numbers
  f_gauss_jet_bounds__statement_p --> concept_ultrametric_norm
  f_gauss_jet_bounds__statement_p --> polynomials
  f_gauss_jet_bounds__statement_w --> f_gauss_jet_bounds__statement_j
  f_gauss_jet_bounds__statement_w --> f_gauss_jet_bounds__statement_g
  f_gauss_jet_bounds__statement_w --> f_gauss_jet_bounds__statement_p
  f_gauss_jet_bounds__statement_w --> concept_ultrametric_norm
  f_gauss_jet_bounds__statement_w --> polynomials
  f_global_twisting__link_exact_aff --> f_global_twisting__sub_closed
  f_global_twisting__link_exact_aff --> concept_chain_complexes_homology
  f_global_twisting__link_exact_aff --> concept_gl_infinity_homology_stability
  f_global_twisting__link_exact_aff --> linear_algebra
  f_global_twisting__link_exact_aff --> rings_fields
  f_link_exactness_stability__sub_closed_and_perm_and_linear_equiv_invariant_uni_m --> f_global_twisting__link_exact_aff
  f_link_exactness_stability__sub_closed_and_perm_and_linear_equiv_invariant_uni_m --> f_global_twisting__sub_closed
  f_link_exactness_stability__sub_closed_and_perm_and_linear_equiv_invariant_uni_m --> linear_algebra
  f_link_exactness_stability__sub_closed_and_perm_and_linear_equiv_invariant_uni_m --> rings_fields
  f_link_exactness_stability__cons_mem_uni_m_iff_map_sub_smul --> f_global_twisting__link_exact_aff
  f_link_exactness_stability__cons_mem_uni_m_iff_map_sub_smul --> linear_algebra
  f_link_exactness_stability__cons_mem_uni_m_iff_map_sub_smul --> rings_fields
  f_link_exactness_stability__link_in_uni_m_eq_shorter_of_form_eq_one --> f_link_exactness_stability__sub_closed_and_perm_and_linear_equiv_invariant_uni_m
  f_link_exactness_stability__link_in_uni_m_eq_shorter_of_form_eq_one --> f_link_exactness_stability__cons_mem_uni_m_iff_map_sub_smul
  f_link_exactness_stability__link_in_uni_m_eq_shorter_of_form_eq_one --> f_global_twisting__link_exact_aff
  f_link_exactness_stability__link_in_uni_m_eq_shorter_of_form_eq_one --> linear_algebra
  f_link_exactness_stability__seq_chain_boundary_prefix_chain --> f_global_twisting__sub_closed
  f_link_exactness_stability__seq_chain_boundary_prefix_chain --> concept_chain_complexes_homology
  f_link_exactness_stability__seq_chain_boundary_prefix_chain --> groups
  f_link_exactness_stability__seq_chain_cycle_retraction_of_link_exact --> f_link_exactness_stability__seq_chain_boundary_prefix_chain
  f_link_exactness_stability__seq_chain_cycle_retraction_of_link_exact --> f_global_twisting__sub_closed
  f_link_exactness_stability__seq_chain_cycle_retraction_of_link_exact --> concept_chain_complexes_homology
  f_link_exactness_stability__exists_homologous_cycle_with_entries_in_of_exact_at_links --> f_link_exactness_stability__seq_chain_cycle_retraction_of_link_exact
  f_link_exactness_stability__exists_homologous_cycle_with_entries_in_of_exact_at_links --> f_link_exactness_stability__seq_chain_boundary_comp_boundary_apply
  f_link_exactness_stability__exists_homologous_cycle_with_entries_in_of_exact_at_links --> f_global_twisting__sub_closed
  f_link_exactness_stability__exists_homologous_cycle_with_entries_in_of_exact_at_links --> concept_chain_complexes_homology
  f_link_exactness_stability__seq_complex_exact_at_of_all_links_exact_at --> f_link_exactness_stability__exists_homologous_cycle_with_entries_in_of_exact_at_links
  f_link_exactness_stability__seq_complex_exact_at_of_all_links_exact_at --> f_global_twisting__sub_closed
  f_link_exactness_stability__seq_complex_exact_at_of_all_links_exact_at --> concept_chain_complexes_homology
  f_exact_at_link_succ_union_translate_of_coord_one --> f_global_twisting__link_exact_aff
  f_exact_at_link_succ_union_translate_of_coord_one --> f_link_exactness_stability__seq_complex_exact_at_of_all_links_exact_at
  f_exact_at_link_succ_union_translate_of_coord_one --> f_link_exactness_stability__link_in_uni_m_eq_shorter_of_form_eq_one
  f_exact_at_link_succ_union_translate_of_coord_one --> f_link_exactness_stability__sub_closed_and_perm_and_linear_equiv_invariant_uni_m
  f_exact_at_link_succ_union_translate_of_coord_one --> concept_gl_infinity_homology_stability
  f_exact_at_link_succ_union_translate_of_coord_one --> concept_chain_complexes_homology
  f_orbital_bounds_conclusion__sqf_roots_inj --> f_period_integrals__sqf_roots_inj
  f_orbital_bounds_conclusion__sqf_roots_inj --> f_squarefree_roots_injective__claim_of
  f_orbital_bounds_conclusion__sqf_roots_inj --> f_wit_main
  f_orbital_bounds_conclusion__sqf_roots_inj --> f_rpow_quarter_pow_four
  f_period_integrals__sqf_roots_inj --> f_period_integrals__sqf_lab
  f_period_integrals__sqf_roots_inj --> polynomials
  f_period_integrals__sqf_roots_inj --> counting
  f_period_integrals__sqf_roots_inj --> modular_arithmetic
  f_squarefree_roots_injective__claim_of --> f_period_integrals__sqf_roots_inj
  f_squarefree_roots_injective__claim_of --> f_period_integrals__sqf_lab
  f_squarefree_roots_injective__claim_of --> algebraic_closure
  f_squarefree_roots_injective__claim_of --> polynomials
  f_squarefree_roots_injective__claim_of --> primes_divisibility
  f_div_count --> polynomials
  f_div_count --> counting
  f_div_count --> modular_arithmetic
  f_two_pow_card_prime_factors_le --> f_squarefree_roots_injective__claim_of
  f_two_pow_card_prime_factors_le --> f_period_integrals__sqf_lab
  f_two_pow_card_prime_factors_le --> primes_divisibility
  f_two_pow_card_prime_factors_le --> polynomials
  f_sum_sq_pow_le_two --> f_two_pow_card_prime_factors_le
  f_sum_sq_pow_le_two --> f_card_le_sum_of_cover
  f_sum_sq_pow_le_two --> infinite_series
  f_sum_sq_pow_le_two --> real_analysis
  f_card_le_sum_of_cover --> f_squarefree_roots_injective__claim_of
  f_card_le_sum_of_cover --> f_div_count
  f_card_le_sum_of_cover --> f_two_pow_card_prime_factors_le
  f_card_le_sum_of_cover --> f_period_integrals__sqf_lab
  f_card_le_sum_of_cover --> algebraic_closure
  f_card_le_sum_of_cover --> polynomials
  f_card_le_sum_of_cover --> counting
  f_rpow_quarter_pow_four --> f_card_le_sum_of_cover
  f_rpow_quarter_pow_four --> f_sum_sq_pow_le_two
  f_rpow_quarter_pow_four --> f_two_pow_card_prime_factors_le
  f_rpow_quarter_pow_four --> f_squarefree_roots_injective__claim_of
  f_rpow_quarter_pow_four --> real_analysis
  f_rpow_quarter_pow_four --> calculus
  f_wit_base --> f_period_integrals__sqf_lab
  f_wit_base --> modular_arithmetic
  f_wit_base --> primes_divisibility
  f_wit_base --> algebraic_closure
  f_wit_base --> rings_fields
  f_wit_main --> f_wit_base
  f_wit_main --> f_squarefree_roots_injective__claim_of
  f_wit_main --> f_period_integrals__sqf_lab
  f_wit_main --> concept_galois_fixed_fields
  f_wit_main --> concept_field_extensions_transcendence
  f_wit_main --> polynomials
  f_wit_main --> algebraic_closure
  f_charpoly_eq_finsum_psi --> f_commutative_algebra__invariant_subspace_mobius_inverse_rec_eq_of_finrank_lt
  f_charpoly_eq_finsum_psi --> f_character_theory__invariant_subspace_mobius_inverse_charpoly_linear_equi
  f_charpoly_eq_finsum_psi --> linear_algebra
  f_charpoly_eq_finsum_psi --> polynomials
  f_charpoly_eq_finsum_psi --> counting
  f_character_theory__invariant_subspace_mobius_inverse_charpoly_linear_equi --> f_commutative_algebra__invariant_subspace_mobius_inverse_rec_eq_of_finrank_lt
  f_character_theory__invariant_subspace_mobius_inverse_charpoly_linear_equi --> linear_algebra
  f_character_theory__invariant_subspace_mobius_inverse_charpoly_linear_equi --> polynomials
  f_finsum_mobius_inverse_charpoly_invariant_le --> f_charpoly_eq_finsum_psi
  f_finsum_mobius_inverse_charpoly_invariant_le --> f_character_theory__invariant_subspace_mobius_inverse_charpoly_linear_equi
  f_finsum_mobius_inverse_charpoly_invariant_le --> linear_algebra
  f_finsum_mobius_inverse_charpoly_transversal_subspaces --> f_charpoly_eq_finsum_psi
  f_finsum_mobius_inverse_charpoly_transversal_subspaces --> f_character_theory__invariant_subspace_mobius_inverse_charpoly_linear_equi
  f_finsum_mobius_inverse_charpoly_transversal_subspaces --> f_commutative_algebra__invariant_subspace_mobius_inverse_rec_eq_of_finrank_lt
  f_finsum_mobius_inverse_charpoly_transversal_subspaces --> linear_algebra
  f_finsum_mobius_inverse_charpoly_transversal_subspaces --> counting
  f_finsum_mobius_inverse_charpoly_transversal_subspaces --> concept_normal_subgroups_quotients
  f_sum_primitive_end_class_function_restrict_mixed_subspac --> f_commutative_algebra__invariant_subspace_mobius_inverse_rec_eq_of_finrank_lt
  f_sum_primitive_end_class_function_restrict_mixed_subspac --> linear_algebra
  f_sum_primitive_end_class_function_restrict_mixed_subspac --> counting
  f_is_primitive_end_class_function_invariant_subspace_mobi --> f_charpoly_eq_finsum_psi
  f_is_primitive_end_class_function_invariant_subspace_mobi --> f_finsum_mobius_inverse_charpoly_invariant_le
  f_is_primitive_end_class_function_invariant_subspace_mobi --> f_finsum_mobius_inverse_charpoly_transversal_subspaces
  f_is_primitive_end_class_function_invariant_subspace_mobi --> f_sum_primitive_end_class_function_restrict_mixed_subspac
  f_is_primitive_end_class_function_invariant_subspace_mobi --> f_character_theory__invariant_subspace_mobius_inverse_charpoly_linear_equi
  f_is_primitive_end_class_function_invariant_subspace_mobi --> f_character_theory__charpoly_block_and_invariant_under_stabilizer_nilradic
  f_is_primitive_end_class_function_invariant_subspace_mobi --> f_commutative_algebra__invariant_subspace_mobius_inverse_rec_eq_of_finrank_lt
  f_is_primitive_end_class_function_invariant_subspace_mobi --> linear_algebra
  f_gauss_jet_bounds__statement_u --> f_gauss_jet_bounds__statement
  f_gauss_jet_bounds__statement_u --> f_gauss_jet_bounds__statement_h
  f_gauss_jet_bounds__statement_u --> f_gauss_jet_bounds__statement_i
  f_gauss_jet_bounds__statement_u --> f_gauss_jet_bounds__statement_j
  f_gauss_jet_bounds__statement_u --> p_adic_numbers
  f_gauss_jet_bounds__statement_u --> polynomials
  f_gauss_jet_bounds__statement_u --> concept_roots_of_unity_kummer
  f_minor_defs --> polynomials
  f_minor_defs --> linear_algebra
  f_minor_defs --> concept_derivations_smoothness
  f_minor_defs --> concept_exterior_powers
  f_minor_b --> f_minor_defs
  f_minor_b --> polynomials
  f_minor_b --> linear_algebra
  f_minor_b --> concept_derivations_smoothness
  f_minor_core_a --> f_minor_defs
  f_minor_core_a --> f_minor_b
  f_minor_core_a --> polynomials
  f_minor_core_a --> linear_algebra
  f_minor_core --> f_minor_defs
  f_minor_core --> f_minor_b
  f_minor_core --> f_minor_core_a
  f_minor_core --> polynomials
  f_minor_core --> linear_algebra
  f_minor_iter --> f_minor_defs
  f_minor_iter --> f_minor_b
  f_minor_iter --> f_minor_core
  f_minor_iter --> polynomials
  f_minor_formula --> f_minor_formulas__cay_div_of
  f_minor_formula --> f_minor_defs
  f_minor_formula --> f_minor_iter
  f_minor_formula --> polynomials
  f_minor_formula --> linear_algebra
  f_minor_formulas__cay_div_of --> f_mollified_integrability__cls_gain_st
  f_minor_formulas__cay_div_of --> f_holomorphic_continuation__is_sing_test
  f_minor_formulas__cay_div_of --> f_holomorphic_continuation__null_sec
  f_minor_formulas__cay_div_of --> polynomials
  f_minor_formulas__cay_div_of --> linear_algebra
  f_minor_formulas__cay_div_of --> complex_analysis
  f_minor_formulas__cay_div_of --> concept_derivations_smoothness
  f_mollified_integrability__cls_gain_st --> f_mollified_integrability__cls_bound_alt
  f_mollified_integrability__cls_gain_st --> f_holomorphic_continuation__is_sing_test
  f_mollified_integrability__cls_gain_st --> complex_analysis
  f_mollified_integrability__cls_gain_st --> concept_hermitian_unitary_matrices
  f_mollified_integrability__cls_gain_st --> linear_algebra
  f_misc_lemmas_p__imports --> linear_algebra
  f_misc_lemmas_p__imports --> complex_numbers
  f_anti_e_is_gl_rep --> f_discrete_series__is_inf_unitary
  f_anti_e_is_gl_rep --> concept_group_representations
  f_anti_e_is_gl_rep --> linear_algebra
  f_gelfand --> f_misc_lemmas_p__imports
  f_gelfand --> f_discrete_series__is_inf_unitary
  f_gelfand --> concept_group_representations
  f_gelfand --> linear_algebra
  f_gelfand_series --> polynomials
  f_gelfand_series --> infinite_series
  f_gelfand_series --> complex_numbers
  f_gelfand_h_w --> f_gelfand
  f_gelfand_h_w --> f_gelfand_series
  f_gelfand_h_w --> f_discrete_series__is_inf_unitary
  f_gelfand_h_w --> concept_group_representations
  f_gelfand_h_w --> linear_algebra
  f_tensor_v --> f_discrete_series__is_inf_unitary
  f_tensor_v --> concept_group_representations
  f_tensor_v --> linear_algebra
  f_partial_trace --> f_tensor_v
  f_partial_trace --> f_gelfand
  f_partial_trace --> f_anti_e_is_gl_rep
  f_partial_trace --> f_misc_lemmas_p__imports
  f_partial_trace --> linear_algebra
  f_resolvent --> f_partial_trace
  f_resolvent --> f_gelfand_h_w
  f_resolvent --> f_gelfand_series
  f_resolvent --> f_anti_e_is_gl_rep
  f_resolvent --> f_gelfand
  f_resolvent --> f_discrete_series__is_inf_unitary
  f_resolvent --> infinite_series
  f_resolvent --> linear_algebra
  f_tensor_representations__residue --> f_resolvent
  f_tensor_representations__residue --> f_gelfand_series
  f_tensor_representations__residue --> infinite_series
  f_tensor_representations__residue --> polynomials
  f_tensor_representations__residue --> real_analysis
  f_fock_resolution_onto__statement_c --> f_fock_resolution_onto__shift_last_letter_thresholds
  f_fock_resolution_onto__statement_c --> f_mahler_measure__is_frozen_inv
  f_fock_resolution_onto__statement_c --> f_mahler_measure__good_count
  f_fock_resolution_onto__statement_c --> f_mahler_measure__statement_t
  f_fock_resolution_onto__statement_c --> p_adic_numbers
  f_fock_resolution_onto__statement_c --> polynomials
  f_fock_resolution_onto__statement_e --> f_fock_resolution_onto__statement_c
  f_fock_resolution_onto__statement_e --> f_fock_resolution_onto__shift_last_letter_thresholds
  f_fock_resolution_onto__statement_e --> f_mahler_measure__statement_t
  f_fock_resolution_onto__statement_e --> f_mahler_measure__is_frozen_inv
  f_fock_resolution_onto__statement_e --> p_adic_numbers
  f_fock_resolution_onto__statement_e --> polynomials
  f_compact_casimir_bound_elementary_apply --> f_jets__sum_io_pr
  f_compact_casimir_bound_elementary_apply --> linear_algebra
  f_jet_harmonics__compact_casimir_le_tensor_operator_raise --> f_jet_harmonics__sum_norm_add_sq_le_of_bounds
  f_jet_harmonics__compact_casimir_le_tensor_operator_raise --> f_jet_harmonics__cas_k_is_symmetric_and_form
  f_jet_harmonics__compact_casimir_le_tensor_operator_raise --> f_jet_harmonics__re_inner_le_on_image_of_intertwining
  f_jet_harmonics__compact_casimir_le_tensor_operator_raise --> f_jets__sum_io_pr
  f_jet_harmonics__compact_casimir_le_tensor_operator_raise --> linear_algebra
  f_jet_harmonics__sum_norm_add_sq_le_of_bounds --> linear_algebra
  f_jet_harmonics__sum_norm_add_sq_le_of_bounds --> real_analysis
  f_base_change_lift_class_function --> f_frobenius_shape_of_side_preserving
  f_base_change_lift_class_function --> f_commutative_algebra__invariant_subspace_mobius_inverse_rec_eq_of_finrank_lt
  f_base_change_lift_class_function --> concept_galois_fixed_fields
  f_base_change_lift_class_function --> groups
  f_frobenius_shape_of_side_preserving --> f_divisor_proofs__galois_twisted_norm_g_l_basic_properties
  f_frobenius_shape_of_side_preserving --> f_is_conj_of_is_conj_gl_field_extension_inclusion
  f_frobenius_shape_of_side_preserving --> concept_group_actions
  f_frobenius_shape_of_side_preserving --> groups
  f_divisor_proofs__galois_twisted_norm_g_l_basic_properties --> f_divisors__orth_subrepresentation
  f_divisor_proofs__galois_twisted_norm_g_l_basic_properties --> concept_galois_fixed_fields
  f_divisor_proofs__galois_twisted_norm_g_l_basic_properties --> concept_group_actions
  f_divisor_proofs__galois_twisted_norm_g_l_basic_properties --> linear_algebra
  f_divisor_proofs__galois_twisted_norm_g_l_basic_properties --> rings_fields
  f_is_conj_of_is_conj_gl_field_extension_inclusion --> f_divisor_proofs__nonempty_linear_equiv_of_pi_fin_pow_finite
  f_is_conj_of_is_conj_gl_field_extension_inclusion --> f_ab_by_p_of_comm
  f_is_conj_of_is_conj_gl_field_extension_inclusion --> linear_algebra
  f_is_conj_of_is_conj_gl_field_extension_inclusion --> polynomials
  f_is_conj_of_is_conj_gl_field_extension_inclusion --> rings_fields
  f_divisor_proofs__nonempty_equiv_of_card_hom --> linear_algebra
  f_divisor_proofs__nonempty_equiv_of_card_hom --> rings_fields
  f_divisor_proofs__nonempty_equiv_of_card_hom --> counting
  f_divisor_proofs__nonempty_equiv_of_card_hom --> concept_normal_subgroups_quotients
  f_divisor_proofs__nonempty_linear_equiv_of_pi_fin_pow_finite --> f_divisor_proofs__nonempty_equiv_of_card_hom
  f_divisor_proofs__nonempty_linear_equiv_of_pi_fin_pow_finite --> linear_algebra
  f_divisor_proofs__nonempty_linear_equiv_of_pi_fin_pow_finite --> counting
  f_orbital_bounds_conclusion__prime_count --> f_chebyshev_prime_bounds_log_fact
  f_orbital_bounds_conclusion__prime_count --> f_count_succ_le
  f_orbital_bounds_conclusion__prime_count --> f_chebyshev_prime_bounds__prime_count_bound_of
  f_orbital_bounds_conclusion__prime_count --> f_chebyshev_prime_bounds__psi_upper_bound_of_lt_thirty_mul_six_pow
  f_orbital_bounds_conclusion__prime_count --> f_period_integrals__prime_count
  f_orbital_bounds_conclusion__prime_count --> concept_chebyshev_functions
  f_orbital_bounds_conclusion__prime_count --> primes_divisibility
  f_chebyshev_prime_bounds_log_fact --> f_chebyshev_prime_bounds__prime_count_bound_of
  f_chebyshev_prime_bounds_log_fact --> concept_chebyshev_functions
  f_chebyshev_prime_bounds_log_fact --> calculus
  f_chebyshev_prime_bounds_log_fact --> real_analysis
  f_count_succ_le --> f_small_loop
  f_count_succ_le --> f_chebyshev_prime_bounds__prime_count_bound_of
  f_count_succ_le --> primes_divisibility
  f_count_succ_le --> counting
  f_count_succ_le --> real_analysis
  f_small_loop --> primes_divisibility
  f_small_loop --> counting
  f_cay_dens_ex_cay_s --> f_archimedean_orbit_measures__meas_lie
  f_cay_dens_ex_cay_s --> f_archimedean_orbit_measures__omega_density
  f_cay_dens_ex_cay_s --> f_archimedean_orbit_measures__upq
  f_cay_dens_ex_cay_s --> f_archimedean_orbit_measures__cay_dens_ex_top
  f_cay_dens_ex_cay_s --> concept_haar_measure_fundamental_domain
  f_cay_dens_ex_cay_s --> concept_hermitian_unitary_matrices
  f_cay_dens_ex_cay_k --> f_cay_dens_ex_cay_s
  f_cay_dens_ex_cay_k --> f_archimedean_orbit_measures__cay_dens_ex_sk
  f_cay_dens_ex_cay_k --> f_archimedean_orbit_measures__cay_dens_ex_top
  f_cay_dens_ex_cay_k --> f_archimedean_orbit_measures__meas_lie
  f_cay_dens_ex_cay_k --> f_archimedean_orbit_measures__upq
  f_cay_dens_ex_cay_k --> concept_haar_measure_fundamental_domain
  f_cay_dens_ex_cay_k --> concept_point_set_topology
  f_abhyankar_exists_fraction_localisation_normalisation --> f_divisor_proofs__loc_hom_algebra_map
  f_abhyankar_exists_fraction_localisation_normalisation --> concept_discrete_valuation_ring
  f_abhyankar_exists_fraction_localisation_normalisation --> concept_integral_closure_fraction_fields
  f_abhyankar_exists_fraction_localisation_normalisation --> concept_prime_ideals_localization
  f_abhyankar_exists_fraction_localisation_normalisation --> concept_tensor_product_of_algebras
  f_abhyankar_exists_local_kummer_element --> f_divisor_proofs__loc_hom_algebra_map
  f_abhyankar_exists_local_kummer_element --> concept_roots_of_unity_kummer
  f_abhyankar_exists_local_kummer_element --> concept_discrete_valuation_ring
  f_abhyankar_exists_local_kummer_element --> concept_integral_closure_fraction_fields
  f_abhyankar_exists_local_kummer_element --> concept_tensor_product_of_algebras
  f_abhyankar_exists_local_kummer_element --> concept_prime_ideals_localization
  f_abhyankar_ramification_idx_eq_one --> f_abhyankar_exists_fraction_localisation_normalisation
  f_abhyankar_ramification_idx_eq_one --> f_abhyankar_exists_local_kummer_element
  f_abhyankar_ramification_idx_eq_one --> f_abhyankar_root_mem_maximal_ideal_non_zero_divisors
  f_abhyankar_ramification_idx_eq_one --> f_divisor_proofs__is_artinian_ring_kummer_adjoin_root_quotient_root
  f_abhyankar_ramification_idx_eq_one --> f_kummer_unit_radicand_quotient_root_is_reduced
  f_abhyankar_ramification_idx_eq_one --> f_maximal_ideal_localization_eq_span_of_reduced_artinian_a
  f_abhyankar_ramification_idx_eq_one --> f_maximal_ideal_span_image_uniformizer
  f_abhyankar_ramification_idx_eq_one --> f_uniformizer_eq_pow_ramification_idx_mul_unit_integral_cl
  f_abhyankar_ramification_idx_eq_one --> concept_dedekind_domains
  f_abhyankar_ramification_idx_eq_one --> concept_discrete_valuation_ring
  f_abhyankar_ramification_idx_eq_one --> concept_separable_polynomials
  f_abhyankar_root_mem_maximal_ideal_non_zero_divisors --> concept_local_rings
  f_abhyankar_root_mem_maximal_ideal_non_zero_divisors --> concept_integral_closure_fraction_fields
  f_abhyankar_root_mem_maximal_ideal_non_zero_divisors --> concept_prime_ideals_localization
  f_abhyankar_root_mem_maximal_ideal_non_zero_divisors --> concept_tensor_product_of_algebras
  f_divisor_proofs__is_artinian_ring_kummer_adjoin_root_quotient_root --> concept_discrete_valuation_ring
  f_divisor_proofs__is_artinian_ring_kummer_adjoin_root_quotient_root --> concept_roots_of_unity_kummer
  f_divisor_proofs__is_artinian_ring_kummer_adjoin_root_quotient_root --> rings_fields
  f_divisor_proofs__is_artinian_ring_kummer_adjoin_root_quotient_root --> linear_algebra
  f_kummer_unit_radicand_quotient_root_is_reduced --> concept_separable_polynomials
  f_kummer_unit_radicand_quotient_root_is_reduced --> concept_discrete_valuation_ring
  f_kummer_unit_radicand_quotient_root_is_reduced --> concept_roots_of_unity_kummer
  f_kummer_unit_radicand_quotient_root_is_reduced --> polynomials
  f_kummer_unit_radicand_quotient_root_is_reduced --> rings_fields
  f_maximal_ideal_localization_eq_span_of_reduced_artinian_a --> concept_prime_ideals_localization
  f_maximal_ideal_localization_eq_span_of_reduced_artinian_a --> concept_local_rings
  f_maximal_ideal_localization_eq_span_of_reduced_artinian_a --> concept_semisimple_algebras_radical
  f_maximal_ideal_localization_eq_span_of_reduced_artinian_a --> rings_fields
  f_maximal_ideal_span_image_uniformizer --> concept_local_rings
  f_maximal_ideal_span_image_uniformizer --> concept_discrete_valuation_ring
  f_maximal_ideal_span_image_uniformizer --> concept_noetherian_and_irreducible_components
  f_uniformizer_eq_pow_ramification_idx_mul_unit_integral_cl --> concept_dedekind_domains
  f_uniformizer_eq_pow_ramification_idx_mul_unit_integral_cl --> concept_discrete_valuation_ring
  f_uniformizer_eq_pow_ramification_idx_mul_unit_integral_cl --> concept_integral_closure_fraction_fields
  f_uniformizer_eq_pow_ramification_idx_mul_unit_integral_cl --> concept_prime_ideals_localization
  f_cauchy_parallelogram_upper_half_plane --> complex_analysis
  f_cauchy_parallelogram_upper_half_plane --> calculus
  f_eichler_integral_from_i_tail_exponential_decay --> f_cauchy_parallelogram_upper_half_plane
  f_eichler_integral_from_i_tail_exponential_decay --> f_integrable_on_vertical_ray_norm_integral_le
  f_eichler_integral_from_i_tail_exponential_decay --> f_top_side_integral_tendsto_zero
  f_eichler_integral_from_i_tail_exponential_decay --> f_foundations__is_d_c_reps
  f_eichler_integral_from_i_tail_exponential_decay --> concept_modular_forms
  f_eichler_integral_from_i_tail_exponential_decay --> complex_analysis
  f_eichler_integral_from_i_tail_exponential_decay --> real_analysis
  f_eichler_period_polynomial_limit_at_cusp --> f_foundation_proofs__eichler_integral_from_i_slash_change_of_variables
  f_eichler_period_polynomial_limit_at_cusp --> f_eichler_integral_from_i_tail_exponential_decay
  f_eichler_period_polynomial_limit_at_cusp --> f_poly_degree_slash_action_right_action_properties
  f_eichler_period_polynomial_limit_at_cusp --> f_foundations__is_d_c_reps
  f_eichler_period_polynomial_limit_at_cusp --> concept_modular_forms
  f_eichler_period_polynomial_limit_at_cusp --> concept_hecke_operators
  f_eichler_period_polynomial_limit_at_cusp --> complex_analysis
  f_integrable_on_vertical_ray_norm_integral_le --> real_analysis
  f_integrable_on_vertical_ray_norm_integral_le --> calculus
  f_integrable_on_vertical_ray_norm_integral_le --> complex_analysis
  f_poly_degree_slash_action_right_action_properties --> polynomials
  f_poly_degree_slash_action_right_action_properties --> linear_algebra
  f_poly_degree_slash_action_right_action_properties --> concept_group_actions
  f_poly_degree_slash_action_right_action_properties --> concept_group_representations
  f_top_side_integral_tendsto_zero --> real_analysis
  f_top_side_integral_tendsto_zero --> calculus
  f_top_side_integral_tendsto_zero --> complex_analysis
  f_ext_v_statement --> f_toroidal_compactification__two_weight_eq_one_add_root
  f_ext_v_statement --> f_toroidal_compactification__is_completed_strict_hens
  f_ext_v_statement --> concept_discrete_valuation_ring
  f_ext_v_statement --> concept_adic_completion
  f_ext_v_statement --> concept_group_schemes
  f_ext_v_statement --> concept_schemes_basics
  f_toroidal_compactification__two_weight_eq_one_add_root --> f_extension_descent__const_gen
  f_toroidal_compactification__two_weight_eq_one_add_root --> f_extension_descent__nonzero_locus
  f_toroidal_compactification__two_weight_eq_one_add_root --> f_toroidal_compactification__is_grp_pullback
  f_toroidal_compactification__two_weight_eq_one_add_root --> f_cubical_structures__cube_symmetric_swap_first
  f_toroidal_compactification__two_weight_eq_one_add_root --> f_cubical_structures__cubical_pull_base_change_st
  f_toroidal_compactification__two_weight_eq_one_add_root --> f_abelian_scheme_quotients__is_abelian_scheme
  f_toroidal_compactification__two_weight_eq_one_add_root --> f_split_tori__split_torus_aff
  f_toroidal_compactification__two_weight_eq_one_add_root --> number_fields
  f_toroidal_compactification__two_weight_eq_one_add_root --> concept_group_schemes
  f_toroidal_compactification__two_weight_eq_one_add_root --> concept_dual_numbers
  f_toroidal_compactification__two_weight_eq_one_add_root --> concept_roots_of_unity_kummer
  f_toroidal_compactification__two_weight_eq_one_add_root --> concept_lattices_in_the_plane
  f_extension_descent__const_gen --> concept_picard_group
  f_extension_descent__const_gen --> concept_group_schemes
  f_extension_descent__const_gen --> concept_schemes_basics
  f_extension_descent__const_gen --> concept_categorical_pullbacks
  f_extension_descent__nonzero_locus --> f_abelian_scheme_quotients__is_abelian_scheme
  f_extension_descent__nonzero_locus --> concept_picard_group
  f_extension_descent__nonzero_locus --> concept_smooth_morphisms
  f_extension_descent__nonzero_locus --> concept_group_schemes
  f_extension_descent__nonzero_locus --> concept_schemes_basics
  f_rt0_conj_neg_ne_zero --> f_toroidal_compactification__two_weight_eq_one_add_root
  f_rt0_conj_neg_ne_zero --> complex_numbers
  f_conjugate_root_zero_second --> f_toroidal_compactification__two_weight_eq_one_add_root
  f_conjugate_root_zero_second --> complex_numbers
  f_abs_zeta_prime_sum_error_le_of_large --> f_riemann_zeta_ne_zero_of_mem_rectangle
  f_abs_zeta_prime_sum_error_le_of_large --> f_integral_eq_interval_integral_add_compl
  f_abs_zeta_prime_sum_error_le_of_large --> f_norm_integral_compl_le
  f_abs_zeta_prime_sum_error_le_of_large --> f_formalism__statement_o_c
  f_abs_zeta_prime_sum_error_le_of_large --> f_zero_free_region__small_height_log_deriv
  f_abs_zeta_prime_sum_error_le_of_large --> f_zero_free_region__statement
  f_abs_zeta_prime_sum_error_le_of_large --> complex_analysis
  f_abs_zeta_prime_sum_error_le_of_large --> real_analysis
  f_abs_zeta_prime_sum_error_le_of_one_le --> f_formalism__statement_o_c
  f_abs_zeta_prime_sum_error_le_of_one_le --> concept_chebyshev_functions
  f_abs_zeta_prime_sum_error_le_of_one_le --> primes_divisibility
  f_abs_zeta_prime_sum_error_le_of_one_le --> real_analysis
  f_gz_p_n_t_of --> f_abs_zeta_prime_sum_error_le_of_large
  f_gz_p_n_t_of --> f_abs_zeta_prime_sum_error_le_of_one_le
  f_gz_p_n_t_of --> f_zero_free_region__statement
  f_gz_p_n_t_of --> f_formalism__statement_o_c
  f_gz_p_n_t_of --> concept_chebyshev_functions
  f_integral_eq_interval_integral_add_compl --> complex_numbers
  f_integral_eq_interval_integral_add_compl --> calculus
  f_integral_eq_interval_integral_add_compl --> complex_analysis
  f_norm_integral_compl_le --> calculus
  f_norm_integral_compl_le --> real_analysis
  f_riemann_zeta_ne_zero_of_mem_rectangle --> f_zero_free_region__small_height_log_deriv
  f_riemann_zeta_ne_zero_of_mem_rectangle --> f_zero_free_region__statement
  f_riemann_zeta_ne_zero_of_mem_rectangle --> complex_analysis
  f_riemann_zeta_ne_zero_of_mem_rectangle --> complex_powers
  f_riemann_zeta_ne_zero_of_mem_rectangle --> zeta_series
  f_is_full_level_at --> f_abelian_scheme_quotients__is_abelian_scheme
  f_is_full_level_at --> f_toroidal_compactification__two_weight_eq_one_add_root
  f_is_full_level_at --> f_extension_descent__const_gen
  f_is_full_level_at --> f_split_tori__split_torus_aff
  f_is_full_level_at --> concept_group_schemes
  f_is_full_level_at --> concept_schemes_basics
  f_is_full_level_at --> algebraic_closure
  f_is_full_level_at --> number_fields
  f_conjugate_root_zero_third --> complex_numbers
  f_conjugate_root_zero_third --> number_fields
  f_conjugate_root_zero_third --> primes_divisibility
  f_cor_a3prime_b --> f_jacobi_path_weights__det_letters
  f_cor_a3prime_b --> f_jacobi_path_weights__index_weights_dominance
  f_cor_a3prime_b --> f_jacobi_path_weights__statement_a
  f_cor_a3prime_b --> f_jacobi_path_weights__statement_b
  f_cor_a3prime_b --> polynomials
  f_cor_a3prime_b --> rings_fields
  f_cor_a3prime_b --> linear_algebra
  f_jacobi_path_weights__defs_col --> concept_exterior_powers
  f_jacobi_path_weights__defs_col --> linear_algebra
  f_jacobi_path_weights__defs_col --> counting
  f_jacobi_path_weights__det_letters --> polynomials
  f_jacobi_path_weights__det_letters --> linear_algebra
  f_jacobi_path_weights__det_letters --> concept_symmetric_polynomials
  f_jacobi_path_weights__det_letters --> rings_fields
  f_jacobi_path_weights__index_weights_dominance --> f_jacobi_path_weights__statement_a
  f_jacobi_path_weights__index_weights_dominance --> f_jacobi_path_weights__statement_b
  f_jacobi_path_weights__index_weights_dominance --> f_jacobi_path_weights__lift_word
  f_jacobi_path_weights__index_weights_dominance --> concept_group_representations
  f_jacobi_path_weights__index_weights_dominance --> linear_algebra
  f_jacobi_path_weights__index_weights_dominance --> counting
  f_jacobi_path_weights__lift_word --> f_jacobi_path_weights__defs_col
  f_jacobi_path_weights__lift_word --> concept_exterior_powers
  f_jacobi_path_weights__lift_word --> linear_algebra
  f_jacobi_path_weights__lift_word --> polynomials
  f_jacobi_path_weights__statement_a --> f_jacobi_path_weights__statement_b
  f_jacobi_path_weights__statement_a --> f_jacobi_path_weights__defs_col
  f_jacobi_path_weights__statement_a --> f_jacobi_path_weights__lift_word
  f_jacobi_path_weights__statement_a --> polynomials
  f_jacobi_path_weights__statement_a --> linear_algebra
  f_jacobi_path_weights__statement_a --> concept_group_representations
  f_jacobi_path_weights__statement_b --> f_jacobi_path_weights__defs_col
  f_jacobi_path_weights__statement_b --> concept_exterior_powers
  f_jacobi_path_weights__statement_b --> polynomials
  f_jacobi_path_weights__statement_b --> counting
  f_jacobi_path_weights__statement_e --> f_jacobi_path_weights__det_letters
  f_jacobi_path_weights__statement_e --> concept_integral_closure_fraction_fields
  f_jacobi_path_weights__statement_e --> polynomials
  f_jacobi_path_weights__statement_e --> rings_fields
  f_jacobi_path_weights__statement_e --> linear_algebra
  f_jacobi_path_weights__statement_p --> f_jacobi_path_weights__index_weights_dominance
  f_jacobi_path_weights__statement_p --> f_jacobi_path_weights__statement_b
  f_jacobi_path_weights__statement_p --> counting
  f_jacobi_path_weights__statement_p --> concept_group_representations
  f_jacobi_path_weights__valuation_products_components --> f_jacobi_path_weights__det_letters
  f_jacobi_path_weights__valuation_products_components --> f_jacobi_path_weights__lift_word
  f_jacobi_path_weights__valuation_products_components --> f_jacobi_path_weights__statement_a
  f_jacobi_path_weights__valuation_products_components --> linear_algebra
  f_jacobi_path_weights__valuation_products_components --> concept_exterior_powers
  f_conjugate_root_zero --> complex_numbers
  f_conjugate_root_zero --> number_fields
  f_conjugate_root_zero --> primes_divisibility
  f_dual_lattices__map_smul_one_mul_vec --> f_dual_lattices__small_level_class_set
  f_dual_lattices__map_smul_one_mul_vec --> linear_algebra
  f_dual_lattices__map_smul_one_mul_vec --> rings_fields
  f_dual_lattices__map_smul_one_mul_vec --> concept_integral_closure_fraction_fields
  f_dual_lattices__moduli_points_state --> f_dual_lattices__sq_zero_of_span
  f_dual_lattices__moduli_points_state --> concept_dual_numbers
  f_dual_lattices__moduli_points_state --> concept_local_rings
  f_dual_lattices__nset_exp_injective_surjective --> f_dual_lattices__moduli_points_state
  f_dual_lattices__nset_exp_injective_surjective --> f_dual_lattices__sq_zero_of_span
  f_dual_lattices__nset_exp_injective_surjective --> f_dual_lattices__st_thm_a
  f_dual_lattices__nset_exp_injective_surjective --> concept_adic_completion
  f_one_add_pow_of_sq --> f_dual_lattices__nset_exp_injective_surjective
  f_one_add_pow_of_sq --> f_dual_lattices__series_state
  f_one_add_pow_of_sq --> f_dual_lattices__tangent_pairing_statement
  f_one_add_pow_of_sq --> f_dual_lattices__st_thm_a
  f_one_add_pow_of_sq --> f_dual_lattices__sq_zero_of_span
  f_one_add_pow_of_sq --> concept_dual_numbers
  f_one_add_pow_of_sq --> concept_projective_modules
  f_dual_lattices__series_state --> f_dual_lattices__sq_zero_of_span
  f_dual_lattices__series_state --> concept_group_schemes
  f_dual_lattices__series_state --> concept_roots_of_unity_kummer
  f_dual_lattices__sq_zero_of_span --> concept_local_rings
  f_dual_lattices__sq_zero_of_span --> concept_dual_numbers
  f_dual_lattices__sq_zero_of_span --> concept_group_schemes
  f_dual_lattices__sq_zero_of_span --> concept_tensor_product_of_algebras
  f_dual_lattices__sq_zero_of_span --> groups
  f_dual_lattices__st_thm_a --> f_dual_lattices__tangent_pairing_statement
  f_dual_lattices__st_thm_a --> f_dual_lattices__moduli_points_state
  f_dual_lattices__st_thm_a --> f_dual_lattices__sq_zero_of_span
  f_dual_lattices__st_thm_a --> concept_dual_numbers
  f_dual_lattices__st_thm_a_full --> f_dual_lattices__nset_exp_injective_surjective
  f_dual_lattices__st_thm_a_full --> f_dual_lattices__moduli_points_state
  f_dual_lattices__st_thm_a_full --> f_dual_lattices__st_thm_a
  f_dual_lattices__st_thm_a_full --> f_dual_lattices__sq_zero_of_span
  f_dual_lattices__st_thm_a_full --> concept_hermitian_unitary_matrices
  f_dual_lattices__st_thm_a_full --> concept_integral_closure_fraction_fields
  f_dual_lattices__tangent_pairing_statement --> f_dual_lattices__moduli_points_state
  f_dual_lattices__tangent_pairing_statement --> f_dual_lattices__sq_zero_of_span
  f_dual_lattices__tangent_pairing_statement --> concept_dual_numbers
  f_thm_a_full --> f_dual_lattices__st_thm_a_full
  f_thm_a_full --> f_one_add_pow_of_sq
  f_thm_a_full --> f_dual_lattices__map_smul_one_mul_vec
  f_thm_a_full --> f_dual_lattices__series_state
  f_thm_a_full --> f_dual_lattices__tangent_pairing_statement
  f_thm_a_full --> f_dual_lattices__nset_exp_injective_surjective
  f_thm_a_full --> f_dual_lattices__st_thm_a
  f_thm_a_full --> linear_algebra
  f_smooth_group_tangent_lift --> concept_schemes_basics
  f_smooth_group_tangent_lift --> concept_smooth_morphisms
  f_smooth_group_tangent_lift --> concept_group_schemes
  f_smooth_group_tangent_lift --> concept_prime_ideals_localization
  f_smooth_group_tangent_lift --> concept_categorical_pullbacks
  f_nontrivial_transvection --> f_adelic_hermitian_forms__is_herm_hyperbolic
  f_nontrivial_transvection --> concept_hermitian_unitary_matrices
  f_nontrivial_transvection --> complex_numbers
  f_nontrivial_transvection --> linear_algebra
  f_nontrivial_transvection --> groups
  f_exists_isotropic_basis_nonorthogonal_two_vectors --> f_adelic_hermitian_forms__is_herm_hyperbolic
  f_exists_isotropic_basis_nonorthogonal_two_vectors --> concept_hermitian_unitary_matrices
  f_exists_isotropic_basis_nonorthogonal_two_vectors --> linear_algebra
  f_quasi_reflection_eq_mul_transvections_of_hyperbolic_pla --> f_nontrivial_transvection
  f_quasi_reflection_eq_mul_transvections_of_hyperbolic_pla --> f_adelic_hermitian_forms__is_herm_hyperbolic
  f_quasi_reflection_eq_mul_transvections_of_hyperbolic_pla --> concept_hermitian_unitary_matrices
  f_quasi_reflection_eq_mul_transvections_of_hyperbolic_pla --> linear_algebra
  f_quasi_reflection_eq_unitary_transvection_mul --> f_quasi_reflection_eq_mul_transvections_of_hyperbolic_pla
  f_quasi_reflection_eq_unitary_transvection_mul --> f_exists_isotropic_basis_nonorthogonal_two_vectors
  f_quasi_reflection_eq_unitary_transvection_mul --> f_unitary_transvection_submonoid_normal_det_one
  f_quasi_reflection_eq_unitary_transvection_mul --> f_nontrivial_transvection
  f_quasi_reflection_eq_unitary_transvection_mul --> f_adelic_hermitian_forms__is_herm_hyperbolic
  f_quasi_reflection_eq_unitary_transvection_mul --> polynomials
  f_quasi_reflection_eq_unitary_transvection_mul --> linear_algebra
  f_special_unitary_hyperbolic_plane_mem_transvections --> f_adelic_hermitian_forms__is_herm_hyperbolic
  f_special_unitary_hyperbolic_plane_mem_transvections --> f_nontrivial_transvection
  f_special_unitary_hyperbolic_plane_mem_transvections --> linear_algebra
  f_unitary_transvection_submonoid_normal_det_one --> f_adelic_lattice_proofs__transvection_identities_unitary
  f_unitary_transvection_submonoid_normal_det_one --> f_adelic_hermitian_forms__is_herm_hyperbolic
  f_unitary_transvection_submonoid_normal_det_one --> concept_hermitian_unitary_matrices
  f_unitary_transvection_submonoid_normal_det_one --> concept_normal_subgroups_quotients
  f_unitary_transvection_submonoid_normal_det_one --> linear_algebra
  f_exists_coordinate --> number_fields
  f_exists_coordinate --> rings_fields
  f_exists_coordinate --> complex_numbers
  f_one_letter_gauss_jets__statement_f --> f_gauss_jet_bounds__statement_k
  f_one_letter_gauss_jets__statement_f --> f_gauss_jet_bounds__statement_m
  f_one_letter_gauss_jets__statement_f --> f_one_letter_gauss_jets__odd_level_gain_sum
  f_one_letter_gauss_jets__statement_f --> f_incoming_bounds__incoming_bound
  f_one_letter_gauss_jets__statement_f --> f_gauss_jet_bounds__statement
  f_one_letter_gauss_jets__statement_f --> concept_ultrametric_norm
  f_one_letter_gauss_jets__statement_f --> concept_roots_of_unity_kummer
  f_one_letter_gauss_jets__statement_f --> concept_exterior_powers
  f_differentiable_class_function_param --> f_minor_formulas__cay_div_of
  f_differentiable_class_function_param --> complex_analysis
  f_differentiable_class_function_param --> polynomials
  f_iterated_deriv_zero_of_bound --> complex_analysis
  f_iterated_deriv_zero_of_bound --> calculus
  f_iterated_deriv_zero_of_bound --> real_analysis
  f_s_prime_of --> f_differentiable_class_function_param
  f_s_prime_of --> f_iterated_deriv_zero_of_bound
  f_s_prime_of --> f_continuous_herm
  f_s_prime_of --> f_differentiable_of_top
  f_s_prime_of --> f_mollified_integrability__cls_bound_alt
  f_s_prime_of --> f_mollified_integrability__cls_gain_st
  f_s_prime_of --> f_minor_formulas__cay_div_of
  f_s_prime_of --> analytic_continuation
  f_s_prime_of --> complex_analysis
  f_continuous_herm --> complex_powers
  f_continuous_herm --> complex_analysis
  f_continuous_herm --> calculus
  f_continuous_herm --> real_analysis
  f_continuous_herm --> f_mollified_integrability__cls_bound_alt
  f_differentiable_of_top --> f_holomorphic_continuation__is_sing_test
  f_differentiable_of_top --> calculus
  f_differentiable_of_top --> real_analysis
  f_mem_right_inv_right_twisted --> groups
  f_mem_right_inv_right_twisted --> linear_algebra
  f_mem_right_inv_right_twisted --> concept_normal_subgroups_quotients
  f_mem_tw_inv --> f_mem_right_inv_right_twisted
  f_mem_tw_inv --> concept_group_homology
  f_mem_tw_inv --> concept_group_representations
  f_mem_tw_inv --> linear_algebra
  f_finrank_twisted_left_invariant_mul_of_free_action --> f_mem_tw_inv
  f_finrank_twisted_left_invariant_mul_of_free_action --> concept_group_actions
  f_finrank_twisted_left_invariant_mul_of_free_action --> concept_normal_subgroups_quotients
  f_finrank_twisted_left_invariant_mul_of_free_action --> counting
  f_finrank_twisted_left_invariant_mul_of_free_action --> linear_algebra
  f_finrank_order_three_relation_add_twisted_invariant_le --> f_mem_tw_inv
  f_finrank_order_three_relation_add_twisted_invariant_le --> linear_algebra
  f_finrank_cocycle_extension_le_order_three_relation_add --> f_mem_tw_inv
  f_finrank_cocycle_extension_le_order_three_relation_add --> concept_group_representations
  f_finrank_cocycle_extension_le_order_three_relation_add --> linear_algebra
  f_finrank_cocycles_add_twisted_invariant_le_extension --> f_mem_tw_inv
  f_finrank_cocycles_add_twisted_invariant_le_extension --> concept_group_homology
  f_finrank_cocycles_add_twisted_invariant_le_extension --> concept_normal_subgroups_quotients
  f_finrank_cocycles_add_twisted_invariant_le_extension --> linear_algebra
  f_finrank_eichler_shimura_cocycles_le_gamma1 --> f_finrank_twisted_left_invariant_mul_of_free_action
  f_finrank_eichler_shimura_cocycles_le_gamma1 --> f_finrank_order_three_relation_add_twisted_invariant_le
  f_finrank_eichler_shimura_cocycles_le_gamma1 --> f_finrank_cocycle_extension_le_order_three_relation_add
  f_finrank_eichler_shimura_cocycles_le_gamma1 --> f_finrank_cocycles_add_twisted_invariant_le_extension
  f_finrank_eichler_shimura_cocycles_le_gamma1 --> f_mem_tw_inv
  f_finrank_eichler_shimura_cocycles_le_gamma1 --> f_foundations__is_d_c_reps
  f_finrank_eichler_shimura_cocycles_le_gamma1 --> concept_modular_forms
  f_finrank_eichler_shimura_cocycles_le_gamma1 --> polynomials
  f_fundamental_domains__signature --> concept_hermitian_unitary_matrices
  f_fundamental_domains__signature --> number_fields
  f_fundamental_domains__signature --> complex_numbers
  f_fundamental_domains__signature --> concept_haar_measure_fundamental_domain
  f_fundamental_domains__signature --> linear_algebra
  f_hermitian_trace_forms__exists_orthogonal_basis_dot_product_apply_eq --> f_fundamental_domains__signature
  f_hermitian_trace_forms__exists_orthogonal_basis_dot_product_apply_eq --> concept_hermitian_unitary_matrices
  f_hermitian_trace_forms__exists_orthogonal_basis_dot_product_apply_eq --> linear_algebra
  f_exists_anisotropic_orthogonal_basis_hermitian --> f_hermitian_trace_forms__exists_orthogonal_basis_dot_product_apply_eq
  f_exists_anisotropic_orthogonal_basis_hermitian --> f_adelic_hermitian_forms__is_herm_form
  f_exists_anisotropic_orthogonal_basis_hermitian --> concept_hermitian_unitary_matrices
  f_exists_anisotropic_orthogonal_basis_hermitian --> number_fields
  f_exists_quasi_reflection_prod_mul_vec_eq --> f_adelic_hermitian_forms__is_herm_form
  f_exists_quasi_reflection_prod_mul_vec_eq --> concept_hermitian_unitary_matrices
  f_exists_quasi_reflection_prod_mul_vec_eq --> linear_algebra
  f_exists_quasi_reflection_prod_mul_vec_eq --> number_fields
  f_unitary_matrix_eq_prod_quasi_reflections --> f_exists_anisotropic_orthogonal_basis_hermitian
  f_unitary_matrix_eq_prod_quasi_reflections --> f_exists_quasi_reflection_prod_mul_vec_eq
  f_unitary_matrix_eq_prod_quasi_reflections --> f_adelic_lattice_proofs__unitary_quasi_reflection_laws
  f_unitary_matrix_eq_prod_quasi_reflections --> f_adelic_hermitian_forms__is_herm_form
  f_unitary_matrix_eq_prod_quasi_reflections --> concept_hermitian_unitary_matrices
  f_product_formula_haar__norm_mod --> concept_haar_measure_fundamental_domain
  f_product_formula_haar__norm_mod --> p_adic_numbers
  f_product_formula_haar__norm_mod --> concept_ultrametric_norm
  f_product_formula_haar__norm_mod --> concept_valuation_rings
  f_product_formula_haar__norm_mod --> number_fields
  f_norm_index --> f_product_formula_haar__norm_mod
  f_norm_index --> concept_haar_measure_fundamental_domain
  f_norm_index --> p_adic_numbers
  f_norm_index --> concept_valuation_rings
  f_card_quotient_eq_abs_norm --> f_product_formula_haar__norm_mod
  f_card_quotient_eq_abs_norm --> concept_dedekind_domains
  f_card_quotient_eq_abs_norm --> concept_ideals_and_discriminant
  f_card_quotient_eq_abs_norm --> concept_valuation_rings
  f_card_quotient_eq_abs_norm --> number_fields
  f_card_quotient_eq_abs_norm --> p_adic_numbers
  f_mod_f_iota_finite_place --> f_product_formula_haar__norm_mod
  f_mod_f_iota_finite_place --> f_cusp_span_norm_bounds__fraction_field_to_generic_stalk_algebra_map_eq
  f_mod_f_iota_finite_place --> concept_ultrametric_norm
  f_mod_f_iota_finite_place --> number_fields
  f_mod_f_iota_finite_place --> p_adic_numbers
  f_product_formula_haar__res_char_iff --> f_product_formula_haar__norm_mod
  f_product_formula_haar__res_char_iff --> f_cusp_span_norm_bounds__psi_e_def
  f_product_formula_haar__res_char_iff --> p_adic_numbers
  f_product_formula_haar__res_char_iff --> concept_dedekind_domains
  f_product_formula_haar__res_char_iff --> concept_haar_measure_fundamental_domain
  f_norm_st --> f_mod_f_iota_finite_place
  f_norm_st --> f_norm_index
  f_norm_st --> f_card_quotient_eq_abs_norm
  f_norm_st --> f_product_formula_haar__res_char_iff
  f_norm_st --> f_product_formula_haar__norm_mod
  f_norm_st --> number_fields
  f_norm_st --> p_adic_numbers
  f_product_formula_haar__tr_base --> p_adic_numbers
  f_product_formula_haar__tr_base --> number_fields
  f_product_formula_haar__tr_base --> concept_tensor_product_of_algebras
  f_period_integrals__prod_formula_e --> f_cusp_span_norm_bounds__fraction_field_to_generic_stalk_algebra_map_eq
  f_period_integrals__prod_formula_e --> f_cusp_span_norm_bounds__psi_e_def
  f_period_integrals__prod_formula_e --> number_fields
  f_period_integrals__prod_formula_e --> p_adic_numbers
  f_period_integrals__prod_formula_e --> concept_ultrametric_norm
  f_w0_eq_of_rt_eq --> primes_divisibility
  f_w0_eq_of_rt_eq --> complex_numbers
  f_w0_eq_of_rt_eq --> number_fields
  f_w0_eq_of_rt_eq --> modular_arithmetic
  f_period_integrals__iso_inv_metric --> concept_hermitian_unitary_matrices
  f_period_integrals__iso_inv_metric --> linear_algebra
  f_period_integrals__iso_inv_metric --> counting
  f_orbital_bounds_conclusion__iso_inv_metric --> f_period_integrals__iso_inv_metric
  f_orbital_bounds_conclusion__iso_inv_metric --> f_iso_inv_metric_of_hw
  f_orbital_bounds_conclusion__iso_inv_metric --> f_poly_eq_zero_of_circle
  f_col_choice_fintype --> f_period_integrals__iso_inv_metric
  f_col_choice_fintype --> concept_hermitian_unitary_matrices
  f_col_choice_fintype --> counting
  f_hermitian_vector_map --> f_col_choice_fintype
  f_hermitian_vector_map --> f_metric_constant_bound
  f_hermitian_vector_map --> linear_algebra
  f_hv_scalar --> f_col_choice_fintype
  f_hv_scalar --> f_vnu_map_zero
  f_hv_scalar --> concept_hermitian_unitary_matrices
  f_iso_inv_metric_of_hw --> f_symmetric_measure_l2_norm_eq_resolution_l2
  f_iso_inv_metric_of_hw --> f_vnu_map_zero
  f_iso_inv_metric_of_hw --> f_hermitian_vector_map
  f_iso_inv_metric_of_hw --> f_oe_eq_of_range_sub
  f_iso_inv_metric_of_hw --> f_quotient_rank
  f_iso_inv_metric_of_hw --> f_hv_scalar
  f_iso_inv_metric_of_hw --> f_col_choice_fintype
  f_metric_constant_bound --> f_col_choice_fintype
  f_metric_constant_bound --> f_monomial_frame_span__det_submatrix_fun
  f_metric_constant_bound --> linear_algebra
  f_oe_eq_of_range_sub --> f_col_choice_fintype
  f_oe_eq_of_range_sub --> linear_algebra
  f_poly_eq_zero_of_circle --> f_col_choice_fintype
  f_poly_eq_zero_of_circle --> f_oe_eq_of_range_sub
  f_poly_eq_zero_of_circle --> f_vnu_map_zero
  f_poly_eq_zero_of_circle --> polynomials
  f_poly_eq_zero_of_circle --> complex_numbers
  f_poly_eq_zero_of_circle --> concept_hermitian_unitary_matrices
  f_quotient_rank --> f_col_choice_fintype
  f_quotient_rank --> concept_hermitian_unitary_matrices
  f_quotient_rank --> linear_algebra
  f_symmetric_measure_l2_norm_eq_resolution_l2 --> f_col_choice_fintype
  f_symmetric_measure_l2_norm_eq_resolution_l2 --> f_period_integrals__iso_inv_metric
  f_symmetric_measure_l2_norm_eq_resolution_l2 --> concept_hermitian_unitary_matrices
  f_symmetric_measure_l2_norm_eq_resolution_l2 --> linear_algebra
  f_vnu_map_zero --> f_col_choice_fintype
  f_vnu_map_zero --> f_oe_eq_of_range_sub
  f_vnu_map_zero --> concept_hermitian_unitary_matrices
  f_vnu_map_zero --> linear_algebra
  f_mem_range_of_integral_at_height_one_over --> f_toric_varieties__krull_domain
  f_mem_range_of_integral_at_height_one_over --> concept_integral_closure_fraction_fields
  f_mem_range_of_integral_at_height_one_over --> concept_prime_ideals_localization
  f_mem_range_of_integral_at_height_one_over --> concept_coordinate_rings_dimension
  f_mem_reg_at_of_codim_one --> f_mem_range_of_integral_at_height_one_over
  f_mem_reg_at_of_codim_one --> f_geometry_proofs__reg_at_fraction_noetherian_closed
  f_mem_reg_at_of_codim_one --> f_geometry_proofs__gen_map_stalk_specializes
  f_mem_reg_at_of_codim_one --> f_global_geometry__is_cpt_gen
  f_mem_reg_at_of_codim_one --> f_global_geometry__coords_at
  f_mem_reg_at_of_codim_one --> concept_schemes_basics
  f_mem_reg_at_of_codim_one --> concept_noetherian_and_irreducible_components
  f_mem_reg_at_of_codim_one --> concept_local_rings
  f_line_lattice_generator_codim_one --> f_mem_reg_at_of_codim_one
  f_line_lattice_generator_codim_one --> f_global_geometry__exists_gen_of_is_v_b_one
  f_line_lattice_generator_codim_one --> f_global_geometry__is_cpt_gen
  f_line_lattice_generator_codim_one --> f_global_geometry__level_sections_exact_kernel_locus_open
  f_line_lattice_generator_codim_one --> concept_schemes_basics
  f_scheme_cohomology__regular_local_domain --> concept_regular_local_rings
  f_scheme_cohomology__regular_local_domain --> concept_local_rings
  f_scheme_cohomology__regular_local_domain --> concept_prime_ideals_localization
  f_scheme_cohomology__regular_local_domain --> concept_coordinate_rings_dimension
  f_scheme_cohomology__regular_u_f_d_serre --> f_scheme_cohomology__regular_local_domain
  f_scheme_cohomology__regular_u_f_d_serre --> concept_regular_local_rings
  f_scheme_cohomology__regular_u_f_d_serre --> concept_projective_modules
  f_scheme_cohomology__regular_u_f_d_serre --> concept_chain_complexes_homology
  f_scheme_cohomology__regular_u_f_d_serre --> concept_local_rings
  f_scheme_cohomology__regular_u_f_d_localization --> f_scheme_cohomology__regular_u_f_d_serre
  f_scheme_cohomology__regular_u_f_d_localization --> f_scheme_cohomology__regular_local_domain
  f_scheme_cohomology__regular_u_f_d_localization --> concept_regular_local_rings
  f_scheme_cohomology__regular_u_f_d_localization --> concept_projective_modules
  f_scheme_cohomology__regular_u_f_d_localization --> concept_prime_ideals_localization
  f_st_adic_completion_regular --> concept_adic_completion
  f_st_adic_completion_regular --> concept_regular_local_rings
  f_st_adic_completion_regular --> concept_prime_ideals_localization
  f_st_derivation_adic_completion --> concept_adic_completion
  f_st_derivation_adic_completion --> concept_derivations_smoothness
  f_st_derivation_adic_completion --> polynomials
  f_st_derivation_cotangent_independent --> concept_derivations_smoothness
  f_st_derivation_cotangent_independent --> concept_local_rings
  f_st_derivation_cotangent_independent --> concept_prime_ideals_localization
  f_complex_analytic_sets__st_flat_normal_fibres --> concept_flat_modules
  f_complex_analytic_sets__st_flat_normal_fibres --> concept_integral_closure_fraction_fields
  f_complex_analytic_sets__st_flat_normal_fibres --> concept_prime_ideals_localization
  f_complex_analytic_sets__st_flat_normal_fibres --> concept_local_rings
  f_complex_analytic_sets__st_formal_fibres_regular --> f_complex_analytic_sets__st_flat_normal_fibres
  f_complex_analytic_sets__st_formal_fibres_regular --> concept_adic_completion
  f_complex_analytic_sets__st_formal_fibres_regular --> concept_finitely_generated_algebras
  f_complex_analytic_sets__st_formal_fibres_regular --> concept_regular_local_rings
  f_st_formal_fibres_regular_polynomial --> f_complex_analytic_sets__st_formal_fibres_regular
  f_st_formal_fibres_regular_polynomial --> concept_adic_completion
  f_st_formal_fibres_regular_polynomial --> concept_regular_local_rings
  f_st_formal_fibres_regular_polynomial --> polynomials
  f_complex_analytic_sets__st_jacobian_prime_derivations --> concept_derivations_smoothness
  f_complex_analytic_sets__st_jacobian_prime_derivations --> concept_prime_ideals_localization
  f_complex_analytic_sets__st_jacobian_prime_derivations --> concept_coordinate_rings_dimension
  f_complex_analytic_sets__st_jacobian_prime_derivations --> polynomials
  f_st_regular_quotient_independent --> concept_regular_local_rings
  f_st_regular_quotient_independent --> concept_local_rings
  f_p_formal_fibres_regular_polynomial --> f_complex_analytic_sets__st_jacobian_prime_derivations
  f_p_formal_fibres_regular_polynomial --> f_st_derivation_adic_completion
  f_p_formal_fibres_regular_polynomial --> f_st_adic_completion_regular
  f_p_formal_fibres_regular_polynomial --> f_st_derivation_cotangent_independent
  f_p_formal_fibres_regular_polynomial --> f_st_regular_quotient_independent
  f_p_formal_fibres_regular_polynomial --> f_st_formal_fibres_regular_polynomial
  f_p_formal_fibres_regular_polynomial --> f_scheme_cohomology__regular_u_f_d_localization
  f_p_formal_fibres_regular_polynomial --> concept_regular_local_rings
  f_p_formal_fibres_regular_polynomial --> concept_adic_completion
  f_link_exactness_stability__seq_chain_cycle_bounded_by_cone --> f_global_twisting__sub_closed
  f_link_exactness_stability__seq_chain_cycle_bounded_by_cone --> concept_chain_complexes_homology
  f_exact_at_of_links_outside_exact_at_of_coned --> f_link_exactness_stability__exists_homologous_cycle_with_entries_in_of_exact_at_links
  f_exact_at_of_links_outside_exact_at_of_coned --> f_link_exactness_stability__seq_chain_cycle_bounded_by_cone
  f_exact_at_of_links_outside_exact_at_of_coned --> f_global_twisting__sub_closed
  f_exact_at_of_links_outside_exact_at_of_coned --> concept_chain_complexes_homology
  f_exact_at_link_nil_coord_subspace_union_translate --> f_exact_at_of_links_outside_exact_at_of_coned
  f_exact_at_link_nil_coord_subspace_union_translate --> f_link_exactness_stability__cons_mem_uni_m_iff_map_sub_smul
  f_exact_at_link_nil_coord_subspace_union_translate --> f_link_exactness_stability__link_in_uni_m_eq_shorter_of_form_eq_one
  f_exact_at_link_nil_coord_subspace_union_translate --> f_link_exactness_stability__sub_closed_and_perm_and_linear_equiv_invariant_uni_m
  f_exact_at_link_nil_coord_subspace_union_translate --> f_global_twisting__link_exact_aff
  f_exact_at_link_nil_coord_subspace_union_translate --> f_global_twisting__sub_closed
  f_exact_at_link_nil_coord_subspace_union_translate --> concept_gl_infinity_homology_stability
  f_exact_at_link_nil_coord_subspace_union_translate --> concept_chain_complexes_homology
  f_divisor_base__omega_factorization --> number_fields
  f_divisor_base__omega_factorization --> concept_ideals_and_discriminant
  f_divisor_base__omega_factorization --> concept_modular_forms
  f_divisor_base__omega_factorization --> complex_analysis
  f_divisor_base__omega_factorization --> analytic_continuation
  f_divisor_proofs__k_fac_differentiable --> f_divisor_base__omega_factorization
  f_divisor_proofs__k_fac_differentiable --> complex_powers
  f_divisor_proofs__k_fac_differentiable --> complex_analysis
  f_divisor_proofs__k_fac_differentiable --> fourier_analysis
  f_hecke_phi_fourier_constant_at_zero_zero --> f_divisor_proofs__k_fac_differentiable
  f_hecke_phi_fourier_constant_at_zero_zero --> calculus
  f_hecke_phi_fourier_constant_at_zero_zero --> complex_numbers
  f_hecke_phi_fourier_constant_at_zero_zero --> real_analysis
  f_divisor_proofs__hecke_phi_fourier_constant_at_zero_differentiable_on --> f_divisor_proofs__k_fac_differentiable
  f_divisor_proofs__hecke_phi_fourier_constant_at_zero_differentiable_on --> f_divisor_base__omega_factorization
  f_divisor_proofs__hecke_phi_fourier_constant_at_zero_differentiable_on --> calculus
  f_divisor_proofs__hecke_phi_fourier_constant_at_zero_differentiable_on --> real_analysis
  f_divisor_proofs__hecke_phi_fourier_constant_at_zero_differentiable_on --> complex_analysis
  f_divisor_proofs__hecke_phi_fourier_constant_at_zero_differentiable_on --> complex_powers
  f_is_smooth_holomorphic_in_sigma_family_mul_left --> f_divisor_proofs__k_fac_differentiable
  f_is_smooth_holomorphic_in_sigma_family_mul_left --> f_divisor_base__omega_factorization
  f_is_smooth_holomorphic_in_sigma_family_mul_left --> complex_analysis
  f_divisor_proofs__is_smooth_holomorphic_in_sigma_family_add --> f_divisor_proofs__k_fac_differentiable
  f_divisor_proofs__is_smooth_holomorphic_in_sigma_family_add --> f_divisor_base__omega_factorization
  f_divisor_proofs__is_smooth_holomorphic_in_sigma_family_add --> real_analysis
  f_divisor_proofs__is_smooth_holomorphic_in_sigma_family_add --> complex_analysis
  f_upper_half_plane_product_prod_im_rpow_cont_diff_on --> f_divisor_base__omega_factorization
  f_upper_half_plane_product_prod_im_rpow_cont_diff_on --> f_divisor_proofs__k_fac_differentiable
  f_upper_half_plane_product_prod_im_rpow_cont_diff_on --> complex_powers
  f_upper_half_plane_product_prod_im_rpow_cont_diff_on --> complex_analysis
  f_prod_im_iterated_wirtinger_deriv_word_differentiable_on --> f_divisor_proofs__is_smooth_holomorphic_in_sigma_family_add
  f_prod_im_iterated_wirtinger_deriv_word_differentiable_on --> f_divisor_base__omega_factorization
  f_prod_im_iterated_wirtinger_deriv_word_differentiable_on --> complex_powers
  f_prod_im_iterated_wirtinger_deriv_word_differentiable_on --> complex_analysis
  f_prod_im_iterated_wirtinger_deriv_word_differentiable_on --> calculus
  f_hecke_eisenstein_zero_frequency_part_is_smooth_holomorphic --> f_hecke_phi_fourier_constant_at_zero_zero
  f_hecke_eisenstein_zero_frequency_part_is_smooth_holomorphic --> f_divisor_proofs__hecke_phi_fourier_constant_at_zero_differentiable_on
  f_hecke_eisenstein_zero_frequency_part_is_smooth_holomorphic --> f_is_smooth_holomorphic_in_sigma_family_mul_left
  f_hecke_eisenstein_zero_frequency_part_is_smooth_holomorphic --> f_upper_half_plane_product_prod_im_rpow_cont_diff_on
  f_hecke_eisenstein_zero_frequency_part_is_smooth_holomorphic --> f_prod_im_iterated_wirtinger_deriv_word_differentiable_on
  f_hecke_eisenstein_zero_frequency_part_is_smooth_holomorphic --> f_divisor_proofs__k_fac_differentiable
  f_hecke_eisenstein_zero_frequency_part_is_smooth_holomorphic --> f_divisor_base__omega_factorization
  f_hecke_eisenstein_zero_frequency_part_is_smooth_holomorphic --> complex_analysis
  f_hecke_eisenstein_zero_frequency_part_is_smooth_holomorphic --> analytic_continuation
  f_hecke_eisenstein_zero_frequency_part_is_smooth_holomorp_statement --> f_hecke_eisenstein_zero_frequency_part_is_smooth_holomorphic
  f_hecke_eisenstein_zero_frequency_part_is_smooth_holomorp_statement --> f_divisor_base__omega_factorization
  f_hecke_eisenstein_zero_frequency_part_is_smooth_holomorp_statement --> f_divisor_proofs__k_fac_differentiable
  f_divisors₂__partial_zeta_functional_equation --> f_divisor_base__omega_factorization
  f_divisors₂__partial_zeta_functional_equation --> functional_equation_zeta
  f_divisors₂__partial_zeta_functional_equation --> gamma_function
  f_divisors₂__partial_zeta_functional_equation --> number_fields
  f_divisors₂__partial_zeta_functional_equation --> concept_ideals_and_discriminant
  f_divisors₂__partial_zeta_functional_equation --> concept_dedekind_domains
  f_ferrand_pushout_affine_flat_and_pushouts --> f_schlessinger_flat_fibre_product
  f_ferrand_pushout_affine_flat_and_pushouts --> f_is_pushout_app_l_e_of_is_pullback_of_is_affine
  f_ferrand_pushout_affine_flat_and_pushouts --> concept_flat_modules
  f_ferrand_pushout_affine_flat_and_pushouts --> concept_categorical_pullbacks
  f_ferrand_pushout_affine_flat_and_pushouts --> concept_schemes_basics
  f_flat_ferrand_pushout_over_fibre_product --> f_ferrand_pushout_affine_flat_and_pushouts
  f_flat_ferrand_pushout_over_fibre_product --> f_is_pullback_of_forall_is_pushout_app
  f_flat_ferrand_pushout_over_fibre_product --> concept_flat_modules
  f_flat_ferrand_pushout_over_fibre_product --> concept_categorical_pullbacks
  f_flat_ferrand_pushout_over_fibre_product --> concept_schemes_basics
  f_flat_quotient_smul_top_of_surjective_flat --> concept_flat_modules
  f_flat_quotient_smul_top_of_surjective_flat --> rings_fields
  f_is_pullback_of_forall_is_pushout_app --> f_is_pushout_app_l_e_of_is_pullback_of_is_affine
  f_is_pullback_of_forall_is_pushout_app --> concept_categorical_pullbacks
  f_is_pullback_of_forall_is_pushout_app --> concept_schemes_basics
  f_is_pushout_app_l_e_of_is_pullback_of_is_affine --> f_base_change_kernels__affine
  f_is_pushout_app_l_e_of_is_pullback_of_is_affine --> concept_categorical_pullbacks
  f_is_pushout_app_l_e_of_is_pullback_of_is_affine --> concept_schemes_basics
  f_is_pushout_app_l_e_of_is_pullback_of_is_affine --> concept_tensor_product_of_algebras
  f_mul_tensor_injective_of_flat_base_change_ker_inf --> concept_flat_modules
  f_mul_tensor_injective_of_flat_base_change_ker_inf --> concept_tensor_product_of_algebras
  f_r_tensor_injective_of_pow_smul_eq_bot --> concept_flat_modules
  f_r_tensor_injective_of_pow_smul_eq_bot --> concept_chain_complexes_homology
  f_r_tensor_injective_of_pow_smul_eq_bot --> concept_tensor_product_of_algebras
  f_schlessinger_flat_fibre_product --> f_r_tensor_injective_of_pow_smul_eq_bot
  f_schlessinger_flat_fibre_product --> f_flat_quotient_smul_top_of_surjective_flat
  f_schlessinger_flat_fibre_product --> f_mul_tensor_injective_of_flat_base_change_ker_inf
  f_schlessinger_flat_fibre_product --> concept_flat_modules
  f_schlessinger_flat_fibre_product --> concept_categorical_pullbacks
  f_schlessinger_flat_fibre_product --> concept_dual_numbers
  f_base_change_kernels__affine --> concept_categorical_pullbacks
  f_base_change_kernels__affine --> concept_schemes_basics
  f_base_change_kernels__affine --> concept_tensor_product_of_algebras
  f_base_change_kernels__affine --> concept_group_schemes
  f_pt_af_type_main --> f_x_pt_af_type
  f_pt_af_type_main --> f_commutative_algebra__lie_lattice_data
  f_pt_af_type_main --> linear_algebra
  f_x_pt_af_type --> f_commutative_algebra__lie_lattice_data
  f_x_pt_af_type --> f_commutative_algebra__is_tight
  f_x_pt_af_type --> linear_algebra
  f_x_pt_af_type --> modular_arithmetic
  f_x_pt_af_type --> concept_lattice_point_counting
  f_divisor_base__trace_dual_different --> number_fields
  f_divisor_base__trace_dual_different --> concept_ideals_and_discriminant
  f_divisor_base__trace_dual_different --> concept_dedekind_domains
  f_divisor_base__trace_dual_different --> concept_lattice_point_counting
  f_divisor_base__trace_dual_different --> concept_integral_closure_fraction_fields
  f_exists_equiv_fourier_classes_pos_cone_summand --> f_rep_ne_zero
  f_exists_equiv_fourier_classes_pos_cone_summand --> f_divisor_base__omega_factorization
  f_exists_equiv_fourier_classes_pos_cone_summand --> number_fields
  f_exists_equiv_fourier_classes_pos_cone_summand --> concept_group_actions
  f_exists_equiv_lattice_classes_fibre_summand --> f_rep_ne_zero
  f_exists_equiv_lattice_classes_fibre_summand --> f_divisor_base__omega_factorization
  f_exists_equiv_lattice_classes_fibre_summand --> number_fields
  f_exists_equiv_lattice_classes_fibre_summand --> concept_group_actions
  f_hilbert_eisenstein_nonconstant_terms_has_sum --> f_lattice_sum_eq_cone_sum
  f_hilbert_eisenstein_nonconstant_terms_has_sum --> f_exists_equiv_lattice_classes_fibre_summand
  f_hilbert_eisenstein_nonconstant_terms_has_sum --> f_exists_equiv_fourier_classes_pos_cone_summand
  f_hilbert_eisenstein_nonconstant_terms_has_sum --> f_divisor_base__trace_dual_different
  f_hilbert_eisenstein_nonconstant_terms_has_sum --> f_divisor_base__omega_factorization
  f_hilbert_eisenstein_nonconstant_terms_has_sum --> f_rep_ne_zero
  f_hilbert_eisenstein_nonconstant_terms_has_sum --> infinite_series
  f_hilbert_eisenstein_nonconstant_terms_has_sum --> concept_modular_forms
  f_lattice_sum_eq_cone_sum --> f_divisor_base__trace_dual_different
  f_lattice_sum_eq_cone_sum --> f_lipschitz_constant_inverse_different_eisenstein
  f_lattice_sum_eq_cone_sum --> f_mem_trace_dual_signed_positive_cone_iff_totally_positive
  f_lattice_sum_eq_cone_sum --> f_divisor_base__omega_factorization
  f_lattice_sum_eq_cone_sum --> concept_lattice_point_counting
  f_lattice_sum_eq_cone_sum --> infinite_series
  f_lipschitz_constant_inverse_different_eisenstein --> f_divisor_base__trace_dual_different
  f_lipschitz_constant_inverse_different_eisenstein --> f_divisor_base__omega_factorization
  f_lipschitz_constant_inverse_different_eisenstein --> concept_ideals_and_discriminant
  f_lipschitz_constant_inverse_different_eisenstein --> number_fields
  f_lipschitz_constant_inverse_different_eisenstein --> complex_powers
  f_mem_trace_dual_signed_positive_cone_iff_totally_positive --> f_divisor_base__trace_dual_different
  f_mem_trace_dual_signed_positive_cone_iff_totally_positive --> f_divisor_base__omega_factorization
  f_mem_trace_dual_signed_positive_cone_iff_totally_positive --> number_fields
  f_mem_trace_dual_signed_positive_cone_iff_totally_positive --> concept_ideals_and_discriminant
  f_rep_ne_zero --> number_fields
  f_rep_ne_zero --> concept_ideals_and_discriminant
  f_rep_ne_zero --> concept_group_actions
  f_rep_ne_zero --> concept_normal_subgroups_quotients
  f_dense_coordinate_torus --> concept_point_set_topology
  f_dense_coordinate_torus --> complex_numbers
  f_integral_ang_meas --> calculus
  f_integral_ang_meas --> complex_analysis
  f_integral_ang_meas --> trigonometry
  f_integral_ang_meas --> real_analysis
  f_section_boundary_closed_and_codense --> f_snc_boundary_coordinate_chart
  f_section_boundary_closed_and_codense --> f_dense_coordinate_torus
  f_section_boundary_closed_and_codense --> f_levi_forms__is_reg_family_inhabit_statement
  f_section_boundary_closed_and_codense --> concept_point_set_topology
  f_section_boundary_closed_and_codense --> concept_complex_analytic_sets
  f_snc_boundary_coordinate_chart --> f_levi_forms__is_reg_family_inhabit_statement
  f_snc_boundary_coordinate_chart --> concept_complex_analytic_sets
  f_snc_boundary_coordinate_chart --> complex_analysis
  f_levi_forms__is_reg_family_inhabit_statement --> f_plurisubharmonic_functions__is_psh_locally_integrable_statement
  f_levi_forms__is_reg_family_inhabit_statement --> f_analytic_forms__ma_int_empty
  f_levi_forms__is_reg_family_inhabit_statement --> f_potential_theory__is_potential_of_fun
  f_levi_forms__is_reg_family_inhabit_statement --> concept_complex_analytic_sets
  f_levi_forms__is_reg_family_inhabit_statement --> complex_analysis
  f_plurisubharmonic_functions__is_psh_locally_integrable_statement --> complex_analysis
  f_plurisubharmonic_functions__is_psh_locally_integrable_statement --> real_analysis
  f_plurisubharmonic_functions__is_psh_locally_integrable_statement --> calculus
  f_plurisubharmonic_functions__is_psh_locally_integrable_statement --> concept_hermitian_unitary_matrices
  f_plurisubharmonic_functions__is_psh_locally_integrable_statement --> f_analytic_forms__ma_int_empty
  f_potential_theory__psh_shift_a --> f_analytic_forms__ma_int_empty
  f_potential_theory__psh_shift_a --> complex_analysis
  f_potential_theory__psh_shift_a --> calculus
  f_potential_theory__psh_shift_a --> linear_algebra
  f_root_power_sum_character_additive_and_x_sub_one_pow --> polynomials
  f_root_power_sum_character_additive_and_x_sub_one_pow --> algebraic_closure
  f_root_power_sum_character_additive_and_x_sub_one_pow --> concept_symmetric_polynomials
  f_divisor_proofs__exists_block_parabolic_subgroup_levi_projection --> linear_algebra
  f_divisor_proofs__exists_block_parabolic_subgroup_levi_projection --> groups
  f_divisor_proofs__exists_block_parabolic_subgroup_levi_projection --> polynomials
  f_divisor_proofs__exists_block_parabolic_subgroup_levi_projection --> concept_group_representations
  f_pairing_cuspidal_character_g_l_root_power_sum_character --> f_pairing_harish_chandra_induction_charpoly_function
  f_pairing_cuspidal_character_g_l_root_power_sum_character --> f_root_power_sum_character_additive_and_x_sub_one_pow
  f_pairing_cuspidal_character_g_l_root_power_sum_character --> f_ab_by_p_of_comm
  f_pairing_cuspidal_character_g_l_root_power_sum_character --> f_commutative_algebra__invariant_subspace_mobius_inverse_rec_eq_of_finrank_lt
  f_pairing_cuspidal_character_g_l_root_power_sum_character --> concept_group_representations
  f_pairing_cuspidal_character_g_l_root_power_sum_character --> counting
  f_pairing_harish_chandra_induction_charpoly_function --> f_divisor_proofs__exists_block_parabolic_subgroup_levi_projection
  f_pairing_harish_chandra_induction_charpoly_function --> f_twisted_harish_chandra_induction_g_l_is_twisted_class_fun
  f_pairing_harish_chandra_induction_charpoly_function --> f_divisors__orth_subrepresentation
  f_pairing_harish_chandra_induction_charpoly_function --> concept_group_representations
  f_pairing_harish_chandra_induction_charpoly_function --> concept_group_actions
  f_pairing_harish_chandra_induction_charpoly_function --> counting
  f_twisted_harish_chandra_induction_g_l_is_twisted_class_fun --> f_character_theory__invariant_subspace_mobius_inverse_charpoly_linear_equi
  f_twisted_harish_chandra_induction_g_l_is_twisted_class_fun --> linear_algebra
  f_twisted_harish_chandra_induction_g_l_is_twisted_class_fun --> groups
  f_twisted_harish_chandra_induction_g_l_is_twisted_class_fun --> concept_group_representations
  f_compact_casimir_bound_embedded_component --> f_jet_harmonics__compact_casimir_le_tensor_operator_raise
  f_compact_casimir_bound_embedded_component --> f_jet_harmonics__cas_k_is_symmetric_and_form
  f_compact_casimir_bound_embedded_component --> f_jets__sum_io_pr
  f_compact_casimir_bound_embedded_component --> concept_hermitian_unitary_matrices
  f_compact_casimir_bound_embedded_component --> linear_algebra
  f_tensor_product_action --> concept_tensor_product_of_algebras
  f_tensor_product_action --> concept_witt_vectors_ainf
  f_tensor_product_action --> concept_flat_modules
  f_tensor_product_action --> concept_exterior_powers
  f_tensor_product_action --> p_adic_numbers
  f_iota_scalar_one --> concept_witt_vectors_ainf
  f_iota_scalar_one --> concept_tensor_product_of_algebras
  f_iota_scalar_one --> linear_algebra
  f_iota_scalar_one --> f_divisors__xi_mul_nu
  f_charpoly_eq_quotient_charpoly_pow --> f_character_theory__charpoly_block_and_invariant_under_stabilizer_nilradic
  f_charpoly_eq_quotient_charpoly_pow --> linear_algebra
  f_charpoly_eq_quotient_charpoly_pow --> polynomials
  f_cyclic_generators_invariant_top --> f_charpoly_eq_quotient_charpoly_pow
  f_cyclic_generators_invariant_top --> f_exists_cyclic_generators_separable_min
  f_cyclic_generators_invariant_top --> concept_separable_polynomials
  f_cyclic_generators_invariant_top --> algebraic_closure
  f_cyclic_generators_invariant_top --> linear_algebra
  f_cyclic_generators_invariant_top --> polynomials
  f_exists_cyclic_generators_separable_min --> concept_separable_polynomials
  f_exists_cyclic_generators_separable_min --> algebraic_closure
  f_exists_cyclic_generators_separable_min --> linear_algebra
  f_exists_cyclic_generators_separable_min --> polynomials
  f_c_m_type_galois__statement_field --> f_c_m_type_galois__statement_group
  f_c_m_type_galois__statement_field --> number_fields
  f_c_m_type_galois__statement_field --> concept_galois_fixed_fields
  f_c_m_type_galois__statement_field --> concept_ideals_and_discriminant
  f_c_m_type_galois__statement_field --> concept_group_actions
  f_c_m_type_galois__statement_group --> f_formalism__statement_c_m
  f_c_m_type_galois__statement_group --> groups
  f_c_m_type_galois__statement_group --> counting
  f_c_m_type_galois__statement_group --> dirichlet_characters
  f_c_m_type_galois__statement_group --> modular_arithmetic
  f_quad_discr --> f_dirichlet_density__statement
  f_quad_discr --> number_fields
  f_quad_discr --> concept_ideals_and_discriminant
  f_quad_discr --> linear_algebra
  f_dirichlet_density__statement --> f_c_m_type_galois__statement_field
  f_dirichlet_density__statement --> f_c_m_type_galois__statement_group
  f_dirichlet_density__statement --> number_fields
  f_dirichlet_density__statement --> dirichlet_characters
  f_dirichlet_density__statement --> primes_divisibility
  f_dirichlet_density__statement --> concept_chebyshev_functions
  f_omega_poly --> dirichlet_characters
  f_omega_poly --> polynomials
  f_omega_poly --> modular_arithmetic
  f_dedekind_factor_k --> concept_lattices_in_the_plane
  f_dedekind_factor_k --> concept_ideals_and_discriminant
  f_dedekind_factor_k --> dirichlet_l_function
  f_dedekind_factor_k --> zeta_series
  f_dedekind_factor_k --> number_fields
  f_lat_i_top_basis --> f_quad_discr
  f_lat_i_top_basis --> f_dedekind_factor_k
  f_lat_i_top_basis --> number_fields
  f_lat_i_top_basis --> concept_lattices_in_the_plane
  f_lat_i_top_basis --> concept_integral_closure_fraction_fields
  f_lat_i_top_basis --> concept_ideals_and_discriminant
  f_formalism__statement_c_m --> modular_arithmetic
  f_formalism__statement_c_m --> counting
  f_formalism__statement_c_m --> primes_divisibility
  f_formalism__statement_c_m --> concept_chebyshev_functions
  f_p_holomorphic_kernel_fibre --> f_st_holomorphic_kernel_fibre
  f_p_holomorphic_kernel_fibre --> f_p_injective_holomorphic_inverse
  f_p_holomorphic_kernel_fibre --> complex_analysis
  f_p_holomorphic_kernel_fibre --> linear_algebra
  f_p_holomorphic_kernel_fibre --> concept_complex_analytic_sets
  f_p_injective_holomorphic_inverse --> f_st_injective_holomorphic_jacobian_ne_zero
  f_p_injective_holomorphic_inverse --> f_st_injective_holomorphic_inverse
  f_p_injective_holomorphic_inverse --> f_complex_analytic_sets__osgood_separate
  f_p_injective_holomorphic_inverse --> complex_analysis
  f_p_injective_holomorphic_inverse --> concept_point_set_topology
  f_st_holomorphic_kernel_fibre --> complex_analysis
  f_st_holomorphic_kernel_fibre --> linear_algebra
  f_st_injective_holomorphic_inverse --> f_st_injective_holomorphic_open
  f_st_injective_holomorphic_inverse --> complex_analysis
  f_st_injective_holomorphic_jacobian_ne_zero --> f_st_injective_holomorphic_open
  f_st_injective_holomorphic_jacobian_ne_zero --> complex_analysis
  f_st_injective_holomorphic_jacobian_ne_zero --> linear_algebra
  f_st_injective_holomorphic_open --> complex_analysis
  f_st_injective_holomorphic_open --> concept_point_set_topology
  f_cyclic_kummer_norm_fixed_hilbert90 --> f_adelic_lattice_proofs__kummer_galois
  f_cyclic_kummer_norm_fixed_hilbert90 --> concept_roots_of_unity_kummer
  f_cyclic_kummer_norm_fixed_hilbert90 --> concept_galois_fixed_fields
  f_cyclic_kummer_norm_fixed_hilbert90 --> concept_group_homology
  f_cyclic_kummer_norm_fixed_hilbert90 --> concept_group_actions
  f_cyclic_kummer_norm_fixed_hilbert90 --> f_adelic_hermitian_forms__mem_pow_sub
  f_adelic_lattice_proofs__exists_superset_mem_s_units --> number_fields
  f_adelic_lattice_proofs__exists_superset_mem_s_units --> concept_dedekind_domains
  f_adelic_lattice_proofs__exists_superset_mem_s_units --> concept_ultrametric_norm
  f_adelic_lattice_proofs__exists_superset_mem_s_units --> concept_ideals_and_discriminant
  f_exists_unit_valuation_eq_of_adm --> number_fields
  f_exists_unit_valuation_eq_of_adm --> concept_dedekind_domains
  f_exists_unit_valuation_eq_of_adm --> concept_ultrametric_norm
  f_exists_unit_valuation_eq_of_adm --> concept_discrete_valuation_ring
  f_galois_places_transitive --> f_adelic_lattice_proofs__with_zero_eq_of_le_exp_iff
  f_galois_places_transitive --> concept_galois_fixed_fields
  f_galois_places_transitive --> concept_group_actions
  f_galois_places_transitive --> concept_dedekind_domains
  f_galois_places_transitive --> number_fields
  f_hilbert90_s_units_kummer --> f_cyclic_kummer_norm_fixed_hilbert90
  f_hilbert90_s_units_kummer --> f_adelic_lattice_proofs__exists_superset_mem_s_units
  f_hilbert90_s_units_kummer --> f_exists_unit_valuation_eq_of_adm
  f_hilbert90_s_units_kummer --> f_galois_places_transitive
  f_hilbert90_s_units_kummer --> f_valuation_unramified_kummer_of_coprime_unit
  f_hilbert90_s_units_kummer --> f_adelic_lattice_proofs__kummer_galois
  f_hilbert90_s_units_kummer --> f_adelic_lattice_proofs__height_one_spectrum_places_over_finite_set
  f_hilbert90_s_units_kummer --> concept_roots_of_unity_kummer
  f_hilbert90_s_units_kummer --> concept_dedekind_domains
  f_valuation_unramified_kummer_of_coprime_unit --> f_galois_places_transitive
  f_valuation_unramified_kummer_of_coprime_unit --> f_adelic_lattice_proofs__kummer_galois
  f_valuation_unramified_kummer_of_coprime_unit --> f_adelic_lattice_proofs__height_one_spectrum_places_over_finite_set
  f_valuation_unramified_kummer_of_coprime_unit --> concept_roots_of_unity_kummer
  f_valuation_unramified_kummer_of_coprime_unit --> concept_ultrametric_norm
  f_valuation_unramified_kummer_of_coprime_unit --> concept_dedekind_domains
  f_valuation_unramified_kummer_of_coprime_unit --> concept_discrete_valuation_ring
  f_adelic_lattice_proofs__with_zero_eq_of_le_exp_iff --> f_adelic_hermitian_forms__sq_sub_le_norm_sub
  f_adelic_lattice_proofs__with_zero_eq_of_le_exp_iff --> concept_ultrametric_norm
  f_adelic_lattice_proofs__with_zero_eq_of_le_exp_iff --> concept_dedekind_domains
  f_adelic_lattice_proofs__with_zero_eq_of_le_exp_iff --> concept_prime_ideals_localization
  f_adelic_lattice_proofs__with_zero_eq_of_le_exp_iff --> number_fields
  f_compact_casimir_bound_projection_dual_tensor --> f_jet_harmonics__compact_casimir_le_tensor_operator_raise
  f_compact_casimir_bound_projection_dual_tensor --> f_jets__sum_io_pr
  f_compact_casimir_bound_projection_dual_tensor --> f_jet_harmonics__cas_k_is_symmetric_and_form
  f_compact_casimir_bound_projection_dual_tensor --> f_jet_harmonics__sum_norm_add_sq_le_of_bounds
  f_compact_casimir_bound_projection_dual_tensor --> concept_hermitian_unitary_matrices
  f_compact_casimir_bound_projection_dual_tensor --> linear_algebra
  f_p_poly_local_generators_diff --> f_statements_poly_local_generators
  f_p_poly_local_generators_diff --> concept_derivations_smoothness
  f_p_poly_local_generators_diff --> concept_local_rings
  f_p_poly_local_generators_diff --> concept_prime_ideals_localization
  f_p_poly_local_generators_diff --> linear_algebra
  f_p_poly_local_generators_diff --> polynomials
  f_arithmetic_bezout__statements --> concept_coordinate_rings_dimension
  f_arithmetic_bezout__statements --> concept_prime_ideals_localization
  f_arithmetic_bezout__statements --> concept_dedekind_domains
  f_arithmetic_bezout__statements --> number_fields
  f_arithmetic_bezout__statements --> polynomials
  f_arithmetic_bezout__statements --> concept_ultrametric_norm
  f_arithmetic_bezout__statements --> concept_haar_measure_fundamental_domain
  f_statements_poly_local_generators --> concept_coordinate_rings_dimension
  f_statements_poly_local_generators --> concept_derivations_smoothness
  f_statements_poly_local_generators --> concept_prime_ideals_localization
  f_statements_poly_local_generators --> polynomials
  f_p_jacobian_prime_derivations --> f_st_poly_derivations_detect_square
  f_p_jacobian_prime_derivations --> f_st_cotangent_basis_in_prime
  f_p_jacobian_prime_derivations --> f_st_derivation_minor_of_detection
  f_p_jacobian_prime_derivations --> f_st_local_generators_clear_denominators
  f_p_jacobian_prime_derivations --> f_complex_analytic_sets__st_jacobian_prime_derivations
  f_p_jacobian_prime_derivations --> concept_derivations_smoothness
  f_st_cotangent_basis_in_prime --> concept_local_rings
  f_st_cotangent_basis_in_prime --> concept_prime_ideals_localization
  f_st_cotangent_basis_in_prime --> concept_derivations_smoothness
  f_st_cotangent_basis_in_prime --> concept_noetherian_and_irreducible_components
  f_st_derivation_minor_of_detection --> concept_derivations_smoothness
  f_st_derivation_minor_of_detection --> concept_local_rings
  f_st_derivation_minor_of_detection --> concept_prime_ideals_localization
  f_st_derivation_minor_of_detection --> linear_algebra
  f_st_local_generators_clear_denominators --> concept_prime_ideals_localization
  f_st_local_generators_clear_denominators --> concept_local_rings
  f_st_local_generators_clear_denominators --> concept_noetherian_and_irreducible_components
  f_st_local_generators_clear_denominators --> concept_finitely_generated_algebras
  f_st_poly_derivations_detect_square --> concept_derivations_smoothness
  f_st_poly_derivations_detect_square --> concept_local_rings
  f_st_poly_derivations_detect_square --> concept_prime_ideals_localization
  f_st_poly_derivations_detect_square --> polynomials
  f_complex_analytic_sets__statements_area --> concept_complex_analytic_sets
  f_complex_analytic_sets__statements_area --> concept_coordinate_rings_dimension
  f_complex_analytic_sets__statements_area --> concept_lattice_point_counting
  f_complex_analytic_sets__statements_area --> linear_algebra
  f_complex_analytic_sets__statements_area --> complex_numbers
  f_complex_analytic_sets__statements_area --> real_analysis
  f_local_hermitian_forms__even_val --> f_symmetric_power_transfer__wcount
  f_local_hermitian_forms__even_val --> concept_hermitian_unitary_matrices
  f_local_hermitian_forms__even_val --> concept_group_actions
  f_local_hermitian_forms__even_val --> concept_discrete_valuation_ring
  f_local_hermitian_forms__even_val --> concept_adic_completion
  f_local_hermitian_forms__even_val --> concept_integral_closure_fraction_fields
  f_local_hermitian_forms__even_val --> concept_valuation_rings
  f_local_hermitian_forms__is_fix_map_iff --> f_local_hermitian_forms__even_val
  f_local_hermitian_forms__is_fix_map_iff --> concept_group_actions
  f_local_hermitian_forms__is_fix_map_iff --> concept_hermitian_unitary_matrices
  f_local_hermitian_forms__is_fix_map_iff --> linear_algebra
  f_local_hermitian_forms__lcount_norm --> f_local_hermitian_forms__even_val
  f_local_hermitian_forms__lcount_norm --> f_symmetric_power_transfer__wcount
  f_local_hermitian_forms__lcount_norm --> concept_discrete_valuation_ring
  f_local_hermitian_forms__lcount_norm --> concept_group_actions
  f_local_hermitian_forms__lcount_norm --> concept_hermitian_unitary_matrices
  f_local_orbit_counts__dat_smul --> f_local_hermitian_forms__even_val
  f_local_orbit_counts__dat_smul --> f_local_hermitian_forms__lcount_norm
  f_local_orbit_counts__dat_smul --> rings_fields
  f_local_orbit_counts__descent --> f_local_hermitian_forms__even_val
  f_local_orbit_counts__descent --> concept_integral_closure_fraction_fields
  f_local_orbit_counts__descent --> concept_discrete_valuation_ring
  f_local_orbit_counts__descent --> concept_adic_completion
  f_split_m --> f_split_unit_elements__split_s
  f_split_m --> f_local_orbit_counts__dat_smul
  f_split_m --> f_local_hermitian_forms__norm_one_is_coboundary_unramified_quadratic
  f_split_m --> f_local_hermitian_forms__even_val
  f_split_m --> concept_discrete_valuation_ring
  f_local_orbit_counts__w_trans --> f_symmetric_power_transfer__wcount
  f_local_orbit_counts__w_trans --> concept_group_actions
  f_local_orbit_counts__w_trans --> concept_normal_subgroups_quotients
  f_local_orbit_counts__w_trans --> counting
  f_local_hermitian_forms__norm_one_is_coboundary_unramified_quadratic --> f_local_hermitian_forms__even_val
  f_local_hermitian_forms__norm_one_is_coboundary_unramified_quadratic --> f_local_hermitian_forms__lcount_norm
  f_local_hermitian_forms__norm_one_is_coboundary_unramified_quadratic --> f_symmetric_power_transfer__wcount
  f_local_hermitian_forms__norm_one_is_coboundary_unramified_quadratic --> concept_hensel_lifting
  f_local_hermitian_forms__norm_one_is_coboundary_unramified_quadratic --> concept_discrete_valuation_ring
  f_local_hermitian_forms__norm_one_is_coboundary_unramified_quadratic --> concept_group_actions
  f_local_hermitian_forms__norm_one_is_coboundary_unramified_quadratic --> concept_roots_of_unity_kummer
  f_split_unit_elements__split_s --> f_local_orbit_counts__descent
  f_split_unit_elements__split_s --> f_local_hermitian_forms__even_val
  f_split_unit_elements__split_s --> concept_integral_closure_fraction_fields
  f_split_unit_elements__split_s --> concept_discrete_valuation_ring
  f_divisors__gal_map_mul --> concept_chain_complexes_homology
  f_divisors__gal_map_mul --> concept_schemes_basics
  f_divisors__gal_map_mul --> concept_etale_ring_maps
  f_divisors__gal_map_mul --> concept_group_representations
  f_divisors__gal_map_mul --> concept_galois_fixed_fields
  f_divisors__gal_map_mul --> concept_categorical_pullbacks
  f_divisors__gal_map_mul --> concept_roots_of_unity_kummer
  f_divisors__ind_et_of_forall_finset --> f_divisors__gal_map_mul
  f_divisors__ind_et_of_forall_finset --> f_moduli_proofs__is_ind_etale_of_forall_finset
  f_divisors__ind_et_of_forall_finset --> f_c_m_moduli__projective_space_over_spec
  f_divisors__ind_et_of_forall_finset --> concept_filtered_colimits
  f_divisors__ind_et_of_forall_finset --> concept_etale_ring_maps
  f_divisors__ind_et_of_forall_finset --> concept_chain_complexes_homology
  f_divisors__ind_et_of_forall_finset --> concept_tensor_product_of_algebras
  f_galois_geometry__is_matrix_form --> concept_group_representations
  f_galois_geometry__is_matrix_form --> concept_galois_fixed_fields
  f_galois_geometry__is_matrix_form --> concept_schemes_basics
  f_galois_geometry__is_matrix_form --> concept_categorical_pullbacks
  f_galois_geometry__is_matrix_form --> concept_chain_complexes_homology
  f_galois_geometry__is_matrix_form --> linear_algebra
  f_galois_geometry__is_strictly_semistable_alt --> f_galois_geometry__is_matrix_form
  f_galois_geometry__is_strictly_semistable_alt --> concept_roots_of_unity_kummer
  f_galois_geometry__is_strictly_semistable_alt --> concept_tensor_product_of_algebras
  f_galois_geometry__is_strictly_semistable_alt --> concept_etale_ring_maps
  f_galois_geometry__is_strictly_semistable_alt --> concept_smooth_morphisms
  f_galois_geometry__is_strictly_semistable_alt --> concept_valuation_rings
  f_divisor_proofs__preserves_filtered_colimits_add_comm_grp_iff_elements --> concept_filtered_colimits
  f_divisor_proofs__preserves_filtered_colimits_add_comm_grp_iff_elements --> groups
  f_divisor_proofs__preserves_filtered_colimits_add_comm_grp_iff_elements --> concept_chain_complexes_homology
  f_preserves_filtered_colimits_module_cat_iff_forget_iff_el --> f_divisor_proofs__preserves_filtered_colimits_add_comm_grp_iff_elements
  f_preserves_filtered_colimits_module_cat_iff_forget_iff_el --> concept_filtered_colimits
  f_preserves_filtered_colimits_module_cat_iff_forget_iff_el --> concept_flat_modules
  f_moduli_proofs__is_ind_etale_of_forall_finset --> f_c_m_moduli__projective_space_over_spec
  f_moduli_proofs__is_ind_etale_of_forall_finset --> concept_filtered_colimits
  f_moduli_proofs__is_ind_etale_of_forall_finset --> concept_etale_ring_maps
  f_moduli_proofs__is_ind_etale_of_forall_finset --> concept_finitely_generated_algebras
  f_divisor_proofs__comap_maximal_ideal_eq_origin --> f_divisor_proofs__origin_ideal
  f_divisor_proofs__comap_maximal_ideal_eq_origin --> f_divisor_proofs__is_z_mod_torsor_finite_projective_base_change
  f_divisor_proofs__comap_maximal_ideal_eq_origin --> f_divisor_proofs__torsors_trivial
  f_divisor_proofs__comap_maximal_ideal_eq_origin --> f_divisor_proofs__torsors_trivial_iff
  f_divisor_proofs__comap_maximal_ideal_eq_origin --> f_c_m_moduli__projective_space_over_spec
  f_divisor_proofs__comap_maximal_ideal_eq_origin --> concept_prime_ideals_localization
  f_divisor_proofs__comap_maximal_ideal_eq_origin --> concept_local_rings
  f_divisor_proofs__comap_maximal_ideal_eq_origin --> concept_tensor_product_of_algebras
  f_divisor_proofs__comap_maximal_ideal_eq_origin --> concept_hensel_lifting
  f_divisor_proofs__comap_maximal_ideal_eq_origin --> polynomials
  f_etale_at_prime_base_change_of_integral_closure_etale --> f_divisor_proofs__closure_finite_etale
  f_etale_at_prime_base_change_of_integral_closure_etale --> f_divisor_proofs__good_iff_etale_at
  f_etale_at_prime_base_change_of_integral_closure_etale --> concept_etale_ring_maps
  f_etale_at_prime_base_change_of_integral_closure_etale --> concept_tensor_product_of_algebras
  f_etale_at_prime_base_change_of_integral_closure_etale --> concept_prime_ideals_localization
  f_etale_at_prime_base_change_of_integral_closure_etale --> concept_integral_closure_fraction_fields
  f_divisor_proofs__is_z_mod_torsor_finite_projective_base_change --> f_divisor_proofs__torsors_trivial
  f_divisor_proofs__is_z_mod_torsor_finite_projective_base_change --> concept_tensor_product_of_algebras
  f_divisor_proofs__is_z_mod_torsor_finite_projective_base_change --> concept_projective_modules
  f_divisor_proofs__is_z_mod_torsor_finite_projective_base_change --> concept_group_actions
  f_divisor_proofs__is_z_mod_torsor_finite_projective_base_change --> concept_flat_modules
  f_orbital_bounds_conclusion__self_dual_loc --> f_period_integrals__self_dual_loc
  f_orbital_bounds_conclusion__self_dual_loc --> f_self_dual_loc_of_loc_basis
  f_orbital_bounds_conclusion__self_dual_loc --> f_self_dual_local_basis__loc_basis
  f_period_integrals__self_dual_loc --> number_fields
  f_period_integrals__self_dual_loc --> p_adic_numbers
  f_period_integrals__self_dual_loc --> concept_tensor_product_of_algebras
  f_period_integrals__self_dual_loc --> concept_dedekind_domains
  f_period_integrals__self_dual_loc --> concept_adic_completion
  f_period_integrals__self_dual_loc --> linear_algebra
  f_self_dual_local_basis__assembly --> f_period_integrals__self_dual_loc
  f_self_dual_local_basis__assembly --> f_dual_basis
  f_self_dual_local_basis__assembly --> f_self_dual_loc_of_dirs
  f_self_dual_local_basis__assembly --> f_one_tmul_mem_oloc
  f_self_dual_local_basis__assembly --> linear_algebra
  f_self_dual_local_basis__assembly --> concept_dedekind_domains
  f_dual_basis --> f_period_integrals__self_dual_loc
  f_dual_basis --> linear_algebra
  f_dual_basis --> concept_tensor_product_of_algebras
  f_dual_basis --> concept_adic_completion
  f_hform_sum_right --> f_period_integrals__self_dual_loc
  f_hform_sum_right --> linear_algebra
  f_hform_sum_right --> rings_fields
  f_hvec_apply --> f_dual_basis
  f_hvec_apply --> f_hform_sum_right
  f_hvec_apply --> linear_algebra
  f_self_dual_local_basis__loc_basis --> f_pad_fam
  f_self_dual_local_basis__loc_basis --> f_dual_basis
  f_self_dual_local_basis__loc_basis --> concept_dedekind_domains
  f_self_dual_local_basis__loc_basis --> concept_prime_ideals_localization
  f_self_dual_local_basis__loc_basis --> linear_algebra
  f_self_dual_local_basis__nondeg --> f_dual_basis
  f_self_dual_local_basis__nondeg --> f_period_integrals__self_dual_loc
  f_self_dual_local_basis__nondeg --> number_fields
  f_self_dual_local_basis__nondeg --> concept_integral_closure_fraction_fields
  f_one_tmul_mem_oloc --> f_dual_basis
  f_one_tmul_mem_oloc --> f_period_integrals__self_dual_loc
  f_one_tmul_mem_oloc --> concept_adic_completion
  f_one_tmul_mem_oloc --> concept_valuation_rings
  f_one_tmul_mem_oloc --> concept_tensor_product_of_algebras
  f_self_dual_loc_of_dirs --> f_dual_basis
  f_self_dual_loc_of_dirs --> f_period_integrals__self_dual_loc
  f_self_dual_loc_of_dirs --> proofs
  f_self_dual_loc_of_loc_basis --> f_self_dual_local_basis__assembly
  f_self_dual_loc_of_loc_basis --> f_self_dual_local_basis__nondeg
  f_self_dual_loc_of_loc_basis --> f_one_tmul_mem_oloc
  f_self_dual_loc_of_loc_basis --> f_hvec_apply
  f_self_dual_loc_of_loc_basis --> f_dual_basis
  f_pad_fam --> f_dual_basis
  f_pad_fam --> concept_dedekind_domains
  f_pad_fam --> concept_prime_ideals_localization
  f_pad_fam --> linear_algebra
  f_pad_fam --> number_fields
  f_alternating_coefficient_formula --> f_foundations__alt_coeff_rho
  f_alternating_coefficient_formula --> polynomials
  f_alternating_coefficient_formula --> concept_symmetric_polynomials
  f_alternating_coefficient_formula --> concept_exterior_powers
  f_alternating_coefficient_formula --> calculus
  f_alternating_coefficient_formula --> counting
  f_hook_functional_power_sum --> f_foundations__alt_coeff_rho
  f_hook_functional_power_sum --> f_degree_formula__flag_deg_formula
  f_hook_functional_power_sum --> concept_symmetric_polynomials
  f_hook_functional_power_sum --> polynomials
  f_hook_functional_power_sum --> counting
  f_hook_functional_power_sum_other --> f_foundations__alt_coeff_rho
  f_hook_functional_power_sum_other --> concept_symmetric_polynomials
  f_hook_functional_power_sum_other --> polynomials
  f_hook_functional_power_sum_other --> counting
  f_kappa_formula_hook_schur --> f_alternating_coefficient_formula
  f_kappa_formula_hook_schur --> f_hook_functional_power_sum
  f_kappa_formula_hook_schur --> f_hook_functional_power_sum_other
  f_kappa_formula_hook_schur --> f_divisor_proofs__flag_degree_vandermonde
  f_kappa_formula_hook_schur --> f_degree_formula__flag_deg_formula
  f_kappa_formula_hook_schur --> f_foundations__alt_coeff_rho
  f_kappa_formula_hook_schur --> concept_symmetric_polynomials
  f_kappa_formula_hook_schur --> polynomials
  f_uniform_theta_substitution__odd_log_relation --> infinite_series
  f_uniform_theta_substitution__odd_log_relation --> polynomials
  f_uniform_theta_substitution__odd_log_relation --> concept_ultrametric_norm
  f_uniform_theta_substitution__odd_log_relation --> p_adic_numbers
  f_uniform_theta_substitution__odd_log_relation --> f_gauss_jet_bounds__statement
  f_uniform_theta_substitution__odd_log_relation --> concept_frobenius_perfect_rings
  f_uniform_theta_substitution__cyclic_power_class_of_exp_equiv --> f_uniform_theta_substitution__odd_log_relation
  f_uniform_theta_substitution__cyclic_power_class_of_exp_equiv --> f_gauss_jet_bounds__statement
  f_uniform_theta_substitution__cyclic_power_class_of_exp_equiv --> concept_ultrametric_norm
  f_uniform_theta_substitution__cyclic_power_class_of_exp_equiv --> p_adic_numbers
  f_uniform_theta_substitution__cyclic_power_class_of_exp_equiv --> concept_newton_polygon
  f_uniform_theta_substitution__cyclic_power_class_of_exp_equiv --> infinite_series
  f_uniform_theta_substitution__statement_m --> f_uniform_theta_substitution__cyclic_power_class_of_exp_equiv
  f_uniform_theta_substitution__statement_m --> f_uniform_theta_substitution__odd_log_relation
  f_uniform_theta_substitution__statement_m --> f_gauss_jet_bounds__statement_i
  f_uniform_theta_substitution__statement_m --> f_gauss_jet_bounds__statement
  f_uniform_theta_substitution__statement_m --> concept_ultrametric_norm
  f_places_add_class --> f_uniform_theta_substitution__statement_m
  f_places_add_class --> f_uniform_theta_substitution__odd_log_relation
  f_places_add_class --> f_gauss_jet_bounds__statement_i
  f_places_add_class --> concept_ultrametric_norm
  f_tensor_relations_g_l__k_type_data --> f_real_place_analysis__statement_a
  f_tensor_relations_g_l__k_type_data --> f_real_place_analysis__statement_e
  f_tensor_relations_g_l__k_type_data --> concept_group_representations
  f_tensor_relations_g_l__k_type_data --> concept_group_actions
  f_tensor_relations_g_l__k_type_data --> concept_hermitian_unitary_matrices
  f_tensor_relations_g_l__k_type_data --> linear_algebra
  f_tensor_relations_g_l__step_formula --> f_tensor_relations_g_l__k_type_data
  f_tensor_relations_g_l__step_formula --> f_real_place_analysis__statement_a
  f_tensor_relations_g_l__step_formula --> f_real_place_analysis__statement_b
  f_tensor_relations_g_l__step_formula --> f_real_place_analysis__statement_e
  f_tensor_relations_g_l__step_formula --> concept_group_representations
  f_tensor_relations_g_l__step_formula --> concept_semisimple_algebras_radical
  f_tensor_relations_g_l__step_formula --> linear_algebra
  f_casimir_bounds__expand --> f_tensor_relations_g_l__k_type_data
  f_casimir_bounds__expand --> f_real_place_analysis__statement_a
  f_casimir_bounds__expand --> linear_algebra
  f_casimir_bounds__expand --> counting
  f_re_swap_sum_le --> f_tensor_relations_g_l__k_type_data
  f_re_swap_sum_le --> linear_algebra
  f_re_swap_sum_le --> concept_hermitian_unitary_matrices
  f_re_swap_sum_le --> complex_numbers
  f_count_same --> f_tensor_relations_g_l__k_type_data
  f_count_same --> counting
  f_count_cross --> f_count_same
  f_count_cross --> f_tensor_relations_g_l__k_type_data
  f_count_cross --> counting
  f_cas_bound_holds --> f_tensor_relations_g_l__step_formula
  f_cas_bound_holds --> f_casimir_bounds__expand
  f_cas_bound_holds --> f_count_cross
  f_cas_bound_holds --> f_re_swap_sum_le
  f_cas_bound_holds --> f_tensor_relations_g_l__k_type_data
  f_cas_bound_holds --> f_real_place_analysis__statement_a
  f_unramified_integrals__mod_defs --> concept_modular_forms
  f_unramified_integrals__mod_defs --> concept_lattices_in_the_plane
  f_unramified_integrals__mod_defs --> infinite_series
  f_unramified_integrals__mod_defs --> concept_roots_of_unity_kummer
  f_unramified_integrals__mod_basic --> f_unramified_integrals__mod_defs
  f_unramified_integrals__mod_basic --> concept_modular_forms
  f_unramified_integrals__mod_basic --> concept_roots_of_unity_kummer
  f_unramified_integrals__mod_basic --> complex_analysis
  f_unramified_integrals__mod_delta_int --> f_unramified_integrals__mod_defs
  f_unramified_integrals__mod_delta_int --> f_unramified_integrals__mod_eis_int
  f_unramified_integrals__mod_delta_int --> modular_arithmetic
  f_unramified_integrals__mod_delta_int --> concept_modular_forms
  f_unramified_integrals__mod_delta_int --> polynomials
  f_unramified_integrals__mod_eis_int --> f_unramified_integrals__mod_defs
  f_unramified_integrals__mod_eis_int --> concept_modular_forms
  f_unramified_integrals__mod_eis_int --> zeta_series
  f_unramified_integrals__mod_eis_int --> infinite_series
  f_unramified_integrals__mod_eis_int --> complex_analysis
  f_unramified_integrals__mod_g_eis --> f_unramified_integrals__mod_defs
  f_unramified_integrals__mod_g_eis --> concept_lattices_in_the_plane
  f_unramified_integrals__mod_g_eis --> concept_modular_forms
  f_unramified_integrals__mod_g_eis --> zeta_series
  f_unramified_integrals__mod_g_eis --> infinite_series
  f_unramified_integrals__mod_j_tau --> f_unramified_integrals__mod_g_eis
  f_unramified_integrals__mod_j_tau --> f_unramified_integrals__mod_basic
  f_unramified_integrals__mod_j_tau --> f_c_m_good_models__statement
  f_unramified_integrals__mod_j_tau --> concept_lattices_in_the_plane
  f_unramified_integrals__mod_j_tau --> concept_modular_forms
  f_unramified_integrals__mod_q_prin --> f_unramified_integrals__mod_basic
  f_unramified_integrals__mod_q_prin --> f_unramified_integrals__mod_delta_int
  f_unramified_integrals__mod_q_prin --> f_unramified_integrals__mod_eis_int
  f_unramified_integrals__mod_q_prin --> f_unramified_integrals__mod_defs
  f_unramified_integrals__mod_q_prin --> concept_modular_forms
  f_unramified_integrals__mod_q_prin --> polynomials
  f_unramified_integrals__mod_q_prin --> infinite_series
  f_c_m_good_models__statement --> concept_lattices_in_the_plane
  f_c_m_good_models__statement --> p_adic_numbers
  f_c_m_good_models__statement --> concept_ultrametric_norm
  f_c_m_good_models__statement --> concept_hensel_lifting
  f_c_m_good_models__statement --> concept_field_extensions_transcendence
  f_c_m_good_models__statement --> number_fields
  f_is_fam_const_level_one --> f_unramified_integrals__mod_basic
  f_is_fam_const_level_one --> f_unramified_integrals__mod_defs
  f_is_fam_const_level_one --> f_divisors__has_q_iff
  f_is_fam_const_level_one --> concept_modular_forms
  f_k_h_free_indep_st --> f_kleiman_ampleness__k_h_free_obj
  f_k_h_free_indep_st --> polynomials
  f_k_h_free_indep_st --> rings_fields
  f_k_h_free_indep_st --> linear_algebra
  f_p_k_h_free_indep --> f_k_h_free_indep_st
  f_p_k_h_free_indep --> f_kleiman_ampleness__k_h_free_obj
  f_p_k_h_free_indep --> concept_prime_ideals_localization
  f_p_k_h_free_indep --> polynomials
  f_p_k_h_free_indep --> rings_fields
  f_regular_local_ring_fraction_field --> f_global_geometry__is_cpt_gen
  f_regular_local_ring_fraction_field --> f_geometry_proofs__spec_stalk_specializes_comp
  f_regular_local_ring_fraction_field --> concept_schemes_basics
  f_regular_local_ring_fraction_field --> concept_local_rings
  f_regular_local_ring_fraction_field --> concept_integral_closure_fraction_fields
  f_regular_local_ring_fraction_field --> concept_prime_ideals_localization
  f_geometry_proofs__spec_stalk_specializes_comp --> f_global_geometry__is_cpt_gen
  f_geometry_proofs__spec_stalk_specializes_comp --> f_global_geometry__lie_model
  f_geometry_proofs__spec_stalk_specializes_comp --> concept_schemes_basics
  f_geometry_proofs__spec_stalk_specializes_comp --> concept_local_rings
  f_geometry_proofs__spec_stalk_specializes_comp --> concept_categorical_pullbacks
  f_rep_g_apply --> concept_group_representations
  f_rep_g_apply --> linear_algebra
  f_rep_g_apply --> polynomials
  f_rep_g_apply --> groups
  f_th_facts --> f_rep_g_apply
  f_th_facts --> concept_symmetric_polynomials
  f_th_facts --> concept_group_representations
  f_th_facts --> linear_algebra
  f_coeff_scale --> f_th_facts
  f_coeff_scale --> f_rep_g_apply
  f_coeff_scale --> polynomials
  f_coeff_scale --> counting
  f_fin_m_h --> f_th_facts
  f_fin_m_h --> f_coeff_scale
  f_fin_m_h --> f_rep_g_apply
  f_fin_m_h --> linear_algebra
  f_fin_m_h --> polynomials
  f_mem_homogeneous_exponents_one_block --> f_rep_g_apply
  f_mem_homogeneous_exponents_one_block --> f_th_facts
  f_mem_homogeneous_exponents_one_block --> f_coeff_scale
  f_mem_homogeneous_exponents_one_block --> f_fin_m_h
  f_mem_homogeneous_exponents_one_block --> linear_algebra
  f_mem_homogeneous_exponents_one_block --> polynomials
  f_mem_homogeneous_exponents_one_block --> counting
  f_h_option --> f_th_facts
  f_h_option --> f_rep_g_apply
  f_h_option --> concept_symmetric_polynomials
  f_h_option --> polynomials
  f_h_option --> counting
  f_hq_three --> f_h_option
  f_hq_three --> f_th_facts
  f_hq_three --> f_rep_g_apply
  f_hq_three --> concept_symmetric_polynomials
  f_homogeneous_trace_diagonal --> f_mem_homogeneous_exponents_one_block
  f_homogeneous_trace_diagonal --> f_fin_m_h
  f_homogeneous_trace_diagonal --> f_th_facts
  f_homogeneous_trace_diagonal --> f_rep_g_apply
  f_homogeneous_trace_diagonal --> concept_symmetric_polynomials
  f_homogeneous_trace_diagonal --> linear_algebra
  f_homogeneous_trace_diagonal --> polynomials
  f_homogeneous_trace_diagonal --> complex_numbers
  f_tr_swap --> f_mem_homogeneous_exponents_one_block
  f_tr_swap --> f_th_facts
  f_tr_swap --> f_rep_g_apply
  f_tr_swap --> f_coeff_scale
  f_tr_swap --> linear_algebra
  f_tr_swap --> polynomials
  f_twine_c --> f_tr_swap
  f_twine_c --> f_hq_three
  f_twine_c --> f_homogeneous_trace_diagonal
  f_twine_c --> f_fin_m_h
  f_twine_c --> f_th_facts
  f_twine_c --> f_rep_g_apply
  f_twine_c --> concept_symmetric_polynomials
  f_twine_c --> algebraic_closure
  f_twine_c --> linear_algebra
  f_eps_of_c_zero --> f_twisted_trace_formula__inverse_chamber_map
  f_eps_of_c_zero --> complex_numbers
  f_eps_of_c_zero --> linear_algebra
  f_eps_of_c_zero --> real_analysis
  f_gamma_function_bounded_support --> f_twisted_trace_formula__inverse_chamber_map
  f_gamma_function_bounded_support --> linear_algebra
  f_gamma_function_bounded_support --> real_analysis
  f_gamma_function_bounded_support --> counting
  f_exponential_gamma_integral_formula --> f_eps_of_c_zero
  f_exponential_gamma_integral_formula --> f_twisted_trace_formula__inverse_chamber_map
  f_exponential_gamma_integral_formula --> concept_haar_measure_fundamental_domain
  f_exponential_gamma_integral_formula --> linear_algebra
  f_exponential_gamma_integral_formula --> calculus
  f_exponential_gamma_integral_formula --> real_analysis
  f_exponential_gamma_integral_formula --> complex_numbers
  f_gamma_integral_alternating_sum --> f_gamma_function_bounded_support
  f_gamma_integral_alternating_sum --> f_exponential_gamma_integral_formula
  f_gamma_integral_alternating_sum --> f_eps_of_c_zero
  f_gamma_integral_alternating_sum --> f_twisted_trace_formula__inverse_chamber_map
  f_gamma_integral_alternating_sum --> calculus
  f_gamma_integral_alternating_sum --> real_analysis
  f_gamma_integral_alternating_sum --> complex_analysis
  f_epsilon_alternating_sum_zero --> f_gamma_integral_alternating_sum
  f_epsilon_alternating_sum_zero --> f_gamma_function_bounded_support
  f_epsilon_alternating_sum_zero --> f_twisted_trace_formula__inverse_chamber_map
  f_epsilon_alternating_sum_zero --> real_analysis
  f_epsilon_alternating_sum_zero --> linear_algebra
  f_gauss_jet_bounds__statement_y --> f_gauss_jet_bounds__statement_n
  f_gauss_jet_bounds__statement_y --> f_gauss_jet_bounds__statement_h
  f_gauss_jet_bounds__statement_y --> f_gauss_jet_bounds__statement
  f_gauss_jet_bounds__statement_y --> concept_ultrametric_norm
  f_gauss_jet_bounds__statement_y --> p_adic_numbers
  f_gauss_jet_bounds__statement_y --> polynomials
  f_cube_map_triple_product_unique --> f_cubical_structures__cube_symmetric_swap_first
  f_cube_map_triple_product_unique --> f_cubical_structures__cubical_pull_base_change_st
  f_cube_map_triple_product_unique --> f_toroidal_compactification__two_weight_eq_one_add_root
  f_cube_map_triple_product_unique --> f_abelian_scheme_quotients__is_abelian_scheme
  f_cube_map_triple_product_unique --> concept_group_schemes
  f_cube_map_triple_product_unique --> concept_categorical_pullbacks
  f_cube_map_triple_product_unique --> number_fields
  f_cube_map_triple_product_unique --> complex_numbers
  f_p_eq_q_of_neg --> linear_algebra
  f_p_eq_q_of_neg --> real_analysis
  f_discrete_valuation_numbers__objects --> polynomials
  f_discrete_valuation_numbers__objects --> concept_discrete_valuation_ring
  f_discrete_valuation_numbers__objects --> concept_prime_ideals_localization
  f_discrete_valuation_numbers__objects --> concept_coordinate_rings_dimension
  f_discrete_valuation_numbers__objects --> concept_ample_nef_line_bundles
  f_discrete_valuation_numbers__objects --> concept_local_rings
  f_discrete_valuation_numbers__objects --> concept_integral_closure_fraction_fields
  f_statements_clopen_components --> f_birational_geometry__inter_st
  f_statements_clopen_components --> f_discrete_valuation_numbers__objects
  f_statements_clopen_components --> concept_point_set_topology
  f_statements_clopen_components --> concept_noetherian_and_irreducible_components
  f_statements_clopen_components --> concept_complex_analytic_sets
  f_statements_clopen_components --> complex_numbers
  f_statements_component_degree --> f_birational_geometry__inter_st
  f_statements_component_degree --> f_birational_geometry__is_intersection_family
  f_statements_component_degree --> f_birational_geometry__is_semipositive_on
  f_statements_component_degree --> f_discrete_valuation_numbers__objects
  f_statements_component_degree --> concept_ample_nef_line_bundles
  f_statements_component_degree --> concept_noetherian_and_irreducible_components
  f_statements_components_additive --> f_birational_geometry__inter_st
  f_statements_components_additive --> f_birational_geometry__is_intersection_family
  f_statements_components_additive --> f_discrete_valuation_numbers__objects
  f_statements_components_additive --> concept_noetherian_and_irreducible_components
  f_statements_components_additive --> concept_haar_measure_fundamental_domain
  f_statements_int_num_components --> f_birational_geometry__inter_st
  f_statements_int_num_components --> f_discrete_valuation_numbers__objects
  f_statements_int_num_components --> concept_prime_ideals_localization
  f_statements_int_num_components --> concept_noetherian_and_irreducible_components
  f_statements_clopen_degree --> f_birational_geometry__inter_st
  f_statements_clopen_degree --> f_birational_geometry__is_intersection_family
  f_statements_clopen_degree --> f_birational_geometry__is_semipositive_on
  f_statements_clopen_degree --> f_discrete_valuation_numbers__objects
  f_statements_clopen_degree --> concept_point_set_topology
  f_statements_clopen_degree --> concept_ample_nef_line_bundles
  f_p_clopen_degree --> f_statements_clopen_components
  f_p_clopen_degree --> f_statements_component_degree
  f_p_clopen_degree --> f_statements_components_additive
  f_p_clopen_degree --> f_statements_int_num_components
  f_p_clopen_degree --> f_statements_clopen_degree
  f_p_clopen_degree --> proofs
  f_intersections__statements --> f_birational_geometry__inter_st
  f_intersections__statements --> f_discrete_valuation_numbers__objects
  f_intersections__statements --> f_birational_geometry__is_intersection_family
  f_intersections__statements --> f_birational_geometry__is_semipositive_on
  f_intersections__statements --> concept_coordinate_rings_dimension
  f_intersections__statements --> calculus
  f_birational_geometry__inter_st --> f_birational_geometry__is_intersection_family
  f_birational_geometry__inter_st --> f_birational_geometry__is_semipositive_on
  f_birational_geometry__inter_st --> concept_ample_nef_line_bundles
  f_birational_geometry__inter_st --> concept_haar_measure_fundamental_domain
  f_birational_geometry__inter_st --> concept_derivations_smoothness
  f_adelic_euler_products__count_data --> number_fields
  f_adelic_euler_products__count_data --> p_adic_numbers
  f_adelic_euler_products__count_data --> fourier_analysis
  f_adelic_euler_products__count_data --> concept_modular_forms
  f_adelic_euler_products__count_data --> concept_lattice_point_counting
  f_adelic_euler_products__count_data --> concept_haar_measure_fundamental_domain
  f_adelic_euler_products__count_data --> concept_ideals_and_discriminant
  f_adelic_euler_products__count_data --> concept_schwartz_functions
  f_cusp_representatives_finite --> number_fields
  f_cusp_representatives_finite --> concept_ideals_and_discriminant
  f_cusp_representatives_finite --> concept_dedekind_domains
  f_cusp_representatives_finite --> concept_integral_closure_fraction_fields
  f_cusp_representatives_finite --> concept_modular_forms
  f_cusp_representatives_finite --> linear_algebra
  f_exists_cusp_reduction_bound --> number_fields
  f_exists_cusp_reduction_bound --> concept_lattice_point_counting
  f_exists_cusp_reduction_bound --> concept_haar_measure_fundamental_domain
  f_exists_cusp_reduction_bound --> concept_lattices_in_the_plane
  f_exists_cusp_reduction_bound --> concept_modular_forms
  f_exists_cusp_reduction_bound --> linear_algebra
  f_exists_cusp_reduction_bound --> complex_numbers
  f_mobius_action_upper_half_plane --> f_adelic_euler_products__count_data
  f_mobius_action_upper_half_plane --> complex_numbers
  f_mobius_action_upper_half_plane --> concept_modular_forms
  f_mobius_action_upper_half_plane --> concept_group_actions
  f_mobius_action_upper_half_plane --> number_fields
  f_unit_balancing_imaginary_parts --> number_fields
  f_unit_balancing_imaginary_parts --> concept_lattice_point_counting
  f_unit_balancing_imaginary_parts --> concept_finitely_generated_abelian_groups
  f_unit_balancing_imaginary_parts --> concept_ideals_and_discriminant
  f_unit_balancing_imaginary_parts --> real_analysis
  f_reduction_to_siegel_domain --> f_exists_cusp_reduction_bound
  f_reduction_to_siegel_domain --> f_cusp_representatives_finite
  f_reduction_to_siegel_domain --> f_unit_balancing_imaginary_parts
  f_reduction_to_siegel_domain --> f_mobius_action_upper_half_plane
  f_reduction_to_siegel_domain --> f_adelic_euler_products__count_data
  f_reduction_to_siegel_domain --> number_fields
  f_reduction_to_siegel_domain --> concept_modular_forms
  f_fock_resolution_onto__statement_d --> f_fock_resolution_onto__statement_c
  f_fock_resolution_onto__statement_d --> f_fock_resolution_onto__shift_last_letter_thresholds
  f_fock_resolution_onto__statement_d --> f_mahler_measure__good_count
  f_fock_resolution_onto__statement_d --> f_mahler_measure__is_frozen_inv
  f_fock_resolution_onto__statement_d --> p_adic_numbers
  f_fock_resolution_onto__statement_d --> polynomials
  f_fock_resolution_onto__statement_d --> concept_derivations_smoothness
  f_fock_resolution_onto__statement_d --> concept_group_representations
  f_fock_resolution_onto__statement_d --> linear_algebra
  f_e_arith --> f_fock_resolution_onto__statement_d
  f_e_arith --> proofs
  f_e_arith --> infinite_series
  f_bijective_linear_combination_of_rank_at_stalk --> concept_flat_modules
  f_bijective_linear_combination_of_rank_at_stalk --> concept_local_rings
  f_bijective_linear_combination_of_rank_at_stalk --> concept_prime_ideals_localization
  f_bijective_linear_combination_of_rank_at_stalk --> linear_algebra
  f_exists_open_affine_hilbert_chart_basic_locus --> f_bijective_linear_combination_of_rank_at_stalk
  f_exists_open_affine_hilbert_chart_basic_locus --> f_free_module_complement_support_compact
  f_exists_open_affine_hilbert_chart_basic_locus --> f_is_pullback_pb_map
  f_exists_open_affine_hilbert_chart_basic_locus --> f_mem_support_quotient_span_iff_of_is_pushout
  f_exists_open_affine_hilbert_chart_basic_locus --> f_sections_finite_flat_rank_of_finite_flat
  f_exists_open_affine_hilbert_chart_basic_locus --> concept_schemes_basics
  f_exists_open_affine_hilbert_chart_basic_locus --> concept_categorical_pullbacks
  f_exists_open_affine_hilbert_chart_basic_locus --> concept_point_set_topology
  f_free_module_complement_support_compact --> f_support_of_quotient_flat_module
  f_free_module_complement_support_compact --> concept_flat_modules
  f_free_module_complement_support_compact --> concept_point_set_topology
  f_is_pullback_pb_map --> concept_categorical_pullbacks
  f_is_pullback_pb_map --> concept_schemes_basics
  f_is_pullback_pb_map --> f_divisor_proofs__comap_bc_comp
  f_mem_support_quotient_iff --> concept_flat_modules
  f_mem_support_quotient_iff --> concept_tensor_product_of_algebras
  f_mem_support_quotient_iff --> concept_prime_ideals_localization
  f_mem_support_quotient_span_iff_of_is_pushout --> f_mem_support_quotient_iff
  f_mem_support_quotient_span_iff_of_is_pushout --> concept_tensor_product_of_algebras
  f_mem_support_quotient_span_iff_of_is_pushout --> concept_categorical_pullbacks
  f_sections_finite_flat_rank_of_finite_flat --> concept_schemes_basics
  f_sections_finite_flat_rank_of_finite_flat --> concept_flat_modules
  f_sections_finite_flat_rank_of_finite_flat --> concept_categorical_pullbacks
  f_support_of_quotient_flat_module --> concept_flat_modules
  f_support_of_quotient_flat_module --> concept_local_rings
  f_support_of_quotient_flat_module --> concept_prime_ideals_localization
  f_support_of_quotient_flat_module --> concept_point_set_topology
  f_support_of_quotient_flat_module --> linear_algebra
  f_tangent_vector_of_dual_hom --> f_global_geometry__is_cochar_lie
  f_tangent_vector_of_dual_hom --> concept_dual_numbers
  f_tangent_vector_of_dual_hom --> concept_schemes_basics
  f_tangent_vector_of_dual_hom --> concept_group_schemes
  f_continuous_on_cos_sq --> concept_hermitian_unitary_matrices
  f_continuous_on_cos_sq --> real_analysis
  f_continuous_on_cos_sq --> trigonometry
  f_cosine_square_pushforward_uniform --> f_divisor_proofs__stereographic_measure_change
  f_cosine_square_pushforward_uniform --> f_divisor_proofs__mobius_change_of_variables
  f_cosine_square_pushforward_uniform --> f_divisor_proofs__fs_one
  f_cosine_square_pushforward_uniform --> f_continuous_on_cos_sq
  f_cosine_square_pushforward_uniform --> complex_analysis
  f_cosine_square_pushforward_uniform --> real_analysis
  f_local_density_bound_near_point --> f_cosine_square_pushforward_uniform
  f_local_density_bound_near_point --> f_continuous_on_cos_sq
  f_local_density_bound_near_point --> f_divisor_proofs__fs_one
  f_local_density_bound_near_point --> f_l2_dbar_estimates__is_local_homeomorph
  f_local_density_bound_near_point --> concept_haar_measure_fundamental_domain
  f_local_density_bound_near_point --> real_analysis
  f_foundations__exp_upper --> concept_modular_forms
  f_foundations__exp_upper --> complex_analysis
  f_foundations__exp_upper --> rings_fields
  f_foundations__exp_upper --> linear_algebra
  f_foundations__letter --> f_foundations__exp_upper
  f_foundations__letter --> concept_hecke_operators
  f_foundations__letter --> concept_adic_completion
  f_foundations__letter --> p_adic_numbers
  f_foundations__letter --> concept_modular_forms
  f_foundations__op_l_d_one_sub_mem_triv --> f_foundations__letter
  f_foundations__op_l_d_one_sub_mem_triv --> f_foundations__exp_upper
  f_foundations__op_l_d_one_sub_mem_triv --> concept_hecke_operators
  f_foundations__op_l_d_one_sub_mem_triv --> polynomials
  f_foundations__op_l_d_one_sub_mem_triv --> modular_arithmetic
  f_foundations__is_root_one --> f_foundations__op_l_d_one_sub_mem_triv
  f_foundations__is_root_one --> f_foundations__letter
  f_foundations__is_root_one --> f_foundations__exp_upper
  f_foundations__is_root_one --> concept_roots_of_unity_kummer
  f_foundations__is_root_one --> concept_adic_completion
  f_foundations__is_root_one --> concept_group_homology
  f_foundations__eigen_of_two_step --> f_foundations__op_l_d_one_sub_mem_triv
  f_foundations__eigen_of_two_step --> f_foundations__letter
  f_foundations__eigen_of_two_step --> f_foundations__exp_upper
  f_foundations__eigen_of_two_step --> linear_algebra
  f_foundations__eigen_of_two_step --> concept_hecke_operators
  f_foundation_proofs__gl_two_pos_rat_mobius_basic_laws --> f_foundations__exp_upper
  f_foundation_proofs__gl_two_pos_rat_mobius_basic_laws --> complex_numbers
  f_foundation_proofs__gl_two_pos_rat_mobius_basic_laws --> complex_analysis
  f_foundation_proofs__gl_two_pos_rat_mobius_basic_laws --> linear_algebra
  f_kummer_class_eval_eq_zero_of_vanishing_on_congruence --> f_foundations__is_root_one
  f_kummer_class_eval_eq_zero_of_vanishing_on_congruence --> f_foundations__letter
  f_kummer_class_eval_eq_zero_of_vanishing_on_congruence --> f_foundations__exp_upper
  f_kummer_class_eval_eq_zero_of_vanishing_on_congruence --> concept_roots_of_unity_kummer
  f_kummer_class_eval_eq_zero_of_vanishing_on_congruence --> concept_adic_completion
  f_kummer_class_eval_eq_zero_of_vanishing_on_congruence --> complex_analysis
  f_kummer_potential_relation_trivial_eq_zero --> f_kummer_class_eval_eq_zero_of_vanishing_on_congruence
  f_kummer_potential_relation_trivial_eq_zero --> f_foundation_proofs__gl_two_pos_rat_mobius_basic_laws
  f_kummer_potential_relation_trivial_eq_zero --> f_foundations__is_root_one
  f_kummer_potential_relation_trivial_eq_zero --> f_foundations__op_l_d_one_sub_mem_triv
  f_kummer_potential_relation_trivial_eq_zero --> concept_adic_completion
  f_kummer_potential_relation_trivial_eq_zero --> p_adic_numbers
  f_map_eisenstein_div_period --> concept_lattices_in_the_plane
  f_map_eisenstein_div_period --> concept_modular_forms
  f_map_eisenstein_div_period --> complex_numbers
  f_map_eisenstein_div_period --> f_divisors__has_q_iff
  f_harish_chandra_induction_g_l_trivial_orthogonal_hyperpl --> f_character_theory__character_coset_sum_eq_zero_of_subgroup_sum
  f_harish_chandra_induction_g_l_trivial_orthogonal_hyperpl --> f_character_theory__virtual_characters_mul_comap_conj_ind_linear
  f_harish_chandra_induction_g_l_trivial_orthogonal_hyperpl --> f_is_character_over_subfield_of_representation
  f_harish_chandra_induction_g_l_trivial_orthogonal_hyperpl --> concept_group_representations
  f_harish_chandra_induction_g_l_trivial_orthogonal_hyperpl --> concept_normal_subgroups_quotients
  f_harish_chandra_induction_g_l_trivial_orthogonal_hyperpl --> linear_algebra
  f_gauss_jet_bounds__statement_s --> f_gauss_jet_bounds__statement
  f_gauss_jet_bounds__statement_s --> f_gauss_jet_bounds__statement_p
  f_gauss_jet_bounds__statement_s --> f_gauss_jet_bounds__statement_h
  f_gauss_jet_bounds__statement_s --> f_incoming_bounds__incoming_bound
  f_gauss_jet_bounds__statement_s --> concept_ultrametric_norm
  f_gauss_jet_bounds__statement_s --> p_adic_numbers
  f_gauss_jet_bounds__statement_s --> polynomials
  f_gauss_jet_bounds__statement_v --> f_gauss_jet_bounds__statement_s
  f_gauss_jet_bounds__statement_v --> f_gauss_jet_bounds__statement
  f_gauss_jet_bounds__statement_v --> f_gauss_jet_bounds__statement_i
  f_gauss_jet_bounds__statement_v --> concept_ultrametric_norm
  f_gauss_jet_bounds__statement_v --> p_adic_numbers
  f_gauss_jet_bounds__statement_x --> f_gauss_jet_bounds__statement_v
  f_gauss_jet_bounds__statement_x --> f_gauss_jet_bounds__statement_s
  f_gauss_jet_bounds__statement_x --> f_gauss_jet_bounds__statement
  f_gauss_jet_bounds__statement_x --> concept_ultrametric_norm
  f_gauss_jet_bounds__statement_x --> p_adic_numbers
  f_p_n_t_dens_ls_a --> infinite_series
  f_p_n_t_dens_ls_a --> complex_powers
  f_p_n_t_dens_ls_a --> complex_analysis
  f_p_n_t_dens_ls_a --> calculus
  f_l_function_bounds_proofs__l_function_eq_g_of_one_lt --> dirichlet_characters
  f_l_function_bounds_proofs__l_function_eq_g_of_one_lt --> dirichlet_l_function
  f_l_function_bounds_proofs__l_function_eq_g_of_one_lt --> analytic_continuation
  f_l_function_bounds_proofs__l_function_eq_g_of_one_lt --> complex_analysis
  f_l_function_bounds__positivity_bound --> f_l_function_bounds__statement
  f_l_function_bounds__positivity_bound --> dirichlet_characters
  f_l_function_bounds__positivity_bound --> dirichlet_l_function
  f_l_function_bounds__positivity_bound --> gamma_function
  f_l_function_bounds__positivity_bound --> linear_algebra
  f_l_function_bounds__statement --> f_formalism__statement
  f_l_function_bounds__statement --> f_formalism__zeta_nonvanishing_chebyshev_weights
  f_l_function_bounds__statement --> dirichlet_characters
  f_l_function_bounds__statement --> dirichlet_l_function
  f_l_function_bounds__statement --> rh_statement
  f_l_function_bounds__statement --> concept_chebyshev_functions
  f_l_function_bounds__statement --> primes_divisibility
  f_formalism__statement_f_l --> f_formalism__statement
  f_formalism__statement_f_l --> f_formalism__statement_o_c
  f_formalism__statement_f_l --> f_formalism__zeta_nonvanishing_chebyshev_weights
  f_formalism__statement_f_l --> dirichlet_characters
  f_formalism__statement_f_l --> dirichlet_l_function
  f_formalism__statement_f_l --> rh_statement
  f_formalism__statement_u --> f_formalism__statement
  f_formalism__statement_u --> f_formalism__statement_o_c
  f_formalism__statement_u --> rh_statement
  f_formalism__statement_u --> concept_chebyshev_functions
  f_formalism__statement_u --> real_analysis
  f_formalism__zeta_nonvanishing_chebyshev_weights --> f_formalism__statement_u
  f_formalism__zeta_nonvanishing_chebyshev_weights --> f_formalism__statement
  f_formalism__zeta_nonvanishing_chebyshev_weights --> rh_statement
  f_formalism__zeta_nonvanishing_chebyshev_weights --> trigonometry
  f_formalism__zeta_nonvanishing_chebyshev_weights --> concept_chebyshev_functions
  f_formalism__zeta_nonvanishing_general_weights --> f_formalism__statement_u
  f_formalism__zeta_nonvanishing_general_weights --> f_formalism__statement
  f_formalism__zeta_nonvanishing_general_weights --> rh_statement
  f_formalism__zeta_nonvanishing_general_weights --> real_analysis
  f_augmentation_quotient_equiv_lattice --> f_form_mem_lin
  f_augmentation_quotient_equiv_lattice --> f_comap_fg_of_valuation_ring
  f_augmentation_quotient_equiv_lattice --> f_dual_lattices__small_level_class_set
  f_augmentation_quotient_equiv_lattice --> f_dual_lattices__tensor_span
  f_augmentation_quotient_equiv_lattice --> f_dual_lattices__cotangent_surjective
  f_augmentation_quotient_equiv_lattice --> concept_valuation_rings
  f_comap_fg_of_valuation_ring --> concept_valuation_rings
  f_comap_fg_of_valuation_ring --> concept_flat_modules
  f_comap_fg_of_valuation_ring --> concept_projective_modules
  f_comap_fg_of_valuation_ring --> concept_local_rings
  f_comap_fg_of_valuation_ring --> linear_algebra
  f_form_mem_lin --> f_comap_fg_of_valuation_ring
  f_form_mem_lin --> f_dual_lattices__small_level_class_set
  f_form_mem_lin --> f_dual_lattices__tensor_span
  f_form_mem_lin --> f_dual_lattices__cotangent_surjective
  f_form_mem_lin --> concept_valuation_rings
  f_form_mem_lin --> modular_arithmetic
  f_form_mem_lin --> linear_algebra
  f_misc_lemmas_l__imports --> concept_integral_closure_fraction_fields
  f_misc_lemmas_l__imports --> rings_fields
  f_misc_lemmas_l__imports --> linear_algebra
  f_dual_lattices__exists_smul_mem_of_mem_span --> f_misc_lemmas_l__imports
  f_dual_lattices__exists_smul_mem_of_mem_span --> f_dual_lattices__tensor_span
  f_dual_lattices__exists_smul_mem_of_mem_span --> concept_valuation_rings
  f_dual_lattices__exists_smul_mem_of_mem_span --> concept_projective_modules
  f_dual_lattices__exists_smul_mem_of_mem_span --> concept_flat_modules
  f_dual_lattices__exists_smul_mem_of_mem_span --> linear_algebra
  f_period_integrals__fgl_gram --> p_adic_numbers
  f_period_integrals__fgl_gram --> concept_ultrametric_norm
  f_period_integrals__fgl_gram --> polynomials
  f_period_integrals__fgl_gram --> linear_algebra
  f_period_integrals__fgl_ph_split --> polynomials
  f_period_integrals__fgl_ph_split --> rings_fields
  f_period_integrals__fgl_ph_split --> linear_algebra
  f_ph_dual_gram --> f_ph_dual_gram_main
  f_ph_dual_gram --> f_period_integrals__fgl_gram
  f_dual_gram_substitution__be_mul_by_zero --> f_dual_gram_substitution__has_subst_ren
  f_dual_gram_substitution__be_mul_by_zero --> f_formal_group_splitting__orthogonal_split_polarization_vanishes
  f_dual_gram_substitution__be_mul_by_zero --> f_period_integrals__fgl_gram
  f_dual_gram_substitution__be_mul_by_zero --> polynomials
  f_dual_gram_substitution__has_subst_ren --> f_formal_group_splitting__exp_congruence_extends_to_sum
  f_dual_gram_substitution__has_subst_ren --> f_period_integrals__fgl_gram
  f_dual_gram_substitution__has_subst_ren --> concept_ultrametric_norm
  f_dual_gram_substitution__has_subst_ren --> polynomials
  f_ph_dual_gram_main --> f_dual_gram_substitution__be_mul_by_zero
  f_ph_dual_gram_main --> f_dual_gram_substitution__has_subst_ren
  f_ph_dual_gram_main --> f_formal_group_splitting__orthogonal_split_polarization_vanishes
  f_ph_dual_gram_main --> f_period_integrals__fgl_gram
  f_ph_dual_gram_main --> f_period_integrals__fgl_ph_split
  f_formal_group_splitting__add_preserves_exp_congruence --> f_formal_group_splitting__development
  f_formal_group_splitting__add_preserves_exp_congruence --> f_period_integrals__fgl_ph_split
  f_formal_group_splitting__add_preserves_exp_congruence --> polynomials
  f_formal_group_splitting__add_preserves_exp_congruence --> infinite_series
  f_formal_group_splitting__add_preserves_exp_congruence --> counting
  f_formal_group_splitting__development --> f_period_integrals__fgl_ph_split
  f_formal_group_splitting__exp_congruence_extends_to_sum --> f_formal_group_splitting__development
  f_formal_group_splitting__exp_congruence_extends_to_sum --> f_formal_group_splitting__orthogonal_split_polarization_vanishes
  f_formal_group_splitting__exp_congruence_extends_to_sum --> f_period_integrals__fgl_ph_split
  f_formal_group_splitting__exp_congruence_extends_to_sum --> polynomials
  f_formal_group_splitting__orthogonal_split_polarization_vanishes --> f_formal_group_splitting__development
  f_formal_group_splitting__orthogonal_split_polarization_vanishes --> f_period_integrals__fgl_ph_split
  f_formal_group_splitting__orthogonal_split_polarization_vanishes --> polynomials
  f_exists_kummer_character_of_upper_half_plane_root --> f_foundation_proofs__upper_half_plane_holomorphic_germ_properties
  f_exists_kummer_character_of_upper_half_plane_root --> f_foundation_proofs__gl_two_pos_rat_mobius_basic_laws
  f_exists_kummer_character_of_upper_half_plane_root --> f_foundations__exp_upper
  f_exists_kummer_character_of_upper_half_plane_root --> f_foundations__is_root_one
  f_exists_kummer_character_of_upper_half_plane_root --> concept_roots_of_unity_kummer
  f_exists_kummer_character_of_upper_half_plane_root --> concept_modular_forms
  f_exists_kummer_character_of_upper_half_plane_root --> complex_analysis
  f_foundation_proofs__upper_half_plane_holomorphic_germ_properties --> f_foundation_proofs__gl_two_pos_rat_mobius_basic_laws
  f_foundation_proofs__upper_half_plane_holomorphic_germ_properties --> complex_analysis
  f_foundation_proofs__upper_half_plane_holomorphic_germ_properties --> concept_point_set_topology
  f_foundation_proofs__upper_half_plane_holomorphic_germ_properties --> complex_numbers
  f_foundation_proofs__upper_half_plane_holomorphic_germ_properties --> concept_roots_of_unity_kummer
  f_exists_eichler_shimura_potential_of_homogeneous_poly_co --> f_gamma1_cap_gamma0_level_acts_freely_upper_half_plane
  f_exists_eichler_shimura_potential_of_homogeneous_poly_co --> f_foundations__op_l_d_one_sub_mem_triv
  f_exists_eichler_shimura_potential_of_homogeneous_poly_co --> f_foundations__exp_upper
  f_exists_eichler_shimura_potential_of_homogeneous_poly_co --> concept_group_actions
  f_exists_eichler_shimura_potential_of_homogeneous_poly_co --> concept_modular_forms
  f_exists_eichler_shimura_potential_of_homogeneous_poly_co --> polynomials
  f_gamma1_cap_gamma0_level_acts_freely_upper_half_plane --> concept_modular_forms
  f_gamma1_cap_gamma0_level_acts_freely_upper_half_plane --> concept_group_actions
  f_gamma1_cap_gamma0_level_acts_freely_upper_half_plane --> modular_arithmetic
  f_gamma1_cap_gamma0_level_acts_freely_upper_half_plane --> f_foundations__exp_upper
  f_gamma1_cap_gamma0_level_acts_freely_upper_half_plane --> complex_numbers
  f_flag_measures__prim_of_is_unit_det --> concept_hermitian_unitary_matrices
  f_flag_measures__prim_of_is_unit_det --> linear_algebra
  f_flag_measures__prim_of_is_unit_det --> rings_fields
  f_flag_measures__prim_of_is_unit_det --> counting
  f_exists_primitive_add_char_involution_invariant --> f_flag_measures__prim_of_is_unit_det
  f_exists_primitive_add_char_involution_invariant --> concept_group_representations
  f_exists_primitive_add_char_involution_invariant --> concept_local_rings
  f_exists_primitive_add_char_involution_invariant --> rings_fields
  f_is_primitive_tuple_of_linear_independent_finite_ring --> f_flag_measures__prim_of_is_unit_det
  f_is_primitive_tuple_of_linear_independent_finite_ring --> concept_group_representations
  f_is_primitive_tuple_of_linear_independent_finite_ring --> linear_algebra
  f_is_primitive_tuple_of_linear_independent_finite_ring --> fourier_analysis
  f_norm_gauss_sum_hermitian_form_linear_le --> f_flag_measures__prim_of_is_unit_det
  f_norm_gauss_sum_hermitian_form_linear_le --> concept_group_representations
  f_norm_gauss_sum_hermitian_form_linear_le --> fourier_analysis
  f_norm_gauss_sum_hermitian_form_linear_le --> complex_numbers
  f_card_hermitian_quadric_affine_subspace_residue_ring --> f_norm_gauss_sum_hermitian_form_linear_le
  f_card_hermitian_quadric_affine_subspace_residue_ring --> f_flag_measures__prim_of_is_unit_det
  f_card_hermitian_quadric_affine_subspace_residue_ring --> fourier_analysis
  f_card_hermitian_quadric_affine_subspace_residue_ring --> concept_group_representations
  f_card_hermitian_quadric_affine_subspace_residue_ring --> counting
  f_ncard_dependent_vectors_affine_gram_le --> f_flag_measures__prim_of_is_unit_det
  f_ncard_dependent_vectors_affine_gram_le --> linear_algebra
  f_ncard_dependent_vectors_affine_gram_le --> counting
  f_ncard_dependent_vectors_affine_gram_le --> rings_fields
  f_card_primitive_tuple_extensions_le --> f_card_hermitian_quadric_affine_subspace_residue_ring
  f_card_primitive_tuple_extensions_le --> f_ncard_dependent_vectors_affine_gram_le
  f_card_primitive_tuple_extensions_le --> f_exists_primitive_add_char_involution_invariant
  f_card_primitive_tuple_extensions_le --> f_is_primitive_tuple_of_linear_independent_finite_ring
  f_card_primitive_tuple_extensions_le --> counting
  f_ncard_primitive_tuples_with_gram_matrix_residue_ring --> f_card_primitive_tuple_extensions_le
  f_ncard_primitive_tuples_with_gram_matrix_residue_ring --> f_flag_measures__prim_of_is_unit_det
  f_ncard_primitive_tuples_with_gram_matrix_residue_ring --> concept_hermitian_unitary_matrices
  f_ncard_primitive_tuples_with_gram_matrix_residue_ring --> counting
  f_ncard_primitive_tuples_with_gram_matrix_residue_ring --> linear_algebra
  f_form_off_variety_mul --> f_is_form_off_mul
  f_form_off_variety_mul --> concept_coordinate_rings_dimension
  f_form_off_variety_mul --> polynomials
  f_rational_sup_metrics__aeval_coord_prod --> polynomials
  f_rational_sup_metrics__aeval_coord_prod --> counting
  f_rational_sup_metrics__aeval_coord_prod --> concept_coordinate_rings_dimension
  f_is_form_off_mul --> f_rational_sup_metrics__aeval_coord_prod
  f_is_form_off_mul --> concept_prime_ideals_localization
  f_is_form_off_mul --> concept_coordinate_rings_dimension
  f_is_form_off_mul --> polynomials
  f_k_h_free_decomp_st --> f_kleiman_ampleness__k_h_free_obj
  f_k_h_free_decomp_st --> concept_chain_complexes_homology
  f_k_h_free_decomp_st --> polynomials
  f_p_k_h_free_decomp --> f_k_h_free_decomp_st
  f_p_k_h_free_decomp --> f_kleiman_ampleness__k_h_free_obj
  f_p_k_h_free_decomp --> concept_prime_ideals_localization
  f_p_k_h_free_decomp --> concept_chain_complexes_homology
  f_p_k_h_free_decomp --> linear_algebra
  f_foundation_proofs__diag_mod --> f_foundations__exp_upper
  f_foundation_proofs__diag_mod --> f_foundations__op_l_d_one_sub_mem_triv
  f_foundation_proofs__diag_mod --> concept_modular_forms
  f_foundation_proofs__diag_mod --> concept_valuation_rings
  f_exists_unit_eval_eq_kummer_class --> f_foundation_proofs__tower_unit_class_mod_prime_pow_properties
  f_exists_unit_eval_eq_kummer_class --> f_local_power_units_tower_closure_properties
  f_exists_unit_eval_eq_kummer_class --> f_foundations__exp_upper
  f_exists_unit_eval_eq_kummer_class --> f_foundations__is_root_one
  f_exists_unit_eval_eq_kummer_class --> concept_adic_completion
  f_exists_unit_eval_eq_kummer_class --> concept_roots_of_unity_kummer
  f_local_power_units_tower_closure_properties --> f_foundations__exp_upper
  f_local_power_units_tower_closure_properties --> concept_valuation_rings
  f_local_power_units_tower_closure_properties --> concept_roots_of_unity_kummer
  f_foundation_proofs__tower_unit_class_mod_prime_pow_properties --> f_foundations__exp_upper
  f_foundation_proofs__tower_unit_class_mod_prime_pow_properties --> f_foundations__is_root_one
  f_foundation_proofs__tower_unit_class_mod_prime_pow_properties --> concept_flat_modules
  f_foundation_proofs__tower_unit_class_mod_prime_pow_properties --> concept_adic_completion
  f_foundation_proofs__tower_unit_class_mod_prime_pow_properties --> p_adic_numbers
  f_foundation_proofs__tower_unit_class_mod_prime_pow_properties --> concept_finitely_generated_abelian_groups
  f_small_on_walls_near_discriminant --> f_vanishing_on_walls_divisible
  f_small_on_walls_near_discriminant --> f_wall_set_compact_dominant
  f_small_on_walls_near_discriminant --> f_foundations__curve_cl
  f_small_on_walls_near_discriminant --> f_degree_formula__flag_deg_formula
  f_small_on_walls_near_discriminant --> linear_algebra
  f_small_on_walls_near_discriminant --> polynomials
  f_small_on_walls_near_discriminant --> concept_point_set_topology
  f_vanishing_on_walls_divisible --> f_x_sub_x_dvd_of_vanish_on_open_hyperplane
  f_vanishing_on_walls_divisible --> f_foundations__curve_cl
  f_vanishing_on_walls_divisible --> f_degree_formula__flag_deg_formula
  f_vanishing_on_walls_divisible --> f_point_degree__pow_sum
  f_vanishing_on_walls_divisible --> polynomials
  f_vanishing_on_walls_divisible --> concept_symmetric_polynomials
  f_vanishing_on_walls_divisible --> rings_fields
  f_wall_set_compact_dominant --> f_foundations__curve_cl
  f_wall_set_compact_dominant --> concept_point_set_topology
  f_wall_set_compact_dominant --> real_analysis
  f_x_sub_x_dvd_of_vanish_on_open_hyperplane --> polynomials
  f_x_sub_x_dvd_of_vanish_on_open_hyperplane --> rings_fields
  f_x_sub_x_dvd_of_vanish_on_open_hyperplane --> concept_point_set_topology
  f_x_sub_x_dvd_of_vanish_on_open_hyperplane --> real_analysis
  f_chebotarev__n_z_ideal --> number_fields
  f_chebotarev__n_z_ideal --> concept_dedekind_domains
  f_chebotarev__n_z_ideal --> concept_ideals_and_discriminant
  f_chebotarev__n_z_ideal --> dirichlet_characters
  f_chebotarev__n_z_ideal --> dirichlet_l_function
  f_chebotarev__n_z_ideal --> infinite_series
  f_chebotarev__euler_fac --> f_chebotarev__n_z_ideal
  f_chebotarev__euler_fac --> concept_dedekind_domains
  f_chebotarev__euler_fac --> concept_ideals_and_discriminant
  f_chebotarev__euler_fac --> primes_divisibility
  f_chebotarev__euler_fin --> f_chebotarev__euler_fac
  f_chebotarev__euler_fin --> f_chebotarev__n_z_ideal
  f_chebotarev__euler_fin --> infinite_series
  f_chebotarev__euler_fin --> concept_dedekind_domains
  f_chebotarev__euler_lim --> f_chebotarev__euler_fin
  f_chebotarev__euler_lim --> f_chebotarev__euler_fac
  f_chebotarev__euler_lim --> f_chebotarev__n_z_ideal
  f_chebotarev__euler_lim --> complex_analysis
  f_chebotarev__euler_lim --> infinite_series
  f_chebotarev__euler_sum --> f_chebotarev__n_z_ideal
  f_chebotarev__euler_sum --> number_fields
  f_chebotarev__euler_sum --> concept_dedekind_domains
  f_chebotarev__euler_sum --> concept_lattice_point_counting
  f_chebotarev__euler_sum --> infinite_series
  f_chebotarev__euler_sum --> zeta_series
  f_chebotarev__prime_asymp --> f_chebotarev__euler_lim
  f_chebotarev__prime_asymp --> f_chebotarev__euler_sum
  f_chebotarev__prime_asymp --> f_chebotarev__n_z_ideal
  f_chebotarev__prime_asymp --> f_chebotarev__casimir_power_surjective_symmetric
  f_chebotarev__prime_asymp --> calculus
  f_chebotarev__prime_asymp --> real_analysis
  f_chebotarev__prime_cont --> f_chebotarev__euler_sum
  f_chebotarev__prime_cont --> f_chebotarev__n_z_ideal
  f_chebotarev__prime_cont --> f_chebotarev__casimir_power_surjective_symmetric
  f_chebotarev__prime_cont --> dirichlet_characters
  f_chebotarev__prime_cont --> complex_analysis
  f_chebotarev__prime_cont --> real_analysis
  f_chebotarev__prime_sum --> f_chebotarev__euler_sum
  f_chebotarev__prime_sum --> f_chebotarev__n_z_ideal
  f_chebotarev__prime_sum --> f_chebotarev__casimir_power_surjective_symmetric
  f_chebotarev__prime_sum --> dirichlet_characters
  f_chebotarev__prime_sum --> infinite_series
  f_chebotarev__prime_sum --> complex_analysis
  f_chebotarev__casimir_power_surjective_symmetric --> f_chebotarev__n_z_ideal
  f_chebotarev__casimir_power_surjective_symmetric --> dirichlet_l_function
  f_chebotarev__casimir_power_surjective_symmetric --> dirichlet_characters
  f_chebotarev__casimir_power_surjective_symmetric --> concept_dedekind_domains
  f_chebotarev__casimir_power_surjective_symmetric --> number_fields
  f_chebotarev__chebyshev_lambda_sub_psi_bounded --> f_chebotarev__euler_lim
  f_chebotarev__chebyshev_lambda_sub_psi_bounded --> f_chebotarev__euler_sum
  f_chebotarev__chebyshev_lambda_sub_psi_bounded --> f_chebotarev__prime_sum
  f_chebotarev__chebyshev_lambda_sub_psi_bounded --> f_chebotarev__prime_asymp
  f_chebotarev__chebyshev_lambda_sub_psi_bounded --> f_chebotarev__prime_cont
  f_chebotarev__chebyshev_lambda_sub_psi_bounded --> f_chebotarev__casimir_power_surjective_symmetric
  f_chebotarev__chebyshev_lambda_sub_psi_bounded --> f_chebotarev__n_z_ideal
  f_chebotarev__chebyshev_lambda_sub_psi_bounded --> dirichlet_l_function
  f_chebotarev__split_def --> f_chebotarev__n_z_ideal
  f_chebotarev__split_def --> number_fields
  f_chebotarev__split_def --> concept_dedekind_domains
  f_chebotarev__split_def --> concept_prime_ideals_localization
  f_chebotarev__split_f --> infinite_series
  f_chebotarev__split_f --> counting
  f_chebotarev__split_c --> f_chebotarev__split_def
  f_chebotarev__split_c --> f_chebotarev__split_f
  f_chebotarev__split_c --> f_chebotarev__chebyshev_lambda_sub_psi_bounded
  f_chebotarev__split_c --> f_chebotarev__prime_asymp
  f_chebotarev__split_c --> f_chebotarev__euler_sum
  f_chebotarev__split_c --> f_chebotarev__n_z_ideal
  f_chebotarev__split_c --> number_fields
  f_lie_model_pullback_equivalence --> f_global_geometry__lie_model
  f_lie_model_pullback_equivalence --> f_toroidal_compactification__is_grp_pullback
  f_lie_model_pullback_equivalence --> f_global_geometry__is_cochar_lie
  f_lie_model_pullback_equivalence --> concept_dual_numbers
  f_lie_model_pullback_equivalence --> concept_categorical_pullbacks
  f_lie_model_pullback_equivalence --> concept_group_schemes
  f_lie_model_pullback_equivalence --> concept_schemes_basics
  f_eisenstein_translation_products__semi_char --> concept_weierstrass_elliptic_functions
  f_eisenstein_translation_products__semi_char --> concept_lattices_in_the_plane
  f_eisenstein_translation_products__semi_char --> complex_analysis
  f_eisenstein_translation_products__legendre --> f_eisenstein_translation_products__semi_char
  f_eisenstein_translation_products__legendre --> concept_weierstrass_elliptic_functions
  f_eisenstein_translation_products__legendre --> complex_analysis
  f_eisenstein_translation_products__theta_line --> f_eisenstein_translation_products__semi_char
  f_eisenstein_translation_products__theta_line --> concept_weierstrass_elliptic_functions
  f_eisenstein_translation_products__theta_line --> complex_analysis
  f_eisenstein_translation_products__theta_zero_log_derivative --> f_eisenstein_translation_products__semi_char
  f_eisenstein_translation_products__theta_zero_log_derivative --> f_eisenstein_translation_products__legendre
  f_eisenstein_translation_products__theta_zero_log_derivative --> concept_weierstrass_elliptic_functions
  f_eisenstein_translation_products__theta_zero_log_derivative --> concept_lattices_in_the_plane
  f_eisenstein_translation_products__theta_zero_log_derivative --> concept_hermitian_unitary_matrices
  f_eisenstein_translation_products__theta_zero_translate_product --> f_eisenstein_translation_products__theta_zero_log_derivative
  f_eisenstein_translation_products__theta_zero_translate_product --> f_eisenstein_translation_products__theta_line
  f_eisenstein_translation_products__theta_zero_translate_product --> f_eisenstein_translation_products__translate_product
  f_eisenstein_translation_products__theta_zero_translate_product --> f_eisenstein_translation_products__semi_char
  f_eisenstein_translation_products__theta_zero_translate_product --> concept_weierstrass_elliptic_functions
  f_eisenstein_translation_products__translate_product --> f_eisenstein_translation_products__semi_char
  f_eisenstein_translation_products__translate_product --> concept_weierstrass_elliptic_functions
  f_eisenstein_translation_products__translate_product --> concept_lattices_in_the_plane
  f_eisenstein_translation_products__c_m_quasi_period_const --> f_eisenstein_translation_products__translate_product
  f_eisenstein_translation_products__c_m_quasi_period_const --> f_eisenstein_translation_products__semi_char
  f_eisenstein_translation_products__c_m_quasi_period_const --> f_eisenstein_translation_products__theta_zero_log_derivative
  f_eisenstein_translation_products__c_m_quasi_period_const --> concept_lattices_in_the_plane
  f_eisenstein_translation_products__c_m_quasi_period_const --> concept_weierstrass_elliptic_functions
  f_eisenstein_translation_products__c_m_quasi_period_const --> concept_ideals_and_discriminant
  f_quadratic_semicharacters__is_semi_char --> f_eisenstein_translation_products__semi_char
  f_quadratic_semicharacters__is_semi_char --> concept_hermitian_unitary_matrices
  f_quadratic_semicharacters__is_semi_char --> concept_lattice_point_counting
  f_quadratic_semicharacters__is_semi_char --> linear_algebra
  f_quadratic_semicharacters__is_semi_char --> complex_analysis
  f_quadratic_semicharacters__product_theta_mem --> f_quadratic_semicharacters__is_semi_char
  f_quadratic_semicharacters__product_theta_mem --> f_eisenstein_translation_products__semi_char
  f_quadratic_semicharacters__product_theta_mem --> f_eisenstein_translation_products__theta_zero_translate_product
  f_quadratic_semicharacters__product_theta_mem --> concept_roots_of_unity_kummer
  f_period_integrals__ker_tens --> f_quadratic_semicharacters__is_semi_char
  f_period_integrals__ker_tens --> f_quadratic_semicharacters__product_theta_mem
  f_period_integrals__ker_tens --> f_eisenstein_translation_products__semi_char
  f_mat_h_h_one --> f_period_integrals__ker_tens
  f_mat_h_h_one --> f_quadratic_semicharacters__is_semi_char
  f_mat_h_h_one --> f_quadratic_semicharacters__product_theta_mem
  f_mat_h_h_one --> complex_analysis
  f_tens_spans --> f_mat_h_h_one
  f_tens_spans --> f_period_integrals__ker_tens
  f_tens_spans --> f_quadratic_semicharacters__is_semi_char
  f_tens_spans --> f_quadratic_semicharacters__product_theta_mem
  f_orbital_bounds_conclusion__ker_tens --> f_tens_spans
  f_orbital_bounds_conclusion__ker_tens --> f_period_integrals__ker_tens
  f_etale_integrally_closed_in_localization --> concept_integral_closure_fraction_fields
  f_etale_integrally_closed_in_localization --> concept_etale_ring_maps
  f_etale_integrally_closed_in_localization --> concept_prime_ideals_localization
  f_etale_integrally_closed_in_localization --> concept_tensor_product_of_algebras
  f_etale_integrally_closed_in_localization --> concept_flat_modules
  f_extension_descent__base_over --> f_extension_descent__const_gen
  f_extension_descent__base_over --> f_abelian_scheme_quotients__is_abelian_scheme
  f_extension_descent__base_over --> concept_group_schemes
  f_extension_descent__base_over --> concept_schemes_basics
  f_extension_descent__base_over --> concept_roots_of_unity_kummer
  f_extension_descent__base_over --> algebraic_closure
  f_extension_descent__lin_comb_triv_g --> f_extension_descent__nonzero_locus
  f_extension_descent__lin_comb_triv_g --> f_abelian_scheme_quotients__is_abelian_scheme
  f_extension_descent__lin_comb_triv_g --> f_cubical_structures__cube_symmetric_swap_first
  f_extension_descent__lin_comb_triv_g --> concept_ample_nef_line_bundles
  f_extension_descent__lin_comb_triv_g --> concept_group_schemes
  f_extension_descent__lin_comb_triv_g --> concept_schemes_basics
  f_theta1 --> f_extension_descent__lin_comb_triv_g
  f_theta1 --> f_extension_descent__theta_pt
  f_theta1 --> f_theta_v_v
  f_theta1 --> f_extension_descent__const_gen
  f_extension_descent__theta_pt --> f_extension_descent__const_gen
  f_extension_descent__theta_pt --> f_extension_descent__base_over
  f_extension_descent__theta_pt --> f_cubical_structures__cube_symmetric_swap_first
  f_extension_descent__theta_pt --> concept_group_schemes
  f_extension_descent__theta_pt --> concept_ample_nef_line_bundles
  f_theta_v_v --> f_extension_descent__theta_pt
  f_theta_v_v --> f_extension_descent__base_over
  f_theta_v_v --> f_extension_descent__const_gen
  f_theta_v_v --> concept_projective_modules
  f_theta_v_v --> concept_ample_nef_line_bundles
  f_annihilator_quotient_smul_top_of_free --> f_cohen_macaulay__mod_depth_g_e
  f_annihilator_quotient_smul_top_of_free --> f_cohen_macaulay__exists_is_regular_append_of_mod_depth_g_e
  f_annihilator_quotient_smul_top_of_free --> f_cohen_macaulay__bridge
  f_annihilator_quotient_smul_top_of_free --> f_maximal_ideal_squares__ring_krull_dim_quotient_span_singleton_add_one
  f_annihilator_quotient_smul_top_of_free --> concept_local_rings
  f_annihilator_quotient_smul_top_of_free --> concept_regular_local_rings
  f_annihilator_quotient_smul_top_of_free --> concept_projective_modules
  f_module_free_of_regular_of_free_quotient_local --> f_annihilator_quotient_smul_top_of_free
  f_module_free_of_regular_of_free_quotient_local --> concept_local_rings
  f_module_free_of_regular_of_free_quotient_local --> concept_projective_modules
  f_module_free_of_regular_of_free_quotient_local --> concept_prime_ideals_localization
  f_divisor_proofs__purity_free --> f_cohen_macaulay__mod_depth_g_e
  f_divisor_proofs__purity_free --> concept_etale_ring_maps
  f_divisor_proofs__purity_free --> concept_local_rings
  f_divisor_proofs__purity_free --> concept_prime_ideals_localization
  f_divisor_proofs__purity_free --> concept_tensor_product_of_algebras
  f_general_b_fact_side__imports --> concept_local_rings
  f_general_b_fact_side__imports --> concept_prime_ideals_localization
  f_cohen_macaulay__bridge --> f_cohen_macaulay__mod_depth_g_e
  f_cohen_macaulay__bridge --> f_commutative_algebra__chain_conn_in_dim
  f_cohen_macaulay__bridge --> concept_local_rings
  f_cohen_macaulay__bridge --> concept_prime_ideals_localization
  f_cohen_macaulay__exists_is_regular_append_of_mod_depth_g_e --> f_cohen_macaulay__mod_depth_g_e
  f_cohen_macaulay__exists_is_regular_append_of_mod_depth_g_e --> f_general_b_fact_side__imports
  f_cohen_macaulay__exists_is_regular_append_of_mod_depth_g_e --> concept_local_rings
  f_cohen_macaulay__exists_is_regular_append_of_mod_depth_g_e --> concept_prime_ideals_localization
  f_maximal_ideal_squares__ring_krull_dim_quotient_span_singleton_add_one --> concept_regular_local_rings
  f_maximal_ideal_squares__ring_krull_dim_quotient_span_singleton_add_one --> concept_local_rings
  f_maximal_ideal_squares__ring_krull_dim_quotient_span_singleton_add_one --> concept_coordinate_rings_dimension
  f_maximal_ideal_squares__ring_krull_dim_quotient_span_singleton_add_one --> concept_prime_ideals_localization
  f_lie_lattice_range_of_stalk --> f_normal_lattice_range
  f_lie_lattice_range_of_stalk --> f_global_geometry__lie_model
  f_lie_lattice_range_of_stalk --> f_global_geometry__is_cpt_gen
  f_normal_lattice_range --> f_global_geometry__lie_model
  f_normal_lattice_range --> f_global_geometry__eig_lat
  f_normal_lattice_range --> f_global_geometry__is_cochar_lie
  f_normal_lattice_range --> f_global_geometry__is_cpt_gen
  f_normal_lattice_range --> f_geometry_proofs__spec_stalk_specializes_comp
  f_normal_lattice_range --> concept_dual_numbers
  f_normal_lattice_range --> concept_group_schemes
  f_normal_lattice_range --> concept_local_rings
  f_multihomogeneous_value_well_defined --> f_valuation_unique_on_forms
  f_valuation_unique_on_forms --> f_rational_sup_metrics__aeval_coord_prod
  f_valuation_unique_on_forms --> polynomials
  f_valuation_unique_on_forms --> rings_fields
  f_gen_pt_specializes --> f_global_geometry__is_cpt_gen
  f_gen_pt_specializes --> concept_schemes_basics
  f_gen_pt_specializes --> concept_local_rings
  f_gen_pt_specializes_of_specializes --> f_gen_pt_specializes
  f_gen_pt_specializes_of_specializes --> f_global_geometry__is_cpt_gen
  f_gen_pt_specializes_of_specializes --> concept_noetherian_and_irreducible_components
  f_gen_pt_specializes_of_specializes --> concept_schemes_basics
  f_is_unit_of_basic_open_nonempty_of_universally_closed --> concept_schemes_basics
  f_is_unit_of_basic_open_nonempty_of_universally_closed --> concept_local_rings
  f_is_unit_of_basic_open_nonempty_of_universally_closed --> concept_point_set_topology
  f_is_unit_of_basic_open_nonempty_of_universally_closed --> concept_integral_closure_fraction_fields
  f_is_unit_of_basic_open_nonempty_of_universally_closed --> polynomials
  f_function_on_connected_fibre_unit --> f_is_unit_of_basic_open_nonempty_of_universally_closed
  f_function_on_connected_fibre_unit --> f_gen_pt_specializes_of_specializes
  f_function_on_connected_fibre_unit --> f_gen_pt_specializes
  f_function_on_connected_fibre_unit --> f_geometry_proofs__gen_map_germ_eq_gen_map_germ
  f_function_on_connected_fibre_unit --> f_global_geometry__is_cpt_gen
  f_function_on_connected_fibre_unit --> concept_discrete_valuation_ring
  f_function_on_connected_fibre_unit --> concept_schemes_basics
  f_function_on_connected_fibre_unit --> concept_point_set_topology
  f_harish_chandra_descent__descent --> f_discrete_series__is_inf_unitary
  f_harish_chandra_descent__descent --> f_discrete_series__defs_rep
  f_harish_chandra_descent__descent --> f_bochner_inequality__cas_val_k
  f_harish_chandra_descent__descent --> f_bochner_inequality__layer_basic
  f_harish_chandra_descent__descent --> concept_highest_weight_casimir
  f_harish_chandra_descent__descent --> concept_hermitian_unitary_matrices
  f_positive_negative_holds --> f_harish_chandra_descent__descent
  f_positive_negative_holds --> concept_hermitian_unitary_matrices
  f_simultaneous_eigenvectors__bl_simeig --> linear_algebra
  f_simultaneous_eigenvectors__bl_simeig --> concept_highest_weight_casimir
  f_bochner_inequality__is_k_unitary_of_is_inf_unitary --> f_discrete_series__is_inf_unitary
  f_bochner_inequality__is_k_unitary_of_is_inf_unitary --> f_simultaneous_eigenvectors__bl_simeig
  f_bochner_inequality__is_k_unitary_of_is_inf_unitary --> f_bochner_inequality__cas_val_k
  f_bochner_inequality__is_k_unitary_of_is_inf_unitary --> concept_highest_weight_casimir
  f_bochner_inequality__is_k_unitary_of_is_inf_unitary --> concept_hermitian_unitary_matrices
  f_bochner_inequality__k_unit_b --> f_bochner_inequality__is_k_unitary_of_is_inf_unitary
  f_bochner_inequality__k_unit_b --> f_casimir_algebra__casimir_k_khw_vec
  f_bochner_inequality__k_unit_b --> f_bochner_inequality__cas_val_k
  f_bochner_inequality__k_unit_b --> concept_hermitian_unitary_matrices
  f_casimir_algebra__casimir_k_khw_vec --> f_discrete_series__is_inf_unitary
  f_casimir_algebra__casimir_k_khw_vec --> concept_highest_weight_casimir
  f_sl2_raise_pow_succ_lower_apply_eq --> concept_highest_weight_casimir
  f_sl2_raise_pow_succ_lower_apply_eq --> linear_algebra
  f_is_chain --> concept_nilpotent_jordan_chains
  f_is_chain --> linear_algebra
  f_exists_chains_of_range --> concept_nilpotent_jordan_chains
  f_exists_chains_of_range --> linear_algebra
  f_cb_is_chain_apply --> f_is_chain
  f_cb_is_chain_apply --> concept_nilpotent_jordan_chains
  f_cb_exists_chain_of_gen --> f_cb_is_chain_apply
  f_cb_exists_chain_of_gen --> f_is_chain
  f_cb_exists_chain_of_gen --> concept_nilpotent_jordan_chains
  f_chain_a --> f_is_chain
  f_chain_a --> concept_nilpotent_jordan_chains
  f_chain_b --> f_cb_exists_chain_of_gen
  f_chain_b --> f_exists_chains_of_range
  f_chain_b --> f_cb_is_chain_apply
  f_chain_b --> f_is_chain
  f_chain_b --> concept_nilpotent_jordan_chains
  f_centralizer_representatives__normal --> f_chain_b
  f_centralizer_representatives__normal --> f_chain_a
  f_centralizer_representatives__normal --> f_is_chain
  f_centralizer_representatives__normal --> concept_nilpotent_jordan_chains
  f_dex_block_frame --> f_centralizer_representatives__normal
  f_dex_block_frame --> f_is_chain
  f_dex_block_frame --> concept_prime_ideals_localization
  f_dex_block_frame --> rings_fields
  f_dex_global --> f_dex_block_frame
  f_dex_global --> concept_semisimple_algebras_radical
  f_dex_global --> concept_prime_ideals_localization
  f_dex_global --> rings_fields
  f_centralizer_representatives__imports --> f_dex_global
  f_centralizer_representatives__imports --> f_is_chain
  f_centralizer_representatives__imports --> linear_algebra
  f_centralizer_representatives__imports --> rings_fields
  f_cauchy_slice_eq_removable_extension --> complex_analysis
  f_cauchy_slice_eq_removable_extension --> calculus
  f_differentiable_at_coordinate_cauchy_integral --> f_analytic_charts__osgood
  f_differentiable_at_coordinate_cauchy_integral --> complex_analysis
  f_differentiable_at_coordinate_cauchy_integral --> calculus
  f_riemann_extension_coordinate_hyperplane --> f_cauchy_slice_eq_removable_extension
  f_riemann_extension_coordinate_hyperplane --> f_differentiable_at_coordinate_cauchy_integral
  f_riemann_extension_coordinate_hyperplane --> complex_analysis
  f_extension_across_zero_of_exp_two_pi_i_bound --> complex_analysis
  f_extension_across_zero_of_exp_two_pi_i_bound --> complex_numbers
  f_locally_bounded_off_coordinate_hyperplanes --> complex_analysis
  f_locally_bounded_off_coordinate_hyperplanes --> concept_point_set_topology
  f_extension_across_coordinate_hyperplanes --> f_extension_across_zero_of_exp_two_pi_i_bound
  f_extension_across_coordinate_hyperplanes --> f_locally_bounded_off_coordinate_hyperplanes
  f_extension_across_coordinate_hyperplanes --> f_riemann_extension_coordinate_hyperplane
  f_extension_across_coordinate_hyperplanes --> complex_analysis
  f_matrix_bound_holds --> f_harish_chandra_descent__descent
  f_matrix_bound_holds --> linear_algebra
  f_matrix_bound_holds --> real_analysis
  f_general_b_fact_rest__imports --> concept_local_rings
  f_general_b_fact_rest__imports --> concept_prime_ideals_localization
  f_general_b_fact_rest__imports --> concept_noetherian_and_irreducible_components
  f_general_b_fact_rest__imports --> rings_fields
  f_cohen_macaulay__ass_dim --> f_general_b_fact_rest__imports
  f_cohen_macaulay__ass_dim --> f_cohen_macaulay__mod_depth_g_e
  f_cohen_macaulay__ass_dim --> concept_coordinate_rings_dimension
  f_cohen_macaulay__ass_dim --> concept_local_rings
  f_cohen_macaulay__unmixed --> f_cohen_macaulay__ass_dim
  f_cohen_macaulay__unmixed --> f_cohen_macaulay__mod_depth_g_e
  f_cohen_macaulay__unmixed --> concept_coordinate_rings_dimension
  f_cohen_macaulay__unmixed --> concept_local_rings
  f_cohen_macaulay__unmixed --> concept_prime_ideals_localization
  f_cohen_macaulay__ring_krull_dim_quotient_of_mem_associated_primes --> f_cohen_macaulay__unmixed
  f_cohen_macaulay__ring_krull_dim_quotient_of_mem_associated_primes --> f_cohen_macaulay__mod_depth_g_e
  f_cohen_macaulay__ring_krull_dim_quotient_of_mem_associated_primes --> concept_local_rings
  f_cohen_macaulay__ring_krull_dim_quotient_of_mem_associated_primes --> concept_coordinate_rings_dimension
  f_gor_indep_statement --> concept_regular_local_rings
  f_gor_indep_statement --> concept_local_rings
  f_gor_indep_statement --> concept_prime_ideals_localization
  f_ring_krull_dim_quotient_add_one_le_of_lt --> concept_coordinate_rings_dimension
  f_ring_krull_dim_quotient_add_one_le_of_lt --> concept_prime_ideals_localization
  f_ring_krull_dim_quotient_add_one_le_of_lt --> rings_fields
  f_basis_e_apply --> f_cusp_span_norm_bounds__psi_e_def
  f_basis_e_apply --> number_fields
  f_basis_e_apply --> p_adic_numbers
  f_basis_e_apply --> linear_algebra
  f_den_eq_one_of_forall_padic_norm_le_one --> p_adic_numbers
  f_den_eq_one_of_forall_padic_norm_le_one --> concept_ultrametric_norm
  f_den_eq_one_of_forall_padic_norm_le_one --> complex_numbers
  f_den_eq_one_of_forall_padic_norm_le_one --> primes_divisibility
  f_prod_formula_e_of --> f_period_integrals__prod_formula_e
  f_prod_formula_e_of --> f_product_formula_haar__norm_mod
  f_prod_formula_e_of --> f_product_formula_haar__res_char_iff
  f_prod_formula_e_of --> f_product_formula_haar__tr_base
  f_prod_formula_e_of --> f_basis_e_apply
  f_prod_formula_e_of --> f_den_eq_one_of_forall_padic_norm_le_one
  f_exp_sum_lower_bound --> f_l_function_bounds__statement
  f_exp_sum_lower_bound --> f_l_function_bounds__positivity_bound
  f_exp_sum_lower_bound --> dirichlet_l_function
  f_exp_sum_lower_bound --> dirichlet_characters
  f_exp_sum_lower_bound --> complex_analysis
  f_rect_residue --> f_exp_sum_lower_bound
  f_rect_residue --> complex_analysis
  f_rect_residue --> complex_numbers
  f_rect_residue --> calculus
  f_rect_double_pole --> f_rect_residue
  f_rect_double_pole --> f_exp_sum_lower_bound
  f_rect_double_pole --> f_zero_free_region__small_height_log_deriv
  f_rect_double_pole --> complex_analysis
  f_rect_double_pole --> calculus
  f_capelli_identities__fixed_subgroup --> concept_group_representations
  f_capelli_identities__fixed_subgroup --> concept_group_actions
  f_capelli_identities__fixed_subgroup --> groups
  f_capelli_identities__fixed_subgroup --> linear_algebra
  f_hecke_algebras__continuous_torus_character --> f_capelli_identities__fixed_subgroup
  f_hecke_algebras__continuous_torus_character --> concept_group_representations
  f_hecke_algebras__continuous_torus_character --> concept_hecke_operators
  f_hecke_algebras__continuous_torus_character --> concept_adic_completion
  f_hecke_algebras__continuous_torus_character --> concept_local_rings
  f_hecke_algebras__continuous_torus_character --> concept_normal_subgroups_quotients
  f_ordinary_hecke_characters__iw_mem_mul --> f_hecke_algebras__continuous_torus_character
  f_ordinary_hecke_characters__iw_mem_mul --> groups
  f_ordinary_hecke_characters__iw_mem_mul --> concept_normal_subgroups_quotients
  f_ordinary_hecke_characters__iwahori_pro_unipotent_finite_index --> f_ordinary_hecke_characters__iw_mem_mul
  f_ordinary_hecke_characters__iwahori_pro_unipotent_finite_index --> f_hecke_algebras__continuous_torus_character
  f_ordinary_hecke_characters__iwahori_pro_unipotent_finite_index --> concept_normal_subgroups_quotients
  f_ordinary_hecke_characters__iwahori_pro_unipotent_finite_index --> counting
  f_ordinary_hecke_characters__u_op_sum --> f_hecke_algebras__continuous_torus_character
  f_ordinary_hecke_characters__u_op_sum --> concept_normal_subgroups_quotients
  f_ordinary_hecke_characters__u_op_sum --> concept_group_representations
  f_ordinary_hecke_characters__u_op_sum --> counting
  f_ordinary_hecke_characters__u_op_mul --> f_ordinary_hecke_characters__u_op_sum
  f_ordinary_hecke_characters__u_op_mul --> f_hecke_algebras__continuous_torus_character
  f_ordinary_hecke_characters__u_op_mul --> concept_hecke_operators
  f_ordinary_hecke_characters__u_op_mul --> concept_group_representations
  f_ordinary_hecke_characters__u_op_nat --> f_hecke_algebras__continuous_torus_character
  f_ordinary_hecke_characters__u_op_nat --> concept_group_representations
  f_ordinary_hecke_characters__u_op_nat --> concept_hecke_operators
  f_ordinary_hecke_characters__u_op_level --> f_ordinary_hecke_characters__u_op_sum
  f_ordinary_hecke_characters__u_op_level --> f_ordinary_hecke_characters__u_op_mul
  f_ordinary_hecke_characters__u_op_level --> f_ordinary_hecke_characters__iw_mem_mul
  f_ordinary_hecke_characters__u_op_level --> f_hecke_algebras__continuous_torus_character
  f_ordinary_hecke_characters__u_op_level --> f_capelli_identities__fixed_subgroup
  f_ordinary_hecke_characters__sp_stab --> f_hecke_algebras__continuous_torus_character
  f_ordinary_hecke_characters__sp_stab --> f_ordinary_hecke_characters__u_op_mul
  f_ordinary_hecke_characters__sp_stab --> f_ordinary_hecke_characters__u_op_level
  f_ordinary_hecke_characters__sp_stab --> f_ordinary_hecke_characters__u_op_nat
  f_ordinary_hecke_characters__sp_stab --> f_ordinary_hecke_characters__iw_mem_mul
  f_ordinary_hecke_characters__sp_stab --> f_capelli_identities__fixed_subgroup
  f_ordinary_hecke_characters__sp_stab --> concept_adic_completion
  f_mem_val_in_of_invariant_and_values_mem_pow --> f_ordinary_hecke_characters__iw_mem_mul
  f_mem_val_in_of_invariant_and_values_mem_pow --> f_hecke_algebras__continuous_torus_character
  f_mem_val_in_of_invariant_and_values_mem_pow --> concept_adic_completion
  f_mem_val_in_of_invariant_and_values_mem_pow --> concept_local_rings
  f_kummer_character_additive_on_congruence --> f_foundation_proofs__upper_half_plane_holomorphic_germ_properties
  f_kummer_character_additive_on_congruence --> f_foundation_proofs__gl_two_pos_rat_mobius_basic_laws
  f_kummer_character_additive_on_congruence --> f_foundations__is_root_one
  f_kummer_character_additive_on_congruence --> f_foundations__exp_upper
  f_kummer_character_additive_on_congruence --> concept_modular_forms
  f_kummer_character_additive_on_congruence --> concept_roots_of_unity_kummer
  f_kummer_character_additive_on_congruence --> complex_analysis
  f_markov_inequality_holds --> f_harish_chandra_descent__descent
  f_markov_inequality_holds --> concept_hermitian_unitary_matrices
  f_markov_inequality_holds --> linear_algebra
  f_markov_inequality_holds --> real_analysis
  f_algebra_map_norm_tensor_eq_prod_conjugates --> concept_tensor_product_of_algebras
  f_algebra_map_norm_tensor_eq_prod_conjugates --> concept_galois_fixed_fields
  f_algebra_map_norm_tensor_eq_prod_conjugates --> linear_algebra
  f_algebra_map_norm_tensor_eq_prod_conjugates --> rings_fields
  f_exists_ring_hom_adic_completion_under --> concept_adic_completion
  f_exists_ring_hom_adic_completion_under --> concept_dedekind_domains
  f_exists_ring_hom_adic_completion_under --> number_fields
  f_exists_ring_hom_adic_completion_under --> p_adic_numbers
  f_hasse_norm_principle_of_cyclic_tower --> f_is_norm_from_base_change_base_change_properties
  f_hasse_norm_principle_of_cyclic_tower --> f_is_norm_from_base_change_of_pow_finrank_cyclic
  f_hasse_norm_principle_of_cyclic_tower --> f_of_intermediate_field_tower
  f_hasse_norm_principle_of_cyclic_tower --> f_exists_ring_hom_adic_completion_under
  f_hasse_norm_principle_of_cyclic_tower --> f_adelic_hermitian_forms__mem_pow_sub
  f_hasse_norm_principle_of_cyclic_tower --> concept_galois_fixed_fields
  f_hasse_norm_principle_of_cyclic_tower --> number_fields
  f_hasse_norm_principle_of_cyclic_tower --> concept_group_actions
  f_hilbert90_base_change --> concept_tensor_product_of_algebras
  f_hilbert90_base_change --> concept_galois_fixed_fields
  f_hilbert90_base_change --> concept_group_actions
  f_hilbert90_base_change --> linear_algebra
  f_is_norm_from_base_change_base_change_properties --> f_adelic_hermitian_forms__mem_pow_sub
  f_is_norm_from_base_change_base_change_properties --> concept_tensor_product_of_algebras
  f_is_norm_from_base_change_base_change_properties --> linear_algebra
  f_is_norm_from_base_change_base_change_properties --> rings_fields
  f_is_norm_from_base_change_of_pow_finrank_cyclic --> f_algebra_map_norm_tensor_eq_prod_conjugates
  f_is_norm_from_base_change_of_pow_finrank_cyclic --> f_hilbert90_base_change
  f_is_norm_from_base_change_of_pow_finrank_cyclic --> f_tensor_exists_of_galois_fixed
  f_is_norm_from_base_change_of_pow_finrank_cyclic --> f_adelic_hermitian_forms__mem_pow_sub
  f_is_norm_from_base_change_of_pow_finrank_cyclic --> concept_tensor_product_of_algebras
  f_is_norm_from_base_change_of_pow_finrank_cyclic --> concept_galois_fixed_fields
  f_is_norm_from_base_change_of_pow_finrank_cyclic --> concept_flat_modules
  f_of_intermediate_field_tower --> f_algebra_map_norm_tensor_eq_prod_conjugates
  f_of_intermediate_field_tower --> f_adelic_hermitian_forms__mem_pow_sub
  f_of_intermediate_field_tower --> concept_normal_subgroups_quotients
  f_of_intermediate_field_tower --> concept_galois_fixed_fields
  f_of_intermediate_field_tower --> concept_tensor_product_of_algebras
  f_tensor_exists_of_galois_fixed --> concept_galois_fixed_fields
  f_tensor_exists_of_galois_fixed --> concept_tensor_product_of_algebras
  f_tensor_exists_of_galois_fixed --> concept_group_actions
  f_tensor_exists_of_galois_fixed --> linear_algebra
  f_cont_diff_on_hecke_eisenstein_fourier_term --> f_divisor_base__omega_factorization
  f_cont_diff_on_hecke_eisenstein_fourier_term --> f_divisor_proofs__k_fac_differentiable
  f_cont_diff_on_hecke_eisenstein_fourier_term --> calculus
  f_cont_diff_on_hecke_eisenstein_fourier_term --> real_analysis
  f_cont_diff_on_hecke_eisenstein_fourier_term --> complex_powers
  f_cont_diff_on_hecke_eisenstein_fourier_term --> fourier_analysis
  f_has_deriv_at_hecke_term_decay_integrand --> f_cont_diff_on_hecke_eisenstein_fourier_term
  f_has_deriv_at_hecke_term_decay_integrand --> f_int_z_eq_fourier
  f_has_deriv_at_hecke_term_decay_integrand --> calculus
  f_has_deriv_at_hecke_term_decay_integrand --> complex_powers
  f_hecke_y_derivative_term_integral_polynomial_decay --> f_integrable_hecke_term_decay_integrand
  f_hecke_y_derivative_term_integral_polynomial_decay --> f_has_deriv_at_hecke_term_decay_integrand
  f_hecke_y_derivative_term_integral_polynomial_decay --> f_norm_hecke_term_decay_fourier_integral_le
  f_hecke_y_derivative_term_integral_polynomial_decay --> f_int_z_eq_fourier
  f_hecke_y_derivative_term_integral_polynomial_decay --> f_cont_diff_on_hecke_eisenstein_fourier_term
  f_hecke_y_derivative_term_integral_polynomial_decay --> fourier_analysis
  f_hecke_y_derivative_term_integral_polynomial_decay --> calculus
  f_hecke_y_derivative_term_integral_polynomial_decay --> concept_schwartz_functions
  f_int_z_eq_fourier --> f_cont_diff_on_hecke_eisenstein_fourier_term
  f_int_z_eq_fourier --> fourier_analysis
  f_int_z_eq_fourier --> complex_powers
  f_integrable_hecke_term_decay_integrand --> f_int_z_eq_fourier
  f_integrable_hecke_term_decay_integrand --> f_cont_diff_on_hecke_eisenstein_fourier_term
  f_integrable_hecke_term_decay_integrand --> real_analysis
  f_integrable_hecke_term_decay_integrand --> complex_powers
  f_norm_hecke_term_decay_fourier_integral_le --> f_int_z_eq_fourier
  f_norm_hecke_term_decay_fourier_integral_le --> real_analysis
  f_norm_hecke_term_decay_fourier_integral_le --> concept_point_set_topology
  f_orbital_bounds_conclusion__unit_det_root --> f_unit_determinant_root__partial
  f_orbital_bounds_conclusion__unit_det_root --> f_glob_fin
  f_orbital_bounds_conclusion__unit_det_root --> f_period_integrals__unit_det_root
  f_period_integrals__unit_det_root --> concept_lattices_in_the_plane
  f_period_integrals__unit_det_root --> concept_lattice_point_counting
  f_period_integrals__unit_det_root --> concept_hermitian_unitary_matrices
  f_period_integrals__unit_det_root --> p_adic_numbers
  f_period_integrals__unit_det_root --> concept_ultrametric_norm
  f_period_integrals__unit_det_root --> number_fields
  f_det_mem_of_entries --> f_global_l_unit
  f_det_mem_of_entries --> f_nsmul_rel_idx_mem
  f_det_mem_of_entries --> f_period_integrals__unit_det_root
  f_det_mem_of_entries --> concept_hermitian_unitary_matrices
  f_det_mem_of_entries --> linear_algebra
  f_det_mem_of_entries --> number_fields
  f_glob_fin --> f_glob_top
  f_glob_fin --> f_glob_vol
  f_glob_fin --> f_global_l_unit
  f_glob_fin --> concept_ideals_and_discriminant
  f_glob_fin --> number_fields
  f_glob_top --> f_ideal_pow_principal
  f_glob_top --> f_global_l_unit
  f_glob_top --> f_nsmul_rel_idx_mem
  f_glob_top --> f_norm_le_one_of_root
  f_glob_top --> concept_class_group
  f_glob_top --> concept_integral_closure_fraction_fields
  f_glob_top --> number_fields
  f_glob_vol --> f_ideal_pow_principal
  f_glob_vol --> f_norm_le_one_of_root
  f_glob_vol --> f_global_l_unit
  f_glob_vol --> linear_algebra
  f_glob_vol --> concept_integral_closure_fraction_fields
  f_glob_vol --> number_fields
  f_global_l_unit --> f_period_integrals__unit_det_root
  f_global_l_unit --> p_adic_numbers
  f_global_l_unit --> number_fields
  f_global_l_unit --> concept_integral_closure_fraction_fields
  f_global_l_unit --> concept_lattices_in_the_plane
  f_ideal_pow_principal --> concept_class_group
  f_ideal_pow_principal --> concept_ideals_and_discriminant
  f_ideal_pow_principal --> concept_dedekind_domains
  f_ideal_pow_principal --> number_fields
  f_ideal_pow_principal --> groups
  f_norm_le_one_of_root --> f_general_b_fact_left_ter__imports
  f_norm_le_one_of_root --> f_global_l_unit
  f_norm_le_one_of_root --> concept_ultrametric_norm
  f_norm_le_one_of_root --> p_adic_numbers
  f_norm_le_one_of_root --> concept_field_extensions_transcendence
  f_norm_le_one_of_root --> algebraic_closure
  f_norm_le_one_of_root --> complex_numbers
  f_nsmul_rel_idx_mem --> f_global_l_unit
  f_nsmul_rel_idx_mem --> f_period_integrals__unit_det_root
  f_nsmul_rel_idx_mem --> concept_lattices_in_the_plane
  f_nsmul_rel_idx_mem --> concept_normal_subgroups_quotients
  f_nsmul_rel_idx_mem --> linear_algebra
  f_unit_determinant_root__partial --> f_unit_det_root_of
  f_unit_determinant_root__partial --> f_det_mem_of_entries
  f_unit_determinant_root__partial --> f_nsmul_rel_idx_mem
  f_unit_determinant_root__partial --> f_norm_le_one_of_root
  f_unit_determinant_root__partial --> f_global_l_unit
  f_unit_det_root_of --> f_global_l_unit
  f_unit_det_root_of --> f_period_integrals__unit_det_root
  f_unit_det_root_of --> p_adic_numbers
  f_unit_det_root_of --> concept_ultrametric_norm
  f_unit_det_root_of --> complex_numbers
  f_general_b_fact_left_ter__imports --> concept_ultrametric_norm
  f_general_b_fact_left_ter__imports --> polynomials
  f_general_b_fact_left_ter__imports --> p_adic_numbers
  f_chebotarev__abs_prod_sub_prod_le_sum_abs_sub --> real_analysis
  f_chebotarev__abs_prod_sub_prod_le_sum_abs_sub --> infinite_series
  f_chebotarev__abs_prod_sub_prod_le_sum_abs_sub --> counting
  f_c_trick --> f_chebotarev__n_z_ideal
  f_c_trick --> f_chebotarev__euler_sum
  f_c_trick --> f_chebotarev__ucoord
  f_c_trick --> concept_class_group
  f_c_trick --> concept_dedekind_domains
  f_c_trick --> dirichlet_l_function
  f_c_trick --> dirichlet_characters
  f_c_trick --> infinite_series
  f_c_trick --> complex_powers
  f_chebotarev__ucoord --> f_chebotarev__abs_prod_sub_prod_le_sum_abs_sub
  f_chebotarev__ucoord --> f_chebotarev__n_z_ideal
  f_chebotarev__ucoord --> number_fields
  f_chebotarev__ucoord --> concept_ideals_and_discriminant
  f_chebotarev__ucoord --> concept_class_group
  f_chebotarev__ucoord --> concept_lattice_point_counting
  f_chebotarev__ucoord --> dirichlet_characters
  f_ker_base_changed_reduction_eq_span_x --> f_divisor_proofs__comap_maximal_ideal_eq_origin
  f_ker_base_changed_reduction_eq_span_x --> f_divisor_proofs__origin_ideal
  f_ker_base_changed_reduction_eq_span_x --> concept_prime_ideals_localization
  f_ker_base_changed_reduction_eq_span_x --> concept_tensor_product_of_algebras
  f_ker_base_changed_reduction_eq_span_x --> concept_local_rings
  f_ker_base_changed_reduction_eq_span_x --> concept_flat_modules
  f_det_leading_minor_gram_iwasawa --> linear_algebra
  f_exists_hermite_reduced_lattice_basis --> f_det_leading_minor_gram_iwasawa
  f_exists_hermite_reduced_lattice_basis --> f_gram_leading_minor_lower_bound_integral
  f_exists_hermite_reduced_lattice_basis --> f_gram_minor_swap_adjacent_columns
  f_exists_hermite_reduced_lattice_basis --> f_iwasawa_decomposition_real_matrix
  f_exists_hermite_reduced_lattice_basis --> f_unipotent_upper_size_reduction
  f_exists_hermite_reduced_lattice_basis --> concept_lattice_point_counting
  f_exists_hermite_reduced_lattice_basis --> linear_algebra
  f_gram_leading_minor_lower_bound_integral --> concept_hermitian_unitary_matrices
  f_gram_leading_minor_lower_bound_integral --> linear_algebra
  f_gram_minor_swap_adjacent_columns --> linear_algebra
  f_iwasawa_decomposition_real_matrix --> linear_algebra
  f_siegel_cover --> f_exists_hermite_reduced_lattice_basis
  f_siegel_cover --> f_adelic_hermitian_forms__adelic_pair
  f_siegel_cover --> concept_haar_measure_fundamental_domain
  f_siegel_cover --> concept_lattice_point_counting
  f_siegel_cover --> linear_algebra
  f_unipotent_upper_size_reduction --> linear_algebra
  f_unipotent_upper_size_reduction --> counting
  f_hyperboloid_chart_measure_formula --> f_period_integrals__rhs_w_lim
  f_hyperboloid_chart_measure_formula --> f_weighted_limit_gauge__orbit_push_cut
  f_hyperboloid_chart_measure_formula --> f_weighted_limit_gauge__orbit_push_e
  f_hyperboloid_chart_measure_formula --> f_orbit_push_q
  f_hyperboloid_chart_measure_formula --> f_orbit_push_loc
  f_hyperboloid_chart_measure_formula --> concept_hermitian_unitary_matrices
  f_hyperboloid_chart_measure_formula --> concept_haar_measure_fundamental_domain
  f_hyperboloid_chart_measure_formula --> calculus
  f_period_integrals__rhs_w_lim --> concept_haar_measure_fundamental_domain
  f_period_integrals__rhs_w_lim --> concept_hermitian_unitary_matrices
  f_period_integrals__rhs_w_lim --> concept_group_actions
  f_period_integrals__rhs_w_lim --> calculus
  f_chart_jac --> f_chart_lim
  f_chart_jac --> f_weighted_limit_gauge__volume_lie_e
  f_chart_jac --> calculus
  f_chart_jac --> real_analysis
  f_chart_lim --> f_weighted_limit_gauge__volume_lie_e
  f_chart_lim --> real_analysis
  f_chart_lim --> calculus
  f_weighted_limit_gauge__orbit_push_cut --> f_weighted_limit_gauge__volume_lie_e
  f_weighted_limit_gauge__orbit_push_cut --> f_period_integrals__rhs_w_lim
  f_weighted_limit_gauge__orbit_push_cut --> real_analysis
  f_weighted_limit_gauge__orbit_push_cut --> concept_haar_measure_fundamental_domain
  f_weighted_limit_gauge__orbit_push_e --> f_weighted_limit_gauge__orbit_push_cut
  f_weighted_limit_gauge__orbit_push_e --> concept_point_set_topology
  f_weighted_limit_gauge__orbit_push_e --> real_analysis
  f_orbit_push_loc --> f_chart_jac
  f_orbit_push_loc --> f_weighted_limit_gauge__orbit_push_cut
  f_orbit_push_loc --> f_weighted_limit_gauge__volume_lie_e
  f_orbit_push_loc --> calculus
  f_orbit_push_q --> f_weighted_limit_gauge__orbit_push_cut
  f_orbit_push_q --> complex_numbers
  f_orbit_push_q --> linear_algebra
  f_weighted_limit_gauge__volume_lie_e --> f_period_integrals__rhs_w_lim
  f_weighted_limit_gauge__volume_lie_e --> concept_haar_measure_fundamental_domain
  f_weighted_limit_gauge__volume_lie_e --> real_analysis
  f_link_exactness_stability__exists_g_l_moving_unimodular_pair_to_last_basis --> concept_gl_infinity_homology_stability
  f_link_exactness_stability__exists_g_l_moving_unimodular_pair_to_last_basis --> f_tensor_hom_cubes__stab_directed_system
  f_link_exactness_stability__exists_g_l_moving_unimodular_pair_to_last_basis --> linear_algebra
  f_link_exactness_stability__exists_g_l_moving_unimodular_pair_to_last_basis --> rings_fields
  f_link_exactness_stability__exists_g_l_split_seq_standard_of_stable_range_le --> f_link_exactness_stability__exists_g_l_moving_unimodular_pair_to_last_basis
  f_link_exactness_stability__exists_g_l_split_seq_standard_of_stable_range_le --> concept_gl_infinity_homology_stability
  f_link_exactness_stability__exists_g_l_split_seq_standard_of_stable_range_le --> concept_group_actions
  f_link_exactness_stability__exists_g_l_split_seq_standard_of_stable_range_le --> linear_algebra
  f_g_l_transitive_split_set_of_stable_range_le --> f_global_twisting__mem_split_seq_iff
  f_g_l_transitive_split_set_of_stable_range_le --> f_tensor_hom_cubes__stab_directed_system
  f_g_l_transitive_split_set_of_stable_range_le --> concept_gl_infinity_homology_stability
  f_g_l_transitive_split_set_of_stable_range_le --> concept_group_actions
  f_g_l_transitive_split_set_of_stable_range_le --> linear_algebra
  f_period_integrals__loc_lat_eq --> number_fields
  f_period_integrals__loc_lat_eq --> concept_dedekind_domains
  f_period_integrals__loc_lat_eq --> concept_ideals_and_discriminant
  f_period_integrals__loc_lat_eq --> p_adic_numbers
  f_period_integrals__loc_lat_eq --> f_cusp_span_norm_bounds__fraction_field_to_generic_stalk_algebra_map_eq
  f_orbital_bounds_conclusion__loc_lat_eq --> f_period_integrals__loc_lat_eq
  f_orbital_bounds_conclusion__loc_lat_eq --> f_local_lattice_equality__development
  f_orbital_bounds_conclusion__loc_lat_eq --> f_avoid_p
  f_orbital_bounds_conclusion__loc_lat_eq --> f_core_fg_of_le
  f_orbital_bounds_conclusion__loc_lat_eq --> f_ep_nontrivial
  f_avoid_p --> f_local_lattice_equality__development
  f_avoid_p --> concept_prime_ideals_localization
  f_avoid_p --> concept_valuation_rings
  f_avoid_p --> concept_ideals_and_discriminant
  f_core_fg_of_le --> f_core_gen_ideal
  f_core_fg_of_le --> f_local_lattice_equality__development
  f_core_fg_of_le --> f_local_lattice_equality__imports
  f_core_fg_of_le --> f_period_integrals__loc_lat_eq
  f_core_fg_of_le --> concept_prime_ideals_localization
  f_core_fg_of_le --> linear_algebra
  f_core_gen_ideal --> f_local_lattice_equality__development
  f_core_gen_ideal --> concept_dedekind_domains
  f_core_gen_ideal --> concept_integral_closure_fraction_fields
  f_core_gen_ideal --> concept_prime_ideals_localization
  f_local_lattice_equality__development --> f_period_integrals__loc_lat_eq
  f_local_lattice_equality__development --> concept_prime_ideals_localization
  f_local_lattice_equality__development --> concept_dedekind_domains
  f_ep_nontrivial --> f_local_lattice_equality__imports
  f_ep_nontrivial --> f_period_integrals__loc_lat_eq
  f_ep_nontrivial --> concept_integral_closure_fraction_fields
  f_ep_nontrivial --> polynomials
  f_ep_nontrivial --> concept_valuation_rings
  f_ep_nontrivial --> number_fields
  f_local_lattice_equality__imports --> f_period_integrals__loc_lat_eq
  f_local_lattice_equality__imports --> number_fields
  f_local_lattice_equality__imports --> concept_integral_closure_fraction_fields
  f_exists_finite_iwahori_double_coset_representatives --> f_ordinary_hecke_characters__iwahori_pro_unipotent_finite_index
  f_exists_finite_iwahori_double_coset_representatives --> f_hecke_algebras__continuous_torus_character
  f_exists_finite_iwahori_double_coset_representatives --> groups
  f_exists_finite_iwahori_double_coset_representatives --> concept_group_actions
  f_exists_finite_iwahori_double_coset_representatives --> concept_normal_subgroups_quotients
  f_exists_finite_iwahori_double_coset_representatives --> counting
  f_desc_st --> concept_tensor_product_of_algebras
  f_desc_st --> concept_galois_fixed_fields
  f_desc_st --> linear_algebra
  f_desc_st --> f_finite_detect_statement
  f_desc_pf --> f_desc_st
  f_desc_pf --> f_finite_detect_statement
  f_desc_pf --> concept_galois_fixed_fields
  f_desc_pf --> concept_tensor_product_of_algebras
  f_desc_pf --> linear_algebra
  f_fin_det_pf --> f_finite_detect_statement
  f_fin_det_pf --> linear_algebra
  f_finite_detect_statement --> concept_tensor_product_of_algebras
  f_finite_detect_statement --> concept_field_extensions_transcendence
  f_finite_detect_statement --> linear_algebra
  f_finite_detect_statement --> concept_galois_fixed_fields
  f_finite_dimensional_base_span --> f_finite_detect_statement
  f_finite_dimensional_base_span --> concept_flat_modules
  f_finite_dimensional_base_span --> concept_tensor_product_of_algebras
  f_finite_dimensional_base_span --> concept_chain_complexes_homology
  f_finite_dimensional_base_span --> linear_algebra
  f_fun_ker_st --> f_finite_detect_statement
  f_fun_ker_st --> f_desc_st
  f_fun_ker_st --> concept_galois_fixed_fields
  f_fun_ker_st --> algebraic_closure
  f_fun_ker_pf --> f_fun_ker_st
  f_fun_ker_pf --> f_rationality_holds
  f_fun_ker_pf --> f_desc_pf
  f_fun_ker_pf --> f_desc_st
  f_fun_ker_pf --> f_finite_dimensional_base_span
  f_fun_ker_pf --> f_finite_detect_statement
  f_fun_ker_pf --> concept_galois_fixed_fields
  f_fun_ker_pf --> concept_field_extensions_transcendence
  f_ker_core_st --> number_fields
  f_ker_core_st --> linear_algebra
  f_ker_core_st --> concept_tensor_product_of_algebras
  f_ker_core_st --> f_finite_detect_statement
  f_ker_core_pf --> f_ker_core_st
  f_ker_core_pf --> f_desc_pf
  f_ker_core_pf --> f_desc_st
  f_ker_core_pf --> f_finite_dimensional_base_span
  f_ker_core_pf --> f_finite_detect_statement
  f_ker_core_pf --> number_fields
  f_ker_core_pf --> concept_galois_fixed_fields
  f_ker_core_pf --> algebraic_closure
  f_rationality_holds --> f_fin_det_pf
  f_rationality_holds --> f_finite_detect_statement
  f_rationality_holds --> f_finite_dimensional_base_span
  f_rationality_holds --> linear_algebra
  f_rationality_holds --> concept_field_extensions_transcendence
  f_commutative_algebra_height__is_local_hom --> concept_adic_completion
  f_commutative_algebra_height__is_local_hom --> concept_local_rings
  f_commutative_algebra_height__is_local_hom --> concept_prime_ideals_localization
  f_commutative_algebra_height__is_local_hom --> concept_coordinate_rings_dimension
  f_commutative_algebra_height__is_local_hom --> f_commutative_algebra__res_map_bijective
  f_commutative_algebra_height__cpl_is --> f_commutative_algebra_height__is_local_hom
  f_commutative_algebra_height__cpl_is --> f_iwasawa_decomposition__is_noetherian_ring_adic_completion_of_noetherian
  f_commutative_algebra_height__cpl_is --> concept_adic_completion
  f_commutative_algebra_height__cpl_is --> concept_prime_ideals_localization
  f_commutative_algebra_height__cpl_is --> concept_local_rings
  f_commutative_algebra_height__cpl_uniq --> f_commutative_algebra_height__cpl_is
  f_commutative_algebra_height__cpl_uniq --> f_commutative_algebra_height__is_local_hom
  f_commutative_algebra_height__cpl_uniq --> f_capelli_identities__level_of_congruence
  f_commutative_algebra_height__cpl_uniq --> concept_adic_completion
  f_commutative_algebra_height__cpl_uniq --> concept_local_rings
  f_commutative_algebra_height__highest_weight_space_finite --> f_commutative_algebra_height__cpl_uniq
  f_commutative_algebra_height__highest_weight_space_finite --> f_commutative_algebra_height__is_local_hom
  f_commutative_algebra_height__highest_weight_space_finite --> concept_flat_modules
  f_commutative_algebra_height__highest_weight_space_finite --> concept_prime_ideals_localization
  f_commutative_algebra_height__highest_weight_space_finite --> concept_coordinate_rings_dimension
  f_capelli_identities__level_of_congruence --> f_commutative_algebra_height__is_local_hom
  f_capelli_identities__level_of_congruence --> concept_adic_completion
  f_capelli_identities__level_of_congruence --> concept_prime_ideals_localization
  f_capelli_identities__level_of_congruence --> rings_fields
  f_saturated_chains__is_saturated_chain --> concept_coordinate_rings_dimension
  f_saturated_chains__is_saturated_chain --> concept_prime_ideals_localization
  f_saturated_chains__is_saturated_chain --> concept_local_rings
  f_saturated_chains__is_saturated_chain --> f_commutative_algebra__chain_conn_in_dim
  f_covolume_bounds__differentiable_on_of_tendsto_locally_uniformly_on --> complex_analysis
  f_covolume_bounds__differentiable_on_of_tendsto_locally_uniformly_on --> real_analysis
  f_covolume_bounds__differentiable_on_of_tendsto_locally_uniformly_on --> infinite_series
  f_covolume_bounds__differentiable_on_of_tendsto_locally_uniformly_on --> calculus
  f_analytic_doubling_map_local_inverse --> complex_analysis
  f_analytic_doubling_map_local_inverse --> calculus
  f_analytic_doubling_map_local_inverse --> linear_algebra
  f_analytic_group_law_bounded_commutator --> complex_analysis
  f_analytic_group_law_bounded_commutator --> real_analysis
  f_doubling_limit_local_logarithm --> f_iter_differentiable_on
  f_doubling_limit_local_logarithm --> infinite_series
  f_doubling_limit_local_logarithm --> real_analysis
  f_iter_differentiable_on --> complex_analysis
  f_iter_differentiable_on --> real_analysis
  f_iter_differentiable_on --> concept_point_set_topology
  f_local_logarithm_homomorphism --> f_iter_differentiable_on
  f_local_logarithm_homomorphism --> real_analysis
  f_local_logarithm_homomorphism --> infinite_series
  f_riemann_form_period_determinant --> f_analytic_group_law_bounded_commutator
  f_riemann_form_period_determinant --> f_analytic_doubling_map_local_inverse
  f_riemann_form_period_determinant --> f_doubling_limit_local_logarithm
  f_riemann_form_period_determinant --> f_local_logarithm_homomorphism
  f_riemann_form_period_determinant --> f_iter_differentiable_on
  f_riemann_form_period_determinant --> f_covolume_bounds__differentiable_on_of_tendsto_locally_uniformly_on
  f_riemann_form_period_determinant --> complex_analysis
  f_riemann_form_period_determinant --> concept_complex_analytic_sets
  f_harish_chandra_induction_g_l_is_character --> f_divisor_proofs__exists_block_parabolic_subgroup_levi_projection
  f_harish_chandra_induction_g_l_is_character --> f_is_character_over_subfield_induced_class_function
  f_harish_chandra_induction_g_l_is_character --> f_induced_class_function_from_subgroup_eq_finsum_cosets
  f_harish_chandra_induction_g_l_is_character --> f_ab_by_p_of_comm
  f_harish_chandra_induction_g_l_is_character --> concept_group_representations
  f_harish_chandra_induction_g_l_is_character --> concept_normal_subgroups_quotients
  f_hermite_normal_forms__smul_strict_mono --> number_fields
  f_hermite_normal_forms__smul_strict_mono --> concept_hermitian_unitary_matrices
  f_hermite_normal_forms__smul_strict_mono --> concept_group_actions
  f_hermite_normal_forms__smul_strict_mono --> concept_chain_complexes_homology
  f_hermite_normal_forms__smul_strict_mono --> concept_lattice_point_counting
  f_hermite_normal_forms__smul_strict_mono --> concept_gl_infinity_homology_stability
  f_hermite_normal_forms__smul_strict_mono --> linear_algebra
  f_reduction_bounds_torsion__act_l_pos --> f_hermite_normal_forms__smul_strict_mono
  f_reduction_bounds_torsion__act_l_pos --> concept_group_homology
  f_reduction_bounds_torsion__act_l_pos --> concept_haar_measure_fundamental_domain
  f_reduction_bounds_torsion__act_l_pos --> concept_hermitian_unitary_matrices
  f_rank_span_le --> concept_flat_modules
  f_rank_span_le --> concept_finitely_generated_abelian_groups
  f_rank_span_le --> linear_algebra
  f_s_b_star_odd_of --> f_rank_span_le
  f_s_b_star_odd_of --> f_reduction_bounds_torsion__s_b_star_odd
  f_s_b_star_odd_of --> f_reduction_bounds_torsion__s_bridge_alt
  f_s_b_star_odd_of --> f_reduction_bounds_torsion__s_b_star
  f_s_b_star_odd_of --> f_s_b_star_of
  f_s_b_star_odd_of --> f_is_prim_cmap
  f_s_b_star_odd_of --> f_reduction_bounds_torsion__act_l_pos
  f_s_b_star_odd_of --> number_fields
  f_is_prim_cmap --> f_reduction_bounds_torsion__s_bridge_alt
  f_is_prim_cmap --> f_reduction_bounds_torsion__act_l_pos
  f_is_prim_cmap --> concept_chain_complexes_homology
  f_res_ring --> rings_fields
  f_res_ring --> linear_algebra
  f_res_ring --> concept_tensor_product_of_algebras
  f_reduction_bounds_torsion__s_b_star --> f_reduction_bounds_torsion__act_l_pos
  f_reduction_bounds_torsion__s_b_star --> f_reduction_bounds_torsion__s_bridge_alt
  f_reduction_bounds_torsion__s_b_star --> f_hermite_normal_forms__smul_strict_mono
  f_reduction_bounds_torsion__s_b_star --> concept_group_homology
  f_reduction_bounds_torsion__s_b_star --> number_fields
  f_reduction_bounds_torsion__s_b_star_odd --> f_reduction_bounds_torsion__s_b_star
  f_reduction_bounds_torsion__s_b_star_odd --> f_reduction_bounds_torsion__s_bridge_alt
  f_reduction_bounds_torsion__s_b_star_odd --> number_fields
  f_reduction_bounds_torsion__s_bridge_alt --> f_reduction_bounds_torsion__act_l_pos
  f_reduction_bounds_torsion__s_bridge_alt --> f_hermite_normal_forms__smul_strict_mono
  f_reduction_bounds_torsion__s_bridge_alt --> f_tensor_hom_cubes__stab_directed_system
  f_reduction_bounds_torsion__s_bridge_alt --> concept_group_homology
  f_reduction_bounds_torsion__s_bridge_alt --> concept_hecke_operators
  f_reduction_bounds_torsion__s_bridge_alt --> concept_haar_measure_fundamental_domain
  f_reduction_bounds_torsion__s_bridge_alt --> concept_gl_infinity_homology_stability
  f_exists_nsmul_eq_zero_of_tmul --> concept_flat_modules
  f_exists_nsmul_eq_zero_of_tmul --> concept_finitely_generated_abelian_groups
  f_s_b_star_of --> f_is_prim_cmap
  f_s_b_star_of --> f_reduction_bounds_torsion__s_bridge_alt
  f_s_b_star_of --> f_reduction_bounds_torsion__s_b_star
  f_s_b_star_of --> f_reduction_bounds_torsion__act_l_pos
  f_s_b_star_of --> f_tensor_hom_cubes__stab_directed_system
  f_s_b_star_of --> concept_group_homology
  f_inertia_ramification__average --> f_inertia_ramification__log_root_disc_char
  f_inertia_ramification__average --> f_inertia_ramification__conductor_local_part_dvd_iff
  f_inertia_ramification__average --> dirichlet_characters
  f_inertia_ramification__average --> primitive_characters
  f_inertia_ramification__average --> primes_divisibility
  f_inertia_ramification__cond_dvd --> f_inertia_ramification__is_imag_quad
  f_inertia_ramification__cond_dvd --> f_inertia_ramification__log_root_disc_char
  f_inertia_ramification__cond_dvd --> dirichlet_characters
  f_inertia_ramification__cond_dvd --> primitive_characters
  f_inertia_ramification__cond_dvd --> concept_normal_subgroups_quotients
  f_inertia_ramification__cond_dvd --> modular_arithmetic
  f_conductor_dvd_field_conductor_of_mem --> f_exists_host_data_wild
  f_conductor_dvd_field_conductor_of_mem --> f_inertia_ramification__cond_dvd
  f_conductor_dvd_field_conductor_of_mem --> f_inertia_ramification__two_power
  f_conductor_dvd_field_conductor_of_mem --> f_inertia_ramification__is_imag_quad
  f_conductor_dvd_field_conductor_of_mem --> f_inertia_ramification__log_root_disc_char
  f_conductor_dvd_field_conductor_of_mem --> dirichlet_characters
  f_conductor_dvd_field_conductor_of_mem --> concept_normal_subgroups_quotients
  f_inertia_ramification__conductor_local_part_dvd_iff --> f_inertia_ramification__log_root_disc_char
  f_inertia_ramification__conductor_local_part_dvd_iff --> dirichlet_characters
  f_inertia_ramification__conductor_local_part_dvd_iff --> primitive_characters
  f_inertia_ramification__conductor_local_part_dvd_iff --> modular_arithmetic
  f_inertia_ramification__conductor_local_part_dvd_iff --> primes_divisibility
  f_inertia_ramification__duality --> f_inertia_ramification__conductor_local_part_dvd_iff
  f_inertia_ramification__duality --> f_inertia_ramification__log_root_disc_char
  f_inertia_ramification__duality --> dirichlet_characters
  f_inertia_ramification__duality --> groups
  f_inertia_ramification__duality --> concept_group_representations
  f_exists_host_data_wild --> f_inertia_ramification__is_imag_quad
  f_exists_host_data_wild --> f_inertia_ramification__log_root_disc_char
  f_exists_host_data_wild --> f_inertia_ramification__cond_dvd
  f_exists_host_data_wild --> dirichlet_characters
  f_inertia_ramification__host_degree --> f_inertia_ramification__is_imag_quad
  f_inertia_ramification__host_degree --> f_inertia_ramification__cond_dvd
  f_inertia_ramification__host_degree --> f_inertia_ramification__two_power
  f_inertia_ramification__host_degree --> f_inertia_ramification__log_root_disc_char
  f_inertia_ramification__host_degree --> dirichlet_characters
  f_inertia_ramification__host_degree --> concept_normal_subgroups_quotients
  f_inertia_ramification__is_imag_quad --> f_inertia_ramification__log_root_disc_char
  f_inertia_ramification__is_imag_quad --> dirichlet_characters
  f_inertia_ramification__is_imag_quad --> primitive_characters
  f_inertia_ramification__is_imag_quad --> concept_normal_subgroups_quotients
  f_inertia_ramification__is_imag_quad --> modular_arithmetic
  f_inertia_ramification__log_root_disc_char --> dirichlet_characters
  f_inertia_ramification__log_root_disc_char --> primitive_characters
  f_inertia_ramification__log_root_disc_char --> modular_arithmetic
  f_inertia_ramification__log_root_disc_char --> number_fields
  f_inertia_ramification__log_root_disc_char --> concept_normal_subgroups_quotients
  f_inertia_ramification__quadratic_character_legendre_symbol --> f_inertia_ramification__is_imag_quad
  f_inertia_ramification__quadratic_character_legendre_symbol --> f_inertia_ramification__log_root_disc_char
  f_inertia_ramification__quadratic_character_legendre_symbol --> dirichlet_characters
  f_inertia_ramification__quadratic_character_legendre_symbol --> primitive_characters
  f_inertia_ramification__quadratic_character_legendre_symbol --> modular_arithmetic
  f_inertia_ramification__quadratic_character_legendre_symbol --> primes_divisibility
  f_inertia_ramification__two_power --> f_inertia_ramification__cond_dvd
  f_inertia_ramification__two_power --> f_inertia_ramification__duality
  f_inertia_ramification__two_power --> f_inertia_ramification__conductor_local_part_dvd_iff
  f_inertia_ramification__two_power --> f_inertia_ramification__log_root_disc_char
  f_inertia_ramification__two_power --> f_inertia_ramification__is_imag_quad
  f_inertia_ramification__two_power --> dirichlet_characters
  f_inertia_ramification__two_power --> primitive_characters
  f_exists_local_zero_expansion_of_bound --> f_zero_factor
  f_exists_local_zero_expansion_of_bound --> f_log_deriv_bound
  f_exists_local_zero_expansion_of_bound --> f_landau_local_of
  f_exists_local_zero_expansion_of_bound --> complex_analysis
  f_exists_local_zero_expansion_of_bound --> real_analysis
  f_local_zero_expansion_with_multiplicity --> f_exists_local_zero_expansion_of_bound
  f_local_zero_expansion_with_multiplicity --> f_landau_zero_free_bounds__no_zero_complex_of
  f_local_zero_expansion_with_multiplicity --> complex_analysis
  f_landau_local_of --> f_zero_free_region__small_height_log_deriv
  f_landau_local_of --> complex_analysis
  f_landau_local_of --> calculus
  f_log_deriv_bound --> complex_analysis
  f_log_deriv_bound --> complex_numbers
  f_log_deriv_bound --> calculus
  f_log_deriv_bound --> f_zero_free_region__small_height_log_deriv
  f_zero_factor --> complex_analysis
  f_zero_factor --> concept_point_set_topology
  f_zero_factor --> polynomials
  f_coefficient_bound_membership --> f_gauss_jet_bounds__statement_h
  f_coefficient_bound_membership --> f_gauss_jet_bounds__statement_c
  f_coefficient_bound_membership --> f_gauss_jet_bounds__statement_g
  f_coefficient_bound_membership --> f_incoming_bounds__incoming_bound
  f_coefficient_bound_membership --> polynomials
  f_coefficient_bound_membership --> linear_algebra
  f_orbital_bounds_conclusion__phi_cube_of_factor --> f_period_integrals__phi_cube_of_factor
  f_orbital_bounds_conclusion__phi_cube_of_factor --> f_exp_mv_eq
  f_orbital_bounds_conclusion__phi_cube_of_factor --> p_adic_numbers
  f_period_integrals__phi_cube_of_factor --> p_adic_numbers
  f_period_integrals__phi_cube_of_factor --> polynomials
  f_period_integrals__phi_cube_of_factor --> infinite_series
  f_period_integrals__phi_cube_of_factor --> concept_ultrametric_norm
  f_exp_mv_eq --> f_period_integrals__phi_cube_of_factor
  f_exp_mv_eq --> f_formal_group_common__coeff_single_lg
  f_exp_mv_eq --> f_formal_group_common__exp_log
  f_exp_mv_eq --> f_period_integrals__fgl_ph_split
  f_exp_mv_eq --> f_formal_group_splitting__add_preserves_exp_congruence
  f_exp_mv_eq --> polynomials
  f_formal_group_common__coeff_single_lg --> polynomials
  f_formal_group_common__coeff_single_lg --> p_adic_numbers
  f_formal_group_common__coeff_single_lg --> f_formal_group_common__exp_log
  f_formal_group_common__exp_log --> f_period_integrals__fgl_ph_split
  f_formal_group_common__exp_log --> f_formal_group_splitting__add_preserves_exp_congruence
  f_formal_group_common__exp_log --> f_formal_group_splitting__orthogonal_split_polarization_vanishes
  f_formal_group_common__exp_log --> calculus
  f_formal_group_common__exp_log --> infinite_series
  f_formal_group_common__exp_log --> concept_ultrametric_norm
  f_formal_group_common__exp_log --> p_adic_numbers
  f_divisor_proofs__exists_filtered_colimit_finite_type_int_rings --> concept_filtered_colimits
  f_divisor_proofs__exists_filtered_colimit_finite_type_int_rings --> concept_finitely_generated_algebras
  f_divisor_proofs__exists_filtered_colimit_finite_type_int_rings --> rings_fields
  f_locally_surjective_of_iso_on_finite_type_approximation --> f_divisor_proofs__exists_filtered_colimit_finite_type_int_rings
  f_locally_surjective_of_iso_on_finite_type_approximation --> f_divisor_proofs__preserves_filtered_colimits_add_comm_grp_iff_elements
  f_locally_surjective_of_iso_on_finite_type_approximation --> concept_filtered_colimits
  f_locally_surjective_of_iso_on_finite_type_approximation --> concept_etale_ring_maps
  f_locally_surjective_of_iso_on_finite_type_approximation --> concept_flat_modules
  f_locally_surjective_of_iso_on_finite_type_approximation --> concept_chain_complexes_homology
  f_p_normal_germ_integrally_closed --> f_complex_analytic_sets__st_normal_germ_integrally_closed
  f_p_normal_germ_integrally_closed --> f_st_rueckert_nullstellensatz
  f_p_normal_germ_integrally_closed --> f_complex_analytic_sets__st_zariski_analytic_normality
  f_p_normal_germ_integrally_closed --> f_complex_analytic_sets__st_normal_model
  f_p_normal_germ_integrally_closed --> f_complex_analytic_sets__osgood_separate
  f_p_normal_germ_integrally_closed --> concept_complex_analytic_sets
  f_p_normal_germ_integrally_closed --> concept_integral_closure_fraction_fields
  f_p_normal_germ_integrally_closed --> concept_prime_ideals_localization
  f_p_normal_germ_integrally_closed --> complex_analysis
  f_complex_analytic_sets__st_normal_germ_integrally_closed --> concept_complex_analytic_sets
  f_complex_analytic_sets__st_normal_germ_integrally_closed --> concept_integral_closure_fraction_fields
  f_complex_analytic_sets__st_normal_germ_integrally_closed --> concept_prime_ideals_localization
  f_complex_analytic_sets__st_normal_germ_integrally_closed --> f_complex_analytic_sets__st_normal_model
  f_st_rueckert_nullstellensatz --> concept_complex_analytic_sets
  f_st_rueckert_nullstellensatz --> concept_finitely_generated_algebras
  f_st_rueckert_nullstellensatz --> complex_analysis
  f_exists_form_defining_value --> f_exists_form_with_valuation
  f_exists_form_defining_value --> polynomials
  f_exists_form_defining_value --> rings_fields
  f_exists_form_with_valuation --> f_rational_sup_metrics__aeval_coord_prod
  f_exists_form_with_valuation --> f_metric_periods__has_multiplier
  f_exists_form_with_valuation --> polynomials
  f_exists_form_with_valuation --> rings_fields
  f_exists_adic_limit_mem_automorphic_space --> concept_adic_completion
  f_exists_adic_limit_mem_automorphic_space --> concept_local_rings
  f_exists_adic_limit_mem_automorphic_space --> concept_group_actions
  f_exists_adic_limit_mem_automorphic_space --> f_capelli_identities__fixed_subgroup
  f_u_operator_pow_eventually_invariant_mod_pow --> f_ordinary_hecke_characters__u_op_level
  f_u_operator_pow_eventually_invariant_mod_pow --> f_ordinary_hecke_characters__u_op_mul
  f_u_operator_pow_eventually_invariant_mod_pow --> f_ordinary_hecke_characters__u_op_nat
  f_u_operator_pow_eventually_invariant_mod_pow --> f_hecke_algebras__continuous_torus_character
  f_u_operator_pow_eventually_invariant_mod_pow --> f_capelli_identities__fixed_subgroup
  f_u_operator_pow_eventually_invariant_mod_pow --> concept_hecke_operators
  f_u_operator_pow_eventually_invariant_mod_pow --> concept_adic_completion
  f_u_operator_pow_eventually_invariant_mod_pow --> concept_local_rings
  f_approximation_of_square_identity --> f_discrete_series__is_inf_unitary
  f_approximation_of_square_identity --> f_discrete_series__defs_rep
  f_approximation_of_square_identity --> f_harish_chandra_descent__descent
  f_approximation_of_square_identity --> f_bochner_inequality__k_unit_b
  f_approximation_of_square_identity --> concept_highest_weight_casimir
  f_approximation_of_square_identity --> concept_hermitian_unitary_matrices
  f_approximation_of_square_identity --> linear_algebra
  f_toroidal_compactification__push_invertible --> f_toroidal_compactification__is_completed_strict_hens
  f_toroidal_compactification__push_invertible --> f_toroidal_compactification__is_grp_pullback
  f_toroidal_compactification__push_invertible --> f_toroidal_compactification__two_weight_eq_one_add_root
  f_toroidal_compactification__push_invertible --> concept_schemes_basics
  f_toroidal_compactification__push_invertible --> concept_group_schemes
  f_toroidal_compactification__push_invertible --> concept_dual_numbers
  f_toroidal_compactification__push_invertible --> concept_categorical_pullbacks
  f_toroidal_compactification__push_invertible --> concept_roots_of_unity_kummer
  f_dominates_lift_unique --> f_toroidal_compactification__push_invertible
  f_dominates_lift_unique --> concept_categorical_pullbacks
  f_dominates_lift_unique --> concept_schemes_basics
  f_join_col --> complex_numbers
  f_join_col --> linear_algebra
  f_join_col --> counting
  f_gaussian_det_square_integral --> f_join_col
  f_gaussian_det_square_integral --> complex_numbers
  f_gaussian_det_square_integral --> linear_algebra
  f_gaussian_det_square_integral --> calculus
  f_gaussian_det_square_integral --> concept_haar_measure_fundamental_domain
  f_gaussian_det_levi_integral --> f_gaussian_det_square_integral
  f_gaussian_det_levi_integral --> f_join_col
  f_gaussian_det_levi_integral --> linear_algebra
  f_gaussian_det_levi_integral --> concept_haar_measure_fundamental_domain
  f_complex_analytic_sets__st_area_multiplicity --> concept_complex_analytic_sets
  f_complex_analytic_sets__st_area_multiplicity --> concept_haar_measure_fundamental_domain
  f_complex_analytic_sets__st_area_multiplicity --> linear_algebra
  f_complex_analytic_sets__st_area_multiplicity --> calculus
  f_p_area_multiplicity --> f_complex_analytic_sets__st_area_multiplicity
  f_p_area_multiplicity --> concept_haar_measure_fundamental_domain
  f_p_area_multiplicity --> linear_algebra
  f_p_area_multiplicity --> calculus
  f_statements_area_multiplicity_weight --> concept_haar_measure_fundamental_domain
  f_statements_area_multiplicity_weight --> linear_algebra
  f_statements_area_multiplicity_weight --> calculus
  f_p_area_multiplicity_weight --> f_statements_area_multiplicity_weight
  f_p_area_multiplicity_weight --> f_p_area_multiplicity
  f_p_area_multiplicity_weight --> concept_haar_measure_fundamental_domain
  f_p_area_multiplicity_weight --> linear_algebra
  f_p_area_multiplicity_weight --> calculus
  f_foundation_proofs__two_var_poly_subst_matrix_basic_laws --> f_foundations__op_l_d_one_sub_mem_triv
  f_foundation_proofs__two_var_poly_subst_matrix_basic_laws --> polynomials
  f_foundation_proofs__two_var_poly_subst_matrix_basic_laws --> linear_algebra
  f_foundation_proofs__two_var_poly_subst_matrix_basic_laws --> rings_fields
  f_cocycle_is_coboundary_of_neg_central_element --> f_foundations__is_root_one
  f_cocycle_is_coboundary_of_neg_central_element --> concept_group_homology
  f_cocycle_is_coboundary_of_neg_central_element --> concept_group_actions
  f_cocycle_is_coboundary_of_neg_central_element --> groups
  f_foundation_proofs__exists_scalar_gamma1_cap_gamma0_mod_level --> concept_modular_forms
  f_foundation_proofs__exists_scalar_gamma1_cap_gamma0_mod_level --> modular_arithmetic
  f_foundation_proofs__exists_scalar_gamma1_cap_gamma0_mod_level --> primes_divisibility
  f_foundation_proofs__exists_scalar_gamma1_cap_gamma0_mod_level --> linear_algebra
  f_homogeneous_poly_cocycle_diff_coboundary_of_eq_on --> f_cocycle_is_coboundary_of_neg_central_element
  f_homogeneous_poly_cocycle_diff_coboundary_of_eq_on --> f_foundation_proofs__exists_scalar_gamma1_cap_gamma0_mod_level
  f_homogeneous_poly_cocycle_diff_coboundary_of_eq_on --> f_foundation_proofs__two_var_poly_subst_matrix_basic_laws
  f_homogeneous_poly_cocycle_diff_coboundary_of_eq_on --> f_foundations__is_root_one
  f_homogeneous_poly_cocycle_diff_coboundary_of_eq_on --> f_foundations__op_l_d_one_sub_mem_triv
  f_homogeneous_poly_cocycle_diff_coboundary_of_eq_on --> concept_group_homology
  f_homogeneous_poly_cocycle_diff_coboundary_of_eq_on --> concept_modular_forms
  f_height_one_prime_dvr_stalk --> f_global_geometry__is_cpt_gen
  f_height_one_prime_dvr_stalk --> f_global_geometry__coords_at
  f_height_one_prime_dvr_stalk --> f_global_geometry__etale_localization_at_prime_tensor_of_low_height
  f_height_one_prime_dvr_stalk --> f_geometry_proofs__spec_stalk_specializes_comp
  f_height_one_prime_dvr_stalk --> concept_discrete_valuation_ring
  f_height_one_prime_dvr_stalk --> concept_schemes_basics
  f_height_one_prime_dvr_stalk --> concept_local_rings
  f_height_one_prime_dvr_stalk --> concept_prime_ideals_localization
  f_height_one_prime_dvr_stalk --> concept_integral_closure_fraction_fields
  f_g_field --> f_gauss_jet_bounds__statement_m
  f_g_field --> concept_ultrametric_norm
  f_g_field --> p_adic_numbers
  f_g_field --> polynomials
  f_g_field --> rings_fields
  f_g_field --> concept_integral_closure_fraction_fields
  f_k_irreducible_existence_holds --> f_harish_chandra_descent__descent
  f_k_irreducible_existence_holds --> f_bochner_inequality__is_k_unitary_of_is_inf_unitary
  f_k_irreducible_existence_holds --> f_discrete_series__is_inf_unitary
  f_k_irreducible_existence_holds --> f_discrete_series__defs_rep
  f_k_irreducible_existence_holds --> concept_highest_weight_casimir
  f_k_irreducible_existence_holds --> concept_hermitian_unitary_matrices
  f_k_irreducible_existence_holds --> linear_algebra
  f_root_bound_of_square_identity --> f_harish_chandra_descent__descent
  f_root_bound_of_square_identity --> f_casimir_algebra__casimir_k_khw_vec
  f_root_bound_of_square_identity --> f_casimir_algebra__mul_mul_sub_mul_mul_eq_add
  f_root_bound_of_square_identity --> f_discrete_series__is_inf_unitary
  f_root_bound_of_square_identity --> f_discrete_series__defs_rep
  f_root_bound_of_square_identity --> f_bochner_inequality__cas_val_k
  f_root_bound_of_square_identity --> concept_highest_weight_casimir
  f_root_bound_of_square_identity --> concept_hermitian_unitary_matrices
  f_behrend_sets__statement --> modular_arithmetic
  f_behrend_sets__statement --> groups
  f_behrend_sets__statement --> counting
  f_behrend_sets__statement --> concept_normal_subgroups_quotients
  f_behrend_sets__statement --> primes_divisibility
  f_behrend_sets__statement_e --> f_behrend_sets__statement
  f_behrend_sets__statement_e --> modular_arithmetic
  f_behrend_sets__statement_e --> groups
  f_behrend_sets__statement_e --> number_fields
  f_behrend_sets__statement_e --> concept_group_actions
  f_behrend_sets__statement_e --> infinite_series
  f_coeff_pow_eq_zero_of_lt --> f_behrend_sets__statement_e
  f_coeff_pow_eq_zero_of_lt --> infinite_series
  f_coeff_pow_eq_zero_of_lt --> polynomials
  f_coeff_pow_eq_zero_of_lt --> rings_fields
  f_mem_window_iff --> f_behrend_sets__statement
  f_mem_window_iff --> modular_arithmetic
  f_mul_abs_sub_lt --> f_behrend_sets__statement
  f_mul_abs_sub_lt --> modular_arithmetic
  f_prob_eq_sum_ite --> f_behrend_sets__statement
  f_prob_eq_sum_ite --> counting
  f_prob_eq_sum_ite --> polynomials
  f_prod_dim_v_ne_zero --> counting
  f_prod_dim_v_ne_zero --> calculus
  f_select --> f_behrend_sets__statement
  f_select --> counting
  f_select --> calculus
  f_space_free_of_behrend_free --> f_mul_abs_sub_lt
  f_space_free_of_behrend_free --> f_behrend_sets__statement_e
  f_space_free_of_behrend_free --> f_behrend_sets__statement
  f_space_free_of_behrend_free --> modular_arithmetic
  f_space_free_of_behrend_free --> groups
  f_totient_le_of_is_primitive_root --> f_behrend_sets__statement_e
  f_totient_le_of_is_primitive_root --> concept_roots_of_unity_kummer
  f_totient_le_of_is_primitive_root --> concept_field_extensions_transcendence
  f_totient_le_of_is_primitive_root --> number_fields
  f_totient_le_of_is_primitive_root --> linear_algebra
  f_totient_le_of_is_primitive_root --> polynomials
  f_totient_le_of_is_primitive_root --> groups
  f_totient_le_of_is_primitive_root --> concept_sylow_theorems
  f_two_le_cast_of_two_le --> f_behrend_sets__statement
  f_two_le_cast_of_two_le --> calculus
  f_two_pow_dvd_pow_two_pow_sub_one --> f_behrend_sets__statement
  f_two_pow_dvd_pow_two_pow_sub_one --> modular_arithmetic
  f_two_pow_dvd_pow_two_pow_sub_one --> primes_divisibility
  f_two_pow_dvd_pow_two_pow_sub_one --> groups
  f_final_e --> f_totient_le_of_is_primitive_root
  f_final_e --> f_behrend_sets__statement_e
  f_exists_regular_local_extension_with_simple_root --> f_regular_smooth
  f_exists_regular_local_extension_with_simple_root --> f_precomplete_bases__is_precomplete_of_basis
  f_exists_regular_local_extension_with_simple_root --> concept_regular_local_rings
  f_exists_regular_local_extension_with_simple_root --> concept_local_rings
  f_exists_regular_local_extension_with_simple_root --> concept_adic_completion
  f_exists_regular_local_extension_with_simple_root --> concept_flat_modules
  f_exists_regular_local_extension_with_simple_root --> concept_separable_polynomials
  f_exists_regular_local_extension_with_simple_root --> concept_hensel_lifting
  f_exists_regular_local_extension_with_simple_root --> polynomials
  f_regular_smooth --> f_scheme_cohomology__regular_local_domain
  f_regular_smooth --> concept_regular_local_rings
  f_regular_smooth --> concept_smooth_morphisms
  f_regular_smooth --> concept_etale_ring_maps
  f_regular_smooth --> concept_flat_modules
  f_regular_smooth --> concept_prime_ideals_localization
  f_regular_smooth --> concept_schemes_basics
  f_generic_fiber_gluing__plus_condition_to_zero_condition --> f_generic_fiber_gluing__semistable_reduction_plus_split
  f_generic_fiber_gluing__plus_condition_to_zero_condition --> f_abelian_scheme_quotients__is_abelian_scheme
  f_generic_fiber_gluing__plus_condition_to_zero_condition --> concept_group_schemes
  f_generic_fiber_gluing__plus_condition_to_zero_condition --> concept_discrete_valuation_ring
  f_generic_fiber_gluing__plus_condition_to_zero_condition --> concept_adic_completion
  f_generic_fiber_gluing__semistable_complete_split --> f_generic_fiber_gluing__semistable_reduction_plus_split
  f_generic_fiber_gluing__semistable_complete_split --> f_generic_fiber_gluing__plus_condition_to_zero_condition
  f_generic_fiber_gluing__semistable_complete_split --> f_split_tori__is_torus
  f_generic_fiber_gluing__semistable_complete_split --> f_split_tori__split_torus_aff
  f_generic_fiber_gluing__semistable_complete_split --> f_abelian_scheme_quotients__is_abelian_scheme
  f_generic_fiber_gluing__semistable_complete_split --> concept_group_schemes
  f_generic_fiber_gluing__semistable_complete_split --> concept_discrete_valuation_ring
  f_generic_fiber_gluing__semistable_reduction_plus_split --> f_abelian_scheme_quotients__is_abelian_scheme
  f_generic_fiber_gluing__semistable_reduction_plus_split --> f_split_tori__is_torus
  f_generic_fiber_gluing__semistable_reduction_plus_split --> concept_group_schemes
  f_generic_fiber_gluing__semistable_reduction_plus_split --> concept_categorical_pullbacks
  f_generic_fiber_gluing__semistable_reduction_plus_split --> concept_discrete_valuation_ring
  f_generic_fiber_gluing__semistable_reduction_plus_split --> concept_adic_completion
  f_generic_fiber_gluing__semistable_reduction_plus_split --> concept_local_rings
  f_precomplete_bases__is_precomplete_of_basis --> f_generic_fiber_gluing__semistable_complete_split
  f_precomplete_bases__is_precomplete_of_basis --> concept_discrete_valuation_ring
  f_precomplete_bases__is_precomplete_of_basis --> concept_adic_completion
  f_precomplete_bases__is_precomplete_of_basis --> concept_local_rings
  f_precomplete_bases__is_precomplete_of_basis --> concept_field_extensions_transcendence
  f_precomplete_bases__is_precomplete_of_basis --> concept_hensel_lifting
  f_precomplete_bases__is_precomplete_of_basis --> polynomials
  f_precomplete_bases__is_precomplete_of_basis --> linear_algebra
  f_split_tori__is_torus --> f_split_tori__split_torus_aff
  f_split_tori__is_torus --> concept_group_schemes
  f_split_tori__is_torus --> concept_categorical_pullbacks
  f_split_tori__is_torus --> concept_finitely_generated_abelian_groups
  f_split_tori__is_torus --> concept_schemes_basics
  f_range_j_subset_ab_locus --> f_toroidal_compactification__push_invertible
  f_range_j_subset_ab_locus --> f_toroidal_compactification__is_completed_strict_hens
  f_range_j_subset_ab_locus --> f_toroidal_compactification__two_weight_eq_one_add_root
  f_range_j_subset_ab_locus --> concept_group_schemes
  f_range_j_subset_ab_locus --> concept_schemes_basics
  f_range_j_subset_ab_locus --> concept_categorical_pullbacks
  f_cone_b_defs --> fourier_analysis
  f_cone_b_defs --> complex_numbers
  f_cone_b_defs --> complex_analysis
  f_cone_b_defs --> real_analysis
  f_cone_b_defs --> concept_point_set_topology
  f_gaussian_fourier_conj_power --> fourier_analysis
  f_gaussian_fourier_conj_power --> complex_numbers
  f_gaussian_fourier_conj_power --> calculus
  f_gaussian_fourier_conj_power --> concept_schwartz_functions
  f_gaussian_fourier_conj_power --> proofs
  f_schwartz_fourier_preimage --> f_cone_b_defs
  f_schwartz_fourier_preimage --> concept_schwartz_functions
  f_schwartz_fourier_preimage --> fourier_analysis
  f_schwartz_fourier_preimage --> concept_haar_measure_fundamental_domain
  f_schwartz_fourier_preimage --> linear_algebra
  f_fourier_nonvanishing_unit_point --> f_cone_b_defs
  f_fourier_nonvanishing_unit_point --> fourier_analysis
  f_fourier_nonvanishing_unit_point --> concept_point_set_topology
  f_fourier_nonvanishing_unit_point --> concept_haar_measure_fundamental_domain
  f_fourier_weight_integral_symmetry --> f_cone_b_defs
  f_fourier_weight_integral_symmetry --> fourier_analysis
  f_fourier_weight_integral_symmetry --> real_analysis
  f_fourier_weight_integral_symmetry --> linear_algebra
  f_exists_test_fourier_nonvanishing --> f_gaussian_fourier_conj_power
  f_exists_test_fourier_nonvanishing --> f_cone_b_defs
  f_exists_test_fourier_nonvanishing --> fourier_analysis
  f_exists_test_fourier_nonvanishing --> gamma_function
  f_exists_test_fourier_nonvanishing --> concept_schwartz_functions
  f_fourier_continuous_nonvanishing --> f_cone_b_defs
  f_fourier_continuous_nonvanishing --> concept_point_set_topology
  f_fourier_continuous_nonvanishing --> real_analysis
  f_fourier_continuous_nonvanishing --> fourier_analysis
  f_fourier_continuous_nonvanishing --> calculus
  f_convolution_decay_integrable_fourier --> f_cone_b_defs
  f_convolution_decay_integrable_fourier --> fourier_analysis
  f_convolution_decay_integrable_fourier --> real_analysis
  f_convolution_decay_integrable_fourier --> linear_algebra
  f_convolution_family_integrable --> f_cone_b_defs
  f_convolution_family_integrable --> real_analysis
  f_convolution_family_integrable --> fourier_analysis
  f_convolution_family_integrable --> concept_point_set_topology
  f_exists_convolution_nonvanishing_weight --> f_fourier_nonvanishing_unit_point
  f_exists_convolution_nonvanishing_weight --> f_fourier_continuous_nonvanishing
  f_exists_convolution_nonvanishing_weight --> f_schwartz_fourier_preimage
  f_exists_convolution_nonvanishing_weight --> f_exists_test_fourier_nonvanishing
  f_exists_convolution_nonvanishing_weight --> f_convolution_decay_integrable_fourier
  f_exists_convolution_nonvanishing_weight --> f_convolution_family_integrable
  f_exists_convolution_nonvanishing_weight --> f_fourier_weight_integral_symmetry
  f_exists_convolution_nonvanishing_weight --> f_cone_b_defs
  f_exists_convolution_nonvanishing_weight --> fourier_analysis
  f_foundations__is_herm_n_d --> concept_hermitian_unitary_matrices
  f_foundations__is_herm_n_d --> concept_valuation_rings
  f_foundations__is_herm_n_d --> concept_lattices_in_the_plane
  f_foundations__is_herm_n_d --> concept_group_actions
  f_foundations__is_herm_n_d --> concept_haar_measure_fundamental_domain
  f_foundations__is_herm_n_d --> linear_algebra
  f_foundations__is_herm_n_d --> p_adic_numbers
  f_semilocal_frames__complement_reference_compact_subgroup --> f_foundations__is_herm_n_d
  f_semilocal_frames__complement_reference_compact_subgroup --> concept_group_actions
  f_semilocal_frames__complement_reference_compact_subgroup --> concept_haar_measure_fundamental_domain
  f_semilocal_frames__complement_reference_compact_subgroup --> concept_valuation_rings
  f_semilocal_frames__complement_reference_compact_subgroup --> concept_hermitian_unitary_matrices
  f_semilocal_frames__complement_reference_compact_subgroup --> concept_lattice_point_counting
  f_semilocal_frames__g_frames --> f_semilocal_frames__complement_reference_compact_subgroup
  f_semilocal_frames__g_frames --> f_foundations__is_herm_n_d
  f_semilocal_frames__g_frames --> number_fields
  f_semilocal_frames__g_frames --> p_adic_numbers
  f_semilocal_frames__g_frames --> concept_dedekind_domains
  f_semilocal_frames__g_frames --> concept_lattices_in_the_plane
  f_semilocal_frames__g_frames --> concept_group_actions
  f_flag_measures__imports_tail --> linear_algebra
  f_flag_measures__imports_tail --> rings_fields
  f_flag_measures__imports_tail --> concept_valuation_rings
  f_flag_measures__imports_tail --> proofs
  f_local_lattice_between_scaled_standard_lattices --> f_flag_measures__imports_tail
  f_local_lattice_between_scaled_standard_lattices --> f_mem_span_single_iff
  f_local_lattice_between_scaled_standard_lattices --> f_foundations__is_herm_n_d
  f_local_lattice_between_scaled_standard_lattices --> f_semilocal_frames__g_frames
  f_local_lattice_between_scaled_standard_lattices --> concept_lattices_in_the_plane
  f_local_lattice_between_scaled_standard_lattices --> concept_valuation_rings
  f_local_lattice_between_scaled_standard_lattices --> linear_algebra
  f_mem_span_single_iff --> f_semilocal_frames__g_frames
  f_mem_span_single_iff --> linear_algebra
  f_mem_span_single_iff --> rings_fields
  f_mem_span_single_iff --> number_fields
  f_mem_span_single_iff --> p_adic_numbers
  f_complex_analytic_sets__p_riemann_extension_analytic --> f_complex_analytic_sets__st_riemann_extension_analytic
  f_complex_analytic_sets__p_riemann_extension_analytic --> f_complex_analytic_sets__osgood_separate
  f_complex_analytic_sets__p_riemann_extension_analytic --> f_regularisation__p_riemann_extension_slices
  f_complex_analytic_sets__p_riemann_extension_analytic --> f_analytic_charts__osgood
  f_complex_analytic_sets__p_riemann_extension_analytic --> concept_complex_analytic_sets
  f_complex_analytic_sets__p_riemann_extension_analytic --> complex_analysis
  f_complex_analytic_sets__p_riemann_extension_analytic --> calculus
  f_complex_analytic_sets__st_riemann_extension_analytic --> concept_complex_analytic_sets
  f_complex_analytic_sets__st_riemann_extension_analytic --> complex_analysis
  f_complex_analytic_sets__st_riemann_extension_analytic --> concept_point_set_topology
  f_p_growth_off_hypersurface_polynomial --> f_st_entire_polynomial_growth
  f_p_growth_off_hypersurface_polynomial --> f_st_growth_off_hypersurface_polynomial
  f_p_growth_off_hypersurface_polynomial --> f_complex_analytic_sets__p_riemann_extension_analytic
  f_p_growth_off_hypersurface_polynomial --> polynomials
  f_p_growth_off_hypersurface_polynomial --> complex_analysis
  f_p_growth_off_hypersurface_polynomial --> concept_point_set_topology
  f_st_entire_polynomial_growth --> polynomials
  f_st_entire_polynomial_growth --> complex_analysis
  f_st_growth_off_hypersurface_polynomial --> polynomials
  f_st_growth_off_hypersurface_polynomial --> complex_analysis
  f_st_growth_off_hypersurface_polynomial --> concept_coordinate_rings_dimension
  f_hida_complete_rings__cofinal_compl --> concept_adic_completion
  f_hida_complete_rings__cofinal_compl --> rings_fields
  f_hida_complete_rings__fin_compl --> concept_adic_completion
  f_hida_complete_rings__fin_compl --> concept_finitely_generated_algebras
  f_hida_complete_rings__fin_compl --> linear_algebra
  f_hida_complete_rings__fin_max --> concept_local_rings
  f_hida_complete_rings__fin_max --> concept_semisimple_algebras_radical
  f_hida_complete_rings__fin_max --> concept_prime_ideals_localization
  f_hida_complete_rings__fin_max --> linear_algebra
  f_hida_complete_rings__idem_lift --> concept_hensel_lifting
  f_hida_complete_rings__idem_lift --> concept_adic_completion
  f_hida_complete_rings__idem_lift --> polynomials
  f_hida_complete_rings__loc_char --> concept_local_rings
  f_hida_complete_rings__loc_char --> concept_adic_completion
  f_hida_complete_rings__loc_char --> concept_prime_ideals_localization
  f_hida_complete_rings__loc_char --> linear_algebra
  f_capelli_identities__precomplete_of_finite --> concept_hensel_lifting
  f_capelli_identities__precomplete_of_finite --> concept_adic_completion
  f_capelli_identities__precomplete_of_finite --> concept_local_rings
  f_capelli_identities__precomplete_of_finite --> concept_semisimple_algebras_radical
  f_capelli_identities__precomplete_of_finite --> concept_finitely_generated_algebras
  f_capelli_identities__precomplete_of_finite --> concept_tensor_product_of_algebras
  f_hida_complete_rings__loc_abs --> f_capelli_identities__precomplete_of_finite
  f_hida_complete_rings__loc_abs --> concept_local_rings
  f_hida_complete_rings__loc_abs --> concept_adic_completion
  f_hida_complete_rings__max_idem --> f_hida_complete_rings__fin_max
  f_hida_complete_rings__max_idem --> f_hida_complete_rings__fin_compl
  f_hida_complete_rings__max_idem --> f_hida_complete_rings__cofinal_compl
  f_hida_complete_rings__max_idem --> f_hida_complete_rings__idem_lift
  f_hida_complete_rings__max_idem --> concept_prime_ideals_localization
  f_hida_complete_rings__max_idem --> concept_local_rings
  f_hida_complete_rings__max_idem --> concept_semisimple_algebras_radical
  f_hecke_restr --> f_hida_complete_rings__loc_abs
  f_hecke_restr --> f_hida_complete_rings__loc_char
  f_hecke_restr --> f_hecke_algebras__continuous_torus_character
  f_hecke_restr --> concept_hecke_operators
  f_hecke_restr --> concept_local_rings
  f_hecke_restr --> concept_adic_completion
  f_arithmetic_bezout__cone_ball --> f_arithmetic_bezout__statements
  f_arithmetic_bezout__cone_ball --> concept_hausdorff_measure
  f_arithmetic_bezout__cone_ball --> concept_complex_analytic_sets
  f_arithmetic_bezout__cone_ball --> number_fields
  f_arithmetic_bezout__statements_cone_slab --> f_arithmetic_bezout__cone_ball
  f_arithmetic_bezout__statements_cone_slab --> f_arithmetic_bezout__statements
  f_arithmetic_bezout__statements_cone_slab --> concept_hausdorff_measure
  f_ring_krull_dim_quot_bot_one --> f_arithmetic_bezout__cone_ball
  f_ring_krull_dim_quot_bot_one --> f_arithmetic_bezout__statements
  f_ring_krull_dim_quot_bot_one --> concept_hausdorff_measure
  f_ring_krull_dim_quot_bot_one --> concept_complex_analytic_sets
  f_ring_krull_dim_quot_bot_one --> concept_coordinate_rings_dimension
  f_ring_krull_dim_quot_bot_one --> linear_algebra
  f_frame_proj_eq --> f_ring_krull_dim_quot_bot_one
  f_frame_proj_eq --> real_analysis
  f_st_graph_jac_continuous --> linear_algebra
  f_st_graph_jac_continuous --> real_analysis
  f_st_graph_jac_continuous --> concept_hausdorff_measure
  f_st_area_graph_piece --> f_st_graph_jac_continuous
  f_st_area_graph_piece --> concept_hausdorff_measure
  f_st_area_graph_piece --> real_analysis
  f_p_area_graph_piece --> f_st_area_graph_piece
  f_p_area_graph_piece --> f_st_graph_jac_continuous
  f_p_area_graph_piece --> concept_hausdorff_measure
  f_p_area_graph_piece --> linear_algebra
  f_volume_lt_hausdorff_unit_ball_twenty --> f_ring_krull_dim_quot_bot_one
  f_volume_lt_hausdorff_unit_ball_twenty --> concept_hausdorff_measure
  f_volume_lt_hausdorff_unit_ball_twenty --> linear_algebra
  f_parts_of_square_identity --> f_harish_chandra_descent__descent
  f_parts_of_square_identity --> f_discrete_series__defs_rep
  f_parts_of_square_identity --> f_discrete_series__is_inf_unitary
  f_parts_of_square_identity --> concept_highest_weight_casimir
  f_parts_of_square_identity --> concept_hermitian_unitary_matrices
  f_test_obj --> f_toroidal_compactification__is_completed_strict_hens
  f_test_obj --> f_toroidal_compactification__is_grp_pullback
  f_test_obj --> f_toroidal_compactification__push_invertible
  f_test_obj --> f_toroidal_compactification__two_weight_eq_one_add_root
  f_test_obj --> concept_schemes_basics
  f_test_obj --> concept_picard_group
  f_dual_weyl_coordinates__defs_obj --> concept_highest_weight_casimir
  f_dual_weyl_coordinates__defs_obj --> concept_group_representations
  f_dual_weyl_coordinates__defs_obj --> concept_discrete_valuation_ring
  f_dual_weyl_coordinates__defs_obj --> concept_exterior_powers
  f_dual_weyl_coordinates__defs_obj --> concept_adic_completion
  f_dual_weyl_coordinates__defs_obj --> linear_algebra
  f_dual_weyl_coordinates__defs_mod --> f_dual_weyl_coordinates__defs_obj
  f_dual_weyl_coordinates__defs_mod --> concept_highest_weight_casimir
  f_dual_weyl_coordinates__defs_mod --> concept_group_representations
  f_dual_weyl_coordinates__defs_mod --> linear_algebra
  f_dual_weyl_coordinates__statement_a --> f_dual_weyl_coordinates__defs_mod
  f_dual_weyl_coordinates__statement_a --> linear_algebra
  f_dual_weyl_coordinates__statement_b --> f_dual_weyl_coordinates__defs_mod
  f_dual_weyl_coordinates__statement_b --> f_dual_weyl_coordinates__defs_obj
  f_dual_weyl_coordinates__statement_b --> concept_tensor_product_of_algebras
  f_dual_weyl_coordinates__statement_b --> linear_algebra
  f_dual_weyl_proofs__b_core_w --> f_dual_weyl_coordinates__defs_mod
  f_dual_weyl_proofs__b_core_w --> f_dual_weyl_coordinates__defs_obj
  f_dual_weyl_proofs__b_core_w --> concept_highest_weight_casimir
  f_dual_weyl_proofs__b_core_w --> counting
  f_dual_weyl_proofs__b_core_t --> f_dual_weyl_proofs__b_core_w
  f_dual_weyl_proofs__b_core_t --> f_dual_weyl_coordinates__defs_mod
  f_dual_weyl_proofs__b_core_t --> f_dual_weyl_coordinates__defs_obj
  f_dual_weyl_proofs__b_core_t --> linear_algebra
  f_dual_weyl_proofs__qb_indep_field --> f_dual_weyl_proofs__b_core_t
  f_dual_weyl_proofs__qb_indep_field --> f_dual_weyl_proofs__b_core_w
  f_dual_weyl_proofs__qb_indep_field --> f_dual_weyl_coordinates__statement_a
  f_dual_weyl_proofs__qb_indep_field --> f_dual_weyl_coordinates__defs_mod
  f_dual_weyl_proofs__qb_indep_field --> linear_algebra
  f_dual_weyl_proofs__qb_basis_apply --> f_dual_weyl_proofs__qb_indep_field
  f_dual_weyl_proofs__qb_basis_apply --> f_dual_weyl_coordinates__statement_a
  f_dual_weyl_proofs__qb_basis_apply --> f_dual_weyl_coordinates__defs_mod
  f_dual_weyl_proofs__qb_basis_apply --> linear_algebra
  f_dual_weyl_proofs__qb_basis_apply --> primes_divisibility
  f_window_bound_odd_cases --> f_dual_weyl_proofs__qb_basis_apply
  f_window_bound_odd_cases --> f_dual_weyl_coordinates__statement_a
  f_window_bound_odd_cases --> f_dual_weyl_coordinates__statement_b
  f_dual_weyl_coordinates__filtration_theorem_of_clauses --> f_dual_weyl_coordinates__statement_b
  f_dual_weyl_coordinates__filtration_theorem_of_clauses --> f_dual_weyl_coordinates__defs_mod
  f_dual_weyl_coordinates__filtration_theorem_of_clauses --> linear_algebra
  f_jet_harmonics__is_adic_colimit_of_factor --> f_extension_descent__thick_trans_comp
  f_jet_harmonics__is_adic_colimit_of_factor --> concept_schemes_basics
  f_jet_harmonics__is_adic_colimit_of_factor --> concept_categorical_pullbacks
  f_jet_harmonics__is_adic_colimit_of_factor --> concept_adic_completion
  f_jet_harmonics__is_adic_colimit_of_factor --> concept_filtered_colimits
  f_is_adic_complete_of_pow_le_of_pow_le --> concept_adic_completion
  f_is_adic_complete_of_pow_le_of_pow_le --> rings_fields
  f_extension_descent__deg_unif --> f_extension_descent__thick_trans_comp
  f_extension_descent__deg_unif --> f_abelian_scheme_quotients__q_surjective
  f_extension_descent__deg_unif --> f_abelian_scheme_quotients__split_ext_defs
  f_extension_descent__deg_unif --> f_abelian_scheme_quotients__is_abelian_scheme
  f_extension_descent__deg_unif --> f_extension_descent__nonzero_locus
  f_extension_descent__deg_unif --> f_cubical_structures__cube_symmetric_swap_first
  f_extension_descent__deg_unif --> f_split_tori__split_torus_aff
  f_extension_descent__deg_unif --> concept_group_schemes
  f_extension_descent__deg_unif --> concept_picard_group
  f_extension_descent__deg_unif --> concept_smooth_morphisms
  f_extension_descent__deg_unif --> concept_adic_completion
  f_extension_descent__thick_trans_comp --> f_extension_descent__nonzero_locus
  f_extension_descent__thick_trans_comp --> f_cubical_structures__cube_symmetric_swap_first
  f_extension_descent__thick_trans_comp --> f_abelian_scheme_quotients__is_abelian_scheme
  f_extension_descent__thick_trans_comp --> concept_schemes_basics
  f_extension_descent__thick_trans_comp --> concept_categorical_pullbacks
  f_extension_descent__thick_trans_comp --> concept_group_schemes
  f_extension_descent__thick_trans_comp --> concept_picard_group
  f_extension_descent__thick_trans_comp --> concept_integral_closure_fraction_fields
  f_extension_descent__thick_trans_comp --> concept_adic_completion
  f_extension_descent__thick_trans_comp --> concept_local_rings
  f_abelian_scheme_quotients__q_surjective --> f_abelian_scheme_quotients__split_ext_defs
  f_abelian_scheme_quotients__q_surjective --> f_split_tori__split_torus_aff
  f_abelian_scheme_quotients__q_surjective --> f_abelian_scheme_quotients__is_abelian_scheme
  f_abelian_scheme_quotients__q_surjective --> f_cubical_structures__cube_symmetric_swap_first
  f_abelian_scheme_quotients__q_surjective --> concept_group_schemes
  f_abelian_scheme_quotients__q_surjective --> concept_flat_modules
  f_abelian_scheme_quotients__q_surjective --> concept_picard_group
  f_abelian_scheme_quotients__split_ext_defs --> f_abelian_scheme_quotients__is_abelian_scheme
  f_abelian_scheme_quotients__split_ext_defs --> concept_group_schemes
  f_abelian_scheme_quotients__split_ext_defs --> concept_picard_group
  f_abelian_scheme_quotients__split_ext_defs --> concept_finitely_generated_abelian_groups
  f_local_hermitian_forms__even_of_norm --> f_local_orbit_counts__sqrt_o
  f_local_hermitian_forms__even_of_norm --> f_local_hermitian_forms__even_val
  f_local_hermitian_forms__even_of_norm --> concept_discrete_valuation_ring
  f_local_hermitian_forms__even_of_norm --> concept_local_rings
  f_local_hermitian_forms__even_of_norm --> concept_hensel_lifting
  f_local_hermitian_forms__even_of_norm --> concept_valuation_rings
  f_local_hermitian_forms__even_of_norm --> modular_arithmetic
  f_local_orbit_counts__hs_n_e --> f_local_hermitian_forms__lcount_norm
  f_local_orbit_counts__hs_n_e --> f_local_hermitian_forms__norm_one_is_coboundary_unramified_quadratic
  f_local_orbit_counts__hs_n_e --> concept_discrete_valuation_ring
  f_local_orbit_counts__hs_n_e --> rings_fields
  f_nonsq_mul --> f_local_orbit_counts__sqrt_o
  f_nonsq_mul --> f_local_orbit_counts__norm_ex
  f_nonsq_mul --> f_local_hermitian_forms__even_val
  f_nonsq_mul --> f_local_hermitian_forms__lcount_norm
  f_nonsq_mul --> concept_discrete_valuation_ring
  f_nonsq_mul --> concept_hensel_lifting
  f_nonsq_mul --> modular_arithmetic
  f_local_orbit_counts__norm_ex --> f_local_hermitian_forms__even_of_norm
  f_local_orbit_counts__norm_ex --> f_local_hermitian_forms__even_val
  f_local_orbit_counts__norm_ex --> f_local_hermitian_forms__lcount_norm
  f_local_orbit_counts__norm_ex --> concept_integral_closure_fraction_fields
  f_local_orbit_counts__norm_ex --> concept_discrete_valuation_ring
  f_local_orbit_counts__sqrt_o --> f_local_hermitian_forms__lcount_norm
  f_local_orbit_counts__sqrt_o --> f_local_hermitian_forms__norm_one_is_coboundary_unramified_quadratic
  f_local_orbit_counts__sqrt_o --> concept_hensel_lifting
  f_local_orbit_counts__sqrt_o --> concept_adic_completion
  f_local_orbit_counts__sqrt_o --> concept_discrete_valuation_ring
  f_local_orbit_counts__sqrt_o --> concept_local_rings
  f_sum_shift --> f_local_orbit_counts__hs_n_e
  f_sum_shift --> f_nonsq_mul
  f_sum_shift --> f_local_hermitian_forms__lcount_norm
  f_sum_shift --> concept_normal_subgroups_quotients
  f_sum_shift --> groups
  f_sum_shift --> complex_numbers
  f_p_normal_zeros_nowhere_dense --> f_complex_analytic_sets__st_normal_germ_integrally_closed
  f_p_normal_zeros_nowhere_dense --> f_st_irreducible_germ_regular_connected
  f_p_normal_zeros_nowhere_dense --> f_st_regular_locus_dense
  f_p_normal_zeros_nowhere_dense --> f_complex_analytic_sets__st_normal_zeros_nowhere_dense
  f_p_normal_zeros_nowhere_dense --> f_analytic_germ
  f_p_normal_zeros_nowhere_dense --> f_regular_locus
  f_p_normal_zeros_nowhere_dense --> f_complex_analytic_sets__osgood_separate
  f_p_normal_zeros_nowhere_dense --> f_complex_analytic_sets__st_normal_model
  f_p_normal_zeros_nowhere_dense --> concept_complex_analytic_sets
  f_p_normal_zeros_nowhere_dense --> concept_point_set_topology
  f_p_normal_zeros_nowhere_dense --> concept_integral_closure_fraction_fields
  f_p_normal_zeros_nowhere_dense --> complex_analysis
  f_st_irreducible_germ_regular_connected --> f_analytic_germ
  f_st_irreducible_germ_regular_connected --> f_regular_locus
  f_st_irreducible_germ_regular_connected --> concept_complex_analytic_sets
  f_st_irreducible_germ_regular_connected --> concept_point_set_topology
  f_complex_analytic_sets__st_normal_zeros_nowhere_dense --> f_complex_analytic_sets__st_normal_model
  f_complex_analytic_sets__st_normal_zeros_nowhere_dense --> concept_complex_analytic_sets
  f_complex_analytic_sets__st_normal_zeros_nowhere_dense --> concept_integral_closure_fraction_fields
  f_complex_analytic_sets__st_normal_zeros_nowhere_dense --> concept_prime_ideals_localization
  f_complex_analytic_sets__st_normal_zeros_nowhere_dense --> concept_point_set_topology
  f_st_regular_locus_dense --> f_analytic_germ
  f_st_regular_locus_dense --> f_regular_locus
  f_st_regular_locus_dense --> concept_complex_analytic_sets
  f_st_regular_locus_dense --> concept_point_set_topology
  f_dual_lattices__cokernel_length_comparison_of --> f_dual_lattices__cokernel_length_comparison_statement
  f_dual_lattices__cokernel_length_comparison_of --> f_dual_lattices__cotangent_surjective
  f_dual_lattices__cokernel_length_comparison_of --> f_dual_lattices__tensor_span
  f_dual_lattices__cokernel_length_comparison_of --> f_dual_lattices__map_smul_one_mul_vec
  f_dual_lattices__cokernel_length_comparison_of --> concept_valuation_rings
  f_dual_lattices__cokernel_length_comparison_of --> linear_algebra
  f_dual_lattices__cokernel_length_comparison_statement --> f_dual_lattices__cotangent_surjective
  f_dual_lattices__cokernel_length_comparison_statement --> f_dual_lattices__tensor_span
  f_dual_lattices__cokernel_length_comparison_statement --> concept_valuation_rings
  f_dual_lattices__cokernel_length_comparison_statement --> linear_algebra
  f_eigen_quotient_smith_statement --> f_dual_lattices__cokernel_length_comparison_of
  f_eigen_quotient_smith_statement --> f_dual_lattices__cotangent_surjective
  f_eigen_quotient_smith_statement --> f_dual_lattices__tensor_span
  f_eigen_quotient_smith_statement --> concept_valuation_rings
  f_eigen_quotient_smith_statement --> linear_algebra
  f_dual_lattices__restricted_hopf_order_approximation_statement --> f_dual_lattices__tensor_span
  f_dual_lattices__restricted_hopf_order_approximation_statement --> f_dual_lattices__cotangent_surjective
  f_dual_lattices__restricted_hopf_order_approximation_statement --> concept_valuation_rings
  f_dual_lattices__restricted_hopf_order_approximation_statement --> linear_algebra
  f_dual_lattices__unramified_cokernel_length_statement --> f_dual_lattices__cotangent_surjective
  f_dual_lattices__unramified_cokernel_length_statement --> f_dual_lattices__tensor_span
  f_dual_lattices__unramified_cokernel_length_statement --> concept_valuation_rings
  f_dual_lattices__unramified_cokernel_length_statement --> infinite_series
  f_dual_lattices__unramified_cokernel_lower_bound_of --> f_dual_lattices__cokernel_length_comparison_statement
  f_dual_lattices__unramified_cokernel_lower_bound_of --> f_dual_lattices__unramified_cokernel_length_statement
  f_dual_lattices__unramified_cokernel_lower_bound_of --> f_dual_lattices__unramified_cokernel_lower_bound_statement
  f_dual_lattices__unramified_cokernel_lower_bound_of --> f_dual_lattices__cotangent_surjective
  f_dual_lattices__unramified_cokernel_lower_bound_of --> f_dual_lattices__map_smul_one_mul_vec
  f_dual_lattices__unramified_cokernel_lower_bound_of --> f_dual_lattices__tensor_span
  f_dual_lattices__unramified_cokernel_lower_bound_of --> concept_valuation_rings
  f_dual_lattices__unramified_cokernel_lower_bound_of --> linear_algebra
  f_dual_lattices__unramified_cokernel_lower_bound_statement --> f_dual_lattices__unramified_cokernel_length_statement
  f_dual_lattices__unramified_cokernel_lower_bound_statement --> f_dual_lattices__cokernel_length_comparison_statement
  f_dual_lattices__unramified_cokernel_lower_bound_statement --> f_dual_lattices__cotangent_surjective
  f_dual_lattices__unramified_cokernel_lower_bound_statement --> concept_valuation_rings
  f_commutative_algebra_height__k_stable_highest_weight_vector --> f_commutative_algebra_height__cpl_is
  f_commutative_algebra_height__k_stable_highest_weight_vector --> f_commutative_algebra_height__cpl_uniq
  f_commutative_algebra_height__k_stable_highest_weight_vector --> f_commutative_algebra_height__is_local_hom
  f_commutative_algebra_height__k_stable_highest_weight_vector --> f_commutative_algebra__res_map_bijective
  f_commutative_algebra_height__k_stable_highest_weight_vector --> concept_adic_completion
  f_commutative_algebra_height__k_stable_highest_weight_vector --> concept_local_rings
  f_commutative_algebra_height__k_stable_highest_weight_vector --> concept_coordinate_rings_dimension
  f_commutative_algebra_height__k_stable_highest_weight_vector --> concept_flat_modules
  f_commutative_algebra_height__k_stable_highest_weight_vector --> concept_prime_ideals_localization
  f_moduli_nonempty_of_obj --> number_fields
  f_moduli_nonempty_of_obj --> concept_field_extensions_transcendence
  f_moduli_nonempty_of_obj --> complex_numbers
  f_moduli_nonempty_of_obj --> concept_roots_of_unity_kummer
  f_casimir_and_root_bounds --> concept_highest_weight_casimir
  f_casimir_and_root_bounds --> concept_hermitian_unitary_matrices
  f_casimir_and_root_bounds --> concept_group_representations
  f_casimir_and_root_bounds --> f_harish_chandra_descent__descent
  f_casimir_and_root_bounds --> f_discrete_series__is_inf_unitary
  f_casimir_and_root_bounds --> f_discrete_series__defs_rep
  f_casimir_and_root_bounds --> f_bochner_inequality__cas_val_k
  f_casimir_and_root_bounds --> f_bochner_inequality__layer_basic
  f_casimir_and_root_bounds --> f_bochner_inequality__k_unit_b
  f_casimir_and_root_bounds --> f_bochner_inequality__is_k_unitary_of_is_inf_unitary
  f_casimir_and_root_bounds --> f_casimir_algebra__casimir_k_khw_vec
  f_bt_order_value_eval --> f_geometry_proofs__section_eq_zero_of_values
  f_bt_order_value_eval --> f_global_geometry__has_values
  f_bt_order_value_eval --> f_hodge_tate_points__val_at_restrict
  f_bt_order_value_eval --> f_commutative_algebra__models
  f_bt_order_value_eval --> f_global_geometry__exists_unit_form_localization_etale_nbhd
  f_bt_order_value_eval --> concept_schemes_basics
  f_der_ring_injective --> concept_dual_numbers
  f_der_ring_injective --> concept_derivations_smoothness
  f_der_ring_injective --> concept_group_schemes
  f_der_ring_injective --> f_global_geometry__lie_model
  f_geometry_proofs__exists_lie_model --> f_global_geometry__lie_model
  f_geometry_proofs__exists_lie_model --> concept_dual_numbers
  f_geometry_proofs__exists_lie_model --> concept_group_schemes
  f_geometry_proofs__exists_lie_model --> concept_schemes_basics
  f_geometry_proofs__exists_lie_model --> concept_categorical_pullbacks
  f_is_irreducible_iff --> concept_group_representations
  f_is_irreducible_iff --> concept_point_set_topology
  f_is_irreducible_iff --> linear_algebra
  f_is_irreducible_iff --> f_foundations__smooth_part_stable
  f_is_irreducible_iff --> f_is_open_stab_of_mem_nhds
  f_is_irreducible_iff --> f_is_open_stabilizer
  f_foundations__smooth_part_stable --> concept_group_representations
  f_foundations__smooth_part_stable --> concept_normal_subgroups_quotients
  f_foundations__smooth_part_stable --> concept_point_set_topology
  f_foundations__smooth_part_stable --> linear_algebra
  f_double_coset_operators_comm_of_anti_involution --> groups
  f_double_coset_operators_comm_of_anti_involution --> concept_normal_subgroups_quotients
  f_double_coset_operators_comm_of_anti_involution --> counting
  f_double_coset_operators_comm_of_anti_involution --> concept_hecke_operators
  f_infinity_type --> number_fields
  f_infinity_type --> complex_numbers
  f_infinity_type --> counting
  f_is_open_stabilizer --> concept_group_actions
  f_is_open_stabilizer --> concept_group_representations
  f_is_open_stabilizer --> concept_point_set_topology
  f_is_open_stabilizer --> groups
  f_is_open_stab_of_mem_nhds --> f_is_open_stabilizer
  f_is_open_stab_of_mem_nhds --> f_transpose_inv
  f_is_open_stab_of_mem_nhds --> concept_group_representations
  f_is_open_stab_of_mem_nhds --> linear_algebra
  f_reg_alg_fam --> f_infinity_type
  f_reg_alg_fam --> number_fields
  f_reg_alg_fam --> complex_numbers
  f_reg_alg_fam --> counting
  f_transpose_inv --> linear_algebra
  f_transpose_inv --> groups
  f_transpose_inv --> concept_point_set_topology
  f_finrank_fixed_eq_one --> f_is_irreducible_iff
  f_finrank_fixed_eq_one --> f_foundations__smooth_part_stable
  f_finrank_fixed_eq_one --> f_double_coset_operators_comm_of_anti_involution
  f_finrank_fixed_eq_one --> concept_hecke_operators
  f_finrank_fixed_eq_one --> concept_group_representations
  f_finrank_fixed_eq_one --> linear_algebra
  f_finrank_fixed_eq_one --> concept_normal_subgroups_quotients
  f_trace_mul_of_finrank_one --> f_finrank_fixed_eq_one
  f_trace_mul_of_finrank_one --> linear_algebra
  f_trace_mul_of_finrank_one --> concept_normal_subgroups_quotients
  f_trace_mul_of_finrank_one --> concept_point_set_topology
  f_witt_logarithm --> f_wf_log_of
  f_witt_logarithm --> f_formal_logarithm_holds
  f_witt_logarithm --> f_period_integrals__inv_ser_sub
  f_witt_logarithm --> concept_witt_vectors_ainf
  f_witt_logarithm --> p_adic_numbers
  f_witt_logarithm --> polynomials
  f_additive_integral_groups__coeff_pow_mem_s --> f_additive_integral_groups__gu_line
  f_additive_integral_groups__coeff_pow_mem_s --> p_adic_numbers
  f_additive_integral_groups__coeff_pow_mem_s --> polynomials
  f_additive_integral_groups__coeff_pow_mem_s --> infinite_series
  f_additive_integral_groups__d_x_eq_derivative --> f_additive_integral_groups__coeff_pow_mem_s
  f_additive_integral_groups__d_x_eq_derivative --> f_additive_integral_groups__gu_line
  f_additive_integral_groups__d_x_eq_derivative --> concept_derivations_smoothness
  f_additive_integral_groups__d_x_eq_derivative --> p_adic_numbers
  f_additive_integral_groups__d_x_eq_derivative --> calculus
  f_additive_integral_groups__glue_holds_var --> f_period_integrals__add_int_g
  f_additive_integral_groups__glue_holds_var --> f_additive_integral_groups__gu_line
  f_additive_integral_groups__glue_holds_var --> concept_ultrametric_norm
  f_additive_integral_groups__glue_holds_var --> p_adic_numbers
  f_additive_integral_groups__glue_holds_var --> concept_weierstrass_elliptic_functions
  f_additive_integral_groups__gu_line --> p_adic_numbers
  f_additive_integral_groups__gu_line --> polynomials
  f_additive_integral_groups__gu_line --> concept_derivations_smoothness
  f_additive_integral_groups__gu_line --> concept_weierstrass_elliptic_functions
  f_additive_integral_groups__subst_mem --> rings_fields
  f_additive_integral_groups__subst_mem --> polynomials
  f_additive_integral_groups__subst_mem --> infinite_series
  f_inv_nat_mem_wf --> f_exponential_integrality__inv_nat_cast_mem_witt_integers
  f_inv_nat_mem_wf --> f_exponential_integrality__development
  f_inv_nat_mem_wf --> f_period_integrals__exp_int_w
  f_inv_nat_mem_wf --> p_adic_numbers
  f_inv_nat_mem_wf --> primes_divisibility
  f_inv_nat_mem_wf --> concept_witt_vectors_ainf
  f_coef_wf_iff --> f_inv_nat_mem_wf
  f_coef_wf_iff --> p_adic_numbers
  f_coef_wf_iff --> polynomials
  f_formal_logarithm_holds --> f_additive_integral_groups__subst_mem
  f_formal_logarithm_holds --> f_additive_integral_groups__coeff_pow_mem_s
  f_formal_logarithm_holds --> f_additive_integral_groups__d_x_eq_derivative
  f_formal_logarithm_holds --> f_additive_integral_groups__gu_line
  f_formal_logarithm_holds --> f_coef_wf_iff
  f_formal_logarithm_holds --> f_inv_nat_mem_wf
  f_formal_logarithm_holds --> p_adic_numbers
  f_wf_log_of --> f_period_integrals__inv_ser_sub
  f_wf_log_of --> f_inv_nat_mem_wf
  f_wf_log_of --> p_adic_numbers
  f_wf_log_of --> concept_witt_vectors_ainf
  f_fock_q_row_div_adj --> f_fock_row_adj
  f_fock_q_row_div_adj --> f_fock_sub_adj
  f_fock_q_row_div_adj --> f_fock_space_tableaux__l_focks_lemmas
  f_fock_q_row_div_adj --> f_graded_weyl_divisibility__statement_a
  f_fock_q_row_div_adj --> f_graded_weyl_divisibility__statement_b
  f_fock_q_row_div_adj --> f_real_place_analysis__fock_pair_gl
  f_fock_q_row_div_adj --> polynomials
  f_fock_q_row_div_adj --> linear_algebra
  f_fock_row_adj --> f_fock_sub_adj
  f_fock_row_adj --> f_fock_space_tableaux__l_focks_lemmas
  f_fock_row_adj --> f_graded_weyl_divisibility__statement_a
  f_fock_row_adj --> concept_hermitian_unitary_matrices
  f_fock_row_adj --> linear_algebra
  f_fock_sub_adj --> f_fock_space_tableaux__l_focks_lemmas
  f_fock_sub_adj --> f_real_place_taylor__prod_factorial_support_sub_single
  f_fock_sub_adj --> f_real_place_analysis__fock_pair_gl
  f_fock_sub_adj --> f_graded_weyl_divisibility__statement_a
  f_fock_sub_adj --> polynomials
  f_fock_sub_adj --> concept_hermitian_unitary_matrices
  f_l_fockq_lemmas --> f_graded_weyl_divisibility__statement_b
  f_l_fockq_lemmas --> polynomials
  f_l_fockq_lemmas --> counting
  f_fock_space_tableaux__l_focks_lemmas --> f_real_place_taylor__prod_factorial_support_sub_single
  f_fock_space_tableaux__l_focks_lemmas --> f_real_place_analysis__fock_pair_gl
  f_fock_space_tableaux__l_focks_lemmas --> f_graded_weyl_divisibility__statement_a
  f_fock_space_tableaux__l_focks_lemmas --> polynomials
  f_fock_space_tableaux__l_focks_lemmas --> linear_algebra
  f_fock_space_tableaux__l_focks_lemmas --> calculus
  f_graded_weyl_divisibility__statement_a --> f_real_place_analysis__fock_pair_gl
  f_graded_weyl_divisibility__statement_a --> concept_highest_weight_casimir
  f_graded_weyl_divisibility__statement_a --> concept_symmetric_polynomials
  f_graded_weyl_divisibility__statement_a --> polynomials
  f_graded_weyl_divisibility__statement_a --> linear_algebra
  f_graded_weyl_divisibility__statement_b --> f_graded_weyl_divisibility__statement_a
  f_graded_weyl_divisibility__statement_b --> concept_highest_weight_casimir
  f_graded_weyl_divisibility__statement_b --> polynomials
  f_graded_weyl_divisibility__statement_b --> linear_algebra
  f_real_place_analysis__fock_pair_gl --> f_real_place_analysis__statement_a
  f_real_place_analysis__fock_pair_gl --> concept_highest_weight_casimir
  f_real_place_analysis__fock_pair_gl --> polynomials
  f_real_place_analysis__fock_pair_gl --> linear_algebra
  f_real_place_taylor__prod_factorial_support_sub_single --> f_real_place_analysis__fock_pair_gl
  f_real_place_taylor__prod_factorial_support_sub_single --> polynomials
  f_real_place_taylor__prod_factorial_support_sub_single --> calculus
  f_real_place_taylor__prod_factorial_support_sub_single --> counting
  f_archimedean_gaussian_fourier --> f_real_gaussian_fourier_transform
  f_archimedean_gaussian_fourier --> fourier_analysis
  f_archimedean_gaussian_fourier --> number_fields
  f_archimedean_gaussian_fourier --> complex_analysis
  f_archimedean_gaussian_fourier --> linear_algebra
  f_quadratic_level_set_density --> f_archimedean_gaussian_fourier
  f_quadratic_level_set_density --> f_schur_function_compact_support_modulo_unipotent
  f_quadratic_level_set_density --> fourier_analysis
  f_quadratic_level_set_density --> real_analysis
  f_quadratic_level_set_density --> number_fields
  f_real_gaussian_fourier_transform --> f_simultaneous_normal_form_majorant
  f_real_gaussian_fourier_transform --> fourier_analysis
  f_real_gaussian_fourier_transform --> complex_powers
  f_real_gaussian_fourier_transform --> linear_algebra
  f_real_gaussian_fourier_transform --> real_analysis
  f_schur_function_compact_support_modulo_unipotent --> fourier_analysis
  f_schur_function_compact_support_modulo_unipotent --> real_analysis
  f_schur_function_compact_support_modulo_unipotent --> concept_schwartz_functions
  f_schur_function_compact_support_modulo_unipotent --> calculus
  f_simultaneous_normal_form_majorant --> concept_hermitian_unitary_matrices
  f_simultaneous_normal_form_majorant --> linear_algebra
  f_alternating_difference_term_window --> f_inertia_eigenvalues__dlt_eq_zero
  f_alternating_difference_term_window --> concept_discrete_valuation_ring
  f_alternating_difference_term_window --> concept_integral_closure_fraction_fields
  f_alternating_difference_term_window --> linear_algebra
  f_inertia_eigenvalues__dlt_eq_zero --> concept_integral_closure_fraction_fields
  f_inertia_eigenvalues__dlt_eq_zero --> concept_discrete_valuation_ring
  f_inertia_eigenvalues__dlt_eq_zero --> counting
  f_finite_scheme_map_from_special_fibre --> concept_schemes_basics
  f_finite_scheme_map_from_special_fibre --> concept_categorical_pullbacks
  f_finite_scheme_map_from_special_fibre --> concept_local_rings
  f_finite_scheme_map_from_special_fibre --> concept_tensor_product_of_algebras
  f_finite_scheme_map_from_special_fibre --> concept_flat_modules
  f_cpl_quot --> f_commutative_algebra_height__cpl_uniq
  f_cpl_quot --> f_commutative_algebra_height__is_local_hom
  f_cpl_quot --> concept_adic_completion
  f_cpl_quot --> concept_local_rings
  f_cpl_quot --> concept_prime_ideals_localization
  f_kur_defs --> p_adic_numbers
  f_kur_defs --> concept_ultrametric_norm
  f_kur_defs --> concept_roots_of_unity_kummer
  f_kur_defs --> concept_frobenius_perfect_rings
  f_kur_defs --> concept_adic_completion
  f_kur_defs --> rings_fields
  f_norm_eq_of_norm_sub_lt --> concept_ultrametric_norm
  f_norm_eq_of_norm_sub_lt --> p_adic_numbers
  f_norm_eq_of_norm_sub_lt --> polynomials
  f_norm_eq_of_norm_sub_lt --> algebraic_closure
  f_norm_eq_of_norm_sub_lt --> concept_hensel_lifting
  f_norm_nat_cast_cl_of_not_dvd --> f_kur_defs
  f_norm_nat_cast_cl_of_not_dvd --> f_norm_eq_of_norm_sub_lt
  f_norm_nat_cast_cl_of_not_dvd --> concept_ultrametric_norm
  f_norm_nat_cast_cl_of_not_dvd --> p_adic_numbers
  f_norm_nat_cast_cl_of_not_dvd --> concept_roots_of_unity_kummer
  f_mu_m_eval_pow_eq_zero --> f_kur_defs
  f_mu_m_eval_pow_eq_zero --> concept_roots_of_unity_kummer
  f_mu_m_eval_pow_eq_zero --> concept_frobenius_perfect_rings
  f_mu_m_eval_pow_eq_zero --> polynomials
  f_mu_m_eval_pow_eq_zero --> concept_integral_closure_fraction_fields
  f_mu_m_eval_pow_eq_zero --> groups
  f_frob_fix_neg_one --> f_kur_defs
  f_frob_fix_neg_one --> concept_frobenius_perfect_rings
  f_frob_fix_neg_one --> modular_arithmetic
  f_frob_fix_neg_one --> primes_divisibility
  f_frob_fix_neg_one --> rings_fields
  f_exists_power_mul_unit_norm --> f_kur_defs
  f_exists_power_mul_unit_norm --> f_frob_fix_neg_one
  f_exists_power_mul_unit_norm --> f_norm_eq_of_norm_sub_lt
  f_exists_power_mul_unit_norm --> f_norm_nat_cast_cl_of_not_dvd
  f_exists_power_mul_unit_norm --> concept_ultrametric_norm
  f_exists_power_mul_unit_norm --> concept_discrete_valuation_ring
  f_exists_teichmuller_rep_mod_prime --> f_kur_defs
  f_exists_teichmuller_rep_mod_prime --> f_exists_power_mul_unit_norm
  f_exists_teichmuller_rep_mod_prime --> f_frob_fix_neg_one
  f_exists_teichmuller_rep_mod_prime --> f_norm_nat_cast_cl_of_not_dvd
  f_exists_teichmuller_rep_mod_prime --> concept_ultrametric_norm
  f_exists_teichmuller_rep_mod_prime --> concept_adic_completion
  f_exists_teichmuller_rep_mod_prime --> concept_local_rings
  f_exists_extend_endomorphism_fractions --> f_kur_defs
  f_exists_extend_endomorphism_fractions --> f_mu_m_eval_pow_eq_zero
  f_exists_extend_endomorphism_fractions --> f_exists_power_mul_unit_norm
  f_exists_extend_endomorphism_fractions --> f_exists_teichmuller_rep_mod_prime
  f_exists_extend_endomorphism_fractions --> f_norm_nat_cast_cl_of_not_dvd
  f_exists_extend_endomorphism_fractions --> concept_integral_closure_fraction_fields
  f_exists_extend_endomorphism_fractions --> concept_ultrametric_norm
  f_exists_extend_endomorphism_fractions --> concept_frobenius_perfect_rings
  f_kmu_incl_dense_range --> f_kur_defs
  f_kmu_incl_dense_range --> f_exists_extend_endomorphism_fractions
  f_kmu_incl_dense_range --> f_exists_teichmuller_rep_mod_prime
  f_kmu_incl_dense_range --> concept_adic_completion
  f_kmu_incl_dense_range --> concept_point_set_topology
  f_kmu_incl_dense_range --> concept_ultrametric_norm
  f_capelli_identities__is_closed_embedding_to_m --> groups
  f_capelli_identities__is_closed_embedding_to_m --> linear_algebra
  f_capelli_identities__is_closed_embedding_to_m --> concept_hermitian_unitary_matrices
  f_capelli_identities__is_closed_embedding_to_m --> concept_point_set_topology
  f_casimir_coefficients__is_closed_embedding_to_m --> f_capelli_identities__is_closed_embedding_to_m
  f_casimir_coefficients__is_closed_embedding_to_m --> concept_haar_measure_fundamental_domain
  f_casimir_coefficients__is_closed_embedding_to_m --> concept_hermitian_unitary_matrices
  f_casimir_coefficients__is_closed_embedding_to_m --> concept_point_set_topology
  f_casimir_coefficients__is_closed_embedding_to_m --> groups
  f_casimir_coefficients__is_closed_kset --> f_casimir_coefficients__is_closed_embedding_to_m
  f_casimir_coefficients__is_closed_kset --> f_casimir_coefficients__psi_exists_statement
  f_casimir_coefficients__is_closed_kset --> concept_highest_weight_casimir
  f_casimir_coefficients__is_closed_kset --> concept_haar_measure_fundamental_domain
  f_casimir_coefficients__is_closed_kset --> concept_group_representations
  f_casimir_coefficients__psi_exists_statement --> f_discrete_series__is_inf_unitary
  f_casimir_coefficients__psi_exists_statement --> f_discrete_series__defs_rep
  f_casimir_coefficients__psi_exists_statement --> concept_highest_weight_casimir
  f_casimir_coefficients__psi_exists_statement --> concept_group_representations
  f_casimir_coefficients__psi_exists_statement --> concept_haar_measure_fundamental_domain
  f_casimir_coefficients__psi_exists_statement --> concept_hermitian_unitary_matrices
  f_casimir_coefficients__deriv_g_a --> linear_algebra
  f_casimir_coefficients__deriv_g_a --> calculus
  f_casimir_coefficients__deriv_g_a --> concept_hermitian_unitary_matrices
  f_cas_chain_a --> complex_analysis
  f_cas_chain_a --> calculus
  f_cas_chain_a --> real_analysis
  f_cas_chain_a --> concept_point_set_topology
  f_cas_chain_b --> f_casimir_coefficients__deriv_g_a
  f_cas_chain_b --> f_casimir_coefficients__psi_exists_statement
  f_cas_chain_b --> f_capelli_identities__is_closed_embedding_to_m
  f_cas_chain_b --> calculus
  f_cas_chain_b --> linear_algebra
  f_cas_chain_b --> concept_hermitian_unitary_matrices
  f_cas_chain --> f_cas_chain_a
  f_cas_chain --> f_cas_chain_b
  f_cas_chain --> f_casimir_coefficients__is_closed_kset
  f_cas_chain --> f_casimir_coefficients__psi_exists_statement
  f_cas_chain --> complex_analysis
  f_cas_chain --> calculus
  f_exists_virtual_character_semidirect_orbit_cross_terms --> f_induced_class_function_from_subgroup_eq_finsum_cosets
  f_exists_virtual_character_semidirect_orbit_cross_terms --> f_is_character_finsum_conj_subgroup_function_extend_by_zer
  f_exists_virtual_character_semidirect_orbit_cross_terms --> f_is_character_over_subfield_induced_class_function
  f_exists_virtual_character_semidirect_orbit_cross_terms --> f_character_theory__virtual_characters_mul_comap_conj_ind_linear
  f_exists_virtual_character_semidirect_orbit_cross_terms --> f_is_character_over_subfield_restrict_class_function_one
  f_exists_virtual_character_semidirect_orbit_cross_terms --> concept_group_actions
  f_exists_virtual_character_semidirect_orbit_cross_terms --> concept_group_representations
  f_exists_virtual_character_semidirect_orbit_cross_terms --> concept_normal_subgroups_quotients
  f_exists_virtual_character_semidirect_orbit_cross_terms --> groups
  f_square_identity_holds --> f_harish_chandra_descent__descent
  f_square_identity_holds --> f_discrete_series__is_inf_unitary
  f_square_identity_holds --> f_discrete_series__defs_rep
  f_square_identity_holds --> concept_highest_weight_casimir
  f_square_identity_holds --> concept_hermitian_unitary_matrices
  f_square_identity_holds --> linear_algebra
  f_hecke_isogeny_kernels --> f_toroidal_compactification__two_weight_eq_one_add_root
  f_hecke_isogeny_kernels --> f_toroidal_compactification__push_invertible
  f_hecke_isogeny_kernels --> f_abelian_scheme_quotients__is_abelian_scheme
  f_hecke_isogeny_kernels --> f_cubical_structures__cube_symmetric_swap_first
  f_hecke_isogeny_kernels --> number_fields
  f_hecke_isogeny_kernels --> concept_ideals_and_discriminant
  f_hecke_isogeny_kernels --> concept_group_schemes
  f_hecke_isogeny_kernels --> concept_hecke_operators
  f_l_partial_sum --> f_l_function_bounds__statement
  f_l_partial_sum --> dirichlet_l_function
  f_l_partial_sum --> dirichlet_characters
  f_l_partial_sum --> complex_powers
  f_l_partial_sum --> infinite_series
  f_l_partial_sum --> calculus
  f_l_growth --> f_l_partial_sum
  f_l_growth --> dirichlet_l_function
  f_l_growth --> dirichlet_characters
  f_l_growth --> modular_arithmetic
  f_l_growth --> counting
  f_complex_analytic_sets__st_holomorphic_fibre_infinite --> complex_analysis
  f_complex_analytic_sets__st_holomorphic_fibre_infinite --> concept_complex_analytic_sets
  f_complex_analytic_sets__st_holomorphic_fibre_infinite --> concept_point_set_topology
  f_complex_analytic_sets__st_implicit_curve --> complex_analysis
  f_complex_analytic_sets__st_implicit_curve --> concept_complex_analytic_sets
  f_complex_analytic_sets__st_implicit_curve --> linear_algebra
  f_complex_analytic_sets__st_implicit_curve --> calculus
  f_st_irreducible_germ_regular_dim_ge --> f_analytic_germ
  f_st_irreducible_germ_regular_dim_ge --> concept_complex_analytic_sets
  f_st_irreducible_germ_regular_dim_ge --> complex_analysis
  f_complex_analytic_sets__p_implicit_curve --> f_complex_analytic_sets__st_implicit_curve
  f_complex_analytic_sets__p_implicit_curve --> f_complex_analytic_sets__osgood_separate
  f_complex_analytic_sets__p_implicit_curve --> complex_analysis
  f_complex_analytic_sets__p_implicit_curve --> calculus
  f_complex_analytic_sets__p_implicit_curve --> linear_algebra
  f_complex_analytic_sets__p_holomorphic_fibre_infinite --> f_complex_analytic_sets__st_holomorphic_fibre_infinite
  f_complex_analytic_sets__p_holomorphic_fibre_infinite --> f_complex_analytic_sets__p_implicit_curve
  f_complex_analytic_sets__p_holomorphic_fibre_infinite --> complex_analysis
  f_complex_analytic_sets__p_holomorphic_fibre_infinite --> linear_algebra
  f_complex_analytic_sets__p_holomorphic_fibre_infinite --> calculus
  f_p_irreducible_germ_regular_dim_ge --> f_st_irreducible_germ_regular_dim_ge
  f_p_irreducible_germ_regular_dim_ge --> f_complex_analytic_sets__p_holomorphic_fibre_infinite
  f_p_irreducible_germ_regular_dim_ge --> f_st_finite_projection_sheets_dense
  f_p_irreducible_germ_regular_dim_ge --> f_analytic_germ
  f_p_irreducible_germ_regular_dim_ge --> concept_complex_analytic_sets
  f_p_irreducible_germ_regular_dim_ge --> concept_point_set_topology
  f_mem_flag_sub_iff --> linear_algebra
  f_mem_first_lattice_iff --> f_mem_flag_sub_iff
  f_mem_first_lattice_iff --> f_commutative_algebra__lie_lattice_data
  f_mem_first_lattice_iff --> f_commutative_algebra__flag_minor
  f_mem_first_lattice_iff --> f_commutative_algebra__is_tight
  f_mem_first_lattice_iff --> f_commutative_algebra__step_order_res
  f_mem_first_lattice_iff --> f_algebra_statements__polarised_flag_statement
  f_mem_first_lattice_iff --> concept_valuation_rings
  f_mem_first_lattice_iff --> linear_algebra
  f_mem_first_lattice_iff --> rings_fields
  f_card_perm_partition_parts_mul_centralizer --> counting
  f_card_perm_partition_parts_mul_centralizer --> groups
  f_card_perm_partition_parts_mul_centralizer --> concept_group_actions
  f_squarefree_label_mass_degree_type_le --> f_foundation_proofs__squarefree_label_torus_card_bounds_and_mul
  f_squarefree_label_mass_degree_type_le --> f_foundation_proofs__mem_monic_squarefree_unit_const_polys_iff_monic_squarefr
  f_squarefree_label_mass_degree_type_le --> polynomials
  f_squarefree_label_mass_degree_type_le --> modular_arithmetic
  f_squarefree_label_mass_degree_type_le --> counting
  f_squarefree_label_mass_degree_type_le --> primes_divisibility
  f_mass_deg_type_le_cycle_type --> f_squarefree_label_mass_degree_type_le
  f_mass_deg_type_le_cycle_type --> f_card_perm_partition_parts_mul_centralizer
  f_mass_deg_type_le_cycle_type --> f_foundation_proofs__squarefree_label_torus_card_bounds_and_mul
  f_mass_deg_type_le_cycle_type --> counting
  f_mass_deg_type_le_cycle_type --> polynomials
  f_squarefree_label_torus_mass_divisor_bound --> f_mass_deg_type_le_cycle_type
  f_squarefree_label_torus_mass_divisor_bound --> f_foundation_proofs__mem_monic_squarefree_unit_const_polys_iff_monic_squarefr
  f_squarefree_label_torus_mass_divisor_bound --> polynomials
  f_squarefree_label_torus_mass_divisor_bound --> counting
  f_fixed_nondeg --> rings_fields
  f_fixed_nondeg --> concept_discrete_valuation_ring
  f_fixed_nondeg --> complex_numbers
  f_block_decomposition__norm_fibre_card_zero --> rings_fields
  f_block_decomposition__norm_fibre_card_zero --> counting
  f_block_decomposition__norm_fibre_card_zero --> linear_algebra
  f_block_decomposition__norm_fibre_card_nonzero --> rings_fields
  f_block_decomposition__norm_fibre_card_nonzero --> groups
  f_block_decomposition__norm_fibre_card_nonzero --> concept_normal_subgroups_quotients
  f_block_decomposition__norm_fibre_card_nonzero --> counting
  f_gauss_sum_hermitian_norm_level_one --> f_block_decomposition__norm_fibre_card_zero
  f_gauss_sum_hermitian_norm_level_one --> f_block_decomposition__norm_fibre_card_nonzero
  f_gauss_sum_hermitian_norm_level_one --> complex_numbers
  f_gauss_sum_hermitian_norm_level_one --> counting
  classDef explained fill:#c8f7c5
  class riemann_hypothesis,grh_dirichlet,step_rh_of_every,step_rh_of_right,step_crit_line,lean_placeholder_conditions,lean_polynomial_function,lean_unipotent_upper_triangular,lean_lower_iff,lean_padic_norm_p,lean_algclosure_q,lean_common_denominator,lean_char_extend,lean_sesquilinear_additive,f_ab_by_p_of_comm,f_linear_map_short_exact_commute,f_is_character_over_subfield_of_representation,f_finite_group_function_pairing_character_eq_finrank_inte,f_exists_character_quotient_of_injective_intertwining,f_exists_is_char_eq_add_of_pair_ne_zero,f_exists_coprime_order_of_pow_prime_pow,f_card_fixed_by_pow_prime_pow_mod_eq,f_exists_sylow_over_subgroup,f_card_fixed_by_quotient_eq_rel_index_of_p_regular,f_exists_abelian_by_prime_power_not_dvd_card_fixed_by,f_analytic_germ,f_st_analytic_root_branch,f_st_irreducible_germ_projection_image_near,f_st_finite_projection_sheets_dense,f_st_primitive_form_sheeted_off_discriminant,f_st_primitive_form_sheeted_locus_cut_out,f_st_primitive_form_sheeted_iff_root_full,f_st_primitive_form_full_branch_constant,f_st_polynomial_root_predicate_factor,f_st_primitive_form_window,f_st_primitive_form_full_root_factor,f_p_primitive_form_full_root_factor,f_regular_locus,f_st_irreducible_finite_germ_projection_open_at,f_st_irreducible_germ_points_off_discriminant,f_st_irreducible_germ_primitive_form,f_st_manifold_zeros_complement_connected,f_st_primitive_form_sheeted_points_near,f_p_irreducible_germ_points_off_discriminant,f_exists_irr_char_add,f_is_character_over_subfield_induction_irreducible,f_lat_defs,f_period_integrals__area_lat,f_period_integrals__ideal_lattice,f_im_conj_mul_combo,f_orbital_bounds_conclusion__area_lat,f_ideal_basis_alt,f_ideal_basis,f_o_k_area,f_assemble,f_orbital_bounds_conclusion__ideal_lattice,f_induced_class_function_from_subgroup_eq_finsum_cosets,f_is_character_finsum_conj_subgroup_function_extend_by_zer,f_is_character_over_subfield_restrict_class_function_one,f_is_character_over_subfield_induced_class_function,f_newton_polygon_dominant_index_x_sub_c_mul,f_newton_polygon_last_dominant_index_mul_x_sub_c,f_card_roots_closed_ball_eq_dominant_index,f_card_roots_closed_ball_bounds_ultrametric,f_onto_o_c_additive_poly,f_exists_transcendence_basis_algebraic,f_monic_polynomial_primitive_over_basis,f_primitive_element_finite_algebraic,f_primitive_element_coordinate_polynomials,f_primitive_element_denominator_clearing,f_polynomial_system_specialization,f_finsum_fiberwise_of_finite_support_complex,f_finsum_orbits_inv_stabilizer_card_mass,f_finsum_orbit_rel_fibred_equivariant,f_stabilizer_eq_centralizer,f_finite_support_stabilizer_weighted_pair_term,f_finsum_conj_classes_centralizer_orbits_eq_pair_orbits,f_st_irreducible_germ_meet_over_hypersurface,f_st_isolated_fibre_local_unbranched,f_st_open_projection_dominant_components,f_p_isolated_fibre_local_unbranched,f_weighted_orbit_sum_eq_pair_orbit_sum,f_dvr_matrix_proj_preimage,f_exists_residue_annihilator_of_not_standard_column_form_a,f_residue_top_factor_through_bottom,f_gl_factor_from_blocks_mod_uniformizer,f_exists_hyperplane_residue_outside_translates,f_exists_prime_gt_dvd_eval,f_exists_large_prime_dvd_int_polynomial_eval,f_sep_int_poly_root_mod_prime_sq,f_divisor_proofs__finite_type_to_number_field,f_divisor_proofs__number_field_to_mod_p_squared,f_nadel_vanishing_lemmas__finite_type_to_number_field,f_nadel_vanishing_lemmas__number_field_to_mod_p_squared,f_finite_type_to_mod_p_squared,f_whisker_left_left_is_pullback_snd,f_exists_factor_closed_immersion_of_locally_on_source,f_exists_glue_closed_immersions_open_cover,f_finite_flat_surjective_closed_subscheme_of_open_cover,f_exists_closed_immersion_represents_of_affine_opens,f_foundations__coset_trace,f_valuation_frobenius_sum_sub_le_nat_cast_prime,f_coset_representative_trace_fixed_properties,f_foundation_proofs__exists_pth_power_scale_thin_shell,f_pow_mul_approx_pow_of_almost_etale_separating_family,f_approx_pth_root_fixed_subfield_of_almost_etale,f_affine_hilbert_scheme_valuative_criterion_existence,f_divisor_proofs__comap_bc_comp,f_exists_flat_ideal_valuation_ring_pullback,f_flat_subscheme_of_quotient_flat_affine,f_divisor_proofs__ideal_sheaf_data_comap_ideal_top_of_is_affine,f_divisor_proofs__imports_alt,f_finite_projection_pushforward,f_st_centred_disc_cover_curve,f_st_finite_germ_projection_open_at,f_complex_analytic_sets__st_unbranched_proper_count_constant,f_exists_isotropic_graph_unitary_is_unit_lower_block,f_exists_isotropic_graph_det_lower_row_ne_zero_field,f_exists_skew_hermitian_mul_add_det_ne_zero_of_pair,f_skew_hermitian_perturb_idempotent_det_ne_zero,f_exists_rank_normal_form_matrix_field,f_lift_mod_maximal_skew,f_card_quot_prime_smul_eq_card_ker_mul_pow_finrank,f_card_zmod_tensor_eq_card_quot_prime_multiples,f_nat_card_homology_restrict_scalars,f_nat_card_homology_of_short_exact_mul,f_short_exact_mul_prime_zmod_tensor_complex,f_finrank_homology_mod_prime_universal_coefficients,f_complex_analytic_sets__st_holomorphic_on_subset,f_complex_analytic_sets__st_normal_model,f_st_normal_riemann_extension,f_st_normal_maximum_principle,f_complex_analytic_sets__st_normal_locally_irreducible,f_st_normal_open_mapping,f_st_branch_fill_dimension,f_st_branch_inverse_off_hypersurface,f_st_branch_contains_normal_point,f_st_branch_inverse_holomorphic,f_p_branch_contains_normal_point,f_p_branch_inverse_holomorphic,f_iwasawa_decomposition__exists_basis_in_finite_domain_trace_mem,f_iwasawa_decomposition__flat_tensor_embeds_tensor_fraction_fields,f_iwasawa_decomposition__integral_of_finite_base_change_image,f_iwasawa_decomposition__is_unit_map_of_mem_non_zero_divisors_tensor,f_iwasawa_decomposition__discr_mul_mem_of_is_integral,f_divisor_proofs__is_excision_nbhd_self,f_divisor_proofs__is_excision_nbhd_trans,f_divisor_proofs__is_excision_nbhd_away,f_divisor_proofs__exists_excision_nbhd_adjoin_root,f_divisor_proofs__exists_pow_sub_mem_span_of_is_unit_mod_of_is_alg_closed,f_unit_power_on_excision_neighbourhood,f_coprime_unit_etale_extension,f_is_integral_of_is_idempotent_elem,f_exists_idempotent_tmul_one_eq_of_smooth_algebra,f_range_comap_include_right_field,f_closure_generic_fibre_clopen_split,f_smooth_generic_fibre_closure_partition,f_is_open_connected_component_of_is_locally_noetherian,f_section_mem_component_generic_of_closed_valuation,f_adelic_hermitian_forms__adelic_pair,f_exists_is_hermitian_log_of_pos_def_gram,f_is_closed_is_hermitian_log_of_pos_def,f_matrix_entries_bounded_of_hermitian_log_trace_sq_le,f_entries_bounded_of_conj_spanning_bounded,f_exists_energy_min,f_foundations__pet_eq_rel_index_mul_pet_prod,f_cusp_form_gamma1_inter_gamma0_slash_rat_is_zero_at,f_foundation_proofs__hecke_u_operator_explicit_eq_sum_slash,f_foundation_proofs__hecke_u_operator_explicit_slash_invariant_gamma1_inter_g_statement,f_foundation_proofs__hecke_u_operator_explicit_slash_invariant_gamma1_inter_gamma0,f_is_zero_at_finset_sum,f_foundation_proofs__mdifferentiable_hecke_operators_explicit,f_exists_det_ne_zero_of_rows_separating,f_mem_sq_localization_of_pderiv_mem,f_exists_mul_mem_of_forall,f_exists_minimal_local_generators,f_exists_generic_jacobian_data_of_prime,f_exists_generic_jacobian_data_iterated,f_divisors__xi_mul_nu,f_divisor_base__sandwich_maps,f_determinant_lattice_principal,f_divisor_proofs__eigen_projection_quotient_lattice,f_divisor_proofs__exists_spanning_image_lattice,f_exterior_power_span_of_lattice,f_exterior_power_top_finrank_one,f_rank_one_lattice_span_singleton,f_splits,f_absolutely_closed_polynomial_splits,f_absolutely_closed_unit_coefficient_root,f_polynomial_roots_of_closed_quotient,f_newton_polygon_slope_existence,f_newton_approximation_of_dichotomy,f_valuation_add_pow_sub_le,f_valuation_sub_one_pow_eq_prime,f_exists_improved_approx_kummer_generator,f_kummer_generator_approx_critical_radius,f_kummer_automorphism_moves_integers_almost_unit,f_orbital_bounds_conclusion__sigma_star_uniq,f_period_integrals__sigma_star_uniq,f_coef_shift,f_complete,f_siegel_set_completeness,f_siegel_set_shift_invariance,f_sigma_star_uniq_of,f_zero_of_coef,f_hecke_u_operator_preserves_modular_form_gamma1_inter_gam_statement,f_hecke_u_operator_preserves_modular_form_gamma1_inter_gamma0,f_slash_rat_is_bounded_at_gamma1_inter_gamma0_level,f_unit_eq_mul_pow_on_etale_excision_nbhd_zero_locus,f_q_act_m_sub_algebra_map,f_character_augmentation_subspace_top_eq_ker_smul,f_character_augmentation_subspace_top_eq_ker_smul_statement,f_exists_idempotent_local_of_character,f_exists_idempotent_local_of_character_statement,f_finrank_quot_one_sub_idempotent_eq_mul,f_finrank_quot_one_sub_idempotent_eq_mul_statement,f_weight_space_iff_idempotent_fixed,f_weight_space_iff_idempotent_fixed_statement,f_finrank_weight_space_projective_tensor_eq,f_adjoin_inverse_is_localization_away,f_kaehler_basis_tower,f_kaehler_finrank_fraction_field,f_localization_kaehler_prime_ideal,f_kaehler_rank_localization_bound,f_exists_nat_mul_mem_range_pi_quotient_minimal_primes,f_is_of_fin_order_of_is_of_fin_order_map_ring_hom,f_pic_is_of_fin_order_of_finite_int,f_pic_pi_is_of_fin_order,f_is_of_fin_order_pic_of_is_reduced_finite_int,f_toroidal_compactification__is_completed_strict_hens,f_represents_kill_ideal,f_ideal_represents_of_away_cover,f_ideal_represents_of_away_cover_statement,f_exists_basic_open_cover_ideal_represents,f_exists_basic_open_cover_ideal_represents_statement,f_ideal_killed_by_ring_maps_with_property_le_ker_app,f_ideal_killed_by_ring_maps_with_property_le_ker_app_statement,f_affine_point_property_of_le_ker_app,f_is_closed_of_local_ideal_point_property,f_diamond_operator_of_matrix_modular_form_gamma1_inter_gam,f_gamma1_inter_gamma0_modular_form_has_sum_q_expansion,f_has_sum_hecke_u_operator_explicit,f_has_sum_hecke_v_operator_explicit,f_q_expansion_coeff_period_one_eq_of_has_sum,f_q_expansion_coeff_hecke_t_operator_gamma1_inter_gamma0,f_adelic_hermitian_forms__is_herm_hyperbolic,f_existence_of_lattices__hat1,f_exists_nsmul_mul_vec_mem,f_adelic_lattice_proofs__imports_ter,f_adelic_lattice_proofs__transvection_identities_unitary,f_exists_trace_zero_adjustment_of_hermitian_lattice,f_unitary_transvection_submonoid_adjust_integral_away,f_homogeneous_ideals__exists_ring_equiv_of_is_transcendence_basis,f_adelic_lattice_proofs__exists_ring_equiv_apply_ne_of_is_algebraic,f_adelic_lattice_proofs__exists_ring_equiv_ne_of_transcendental,f_adelic_lattice_proofs__exists_rat_of_forall_complex_ring_equiv_fixed,f_adelic_lattice_proofs__galois_stable_submodule_le_span_rational,f_mem_span_rational_kronecker_invariants,f_convex_nerve_complexes__nerve_face_closed,f_alt_double_sum,f_bd_mem,f_acyc_cone,f_acyc_directed,f_acyc_union,f_nerve_cut,f_nerve_sep,f_nerve_compact,f_nerve_convex,f_pow_form,f_divisor_proofs__poly_mul_gaussian_bounded,f_gaussian_iterated_f_deriv_weighted_exp_bounded,f_norm_gaussian_convolution_series_coefficient_le_integr,f_norm_iterated_f_deriv_multilinear_diagonal_le,f_gaussian_convolution_series_coefficient_desc_factoria,f_summable_seminorm_gaussian_convolution_series_term,f_nonempty_alg_hom_adjoin,f_adjoin_hom_extend_of_denominator,f_extend_alg_hom_adjoin_integral_root,f_is_integrally_closed_adjoin,f_linear_indep_on_pow_of_is_domain_tensor_purely_inseparabl,f_exists_primitive_element_separability_certificate,f_exists_finite_separable_point_of_separable_closure_poin,f_exists_separable_point_of_geometrically_domain,f_divisors__has_q_iff,f_divisors__zeta_act_refl,f_root_of_unity_exp_z_mod_additive_character_properties,f_tsum_residue_class_split_by_sign,f_has_sum_lambert_double_series_divisors,f_torsion_point_row_sum_eq_q_expansion_series,f_torsion_point_rows_sum_eq_divisor_series,f_hermitian_local_continuous_congruence_section,f_dedekind_power_localization,f_divisor_proofs__tensor_involution_algebra_properties,f_flat_localization_membership,f_gram_fiber_measures_unique_ae,f_localization_inverse_mod_f,f_primitive_vector_quadratic_level_measure,f_localization_residue_approximation,f_divisor_proofs__local_hermitian_diagonalization_units,f_nilpotent_approximation_surjective,f_etale_unique_prime_le_map_maximal,f_isolate_maximal_among_primes_containing_etale,f_etale_away_quotient_eq_localization,f_commuting_semisimple_eigenspaces_span,f_dvr_rep_eigenspaces_span_top,f_exists_ring_hom_of_joint_eigenvalue,f_exists_separable_annihilating_poly,f_padic_ring_hom_unique_adic_complete,f_ring_hom_from_padic_unique_of_sep,f_scalar_rep_commute_and_annihilate,f_period_integrals__add_int_g,f_period_integrals__exp_int_w,f_period_integrals__inv_ser_sub,f_exponential_integrality__development,f_exponential_integrality__inv_nat_cast_mem_witt_integers,f_roots_of_unity_ring_le_witt_integers,f_step_i_i_i,f_flog_constant_coeff,f_w2pair,f_wf_ring,f_wf_subst,f_divisor_proofs__div_fractions_bilinear_formula,f_fibre_cosine_explicit_formula,f_fibre_cosine_pushforward_uniform,f_divisor_proofs__fs_one,f_divisor_proofs__h_poly_add_two,f_divisor_proofs__mobius_change_of_variables,f_divisor_proofs__stereographic_measure_change,f_period_integrals__primes_dyadic_r_s,f_period_integrals__sqf_lab,f_sqf_prime_factor,f_ana_core,f_squarefree_prime_factor__analytic,f_big_primes,f_squarefree_prime_factor__claim_of,f_irreducible_count_lower_bound,f_monic_deg_fn_nat_degree,f_sqf_prime_factor_of,f_squarefree_count_estimate,f_commutative_algebra__dual_order,f_commutative_algebra__models,f_commutative_algebra__translate_mem_ind_order,f_global_geometry__exists_unit_form_localization_etale_nbhd,f_base_change_points_compat,f_regular_at_base_change,f_htat_bc_pull,f_p_adic_hodge__finite_flat,f_global_twisting__perm_rep_single,f_exists_free_resolution_short_exact,f_group_homology_dimension_shift_is_iso,f_group_homology_long_exact_maps_natural_of_res,f_perm_coef_preserves_short_exact,f_projective_perm_tensor_free,f_projective_rep_group_homology_pos_vanishes,f_projective_res_free_rep_of_injective,f_shapiro_is_iso_group_homology_zero,f_shapiro_lemma_transitive_group_homology,f_witt_exact_sequences__is_compl,f_cov_of_alg_hom,f_block_decomposition__exists_fg_tmul_eq_zero,f_block_decomposition__exists_perfect_radical,f_block_decomposition__exists_p_q,f_block_decomposition__exists_ring_hom_pow_prime_pow,f_block_decomposition__pf_facts,f_block_decomposition__perfect_frobenius_root_solution,f_block_decomposition__frobenius_power_solution_lift,f_block_decomposition__one_tmul_mem_range_iff,f_exists_retraction,f_global_geometry__is_cpt_gen,f_global_geometry__coords_at,f_global_geometry__etale_localization_at_prime_tensor_of_low_height,f_global_geometry__exists_gen_of_is_v_b_one,f_global_geometry__is_generic_flag,f_global_geometry__is_line_gen_on,f_global_geometry__level_sections_exact_kernel_locus_open,f_geometry_proofs__gen_map_germ_eq_gen_map_germ,f_frame_near_generic_point,f_additive_poly_taylor_coeff_sub_norm_le,f_few_roots_small_disc,f_multiset_many_separated_points,f_separated_roots_additive_poly,f_commutative_algebra__invariant_subspace_mobius_inverse_rec_eq_of_finrank_lt,f_character_theory__charpoly_block_and_invariant_under_stabilizer_nilradic,f_exists_perm_of_sum_min_eq_positive_family,f_primary_endomorphism_cyclic_decomposition_finrank_ker,f_conj_of_primary_finrank_ker_pow_eq,f_ker_aeval_add_stabilizer_nilradical_socle,f_primitive_end_class_function_eq_zero_of_primary,f_block_decomposition__perfect_tensor_product,f_block_decomposition__pq_lift,f_block_decomposition__perfect_tensor_generated_lift,f_pq_base_change_polynomial,f_valuation_at_centre_order,f_order_valuation_compare,f_character_theory__card_subspaces_of_finrank_mul_card_bases,f_card_subspaces_mul_general_linear_group_card,f_endomorphism_mass_eq_of_linear_equiv_invariant,f_finsum_subspace_stabilizer_mul_block_functions,f_endomorphism_mass_mul_parabolic_induction_trivial,f_real_place_analysis__statement_a,f_real_place_analysis__statement_b,f_real_place_analysis__statement_e,f_is_top,f_coef_diff,f_curve,f_inv_curve,f_line_deriv,f_bracket,f_gl_rel,f_subsingleton_of_adic_completion_tensor,f_torsion_of_localization_flat,f_quotient_flat_of_completion_flat,f_smul_regular_tensor_of_quotient_flat,f_localization_projective_kernel_finite,f_completion_flat_kernel_finite,f_finite_of_localization_and_completion,f_finite_projective,f_commute_image_abelian_by_prime_power_of_normal_central,f_exists_character_eigenvector_of_commuting_representat,f_exists_monomial_basis_abelian_by_prime_power,f_exists_monomial_basis_of_imprimitive,f_character_theory__imports,f_invariant_eq_top_of_irreducible,f_is_abelian_by_prime_power_group_subgroup,f_complex_analytic_sets__p_manifold_zeros_complement_connected,f_p_proper_open_projection_local_cover,f_p_unbranched_proper_count_constant,f_p_unbranched_proper_count_locally_constant,f_st_proper_open_projection_local_cover,f_st_proper_open_projection_local_unbranched,f_st_unbranched_proper_count_locally_constant,f_divisor_proofs__etale_localization_at_prime_tensor_of_low_height,f_exists_smul_dvd_of_localization_at_prime_tensor,f_finite_etale_of_galois_descent_hartogs,f_finite_of_galois_trace_relation,f_gal_map_gal_elt,f_galois_comparison_map_injective_of_flat,f_galois_element_dvd_of_formally_unramified,f_hart_tensor_of_flat,f_divisor_proofs__torsion_free_over,f_algebra_trace_map_of_cokernel_killed_by_scalar,f_discr_is_unit,f_etale_of_etale_at_height_one_primes,f_exists_smul_mem_range_of_surjective_localized_map,f_finite_length_coker_of_etale_punctured_spectrum,f_localization_tensor_map_injective_coker_killed,f_smul_mem_of_maximal_ideal_pow_of_locally_surjective,f_surjective_of_trace_of_smul_mem_range,f_commutative_algebra__chain_conn_in_dim,f_cohen_macaulay__mod_depth_g_e,f_exists_sq_zero_extend_localization_away_pow,f_exists_square_zero_lift_basic_open_pair_agree,f_divisor_proofs__is_affine_combination_in_chart_spec_map_comp,f_divisor_proofs__is_comb_in,f_divisor_proofs__lift_at,f_divisor_proofs__preimage_eq_of_square_zero_thickening,f_adelic_hermitian_forms__mem_pow_sub,f_adelic_hermitian_forms__sq_sub_le_norm_sub,f_adelic_lattice_proofs__pow_index_torsion_ker_range_mul,f_rel_index_one_units_mul_eq_card_quotient,f_subgroup_pow_image_units_congruent_one_mod_of_is_adic_comp,f_subgroup_pow_rel_index_units_of_is_adic_complete,f_global_twisting__mem_split_seq_iff,f_global_twisting__sub_closed,f_link_exactness_stability__seq_chain_boundary_comp_boundary_apply,f_split_set_perm_rep_chains_iso_split_seq_chains,f_split_sequence_rep_complex_exact,f_published_theorems__k_acyclic_homology,f_tensor_hom_cubes__is_acyclic_space,f_tensor_hom_cubes__simplex_face,f_tensor_hom_cubes__stab_directed_system,f_period_integrals__minkowski,f_period_integrals__minkowski_q,f_orbital_bounds_conclusion__minkowski,f_orbital_bounds_conclusion__minkowski_q,f_minkowski_bound__assemble,f_charpoly_dvd_of_pow_eq_one,f_minkowski_bound_of_steps,f_power_sum,f_power_sum_step,f_minkowski_torsion_free__lattice,f_unit_t_zpow,f_haar_transversals__fold_bound,f_haar_transversals__poincare_series_square_integrable,f_period_integrals__fold_mult,f_period_integrals__fold_unfold,f_orbital_bounds_conclusion__fold_mult,f_orbital_bounds_conclusion__fold_unfold,f_poincare_series_mem_lp,f_measurable_mult,f_fold_l2_double_coset,f_unfolding_identity__fold_unfold_main,f_character_theory__eq_zero_of_not_primary,f_character_theory__exists_conj_eq_add_of_is_coprime,f_finite_monic_nat_degree,f_is_unit_iff_charpoly_coeff_zero_ne,f_invertible_end_inner_product_root_power_sum_eq_torus_sum,f_inner_product_root_power_sum_eq_of_frobenius_mod_eq,f_exists_integral_hecke_eigensystem_deligne_serre,f_exists_matrices_intertwining_of_semilinear,f_finite_joint_eigensystems,f_matrix_exists_common_eigenvector_mem,f_norm_eigenvalue_le_one_of_entries,f_dvd_trace_of_balanced_tensor,f_finite_open_le_closed_fibre,f_is_fin_open_sub_of_finite,f_hodge_tate_points__val_at_restrict,f_geometry_proofs__coord_tie_comp_equiv,f_geometry_proofs__germ_gen_pt_injective_range_reg_at,f_piece_localization_at_element,f_geometry_proofs__prod_update_div,f_reg_at_is_local_ring_is_fraction_ring_stalk,f_exists_kill,f_c_m_moduli__projective_space_over_spec,f_divisor_proofs__closure_finite_etale,f_etale_away_of_is_etale_at_off_submonoid,f_divisor_proofs__etale_localization_at_prime_is_domain_is_integrally_clos,f_divisor_proofs__good_iff_etale_at,f_divisor_proofs__origin_ideal,f_divisor_proofs__point_at_zero,f_divisor_proofs__torsors_trivial,f_divisor_proofs__zmod_torsor_exists_point_finite_separable,f_homogeneous_ideals__is_domain_and_is_integrally_closed_at_prime_of_smooth_of_co,f_eval_complex_poly_eq_zero_on_rat_zariski_closure,f_adelic_lattice_proofs__mem_span_rat_polys_vanishing_of_aut_stable,f_coords_left_mul_matrix_const_base_change,f_exists_is_q_group_weil_restriction,f_exists_rational_coord_polynomial_base_change,f_exists_rational_equations_weil_restriction,f_gl_free_algebra_to_special_linear_emb_injective_hom,f_mem_rat_zariski_closure_points_iff_of_is_reduced,f_restrict_scalars_matrix_of_basis_hom_injective_is_unit,f_foundations__curve_cl,f_exists_class_degree_one,f_limits_of_shift_functionals,f_shift_functional_power_sum,f_degree_formula__flag_deg_formula,f_point_degree__perm_exp_inj,f_point_degree__pow_sum,f_etale_localization_at_prime_tensor_of_etale_away,f_corank_share__statement_f_r,f_eichler_equivalence_holds,f_has_deriv_at_sphere_chart_last,f_lf_prod,f_neighbourhood_hilbert_schmidt_holds,f_kernel_bound_rel,f_statement_c_s,f_statement_e_i,f_statement_f_u,f_statement_l_f,f_statement_m_v,f_statement_n_c,f_statement_s_b,f_character_theory__character_coset_sum_eq_zero_of_subgroup_sum,f_exists_standard_unipotent_radical_bij_on_nilradical,f_general_linear_function_extend_zero_end_properties,f_is_primitive_extend_zero_of_sum_unipotent_radical,f_p_number_field_box_count_x,f_heights__kernels_lattice,f_p_covolume_rel_index,f_p_embedding_sum_places,f_p_lattice_count_volume,f_p_lattice_image_z_lattice,f_p_mixed_box_count,f_p_number_field_box_count,f_statements_covolume_rel_index,f_statements_embedding_sum_places,f_statements_lattice_count_volume,f_statements_lattice_image_z_lattice,f_statements_mixed_box_count,f_statements_number_field_box_count,f_card_step,f_torsion_bounds_chains__face_d_single,f_fin_group,f_group_homology_long_exact,f_torsion_bounds_chains__imports_alt,f_ind_perm,f_map_nsmul,f_orb_step,f_perm_card,f_perm_empty,f_perm_split,f_perm_trans,f_torsion_bounds_chains__shapiro,f_subquot,f_torsion_bounds_chains__transport,f_period_integrals__prime_count,f_chebyshev_prime_bounds__log_factorial_eq_sum_of_le,f_chebyshev_prime_bounds__log_factorial_le,f_chebyshev_prime_bounds__prime_count_bound_of,f_chebyshev_prime_bounds__psi_lower_bound_holds,f_chebyshev_prime_bounds__psi_upper_bound_of_lt_thirty_mul_six_pow,f_claim_of_two,f_floor_half,f_theta_diff,f_wedge_line_lattice_vector_bundle,f_line_lattice_vector_bundle,f_complex_analytic_sets__st_zariski_analytic_normality,f_complex_analytic_sets__st_analytic_germs_noetherian,f_complex_analytic_sets__st_germ_weierstrass_division,f_complex_analytic_sets__st_germ_general_coordinates,f_complex_analytic_sets__p_analytic_germs_noetherian,f_complex_analytic_sets__st_prime_germ_nullstellensatz,f_complex_analytic_sets__st_prime_germ_primitive_presentation,f_st_finite_germ_projection_objects,f_st_prime_germ_projection_step,f_st_germ_projection_function_form,f_complex_analytic_sets__st_prime_germ_finite_projection,f_p_prime_germ_finite_projection,f_real_place_analysis__complexify,f_pf_d,f_partial_fraction_diagonal_identity,f_partial_fraction_off_diagonal_identity,f_partial_fraction_square_identity,f_exists_unitary_interlacing_realization,f_smith_zp,f_mahler_measure__statement,f_mahler_measure__statement_b,f_mahler_measure__statement_d,f_defs_d_v_r,f_defs_gram,f_smith_exists,f_statement_d_v_r,f_smith_determinants__statement_gram,f_truncation_chain_bound_nonneg_exponents,f_closure_prime_regular_height,f_counting_bound,f_dixmier_schur_of_rank_le_aleph0,f_operator_stable_pi_tensor_pure_kernel_span,f_simple_over,f_simple_over_stable_submodule_pi_tensor,f_simple_over_stable_submodule_tensor_pure_kernel_span,f_simple_tensor_product_operator_stable_countable,f_coker_tors,f_det_nat_abs_le_prod_l1_norms,f_full_enum,f_torsion_bounds_chains__imports,f_index_le,f_ker_orb,f_l1_map_domain_le_and_l1_face_d_single_le,f_torsion_bounds_chains__max_indep,f_quotients_equiv_of_ker_eq,f_tors_sat,f_tors_sat_mult,f_character_theory__virtual_characters_mul_comap_conj_ind_linear,f_exists_lt_commutator_mem_of_ne_top,f_inertia_eigenvalues__ind_apply_one,f_galois_cohomology₂__brauer_degree_zero,f_analytic_forms__ma_int_empty,f_potential_theory__is_potential_of_fun,f_divisor_base__model_ddc_forms,f_divisor_proofs__boundary_potential_smooth_off_divisor,f_divisor_proofs__levi_form_log_potential_formula,f_divisor_proofs__potential_smooth_in_chart,f_poincare_form_bound_of_ddc,f_sup_meas,f_semidirect_quotient_measure_conjugation_invariant,f_conjugation_measure_preserving_semidirect,f_semidirect_measure_restriction_normal_part,f_countable_transversal_measure_extension,f_normalizing_element_fundamental_domain_scaling,f_quotient_measure_conjugation_invariant,f_global_geometry__has_values,f_global_geometry__lie_model,f_geometry_proofs__exists_unique_tangent_dual_number,f_torsion_embedding_base_change,f_htat_bc_tors,f_htat_ht,f_abelian_scheme_quotients__is_abelian_scheme,f_split_tori__split_torus_aff,f_eq_of_sec_alg_top,f_kappa_apply_eq,f_section_tensor_pullback_ring_hom_bijective,f_ideal_sheaf_comap_ideal_affine_open_of_is_affine,f_divisor_proofs__affine_hilbert_ideal_sheaf_of_quotient_ideal_top,f_affine_hilbert_base_change_app_l_e_comp_spec_tensor,f_ker_affine_hilbert_tensor_pullback_eq_map,f_foundation_proofs__finite_index_of_gamma_le,f_slash_q_expansion_coeff_width_transform,f_slash_sub_q_expansion_partial_sum_is_big_o,f_coeff_eq_zero_of_sum_plus_minus_reps_eq_zero,f_exists_level_one_form_one_add_exp_decay,f_exists_eq_discriminant_mul_of_exp_decay_cusps,f_reduces_to_smaller_odd_weight_of_leading_coeff_matrix_det,f_one_add_smul_mem_of_sq_zero,f_exists_rat_projector_of_aut_stable_matrices,f_exists_rat_linear_param_block_diag_kernel,f_uniformization_proofs__exists_graded_ring_kernel_lift,f_moduli_proofs__is_noetherian_ring_of_is_adic_complete,f_iwasawa_decomposition__is_noetherian_ring_adic_completion_of_noetherian,f_algebra_tools__is_cpl_at_self,f_algebra_tools__ca_cpl_ex,f_algebra_tools__ca_cpl_map,f_algebra_tools__ca_cpl_lift,f_algebra_tools__ca_cpl_uniq,f_algebra_tools__ca_cpl_flat,f_ca_cpl_spec,f_global_geometry__eig_lat,f_quadratic_character_prescribed_places,f_exists_point_localization_prime,f_lattice_eq_of_codim_one_eq,f_geometry_proofs__reg_at_fraction_noetherian_closed,f_lattices_agree_of_height_one,f_toric_varieties__krull_domain,f_class_number_bounds__totally_real_roots,f_gal_abelian,f_totally_real_roots__gal_aut,f_totally_real_roots__gal_defs,f_gal_roots,f_totally_real_roots__le_nu_iff_pow_mem_princ,f_level_group_sup_level_inertia,f_level_lift,f_nu_basic,f_princ_top,f_units_map_surj_of_zmod,f_line_lattice_generic_sections,f_regular_everywhere_is_integral,f_valuation_centre_regular_unit,f_valuation_centre_exists,f_exists_basis_of_lattice_span,f_exists_basis_quotient_lattice_eigen,f_exterior_power_basis_lattice_principal,f_dual_lattices__small_level_class_set,f_wedge_ne_zero_of_linear_independent,f_induced_class_function_from_subgroup_trans,f_divisors__orth_subrepresentation,f_alpha_kernel_derivative_vanishes,f_exists_formal_germ_open_affine,f_lift_all_preserves_degree_and_regularity,f_lift_l_deg_reg,f_not_mod_eq_of_lt,f_regular_pair_lift_to_prime_power_field,f_capelli_identities__det_mul_expand,f_algebraic_independent_of_adjoin,f_geometry_proofs__exists_unit_of_sum_eq_one,f_contour_shift_gaussian_decay,f_gauss_tube_of_tube_good,f_tube_transform_horizontal_invariance,f_tube_transform_vertical_invariance,f_tube_transform_independent_of_base,f_siegel_eisenstein_continuation__strip_entire,f_exists_derivations_dual_to_family_of_nilpotent_aug,f_exists_generators_dual_point_derivations_augmented,f_exists_invariant_derivation_of_counital_comul,f_exists_square_presentation_of_tower,f_frobenius_subalgebra_counital_comul,f_ker_aeval_truncated_polynomial_presentation,f_square_presentation_of_counital_comul,f_truncated_monomials_linear_independent_over_constants,f_localization_closure_equal,f_lu_decomposition_of_minors,f_finite_point_extends_section,f_regular_at_translate,f_translate_into_smaller_open,f_bt_order_eq_of_le,f_foundations__alt_coeff_rho,f_flag_degree_formula,f_flag_degree_eq_discriminant_multiple,f_divisor_proofs__flag_degree_vandermonde,f_coarse_lipschitz_exponential_estimate,f_coset_series_summable_shifted,f_holomorphic_series_uniform_tube,f_section_invariance_coset_sum,f_crossing_of_walls_and_heights,f_expansion_coeff_valuation_ge,f_minor_prod_span_has_compl,f_nabla_span_c,f_step_back,f_monomial_frame_span__det_submatrix_fun,f_basis_monomials_apply,f_sat_defs,f_sat_proj,f_sat_fin,f_gen_frame_s_b_of,f_gen_frame_s_b_of_span,f_gen_frame_s_b,f_dominating_pieces_smooth,f_gen_map_stalk_map,f_geometry_proofs__gen_map_stalk_specializes,f_holomorphic_continuation__is_sing_test,f_holomorphic_continuation__null_sec,f_polynomial_derivatives__fock_mono,f_polynomial_derivatives__core_st,f_polynomial_derivatives__equiv_lift,f_fform_smul_right,f_monomial_mem_supported,f_adjoin_first_operators_preserves_family,f_polynomial_derivatives__null_stable_alt,f_k_alg_of_adjoin_restrict,f_metric_periods__in_flag_domain_one,f_metric_proofs__cont_diff_at_frame_entry,f_exists_holomorphic_normal_frame,f_weighted_polynomial_homogeneous_coeff_bound,f_projective_line_normal_frame,f_triple_deriv,f_local_unitary_normal_frame2x2,f_analytic_charts__osgood,f_analytic_charts__osgood_a,f_formalism__statement_o_c,f_formalism__statement,f_zero_free_region__statement,f_zero_free_region__small_height_log_deriv,f_norm_log_deriv_le_lam_f,f_log_deriv_right,f_zeta_inv_bound,f_landau_zero_free_bounds__statement,f_landau_zero_free_bounds__no_zero_complex_of,f_l_right,f_divisor_proofs__exists_mul_mem_integral_closure_over_generic_fibre,f_injective_trace_galois_data,f_integral_closure_over_generic_fibre_hartogs,f_integral_closure_zmod_torsor_generic_fibre_data,f_divisor_proofs__loc_hom_algebra_map,f_algebra_map_integral_closure_tensor_eq,f_etale_adjoin_root_x_pow_sub_c,f_finite_integral_closure_of_formally_unramified,f_kummer_uniformiser_adjoin_root_tensor_is_reduced,f_localization_integral_closure_artinian_reduced_domain,f_normalisation_dvr_tensor_separable_finite,f_localization_normalization_root_adjoin_is_d_v_r,f_period_integrals__zeros_window,f_period_integrals__zeros_window_in,f_right_half_with,f_jensen,f_right_chi,f_right_one,f_zero_window__transfer,f_finsum_mem_le_finsum_mem,f_zero_window__assemble,f_orbital_bounds_conclusion__zeros_window,f_is_h_t_form_over,f_geometry_proofs__std_smooth_mv_polynomial,f_ga_is_h_t_form_over,f_localization_closure_smooth,f_induced_one_sub_index_mem_degree_one_character_diff,f_lattice_generator_invert_constant,f_geometry_proofs__stalk_closed_point_to_germ_top,f_geometry_proofs__zmod_torsor_base_change_transport_point,f_line_lattice_spread,f_gaussian_polynomial_density,f_gaussian_quadratic_form_schwartz_bounds,f_norm_iterated_f_deriv_trunc_exp_i_comp_le,f_divisor_proofs__schwartz_continuous_at_of_pointwise_of_bounded,f_schwartz_taylor_partial_sum_deriv_bound,f_schwartz_taylor_series_converges,f_schwartz_tendsto_of_pointwise_uniform_bounds,f_aeval_sum_elim_eq_zero_of_mem_pts,f_eq_zero_of_contractions,f_rat_component_mem_rat_polys_vanishing_on_matrix_set,f_fourier_modulated_schwartz_bounds,f_iterated_f_deriv_weighted_integral,f_schwartz_family_pairing_integral_commute,f_schwartz_fourier_superposition,f_tempered_functional_vanish_mul,f_exists_rat_idempotent_block_diag_part_kills_span,f_exists_rat_idempotent_of_aut_stable_subspace,f_invariant_subspace_not_semisimple,f_normalized_minor_extends,f_period_integrals__weil_quot_meas,f_weil_quotient_measure__step_bruhat,f_weil_quotient_measure__lintegral_mul_avg_comm,f_weil_quotient_measure__bruhat,f_closed_subgroup_quotient_measure,f_finite_covolume_unimodular,f_quotient_measure_tower,f_modular_character_trivial_finite_covolume,f_l2_dbar_estimates__is_local_homeomorph,f_holo_section_statement,f_esymm_zero,f_line_finite,f_removable_finset,f_symmetric_sections__section,f_sheets,f_symm_diff,f_symm_growth,f_symm_vanish,f_norm_vanish_of_parts,f_norm_vanish_of_holo_section,f_jets__sum_io_pr,f_real_place_analysis__statement_k_t,f_formal_degree_bessel__statement_d_s,f_wt_near_orth_decomp,f_weight_near_diagonal_operators_bounds,f_spec_hom_ext_of_localization_away_span_eq_top,f_is_affine_combination_in_chart_unique,f_is_affine_combination_independent_of_chart,f_exists_affine_combination_square_zero_lifts_chart,f_exists_lifts_agree_of_cocycle,f_orbital_bounds_conclusion__sqf_root_shift,f_period_integrals__sqf_root_shift,f_arith_p,f_count_a,f_count_b,f_count_c,f_count_d,f_squarefree_root_shift__development,f_sum_le_prod_of_two_le,f_in_p_apply_eq_zero,f_closure_k,f_conj_transpose_eq_of_in_g,f_iterated_deriv_orbit,f_analytic_vectors__taylor,f_bochner_inequality__cas_val_k,f_bochner_inequality__layer_basic,f_casimir_algebra__mul_mul_sub_mul_mul_eq_add,f_discrete_series__defs_rep,f_discrete_series__is_inf_unitary,f_ca_cpl_quot,f_one_mom,f_integrable_rpow_gauss,f_integrable_monomial,f_gaussian_moment_recurrence,f_contr_eq_of_subset,f_fock_mom_of_basic,f_affine_hilbert_scheme_functor_is_sheaf_zariski,f_exists_ideal_sheaf_comap_eq_of_open_cover_statement,f_exists_ideal_sheaf_comap_eq_of_open_cover,f_exists_ideal_sheaf_data_of_compatible,f_ideal_sheaf_data_ext_of_open_cover,f_ideal_sheaf_data_ext_of_open_cover_statement,f_ideal_sheaf_glue_of_open_immersions,f_is_finite_flat_rank_closed_subscheme_of_open_cover,f_is_finite_flat_rank_closed_subscheme_of_open_cover_statement,f_noether_normalization_chart,f_proof_simp,f_pseudo_division,f_sum_r_mul_ne,f_p_generic_freeness,f_p_generic_freeness_closed,f_p_generic_freeness_loc,f_p_generic_noether_normalisation,f_st_generic_freeness,f_st_generic_noether_normalisation,f_high_degree_in_power_sum_ideal,f_polynomial_reduction_mod_elementary,f_power_sum_decomposition_homogeneous,f_span_psum_eq_span_esymm,f_exists_perm_normalized_minors,f_covolume_bounds__linear_independent_real_of_int_of_discrete,f_norm_det_mul_prod_sq_le_of_entry_le,f_integral_closure_fg_finite_etale_dvr,f_period_integrals__unimod_loc_std,f_unimodular_local_standard__key_def,f_key_exact,f_key_newton,f_unimodular_local_standard__rep_arith,f_unimodular_local_standard__rep_basic,f_unimodular_local_standard__rep_defs,f_unimodular_local_standard__rep_exact,f_rep_key,f_unimodular_local_standard__rep_newton,f_mollified_integrability__cls_bound_alt,f_continuous_cexp_ip,f_dens_defs,f_exp_combine,f_moll_id,f_moll_id_a,f_step_b,f_step_c,f_poincare_form_two_sided_bound,f_square_norm_bound,f_has_f_deriv_at_ev_x,f_null_operator_evaluation,f_null_stable,f_partial_deriv_quadratic_pairing,f_poly_exp_bound,f_sum_pderiv_x_mem,f_abstract,f_band_cc,f_band_kill,f_conv_assoc,f_conv_eig,f_eig_band,f_eq_zero_of_test,f_exists_compact_tail,f_fourier,f_is_band,f_kills_of_idem,f_op_le_half,f_real_bands__transl,f_unfold,f_foundations__is_d_c_reps,f_coeff_eq_zero_of_exp_decay_of_integral_identity,f_cusp_form_eq_zero_of_periodic_of_bound,f_foundation_proofs__eichler_integral_from_i_slash_change_of_variables,f_green_formula_periodic_rectangle_upper_half_plane,f_integral_conj_mul_exp_eq_conj_q_expansion_coeff,f_wirtinger_eichler,f_st_sandwich,f_witt_statement,f_witt_extension_theorem,f_anisotropic,f_anisotropic_holds,f_enlarge_step,f_witt_decomposition__imports,f_witt_decomposition__nondeg,f_one_vector,f_witt_of,f_witt_extension,f_adic_completion_principal_perfect,f_adic_completion_valuation_ring_complete_valuation_doma,f_bounded_powers_or_exists_valuation_subring_dvd,f_descent_of_points_killed,f_dvd_all_pow_of_frobenius_eq_killed_by_perfect_points,f_exists_valuation_subring_alg_closed_not_is_unit,f_frobenius_pow_equation_dvd_all_pow,f_pow_dvd_of_vanishing_at_perfect_valuation_points,f_period_integrals__unitary_approx,f_unitary_approx_fin,f_unitary_approximation__assembly,f_unitary_approximation__cayley,f_unitary_approximation__development,f_mem_int_o_e_of_is_integral,f_sigma_mem_int_o_e,f_skew_approx,f_weak_approx_f,f_general_b_fact_right_ter__imports,f_complex_analytic_sets__osgood_separate,f_p_non_isolated_fibre_curve,f_st_analytic_germ_components,f_st_irreducible_germ_curve,f_st_non_isolated_fibre_curve,f_regularisation__p_riemann_extension_slices,f_regularisation__st_riemann_slices,f_alpha_uniqueness__statement,f_fock_gram__statement_herm,f_fock_gram__statement_lat,f_hermitian_lattices__defs_c_s,f_discr_finite,f_hermitian_lattices__genus_covol_bound,f_hermitian_lattices__statement_lat,f_hermitian_lattices__statement_theta,f_theta_l_euclid,f_lattice_theta__statement,f_card_nonregular_residues_mod_pow_sub_one_le,f_no_norm_eight_of_fourier_vanishing_order_fifteen,f_no_norm_twelve_order_sixtythree,f_orthogonal_int_vectors_not_agree_on_regular,f_parseval_bound_integer_vector_small_fourier_support,f_separation_numerical_ineq_cuspidal_g_l,f_mahler_measure__level_sum,f_mahler_measure__good_count,f_mahler_measure__is_frozen_inv,f_mahler_measure__has_order,f_mahler_measure__cs_saturated,f_mahler_measure__quotient_upper_bounds_of_power_bounds,f_mahler_measure__statement_t,f_mahler_measure__statement_t_m,f_fock_resolution_onto__shift_last_letter_thresholds,f_fock_resolution_onto__statement_a,f_meets_open_cosets,f_div_w_core_lac_use_type,f_open_coset,f_chain_pf,f_sep_poly_proof,f_coset_of_cover,f_open_coset_pf,f_cycle_count,f_fin_dense_pf,f_fin_fin_dense,f_geometry_proofs__section_eq_zero_of_values,f_hodge_tate_functional_unique,f_archimedean_orbit_measures__upq,f_archimedean_orbit_measures__omega_density,f_cay_dens_ex_om,f_archimedean_orbit_measures__imports,f_archimedean_orbit_measures__is_unimodular,f_archimedean_orbit_measures__is_c_m_unram,f_archimedean_orbit_measures__base_lattice_is_unimodular,f_archimedean_orbit_measures__inst_topological_space_h_a,f_archimedean_orbit_measures__is_inf_emb,f_archimedean_orbit_measures__meas_lie,f_archimedean_orbit_measures__one_per_place,f_archimedean_orbit_measures__cay_dens_ex_sk,f_archimedean_orbit_measures__cay_dens_ex_top,f_diamond_diag_mul_eq_mul_of_dvd_lower_left_gamma1_inter_gamm,f_diamond_diag_mul_eq_mul_upper_triangular_of_not_dvd_lower_l,f_hecke_operators_on_half_plane_functions_agree_explicit,f_hecke_t_slash_invariant,f_hecke_tq_representatives_cosets_distinct,f_upper_mul_eq_mul_diamond_diag_gamma1_inter_gamma0,f_upper_triangular_mul_eq_mul_upper_triangular_gamma1_inte,f_has_fderiv_at_schwartz_operator_first,f_has_temperate_growth_prod_mk_const,f_schwartz_operator_parametric_extension,f_divisor_proofs__schwartz_seminorm_translate_sub_line_deriv_le,f_schwartz_slice_seminorm_le,f_schwartz_translate_taylor_second_order,f_adelic_hermitian_forms__is_herm_form,f_exists_denominator_primes_prescribed,f_exists_nat_smul_mem,f_exists_norm_one_reflection_correction_at_level,f_exists_pos_nat_mul_mem_ring_of_integers,f_norm_one_approximation_at_level_primes,f_adelic_lattice_proofs__unitary_quasi_reflection_laws,f_valuation_eq_one_of_norm_one_of_not_moved,f_foundations__same_part_iff_of_ne_zero,f_card_monic_squarefree_unit_const_polys_ge,f_foundation_proofs__mem_monic_squarefree_unit_const_polys_iff_monic_squarefr,f_one_sub_two_div_le_squarefree_label_mass,f_foundation_proofs__squarefree_label_torus_card_bounds_and_mul,f_cyclotomic_norms__statement_i,f_cyclotomic_norms__statement_t,f_orbital_bounds_conclusion__sigma_star_ex,f_period_integrals__sigma_star_ex,f_theta_series_existence__development,f_gen_eq_of,f_lat_ext,f_theta_series_existence__reduce,f_theta_series_existence__sigma_star_ex,f_theta_a,f_theta_deriv_ne,f_theta_nz,f_commutative_algebra__is_tight,f_commutative_algebra__step_order_res,f_hopf_order_contains_add_characters,f_hodge_tate_points__ra_char,f_dual_lattices__cotangent_surjective,f_dual_lattices__tensor_span,f_dual_lattices__valuation_det_eq_of_span_eq,f_dual_lattices__valuation_fourier_le_one,f_fock_resolution_onto__statement_b,f_non_galois_descent__fourier_match,f_non_galois_descent__linear_descent,f_non_galois_descent__unit_lemma_group,f_exists_finset_cosets_integral_norm_units,f_inertia_eigenvalues__exists_power_basis_of_charpoly_separable,f_fg_units_quot_integral_units_finite_field_ext,f_fg_units_quot_integral_units_reduced_finite_algebra,f_is_reduced_of_separable_marked_charpoly,f_complex_witt_basis_normal_form,f_conj_transpose_mul_mul_self_of_unitary_conj,f_exists_levi_element_isotropic_orthogonal_complex,f_hermitian_flag_complement_pos_def_factorization,f_hermitian_flag_unipotent_matrix_exists_sparse,f_pos_def_exists_conj_transpose_mul_mul_eq_one,f_radical_elt_moving_dual_to_majorant,f_min_weight_sum_add_cost_abs_bound,f_sizes_rows7,f_gauss_jet_bounds__statement,f_gauss_jet_bounds__statement_a,f_gauss_jet_bounds__statement_c,f_gauss_jet_bounds__statement_e,f_gauss_jet_bounds__statement_g,f_gauss_jet_bounds__statement_h,f_gauss_jet_bounds__statement_i,f_gauss_jet_bounds__statement_n,f_statement_q,f_incoming_bounds__incoming_bound,f_quot_meas_uniq,f_orbital_bounds_conclusion__weil_quot_meas,f_q_lift_is_mul_left_invariant,f_qmu_weight,f_weight,f_wq_unique_of,f_inv_inv,f_box_le_first_family,f_sym_k_eq_zero_of_om,f_symbol_first_family_of_mem,f_zero_right,f_lattice_theorem_of_discharge,f_trace_isometry_weights__statement_c,f_trace_isometry_weights__statement_f,f_trace_isometry_weights__statement_g,f_adelic_lattice_proofs__is_quadratic_sqrt_extension_basic_facts,f_adelic_lattice_proofs__height_one_spectrum_places_over_finite_set,f_two_places_of_embeddings,f_adelic_lattice_proofs__exists_two_places_over_of_is_square_local,f_adelic_lattice_proofs__kummer_galois,f_ncard_places_over_eq_of_prime_degree,f_prime_mul_card_places_le_card_over_kummer,f_parabolic_induction_trivial_preserves_virtual_charact,f_statement_p_w,f_dedekind_finite_type_ideal_codimension,f_exists_degree_lt_two_correction_simple_zero,f_exists_linear_system_maximal_degree_factorization,f_exists_low_degree_coords_mod_mul,f_exists_norm_form,f_exists_squarefree_poly_distinct_zeros_on_curve,f_norm_degree_bound_polynomial_combination,f_reduced_fibres_almost_all,f_bad_crit,f_jet_harmonics__cas_k_is_symmetric_and_form,f_compact_casimir_le_subspace_monotone,f_lev_subspace_mono,f_jet_harmonics__re_inner_le_on_image_of_intertwining,f_wt_near_le_of_add_dist_le,f_hypersurface_diff_is_preirreducible_of_no_splitting,f_hypersurface_part_geometric_irreducible_spreads,f_no_common_zero_spreads_constructible_nbhd,f_no_splitting_factorisation_of_pderiv_ne_zero,f_preirreducible_fibre_standard_etale_spreads,f_preirreducible_space_fibre_hypersurface_spectrum_iff,f_splitting_absence_spreads,f_standard_etale_mv_polynomial_hypersurface,f_fock_gram_proofs__covol_gram,f_det_sym_pow,f_fock_herm,f_fock_perm,f_fock_sesq,f_herm_dual_of,f_hermitian_tensor_mul_hermitian,f_sub_index_norm,f_statement_fock,f_statement_sym_pos,f_statement_tensor,f_sym_gram_pos_semidef,f_orbital_fiber_card_formula,f_orbital_fiber_decomposition,f_orbital_fiber_of_bot,f_orbital_fiber_pushforward,f_orbital_fiber_pushforward_eq_zero,f_symmetric_fiber_covering,f_fib_abs,f_trace_formula_eigenvalues__forms_fin,f_trace_formula_eigenvalues__is_gen_eig,f_symmetric_power_transfer__wcount,f_global_signature__invariant_radon_fibre,f_exists_bruhat_function_closed_subgroup,f_global_interpolation__exists_unique_haar_of_invariant_radon_on_cosets,f_quotient_invariant_measure_exists_unique_unimodular,f_quotient_measure_normalised_by_haar_unique,f_weil_criterion_invariant_measure_homogeneous_space,f_content_distance_bounds,f_params_window,f_joint_exact_exponent_stop_high,f_local_component_g_l,f_max_val_eq_zero_of_lt,f_pieri_block_ideals__statement,f_pieri_block_ideals__statement_c,f_pieri_block_ideals__statement_j,f_rank_gap_bounds__cloud_min_false,f_rank_gap_bounds__large_prime_factor,f_card_large_prime_factors_le_one_holds,f_one_letter_gauss_jets__odd_level_gain_sum,f_one_letter_gauss_jets__statement_j,f_gauss_jet_bounds__statement_j,f_descend,f_determinant_representations__ext_gen,f_extend_poly,f_determinant_representations__gen_eval,f_determinant_representations__gen_span,f_determinant_representations__inj_test,f_lift_indep,f_determinant_representations__map_api,f_commutative_algebra__res_map_bijective,f_weil_group_characters__rep_alg,f_metric_periods__has_multiplier,f_metric_proofs__hermitian_line_shift_properties,f_aeval_eq_zero_of_mem,f_rational_sup_metrics__hermitian_line_shift_properties,f_birational_geometry__arithmetic_hilbert_samuel_lower_bound,f_birational_geometry__is_intersection_family,f_birational_geometry__is_semipositive_on,f_birational_geometry__pen_host,f_birational_geometry__pen_vol,f_p_hol_germs_domain,f_st_germ_weierstrass_preparation,f_weierstrass_polynomial_ring,f_weierstrass_remainder_unique,f_exists_value_basis,f_formally_smooth_section_stalk,f_formally_smooth_surjective_derivation,f_one_left_congr,f_span_linear_independent_base,f_norm_iterated_f_deriv_rem_comp_le,f_schwartz_family_phase_bound,f_schwartz_fourier_representation,f_schwartz_inner_product_continuous,f_schwartz_integral_superposition,f_translation_character_invariant_form,f_first_lemma_f,f_first_lemma_g,f_imports_ter_alt,f_int_mv_pderiv,f_capelli_identities__integral_mv,f_integral_polynomial_fifth,f_integral_polynomial_first,f_integral_polynomial_fourth,f_integral_polynomial_second,f_integral_polynomial_sixth,f_integral_polynomial_third,f_capelli_identities__is_integral_nat_cast,f_unit_ball,f_jets_ph_w,f_jet_integrality__exp_log,f_period_integrals__fold_d_c_unfold,f_orbital_bounds_conclusion__fold_d_c_unfold,f_complex_double_coset,f_cplx_d_c,f_double_coset_translation,f_fold_d_c_unfold_of,f_trans_exists,f_translation_independent,f_global_geometry__is_cochar_lie,f_lie_chart,f_toroidal_compactification__is_grp_pullback,f_cubical_structures__cube_symmetric_swap_first,f_cubical_structures__cubical_pull_base_change_st,f_eventually_finite_base_change_filtered_colimit,f_exists_presentation_matrix_of_projective_base_change,f_gen_fib_map_algebra_map,f_is_z_mod_torsor_iff,f_polynomial_system_eventually_solvable_colimit,f_projective_base_change_of_presentation_matrix_split,f_projective_eventually_filtered_colimit_algebra,f_divisor_proofs__torsors_trivial_iff,f_k_h_free_bad_finite_st,f_kleiman_ampleness__k_h_free_obj,f_p_k_h_free_bad_finite,f_kleiman_nefness__alg_defs,f_kleiman_nefness__alg_s_free_st,f_kleiman_nefness__ample_st,f_kleiman_nefness__kleiman_st,f_multihomogeneous_ideals__is_field_intersection,f_period_integrals__explicit_formula,f_explicit_formula__good_height_exists,f_l_growth_defs,f_l_growth_gamma,f_l_growth_f_e,f_l_growth_zeta,f_l_growth_main,f_l_growth_final,f_foundations__not_coboundary_constant_one,f_laurent_series_eq_sum_single_mul_pow,f_laurent_series_padic_exists_pth_power_combination,f_p_adic_completion_laurent_eq_sum_pth_powers_mod_p,f_frobenius_surjective_mod_prime_cyclotomic_kummer_tower,f_cusp_span_norm_bounds__psi_e_def,f_period_integrals__tr_dual_loc,f_d_surj_def,f_t2_space_of_nonarchimedean_local_field,f_trace_of_ker,f_is_integral_of_tmul_mem,f_trace_dual_local__is_integral_nat_cast,f_trace_dual_local__imports,f_orbital_bounds_conclusion__tr_dual_loc,f_cusp_span_norm_bounds__point,f_cusp_span_norm_bounds__fraction_field_to_generic_stalk_algebra_map_eq,f_twisted_trace_formula__inverse_chamber_map,f_root_decompose_orthogonal,f_gram_det_option_formula,f_projection_erase_root_formula,f_exists_root_involution_parabolic,f_gram_root_determinant_erase,f_parabolic_residue_sum_zero,f_commutative_algebra__flag_minor,f_commutative_algebra__lie_lattice_data,f_x_pt_seq_lin,f_hodge_kernel_image_lattice,f_algebra_statements__polarised_flag_statement,f_herbrand_prime_order,f_index_range_ker_iterate_endomorphism,f_norm_difference_index_identity,f_pow_index_torsion_finite_ker_range,f_pow_prime_range_eq_iterated_difference,f_aff_char,f_generators,f_matrix_entry_abs_sum_unitary_lie_coordinates_split,f_int_mv_polynomial_coeff_abs_sum_add_le,f_piece_add,f_piece_hom,f_aeval_single_zero,f_gen_fund,f_gen_red,f_gen_trunc,f_coeff_l1_norm_nonneg,f_gen_pieces,f_gen_pieces_k,f_discharge,f_gauss_jet_bounds__statement_k,f_gauss_jet_bounds__statement_m,f_gauss_jet_bounds__statement_p,f_gauss_jet_bounds__statement_w,f_global_twisting__link_exact_aff,f_link_exactness_stability__sub_closed_and_perm_and_linear_equiv_invariant_uni_m,f_link_exactness_stability__cons_mem_uni_m_iff_map_sub_smul,f_link_exactness_stability__link_in_uni_m_eq_shorter_of_form_eq_one,f_link_exactness_stability__seq_chain_boundary_prefix_chain,f_link_exactness_stability__seq_chain_cycle_retraction_of_link_exact,f_link_exactness_stability__exists_homologous_cycle_with_entries_in_of_exact_at_links,f_link_exactness_stability__seq_complex_exact_at_of_all_links_exact_at,f_exact_at_link_succ_union_translate_of_coord_one,f_orbital_bounds_conclusion__sqf_roots_inj,f_period_integrals__sqf_roots_inj,f_squarefree_roots_injective__claim_of,f_div_count,f_two_pow_card_prime_factors_le,f_sum_sq_pow_le_two,f_card_le_sum_of_cover,f_rpow_quarter_pow_four,f_wit_base,f_wit_main,f_charpoly_eq_finsum_psi,f_character_theory__invariant_subspace_mobius_inverse_charpoly_linear_equi,f_finsum_mobius_inverse_charpoly_invariant_le,f_finsum_mobius_inverse_charpoly_transversal_subspaces,f_sum_primitive_end_class_function_restrict_mixed_subspac,f_is_primitive_end_class_function_invariant_subspace_mobi,f_gauss_jet_bounds__statement_u,f_minor_defs,f_minor_b,f_minor_core_a,f_minor_core,f_minor_iter,f_minor_formula,f_minor_formulas__cay_div_of,f_mollified_integrability__cls_gain_st,f_misc_lemmas_p__imports,f_anti_e_is_gl_rep,f_gelfand,f_gelfand_series,f_gelfand_h_w,f_tensor_v,f_partial_trace,f_resolvent,f_tensor_representations__residue,f_fock_resolution_onto__statement_c,f_fock_resolution_onto__statement_e,f_compact_casimir_bound_elementary_apply,f_jet_harmonics__compact_casimir_le_tensor_operator_raise,f_jet_harmonics__sum_norm_add_sq_le_of_bounds,f_base_change_lift_class_function,f_frobenius_shape_of_side_preserving,f_divisor_proofs__galois_twisted_norm_g_l_basic_properties,f_is_conj_of_is_conj_gl_field_extension_inclusion,f_divisor_proofs__nonempty_equiv_of_card_hom,f_divisor_proofs__nonempty_linear_equiv_of_pi_fin_pow_finite,f_orbital_bounds_conclusion__prime_count,f_chebyshev_prime_bounds_log_fact,f_count_succ_le,f_small_loop,f_cay_dens_ex_cay_s,f_cay_dens_ex_cay_k,f_abhyankar_exists_fraction_localisation_normalisation,f_abhyankar_exists_local_kummer_element,f_abhyankar_ramification_idx_eq_one,f_abhyankar_root_mem_maximal_ideal_non_zero_divisors,f_divisor_proofs__is_artinian_ring_kummer_adjoin_root_quotient_root,f_kummer_unit_radicand_quotient_root_is_reduced,f_maximal_ideal_localization_eq_span_of_reduced_artinian_a,f_maximal_ideal_span_image_uniformizer,f_uniformizer_eq_pow_ramification_idx_mul_unit_integral_cl,f_cauchy_parallelogram_upper_half_plane,f_eichler_integral_from_i_tail_exponential_decay,f_eichler_period_polynomial_limit_at_cusp,f_integrable_on_vertical_ray_norm_integral_le,f_poly_degree_slash_action_right_action_properties,f_top_side_integral_tendsto_zero,f_ext_v_statement,f_toroidal_compactification__two_weight_eq_one_add_root,f_extension_descent__const_gen,f_extension_descent__nonzero_locus,f_rt0_conj_neg_ne_zero,f_conjugate_root_zero_second,f_abs_zeta_prime_sum_error_le_of_large,f_abs_zeta_prime_sum_error_le_of_one_le,f_gz_p_n_t_of,f_integral_eq_interval_integral_add_compl,f_norm_integral_compl_le,f_riemann_zeta_ne_zero_of_mem_rectangle,f_is_full_level_at,f_conjugate_root_zero_third,f_cor_a3prime_b,f_jacobi_path_weights__defs_col,f_jacobi_path_weights__det_letters,f_jacobi_path_weights__index_weights_dominance,f_jacobi_path_weights__lift_word,f_jacobi_path_weights__statement_a,f_jacobi_path_weights__statement_b,f_jacobi_path_weights__statement_e,f_jacobi_path_weights__statement_p,f_jacobi_path_weights__valuation_products_components,f_conjugate_root_zero,f_dual_lattices__map_smul_one_mul_vec,f_dual_lattices__moduli_points_state,f_dual_lattices__nset_exp_injective_surjective,f_one_add_pow_of_sq,f_dual_lattices__series_state,f_dual_lattices__sq_zero_of_span,f_dual_lattices__st_thm_a,f_dual_lattices__st_thm_a_full,f_dual_lattices__tangent_pairing_statement,f_thm_a_full,f_smooth_group_tangent_lift,f_nontrivial_transvection,f_exists_isotropic_basis_nonorthogonal_two_vectors,f_quasi_reflection_eq_mul_transvections_of_hyperbolic_pla,f_quasi_reflection_eq_unitary_transvection_mul,f_special_unitary_hyperbolic_plane_mem_transvections,f_unitary_transvection_submonoid_normal_det_one,f_exists_coordinate,f_one_letter_gauss_jets__statement_f,f_differentiable_class_function_param,f_iterated_deriv_zero_of_bound,f_s_prime_of,f_continuous_herm,f_differentiable_of_top,f_mem_right_inv_right_twisted,f_mem_tw_inv,f_finrank_twisted_left_invariant_mul_of_free_action,f_finrank_order_three_relation_add_twisted_invariant_le,f_finrank_cocycle_extension_le_order_three_relation_add,f_finrank_cocycles_add_twisted_invariant_le_extension,f_finrank_eichler_shimura_cocycles_le_gamma1,f_fundamental_domains__signature,f_hermitian_trace_forms__exists_orthogonal_basis_dot_product_apply_eq,f_exists_anisotropic_orthogonal_basis_hermitian,f_exists_quasi_reflection_prod_mul_vec_eq,f_unitary_matrix_eq_prod_quasi_reflections,f_product_formula_haar__norm_mod,f_norm_index,f_card_quotient_eq_abs_norm,f_mod_f_iota_finite_place,f_product_formula_haar__res_char_iff,f_norm_st,f_product_formula_haar__tr_base,f_period_integrals__prod_formula_e,f_w0_eq_of_rt_eq,f_period_integrals__iso_inv_metric,f_orbital_bounds_conclusion__iso_inv_metric,f_col_choice_fintype,f_hermitian_vector_map,f_hv_scalar,f_iso_inv_metric_of_hw,f_metric_constant_bound,f_oe_eq_of_range_sub,f_poly_eq_zero_of_circle,f_quotient_rank,f_symmetric_measure_l2_norm_eq_resolution_l2,f_vnu_map_zero,f_mem_range_of_integral_at_height_one_over,f_mem_reg_at_of_codim_one,f_line_lattice_generator_codim_one,f_scheme_cohomology__regular_local_domain,f_scheme_cohomology__regular_u_f_d_serre,f_scheme_cohomology__regular_u_f_d_localization,f_st_adic_completion_regular,f_st_derivation_adic_completion,f_st_derivation_cotangent_independent,f_complex_analytic_sets__st_flat_normal_fibres,f_complex_analytic_sets__st_formal_fibres_regular,f_st_formal_fibres_regular_polynomial,f_complex_analytic_sets__st_jacobian_prime_derivations,f_st_regular_quotient_independent,f_p_formal_fibres_regular_polynomial,f_link_exactness_stability__seq_chain_cycle_bounded_by_cone,f_exact_at_of_links_outside_exact_at_of_coned,f_exact_at_link_nil_coord_subspace_union_translate,f_divisor_base__omega_factorization,f_divisor_proofs__k_fac_differentiable,f_hecke_phi_fourier_constant_at_zero_zero,f_divisor_proofs__hecke_phi_fourier_constant_at_zero_differentiable_on,f_is_smooth_holomorphic_in_sigma_family_mul_left,f_divisor_proofs__is_smooth_holomorphic_in_sigma_family_add,f_upper_half_plane_product_prod_im_rpow_cont_diff_on,f_prod_im_iterated_wirtinger_deriv_word_differentiable_on,f_hecke_eisenstein_zero_frequency_part_is_smooth_holomorphic,f_hecke_eisenstein_zero_frequency_part_is_smooth_holomorp_statement,f_divisors₂__partial_zeta_functional_equation,f_ferrand_pushout_affine_flat_and_pushouts,f_flat_ferrand_pushout_over_fibre_product,f_flat_quotient_smul_top_of_surjective_flat,f_is_pullback_of_forall_is_pushout_app,f_is_pushout_app_l_e_of_is_pullback_of_is_affine,f_mul_tensor_injective_of_flat_base_change_ker_inf,f_r_tensor_injective_of_pow_smul_eq_bot,f_schlessinger_flat_fibre_product,f_base_change_kernels__affine,f_pt_af_type_main,f_x_pt_af_type,f_divisor_base__trace_dual_different,f_exists_equiv_fourier_classes_pos_cone_summand,f_exists_equiv_lattice_classes_fibre_summand,f_hilbert_eisenstein_nonconstant_terms_has_sum,f_lattice_sum_eq_cone_sum,f_lipschitz_constant_inverse_different_eisenstein,f_mem_trace_dual_signed_positive_cone_iff_totally_positive,f_rep_ne_zero,f_dense_coordinate_torus,f_integral_ang_meas,f_section_boundary_closed_and_codense,f_snc_boundary_coordinate_chart,f_levi_forms__is_reg_family_inhabit_statement,f_plurisubharmonic_functions__is_psh_locally_integrable_statement,f_potential_theory__psh_shift_a,f_root_power_sum_character_additive_and_x_sub_one_pow,f_divisor_proofs__exists_block_parabolic_subgroup_levi_projection,f_pairing_cuspidal_character_g_l_root_power_sum_character,f_pairing_harish_chandra_induction_charpoly_function,f_twisted_harish_chandra_induction_g_l_is_twisted_class_fun,f_compact_casimir_bound_embedded_component,f_tensor_product_action,f_iota_scalar_one,f_charpoly_eq_quotient_charpoly_pow,f_cyclic_generators_invariant_top,f_exists_cyclic_generators_separable_min,f_c_m_type_galois__statement_field,f_c_m_type_galois__statement_group,f_quad_discr,f_dirichlet_density__statement,f_omega_poly,f_dedekind_factor_k,f_lat_i_top_basis,f_formalism__statement_c_m,f_p_holomorphic_kernel_fibre,f_p_injective_holomorphic_inverse,f_st_holomorphic_kernel_fibre,f_st_injective_holomorphic_inverse,f_st_injective_holomorphic_jacobian_ne_zero,f_st_injective_holomorphic_open,f_cyclic_kummer_norm_fixed_hilbert90,f_adelic_lattice_proofs__exists_superset_mem_s_units,f_exists_unit_valuation_eq_of_adm,f_galois_places_transitive,f_hilbert90_s_units_kummer,f_valuation_unramified_kummer_of_coprime_unit,f_adelic_lattice_proofs__with_zero_eq_of_le_exp_iff,f_compact_casimir_bound_projection_dual_tensor,f_p_poly_local_generators_diff,f_arithmetic_bezout__statements,f_statements_poly_local_generators,f_p_jacobian_prime_derivations,f_st_cotangent_basis_in_prime,f_st_derivation_minor_of_detection,f_st_local_generators_clear_denominators,f_st_poly_derivations_detect_square,f_complex_analytic_sets__statements_area,f_local_hermitian_forms__even_val,f_local_hermitian_forms__is_fix_map_iff,f_local_hermitian_forms__lcount_norm,f_local_orbit_counts__dat_smul,f_local_orbit_counts__descent,f_split_m,f_local_orbit_counts__w_trans,f_local_hermitian_forms__norm_one_is_coboundary_unramified_quadratic,f_split_unit_elements__split_s,f_divisors__gal_map_mul,f_divisors__ind_et_of_forall_finset,f_galois_geometry__is_matrix_form,f_galois_geometry__is_strictly_semistable_alt,f_divisor_proofs__preserves_filtered_colimits_add_comm_grp_iff_elements,f_preserves_filtered_colimits_module_cat_iff_forget_iff_el,f_moduli_proofs__is_ind_etale_of_forall_finset,f_divisor_proofs__comap_maximal_ideal_eq_origin,f_etale_at_prime_base_change_of_integral_closure_etale,f_divisor_proofs__is_z_mod_torsor_finite_projective_base_change,f_orbital_bounds_conclusion__self_dual_loc,f_period_integrals__self_dual_loc,f_self_dual_local_basis__assembly,f_dual_basis,f_hform_sum_right,f_hvec_apply,f_self_dual_local_basis__loc_basis,f_self_dual_local_basis__nondeg,f_one_tmul_mem_oloc,f_self_dual_loc_of_dirs,f_self_dual_loc_of_loc_basis,f_pad_fam,f_alternating_coefficient_formula,f_hook_functional_power_sum,f_hook_functional_power_sum_other,f_kappa_formula_hook_schur,f_uniform_theta_substitution__odd_log_relation,f_uniform_theta_substitution__cyclic_power_class_of_exp_equiv,f_uniform_theta_substitution__statement_m,f_places_add_class,f_tensor_relations_g_l__k_type_data,f_tensor_relations_g_l__step_formula,f_casimir_bounds__expand,f_re_swap_sum_le,f_count_same,f_count_cross,f_cas_bound_holds,f_unramified_integrals__mod_defs,f_unramified_integrals__mod_basic,f_unramified_integrals__mod_delta_int,f_unramified_integrals__mod_eis_int,f_unramified_integrals__mod_g_eis,f_unramified_integrals__mod_j_tau,f_unramified_integrals__mod_q_prin,f_c_m_good_models__statement,f_is_fam_const_level_one,f_k_h_free_indep_st,f_p_k_h_free_indep,f_regular_local_ring_fraction_field,f_geometry_proofs__spec_stalk_specializes_comp,f_rep_g_apply,f_th_facts,f_coeff_scale,f_fin_m_h,f_mem_homogeneous_exponents_one_block,f_h_option,f_hq_three,f_homogeneous_trace_diagonal,f_tr_swap,f_twine_c,f_eps_of_c_zero,f_gamma_function_bounded_support,f_exponential_gamma_integral_formula,f_gamma_integral_alternating_sum,f_epsilon_alternating_sum_zero,f_gauss_jet_bounds__statement_y,f_cube_map_triple_product_unique,f_p_eq_q_of_neg,f_discrete_valuation_numbers__objects,f_statements_clopen_components,f_statements_component_degree,f_statements_components_additive,f_statements_int_num_components,f_statements_clopen_degree,f_p_clopen_degree,f_intersections__statements,f_birational_geometry__inter_st,f_adelic_euler_products__count_data,f_cusp_representatives_finite,f_exists_cusp_reduction_bound,f_mobius_action_upper_half_plane,f_unit_balancing_imaginary_parts,f_reduction_to_siegel_domain,f_fock_resolution_onto__statement_d,f_e_arith,f_bijective_linear_combination_of_rank_at_stalk,f_exists_open_affine_hilbert_chart_basic_locus,f_free_module_complement_support_compact,f_is_pullback_pb_map,f_mem_support_quotient_iff,f_mem_support_quotient_span_iff_of_is_pushout,f_sections_finite_flat_rank_of_finite_flat,f_support_of_quotient_flat_module,f_tangent_vector_of_dual_hom,f_continuous_on_cos_sq,f_cosine_square_pushforward_uniform,f_local_density_bound_near_point,f_foundations__exp_upper,f_foundations__letter,f_foundations__op_l_d_one_sub_mem_triv,f_foundations__is_root_one,f_foundations__eigen_of_two_step,f_foundation_proofs__gl_two_pos_rat_mobius_basic_laws,f_kummer_class_eval_eq_zero_of_vanishing_on_congruence,f_kummer_potential_relation_trivial_eq_zero,f_map_eisenstein_div_period,f_harish_chandra_induction_g_l_trivial_orthogonal_hyperpl,f_gauss_jet_bounds__statement_s,f_gauss_jet_bounds__statement_v,f_gauss_jet_bounds__statement_x,f_p_n_t_dens_ls_a,f_l_function_bounds_proofs__l_function_eq_g_of_one_lt,f_l_function_bounds__positivity_bound,f_l_function_bounds__statement,f_formalism__statement_f_l,f_formalism__statement_u,f_formalism__zeta_nonvanishing_chebyshev_weights,f_formalism__zeta_nonvanishing_general_weights,f_augmentation_quotient_equiv_lattice,f_comap_fg_of_valuation_ring,f_form_mem_lin,f_misc_lemmas_l__imports,f_dual_lattices__exists_smul_mem_of_mem_span,f_period_integrals__fgl_gram,f_period_integrals__fgl_ph_split,f_ph_dual_gram,f_dual_gram_substitution__be_mul_by_zero,f_dual_gram_substitution__has_subst_ren,f_ph_dual_gram_main,f_formal_group_splitting__add_preserves_exp_congruence,f_formal_group_splitting__development,f_formal_group_splitting__exp_congruence_extends_to_sum,f_formal_group_splitting__orthogonal_split_polarization_vanishes,f_exists_kummer_character_of_upper_half_plane_root,f_foundation_proofs__upper_half_plane_holomorphic_germ_properties,f_exists_eichler_shimura_potential_of_homogeneous_poly_co,f_gamma1_cap_gamma0_level_acts_freely_upper_half_plane,f_flag_measures__prim_of_is_unit_det,f_exists_primitive_add_char_involution_invariant,f_is_primitive_tuple_of_linear_independent_finite_ring,f_norm_gauss_sum_hermitian_form_linear_le,f_card_hermitian_quadric_affine_subspace_residue_ring,f_ncard_dependent_vectors_affine_gram_le,f_card_primitive_tuple_extensions_le,f_ncard_primitive_tuples_with_gram_matrix_residue_ring,f_form_off_variety_mul,f_rational_sup_metrics__aeval_coord_prod,f_is_form_off_mul,f_k_h_free_decomp_st,f_p_k_h_free_decomp,f_foundation_proofs__diag_mod,f_exists_unit_eval_eq_kummer_class,f_local_power_units_tower_closure_properties,f_foundation_proofs__tower_unit_class_mod_prime_pow_properties,f_small_on_walls_near_discriminant,f_vanishing_on_walls_divisible,f_wall_set_compact_dominant,f_x_sub_x_dvd_of_vanish_on_open_hyperplane,f_chebotarev__n_z_ideal,f_chebotarev__euler_fac,f_chebotarev__euler_fin,f_chebotarev__euler_lim,f_chebotarev__euler_sum,f_chebotarev__prime_asymp,f_chebotarev__prime_cont,f_chebotarev__prime_sum,f_chebotarev__casimir_power_surjective_symmetric,f_chebotarev__chebyshev_lambda_sub_psi_bounded,f_chebotarev__split_def,f_chebotarev__split_f,f_chebotarev__split_c,f_lie_model_pullback_equivalence,f_eisenstein_translation_products__semi_char,f_eisenstein_translation_products__legendre,f_eisenstein_translation_products__theta_line,f_eisenstein_translation_products__theta_zero_log_derivative,f_eisenstein_translation_products__theta_zero_translate_product,f_eisenstein_translation_products__translate_product,f_eisenstein_translation_products__c_m_quasi_period_const,f_quadratic_semicharacters__is_semi_char,f_quadratic_semicharacters__product_theta_mem,f_period_integrals__ker_tens,f_mat_h_h_one,f_tens_spans,f_orbital_bounds_conclusion__ker_tens,f_etale_integrally_closed_in_localization,f_extension_descent__base_over,f_extension_descent__lin_comb_triv_g,f_theta1,f_extension_descent__theta_pt,f_theta_v_v,f_annihilator_quotient_smul_top_of_free,f_module_free_of_regular_of_free_quotient_local,f_divisor_proofs__purity_free,f_general_b_fact_side__imports,f_cohen_macaulay__bridge,f_cohen_macaulay__exists_is_regular_append_of_mod_depth_g_e,f_maximal_ideal_squares__ring_krull_dim_quotient_span_singleton_add_one,f_lie_lattice_range_of_stalk,f_normal_lattice_range,f_multihomogeneous_value_well_defined,f_valuation_unique_on_forms,f_gen_pt_specializes,f_gen_pt_specializes_of_specializes,f_is_unit_of_basic_open_nonempty_of_universally_closed,f_function_on_connected_fibre_unit,f_harish_chandra_descent__descent,f_positive_negative_holds,f_simultaneous_eigenvectors__bl_simeig,f_bochner_inequality__is_k_unitary_of_is_inf_unitary,f_bochner_inequality__k_unit_b,f_casimir_algebra__casimir_k_khw_vec,f_sl2_raise_pow_succ_lower_apply_eq,f_is_chain,f_exists_chains_of_range,f_cb_is_chain_apply,f_cb_exists_chain_of_gen,f_chain_a,f_chain_b,f_centralizer_representatives__normal,f_dex_block_frame,f_dex_global,f_centralizer_representatives__imports,f_cauchy_slice_eq_removable_extension,f_differentiable_at_coordinate_cauchy_integral,f_riemann_extension_coordinate_hyperplane,f_extension_across_zero_of_exp_two_pi_i_bound,f_locally_bounded_off_coordinate_hyperplanes,f_extension_across_coordinate_hyperplanes,f_matrix_bound_holds,f_general_b_fact_rest__imports,f_cohen_macaulay__ass_dim,f_cohen_macaulay__unmixed,f_cohen_macaulay__ring_krull_dim_quotient_of_mem_associated_primes,f_gor_indep_statement,f_ring_krull_dim_quotient_add_one_le_of_lt,f_basis_e_apply,f_den_eq_one_of_forall_padic_norm_le_one,f_prod_formula_e_of,f_exp_sum_lower_bound,f_rect_residue,f_rect_double_pole,f_capelli_identities__fixed_subgroup,f_hecke_algebras__continuous_torus_character,f_ordinary_hecke_characters__iw_mem_mul,f_ordinary_hecke_characters__iwahori_pro_unipotent_finite_index,f_ordinary_hecke_characters__u_op_sum,f_ordinary_hecke_characters__u_op_mul,f_ordinary_hecke_characters__u_op_nat,f_ordinary_hecke_characters__u_op_level,f_ordinary_hecke_characters__sp_stab,f_mem_val_in_of_invariant_and_values_mem_pow,f_kummer_character_additive_on_congruence,f_markov_inequality_holds,f_algebra_map_norm_tensor_eq_prod_conjugates,f_exists_ring_hom_adic_completion_under,f_hasse_norm_principle_of_cyclic_tower,f_hilbert90_base_change,f_is_norm_from_base_change_base_change_properties,f_is_norm_from_base_change_of_pow_finrank_cyclic,f_of_intermediate_field_tower,f_tensor_exists_of_galois_fixed,f_cont_diff_on_hecke_eisenstein_fourier_term,f_has_deriv_at_hecke_term_decay_integrand,f_hecke_y_derivative_term_integral_polynomial_decay,f_int_z_eq_fourier,f_integrable_hecke_term_decay_integrand,f_norm_hecke_term_decay_fourier_integral_le,f_orbital_bounds_conclusion__unit_det_root,f_period_integrals__unit_det_root,f_det_mem_of_entries,f_glob_fin,f_glob_top,f_glob_vol,f_global_l_unit,f_ideal_pow_principal,f_norm_le_one_of_root,f_nsmul_rel_idx_mem,f_unit_determinant_root__partial,f_unit_det_root_of,f_general_b_fact_left_ter__imports,f_chebotarev__abs_prod_sub_prod_le_sum_abs_sub,f_c_trick,f_chebotarev__ucoord,f_ker_base_changed_reduction_eq_span_x,f_det_leading_minor_gram_iwasawa,f_exists_hermite_reduced_lattice_basis,f_gram_leading_minor_lower_bound_integral,f_gram_minor_swap_adjacent_columns,f_iwasawa_decomposition_real_matrix,f_siegel_cover,f_unipotent_upper_size_reduction,f_hyperboloid_chart_measure_formula,f_period_integrals__rhs_w_lim,f_chart_jac,f_chart_lim,f_weighted_limit_gauge__orbit_push_cut,f_weighted_limit_gauge__orbit_push_e,f_orbit_push_loc,f_orbit_push_q,f_weighted_limit_gauge__volume_lie_e,f_link_exactness_stability__exists_g_l_moving_unimodular_pair_to_last_basis,f_link_exactness_stability__exists_g_l_split_seq_standard_of_stable_range_le,f_g_l_transitive_split_set_of_stable_range_le,f_period_integrals__loc_lat_eq,f_orbital_bounds_conclusion__loc_lat_eq,f_avoid_p,f_core_fg_of_le,f_core_gen_ideal,f_local_lattice_equality__development,f_ep_nontrivial,f_local_lattice_equality__imports,f_exists_finite_iwahori_double_coset_representatives,f_desc_st,f_desc_pf,f_fin_det_pf,f_finite_detect_statement,f_finite_dimensional_base_span,f_fun_ker_st,f_fun_ker_pf,f_ker_core_st,f_ker_core_pf,f_rationality_holds,f_commutative_algebra_height__is_local_hom,f_commutative_algebra_height__cpl_is,f_commutative_algebra_height__cpl_uniq,f_commutative_algebra_height__highest_weight_space_finite,f_capelli_identities__level_of_congruence,f_saturated_chains__is_saturated_chain,f_covolume_bounds__differentiable_on_of_tendsto_locally_uniformly_on,f_analytic_doubling_map_local_inverse,f_analytic_group_law_bounded_commutator,f_doubling_limit_local_logarithm,f_iter_differentiable_on,f_local_logarithm_homomorphism,f_riemann_form_period_determinant,f_harish_chandra_induction_g_l_is_character,f_hermite_normal_forms__smul_strict_mono,f_reduction_bounds_torsion__act_l_pos,f_rank_span_le,f_s_b_star_odd_of,f_is_prim_cmap,f_res_ring,f_reduction_bounds_torsion__s_b_star,f_reduction_bounds_torsion__s_b_star_odd,f_reduction_bounds_torsion__s_bridge_alt,f_exists_nsmul_eq_zero_of_tmul,f_s_b_star_of,f_inertia_ramification__average,f_inertia_ramification__cond_dvd,f_conductor_dvd_field_conductor_of_mem,f_inertia_ramification__conductor_local_part_dvd_iff,f_inertia_ramification__duality,f_exists_host_data_wild,f_inertia_ramification__host_degree,f_inertia_ramification__is_imag_quad,f_inertia_ramification__log_root_disc_char,f_inertia_ramification__quadratic_character_legendre_symbol,f_inertia_ramification__two_power,f_exists_local_zero_expansion_of_bound,f_local_zero_expansion_with_multiplicity,f_landau_local_of,f_log_deriv_bound,f_zero_factor,f_coefficient_bound_membership,f_orbital_bounds_conclusion__phi_cube_of_factor,f_period_integrals__phi_cube_of_factor,f_exp_mv_eq,f_formal_group_common__coeff_single_lg,f_formal_group_common__exp_log,f_divisor_proofs__exists_filtered_colimit_finite_type_int_rings,f_locally_surjective_of_iso_on_finite_type_approximation,f_p_normal_germ_integrally_closed,f_complex_analytic_sets__st_normal_germ_integrally_closed,f_st_rueckert_nullstellensatz,f_exists_form_defining_value,f_exists_form_with_valuation,f_exists_adic_limit_mem_automorphic_space,f_u_operator_pow_eventually_invariant_mod_pow,f_approximation_of_square_identity,f_toroidal_compactification__push_invertible,f_dominates_lift_unique,f_join_col,f_gaussian_det_square_integral,f_gaussian_det_levi_integral,f_complex_analytic_sets__st_area_multiplicity,f_p_area_multiplicity,f_statements_area_multiplicity_weight,f_p_area_multiplicity_weight,f_foundation_proofs__two_var_poly_subst_matrix_basic_laws,f_cocycle_is_coboundary_of_neg_central_element,f_foundation_proofs__exists_scalar_gamma1_cap_gamma0_mod_level,f_homogeneous_poly_cocycle_diff_coboundary_of_eq_on,f_height_one_prime_dvr_stalk,f_g_field,f_k_irreducible_existence_holds,f_root_bound_of_square_identity,f_behrend_sets__statement,f_behrend_sets__statement_e,f_coeff_pow_eq_zero_of_lt,f_mem_window_iff,f_mul_abs_sub_lt,f_prob_eq_sum_ite,f_prod_dim_v_ne_zero,f_select,f_space_free_of_behrend_free,f_totient_le_of_is_primitive_root,f_two_le_cast_of_two_le,f_two_pow_dvd_pow_two_pow_sub_one,f_final_e,f_exists_regular_local_extension_with_simple_root,f_regular_smooth,f_generic_fiber_gluing__plus_condition_to_zero_condition,f_generic_fiber_gluing__semistable_complete_split,f_generic_fiber_gluing__semistable_reduction_plus_split,f_precomplete_bases__is_precomplete_of_basis,f_split_tori__is_torus,f_range_j_subset_ab_locus,f_cone_b_defs,f_gaussian_fourier_conj_power,f_schwartz_fourier_preimage,f_fourier_nonvanishing_unit_point,f_fourier_weight_integral_symmetry,f_exists_test_fourier_nonvanishing,f_fourier_continuous_nonvanishing,f_convolution_decay_integrable_fourier,f_convolution_family_integrable,f_exists_convolution_nonvanishing_weight,f_foundations__is_herm_n_d,f_semilocal_frames__complement_reference_compact_subgroup,f_semilocal_frames__g_frames,f_flag_measures__imports_tail,f_local_lattice_between_scaled_standard_lattices,f_mem_span_single_iff,f_complex_analytic_sets__p_riemann_extension_analytic,f_complex_analytic_sets__st_riemann_extension_analytic,f_p_growth_off_hypersurface_polynomial,f_st_entire_polynomial_growth,f_st_growth_off_hypersurface_polynomial,f_hida_complete_rings__cofinal_compl,f_hida_complete_rings__fin_compl,f_hida_complete_rings__fin_max,f_hida_complete_rings__idem_lift,f_hida_complete_rings__loc_char,f_capelli_identities__precomplete_of_finite,f_hida_complete_rings__loc_abs,f_hida_complete_rings__max_idem,f_hecke_restr,f_arithmetic_bezout__cone_ball,f_arithmetic_bezout__statements_cone_slab,f_ring_krull_dim_quot_bot_one,f_frame_proj_eq,f_st_graph_jac_continuous,f_st_area_graph_piece,f_p_area_graph_piece,f_volume_lt_hausdorff_unit_ball_twenty,f_parts_of_square_identity,f_test_obj,f_dual_weyl_coordinates__defs_obj,f_dual_weyl_coordinates__defs_mod,f_dual_weyl_coordinates__statement_a,f_dual_weyl_coordinates__statement_b,f_dual_weyl_proofs__b_core_w,f_dual_weyl_proofs__b_core_t,f_dual_weyl_proofs__qb_indep_field,f_dual_weyl_proofs__qb_basis_apply,f_window_bound_odd_cases,f_dual_weyl_coordinates__filtration_theorem_of_clauses,f_jet_harmonics__is_adic_colimit_of_factor,f_is_adic_complete_of_pow_le_of_pow_le,f_extension_descent__deg_unif,f_extension_descent__thick_trans_comp,f_abelian_scheme_quotients__q_surjective,f_abelian_scheme_quotients__split_ext_defs,f_local_hermitian_forms__even_of_norm,f_local_orbit_counts__hs_n_e,f_nonsq_mul,f_local_orbit_counts__norm_ex,f_local_orbit_counts__sqrt_o,f_sum_shift,f_p_normal_zeros_nowhere_dense,f_st_irreducible_germ_regular_connected,f_complex_analytic_sets__st_normal_zeros_nowhere_dense,f_st_regular_locus_dense,f_dual_lattices__cokernel_length_comparison_of,f_dual_lattices__cokernel_length_comparison_statement,f_eigen_quotient_smith_statement,f_dual_lattices__restricted_hopf_order_approximation_statement,f_dual_lattices__unramified_cokernel_length_statement,f_dual_lattices__unramified_cokernel_lower_bound_of,f_dual_lattices__unramified_cokernel_lower_bound_statement,f_commutative_algebra_height__k_stable_highest_weight_vector,f_moduli_nonempty_of_obj,f_casimir_and_root_bounds,f_bt_order_value_eval,f_der_ring_injective,f_geometry_proofs__exists_lie_model,f_is_irreducible_iff,f_foundations__smooth_part_stable,f_double_coset_operators_comm_of_anti_involution,f_infinity_type,f_is_open_stabilizer,f_is_open_stab_of_mem_nhds,f_reg_alg_fam,f_transpose_inv,f_finrank_fixed_eq_one,f_trace_mul_of_finrank_one,f_witt_logarithm,f_additive_integral_groups__coeff_pow_mem_s,f_additive_integral_groups__d_x_eq_derivative,f_additive_integral_groups__glue_holds_var,f_additive_integral_groups__gu_line,f_additive_integral_groups__subst_mem,f_inv_nat_mem_wf,f_coef_wf_iff,f_formal_logarithm_holds,f_wf_log_of,f_fock_q_row_div_adj,f_fock_row_adj,f_fock_sub_adj,f_l_fockq_lemmas,f_fock_space_tableaux__l_focks_lemmas,f_graded_weyl_divisibility__statement_a,f_graded_weyl_divisibility__statement_b,f_real_place_analysis__fock_pair_gl,f_real_place_taylor__prod_factorial_support_sub_single,f_archimedean_gaussian_fourier,f_quadratic_level_set_density,f_real_gaussian_fourier_transform,f_schur_function_compact_support_modulo_unipotent,f_simultaneous_normal_form_majorant,f_alternating_difference_term_window,f_inertia_eigenvalues__dlt_eq_zero,f_finite_scheme_map_from_special_fibre,f_cpl_quot,f_kur_defs,f_norm_eq_of_norm_sub_lt,f_norm_nat_cast_cl_of_not_dvd,f_mu_m_eval_pow_eq_zero,f_frob_fix_neg_one,f_exists_power_mul_unit_norm,f_exists_teichmuller_rep_mod_prime,f_exists_extend_endomorphism_fractions,f_kmu_incl_dense_range,f_capelli_identities__is_closed_embedding_to_m,f_casimir_coefficients__is_closed_embedding_to_m,f_casimir_coefficients__is_closed_kset,f_casimir_coefficients__psi_exists_statement,f_casimir_coefficients__deriv_g_a,f_cas_chain_a,f_cas_chain_b,f_cas_chain,f_exists_virtual_character_semidirect_orbit_cross_terms,f_square_identity_holds,f_hecke_isogeny_kernels,f_l_partial_sum,f_l_growth,f_complex_analytic_sets__st_holomorphic_fibre_infinite,f_complex_analytic_sets__st_implicit_curve,f_st_irreducible_germ_regular_dim_ge,f_complex_analytic_sets__p_implicit_curve,f_complex_analytic_sets__p_holomorphic_fibre_infinite,f_p_irreducible_germ_regular_dim_ge,f_mem_flag_sub_iff,f_mem_first_lattice_iff,f_card_perm_partition_parts_mul_centralizer,f_squarefree_label_mass_degree_type_le,f_mass_deg_type_le_cycle_type,f_squarefree_label_torus_mass_divisor_bound,f_fixed_nondeg,f_block_decomposition__norm_fibre_card_zero,f_block_decomposition__norm_fibre_card_nonzero,f_gauss_sum_hermitian_norm_level_one explained
  classDef textbook fill:#cfe2ff
  class rh_statement,zeta_series,analytic_continuation,trivial_zeros,functional_equation_zeta,factors_nonzero,gamma_function,fourier_analysis,complex_analysis,complex_powers,real_analysis,dirichlet_characters,dirichlet_l_function,primitive_characters,functional_equation_dirichlet,groups,number_fields,p_adic_numbers,algebraic_closure,rings_fields,linear_algebra,polynomials,counting,complex_numbers,trigonometry,calculus,infinite_series,primes_divisibility,modular_arithmetic,proofs,concept_group_representations,concept_group_actions,concept_sylow_theorems,concept_normal_subgroups_quotients,concept_complex_analytic_sets,concept_point_set_topology,concept_lattices_in_the_plane,concept_ideals_and_discriminant,concept_ultrametric_norm,concept_newton_polygon,concept_field_extensions_transcendence,concept_discrete_valuation_ring,concept_finitely_generated_algebras,concept_separable_polynomials,concept_schemes_basics,concept_categorical_pullbacks,concept_galois_fixed_fields,concept_flat_modules,concept_valuation_rings,concept_local_rings,concept_hermitian_unitary_matrices,concept_chain_complexes_homology,concept_finitely_generated_abelian_groups,concept_integral_closure_fraction_fields,concept_coordinate_rings_dimension,concept_prime_ideals_localization,concept_etale_ring_maps,concept_dedekind_domains,concept_hensel_lifting,concept_tensor_product_of_algebras,concept_smooth_morphisms,concept_noetherian_and_irreducible_components,concept_modular_forms,concept_hecke_operators,concept_petersson_product,concept_derivations_smoothness,concept_exterior_powers,concept_witt_vectors_ainf,concept_roots_of_unity_kummer,concept_picard_group,concept_group_homology,concept_frobenius_perfect_rings,concept_gl_infinity_homology_stability,concept_haar_measure_fundamental_domain,concept_lattice_point_counting,concept_chebyshev_functions,concept_dual_numbers,concept_group_schemes,concept_adic_completion,concept_schwartz_functions,concept_semisimple_algebras_radical,concept_filtered_colimits,concept_projective_modules,concept_ample_nef_line_bundles,concept_symmetric_polynomials,concept_regular_local_rings,concept_weierstrass_elliptic_functions,concept_highest_weight_casimir,concept_nilpotent_jordan_chains,concept_class_group,concept_hausdorff_measure textbook
  classDef unmapped fill:#eeeeee,stroke-dasharray:4
  class every_character,l2_literature_of_vwin,l2_local_langlands,l2_galois_local_global,l2_vwin_of_row unmapped
```
