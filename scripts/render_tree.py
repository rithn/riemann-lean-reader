import os, sys
import csv, collections, re, json
csv.field_size_limit(10**9)
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'folder_tree.py')).read().split("out=[]")[0])   # reuse loading, toks, clusters
under=collections.defaultdict(list)
for r in rows:
    p=r['file'].split('/')
    for i in range(1,len(p)): under['/'.join(p[:i])].append(p[-1][:-5])
def kw(names,k=12):
    c=collections.Counter(t for n in names for t in toks(n)); return c.most_common(k)
A=json.load(open('adapt.json'))
G={
'Proofs':'the proofs; everything else in this area is definitions and statements',
'DivisorProofs':'the largest single block in the project (24% of all files)',
'UniformizationProofs':'complex uniformisation of abelian varieties','UnitaryExistence':'existence of forms/representations on unitary groups',
'HeightProofs':'heights of abelian varieties','AdelicLatticeProofs':'lattices over the adeles','CuspFormEvaluations':'values of cusp forms at special points',
'SiegelThetaTransformation':'how Siegel theta functions transform','UnramifiedDepth':'unramified local computations','CubicalLineBundles':'cubical structures on line bundles (theorem of the cube)',
'ThetaShiftProofs':'shifting theta functions','ThetaLawProofs':'functional laws of theta functions','RingsOfIntegers':'rings of integers of number fields',
'Definitions':'definitions used by the proofs','BlockTheory':'block decompositions (representation theory)','PublishedTheorems':'known published results, re-proved',
'Counterexamples':'examples and "surveys"; likely checks that hypotheses are needed','Statements':'named statements, proved elsewhere','CrystallinePeriods':'crystalline period rings',
'AutomorphicVarieties':'Shimura-variety and Galois-representation machinery','ModularityArgument':'looks like a Taylor–Wiles-style modularity lifting argument',
'ThresholdArguments':'threshold/case analysis inside the modularity argument','SymmetricPowerTransfer':'symmetric power functoriality','TraceFormula':'trace formula',
'InductionEstimates':'estimates for an induction','KatoQuadraticCharacters':'quadratic characters (Kato-style)','AutomorphyLifting':'automorphy lifting theorems',
'CrystallineOrdinaryIdeals':'crystalline/ordinary deformation conditions','LiteratureResults':'results taken from the literature, re-proved','WeakShimuraTheory':'Shimura varieties (weak form)',
'BuildingsResidueChars':'Bruhat–Tits buildings and residue characteristic','GaloisLibrary':'general Galois-theory library','PatchingModules':'Taylor–Wiles patching',
'PadicHodgeTheory':'p-adic Hodge theory','HeckeAlgebras':'Hecke algebras','Foundations':'foundational layer','GaloisRepresentations':'Galois representations attached to automorphic forms',
'ThetaParseval':'Parseval identities for theta lifts (the note mentions iterating Parseval)','IntegralStructures':'integral structures; holds the theorem that feeds the final step','KunnethLefschetz':'Künneth and Lefschetz formulas',
'Convolution':'convolution algebras and analysis on groups','RealGroupAnalysis':'analysis on real groups','LocalLanglands':'local Langlands correspondence',
'ThetaCorrespondence':'theta correspondence between pairs of groups','ThetaPairLifts':'the chain of theta lifts the note describes','ThirdPlaceSeries':'main body of the theta-lift chain; holds the step that derives GRH from the lifts',
'LocalTypeDictionary':'dictionary of local representation types','HodgeBundleWeights':'weights of Hodge bundles','IntegralCasts':'integrality arguments; includes Capelli identities and some of the largest files',
'DivisorFrames':'frames for divisors','Proofs/BlockDecomposition':'','BlockDecomposition':'decomposing spaces of automorphic forms into blocks','GeometryProofs':'geometry: Hodge structures, models, lattices',
'MetricProofs':'metrics on flag varieties and charts','AlgebraProofs':'algebra','GlobalProofs':'global arguments','DivisibilityProofs':'divisibility arguments',
'CoreStatements':'core statements and their proofs','AutomorphicKernels':'kernel functions for automorphic forms','PadicHodgeComparison':'p-adic Hodge comparison theorems','HodgeTatePoints':'Hodge–Tate points/periods',
'TorusUniformisation':'uniformisation by tori','RepresentationTheoryGL':'representation theory of GL(n)','ArchimedeanBaseChange':'base change at the real/complex place','SiegelWeilProof':'the Siegel–Weil formula',
'UnitaryDualProof':'classification of unitary representations','RegularisedSiegelWeil':'regularised Siegel–Weil formula','ResidualSpectrum':'residual spectrum (Eisenstein residues)','ThetaLifts':'theta lifts',
'EtaleSheaves':'étale sheaves','TateTwists':'Tate twists','CohomologicalPurity':'purity theorem','KummerTheory':'Kummer theory','EtaleTrace':'trace maps','DivisorCycles':'cycle classes of divisors',
'SiegelLatticeTheory':'lattice theory behind Siegel-type mass formulas','CokernelGLCounts':'counting cokernels / points over GL','RankPointCounts':'counting points by rank','FlagStabilizerTensors':'stabilisers of flags',
'ClosedLocalOrbits':'closed orbits of local groups','TorsionIntegrality':'integrality of torsion','IndefiniteReal':'indefinite forms at the real place; one of the two custom-tactic files is here','UnitaryGroupMassFormula':'mass formula for unitary groups (the note mentions "Siegel mass")',
'StabilizerVolume':'volumes of stabilisers','ArchimedeanOrbitMeasures':'orbit measures at the real place','CountingFormula':'the counting formula itself','OrbitalBoundsConclusion':'final orbital bounds',
'GrowthBounds':'growth bounds (factorials, binomials, valuations)','LevelLetterCocycles':'cocycles indexed by level','CuspSpanNormBounds':'norm bounds near cusps; several of the largest files','HermitianCurvatureProofs':'curvature computations; mostly one flat folder',
'Heights':'Arakelov-style height theory','ComplexAnalyticSets':'complex analytic sets','HilbertSamuel':'arithmetic Hilbert–Samuel theorem','KleimanAmpleness':'Kleiman\'s ampleness criterion','Intersections':'intersection theory',
'ArithmeticBezout':'arithmetic Bézout theorem','HodgeLowerBound':'Hodge-index-type lower bounds','ArithmeticGeometry':'arithmetic geometry of reductive groups','FundamentalDomains':'fundamental domains (reduction theory)',
'ArakelovVolumes':'Arakelov volumes','BirationalGeometry':'birational geometry, toroidal compactifications','HeightTheory':'heights','DiscreteSeries':'discrete series representations','LaplaceOperators':'Laplace/Casimir operators',
'MultiplicityOne':'multiplicity one','FormalDegree':'formal degrees','ExceptionalGroupG2':'the exceptional group G2','DiscreteSeriesExistence':'existence of discrete series',
'LocalGlobalProofs':'local-to-global arguments','AdelicAnalysis':'analysis on adelic groups','StableLattices':'semistable lattices','ConvexCones':'convex cones',
}
def words(n): return re.sub(r'(?<=[a-z0-9])(?=[A-Z])',' ',n)
o=["","## Inside the big folders (adaptive depth)","",
"**Rule:** keep splitting a folder while it has more than 1,000 files. Small siblings are merged into one \"other\" row. A folder marked **flat** is over 1,000 files with no subfolders; those get a word profile in the next section.","",
"Each row: name (files), my guess where I have one, then the most common words in its file names. Rows without a guess are the folder name plus the words.",""]
skip_other_top={'Formalism/(other)','GroundTheory/(other)','ReciprocityTheory/(other)'}
bigtops={a['path'] for a in A if a['kind']=='split' and a['path'].count('/')==1}
for a in A:
    p=a['path']; parts=p.split('/')
    if len(parts)<2: continue
    top2='/'.join(parts[:2])
    if top2 not in bigtops: continue
    d=len(parts)-2; ind='  '*d; name=parts[-1]; f=f"{a['files']:,}"
    if a['kind']=='split' and d==0:
        o+=["",f"### {top2} ({f} files)",""]; continue
    if a['kind'] in('loose',):
        o.append(f"{ind}- *loose files* ({f})"); continue
    if a['kind']=='other':
        o.append(f"{ind}- *other: {a['nf']} folders* ({f}), e.g. {', '.join(words(x) for x in a['eg'][:4])}"); continue
    g=G.get(name,'')
    if a['kind']=='flat':
        nm = name if name!='(loose files)' else 'loose files'
        o.append(f"{ind}- **{nm}** ({f}) **flat**" + (f": {g}" if g else '')); continue
    k=', '.join(t for t,_ in kw(under[p],4))
    if a['kind']=='split':
        o.append(f"{ind}- **{name}** ({f})" + (f": {g}" if g else '')); continue
    o.append(f"{ind}- {name} ({f})" + (f": {g}." if g else '.') + (f" Words: {k}." if k else ''))
o+=["","## Word profiles of the flat folders","",
"These folders have no subfolders, and namespaces don't split them either. The only cheap signal is which words appear in file names. A file can count under several words. This is rough: the spot check showed names are weak evidence.","",
"| Folder | Files | Most common words in file names (share of files) |","|---|---|---|"]
for a in A:
    if a['kind']!='flat': continue
    p=a['path']; base=p.replace('/(loose files)','')
    names=direct[base]; n=len(names)
    s=', '.join(f"{t} {100*c/n:.0f}%" for t,c in kw(names,10))
    o.append(f"| {'/'.join(base.split('/')[-2:])} | {n:,} | {s} |")
json.dump(o,open('partB.json','w')); print(len(o))
