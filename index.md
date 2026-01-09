 <head>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;800&family=Open+Sans:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
</head>

<style>
  /* --- 0. THEME OVERRIDE --- */
  .wrapper { width: 100% !important; margin: 0 !important; max-width: 100% !important; }
  header { display: none !important; }
  footer { display: none !important; }
  section { width: 100% !important; max-width: 100% !important; padding: 0 !important; display: block !important; }
  body { background-color: #F7F7F7 !important; margin: 0 !important; padding: 0 !important; }
  
  /* --- 1. CORE BRANDING --- */
  .custom-body {
    font-family: 'Open Sans', Helvetica, Arial, sans-serif; /* UPDATED FONT */
    color: #333;
    background-color: #F7F7F7;
    line-height: 1.7; /* Slightly more breathing room */
    width: 100%;
  }

  /* --- 2. HEADER SECTION --- */
  .custom-header {
    background-color: #002BFF;
    color: white;
    padding: 70px 20px;
    text-align: center;
    border-bottom: 8px solid #0B1157;
    width: 100%;
    box-sizing: border-box;
  }

  .custom-header h1 {
    font-family: 'Montserrat', sans-serif; /* BRAND HEADER FONT */
    font-weight: 800;
    font-size: 3em;
    margin: 0 0 15px 0;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    line-height: 1.1;
    color: white;
  }

  .custom-header p {
    font-family: 'Montserrat', sans-serif;
    font-size: 1.4em;
    opacity: 0.9;
    font-weight: 400;
    margin: 0;
    color: white;
  }

  /* --- 3. MAIN CONTENT CONTAINER --- */
  .main-content {
    max-width: 900px;
    margin: -50px auto 50px;
    background: white;
    padding: 70px; /* More white space */
    box-shadow: 0 15px 40px rgba(0,0,0,0.1);
    border-radius: 8px;
    position: relative;
    z-index: 10;
  }

  /* --- 4. NAVIGATION BAR --- */
  .nav-bar {
    background: #0B1157;
    color: white;
    padding: 15px 30px;
    font-size: 0.85em;
    text-align: right;
    letter-spacing: 0.5px;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    width: 100%;
    box-sizing: border-box;
  }
  
  .nav-bar a {
    color: white !important;
    text-decoration: none;
    margin-left: 20px;
    border-bottom: 2px solid transparent;
    transition: all 0.2s ease;
  }
  
  .nav-bar a:hover {
    color: #78DCFF !important;
    border-bottom: 2px solid #78DCFF;
  }

  /* --- 5. TYPOGRAPHY --- */
  h1, h2, h3, h4 { 
    color: #0B1157; 
    font-family: 'Montserrat', sans-serif; /* BRAND HEADING FONT */
    margin-top: 45px;
  }
  
  h3 {
    color: #002BFF;
    border-bottom: 3px solid #78DCFF;
    padding-bottom: 10px;
    font-size: 1.7em;
    font-weight: 700;
  }
  
  h4 {
    font-size: 1.3em;
    font-weight: 700;
    color: #0B1157;
  }
  
  /* --- 6. COMPONENTS --- */
  figure {
    margin: 45px 0;
    text-align: center;
    background: #f4f7fa;
    padding: 25px;
    border-radius: 8px;
    border: 1px solid #e1e4e8;
  }
  img { max-width: 100%; height: auto; border-radius: 4px; box-shadow: 0 4px 10px rgba(0,0,0,0.08); }
  figcaption { font-size: 0.9em; color: #555; margin-top: 15px; font-family: 'Open Sans', sans-serif; font-style: italic; }

  .callout-box {
    background-color: #E6F0FF;
    border-left: 6px solid #002BFF;
    padding: 25px;
    margin: 35px 0;
    font-size: 1.1em;
    border-radius: 0 6px 6px 0;
  }
  
  .author-card {
    border-left: 4px solid #002BFF;
    padding-left: 15px;
    margin-bottom: 50px;
    color: #555;
    font-style: italic;
  }
  
  /* --- 7. FOOTER --- */
  .custom-footer {
    background-color: #0B1157;
    color: white;
    padding: 50px 20px;
    text-align: center;
    font-family: 'Montserrat', sans-serif;
    font-size: 0.9em;
    margin-top: 0;
  }
  
  .custom-footer a { color: #78DCFF; text-decoration: none; }
  .custom-footer a:hover { color: white; text-decoration: underline; }
  .references { font-size: 0.85em; color: #666; border-top: 1px solid #eee; padding-top: 20px; margin-top: 60px; }

  /* Mobile Fixes */
  @media (max-width: 768px) {
    .main-content { padding: 30px 20px; width: 90%; }
    .custom-header h1 { font-size: 2em; }
    .nav-bar { text-align: center; padding: 10px; }
    .nav-bar a { display: inline-block; margin: 5px 10px; }
  }
</style>

<div class="custom-body">

<div class="nav-bar">
  <a href="https://breakthrought1d.org.uk/" target="_blank"><b>BREAKTHROUGH T1D UK</b></a>
  <a href="https://breakthrought1d.org.uk/about-breakthrough-t1d-uk-and-our-impact/our-research/" target="_blank">RESEARCH</a>
  <a href="https://breakthrought1d.org.uk/how-to-help/" target="_blank">GET INVOLVED</a>
  <a href="https://breakthrought1d.org.uk/how-to-help/give/donate/" target="_blank" style="color:#78DCFF !important;">DONATE</a>
</div>

<div class="custom-header">
  <h1>The Future of GLP-1 Research</h1>
  <p>An Analysis of Emerging Therapies for Type 1 Diabetes</p>
</div>

<div class="main-content">

  <div class="author-card">
    <p><strong>By Thomas Knight</strong><br>
    Research & Involvement Candidate | January 2026<br>
    <em>Reading time: approx. 6 minutes</em></p>
  </div>

  <div style="background:#fafafa; padding:25px; border:1px solid #e1e4e8; border-radius:6px; margin-bottom:50px;">
    <strong style="font-family:'Montserrat', sans-serif; color:#0B1157;">In this article:</strong>
    <ul style="margin:10px 0 0 20px; padding:0; font-size:0.95em;">
      <li><a href="#what-is-glp1">What is GLP-1?</a></li>
      <li><a href="#the-science-of-glp-1">The Science & Structure</a></li>
      <li><a href="#breakthrough-in-oral-delivery">The Oral Delivery Breakthrough</a></li>
      <li><a href="#status-of-small-molecule-oral-glp-1-agonists-non-peptides">Status of Small Molecules (2026)</a></li>
    </ul>
  </div>

  <h3 id="what-is-glp1">What is GLP-1?</h3>
  <p>GLP-1 (Glucagon-Like Peptide-1) is a naturally occurring hormone produced in the small intestine and brain. It acts as an incretin, meaning it triggers metabolic responses to food intake, primarily by stimulating insulin release and regulating appetite.</p>
  <p>In modern medicine, the term "GLP-1" typically refers to GLP-1 receptor agonists, a class of medications designed to mimic this hormone to treat conditions like type 2 diabetes and obesity.</p>

  <h3>How GLP-1 Works</h3>
  <p>GLP-1 medications activate receptors throughout the body to produce several key effects:</p>
  <ul>
    <li><strong>Regulates Blood Sugar:</strong> It prompts the pancreas to release more insulin when blood sugar levels rise and suppresses glucagon, a hormone that increases sugar production in the liver.</li>
    <li><strong>Promotes Fullness:</strong> It targets satiety centers in the brain to reduce hunger and "food noise" (persistent thoughts about eating).</li>
    <li><strong>Slowing Digestion:</strong> It delays gastric emptying, meaning food stays in the stomach longer, which leads to feeling full faster and for longer periods.</li>
  </ul>

  <h3>Common GLP-1 Medications</h3>
  <p>These drugs are primarily administered via weekly or daily self-injections, though oral versions are becoming more common in 2026.</p>
  <ul>
    <li><strong>Semaglutide:</strong> Brands include Ozempic and Rybelsus (licensed for type 2 diabetes) and Wegovy (licensed for weight loss).</li>
    <li><strong>Tirzepatide:</strong> Marketed as Mounjaro (diabetes/weight loss) and Zepbound (weight loss), this is a "dual agonist" that mimics both GLP-1 and another hormone, GIP.</li>
    <li><strong>Liraglutide:</strong> Brands include Victoza (diabetes) and Saxenda (weight loss).</li>
  </ul>

  <h3>Benefits and Risks</h3>
  <ul>
    <li><strong>Beyond Weight Loss:</strong> Recent 2025/2026 data shows these drugs may also reduce the risk of heart attack, stroke, and kidney disease. They are also being studied for potential benefits in treating Alzheimer’s and substance use disorders.</li>
    <li><strong>Common Side Effects:</strong> Nausea, vomiting, diarrhea, and constipation are frequent, especially when starting the medication.</li>
    <li><strong>Serious Risks:</strong> Though rare, they have been linked to pancreatitis, gallbladder issues, and a potential risk of thyroid C-cell tumors.</li>
    <li><strong>Regain upon Cessation:</strong> 2026 research indicates that many patients regain a significant portion of lost weight within two years of stopping the medication if lifestyle changes are not maintained.</li>
  </ul>

  <h3 id="the-science-of-glp-1">The Science of GLP-1</h3>

  <h4>GLP1-peptide</h4>
  <p>Naturally occurring GLP-1 is a peptide hormone derived from the proglucagon gene. Its structure is defined by its specific amino acid sequence and its three-dimensional shape, which are critical for its biological function.</p>
  
  <p><strong>Secondary and Tertiary Structure</strong><br>
  The hormone's shape changes depending on whether it is in a solution or bound to its receptor:</p>
  <ul>
    <li><strong>Solution Structure:</strong> In aqueous environments, GLP-1 is largely disordered and flexible.</li>
    <li><strong>Receptor-Bound Structure:</strong> When active, it adopts a distinct configuration consisting of:
      <ul>
        <li><strong>N-Terminal Random Coil (Residues 7–13):</strong> A flexible "tail" that is essential for activating the receptor.</li>
        <li><strong>Two Alpha-Helices:</strong> These segments (typically residues 13–20 and 24–35) are separated by a short linker region (residues 21–23).</li>
        <li><strong>The "Kink":</strong> A structural break at Glycine-22 allows the peptide to bend and present a hydrophobic surface that facilitates binding to its target.</li>
      </ul>
    </li>
  </ul>

  <p><strong>Key Structural Features</strong></p>
  <ul>
    <li><strong>Histidine at Position 7:</strong> The free N-terminal amino acid (Histidine) is vital for the hormone’s insulin-stimulating activity.</li>
    <li><strong>DPP-4 Cleavage Site:</strong> The bond between Alanine-8 and Glutamic acid-9 is the primary target for the enzyme DPP-4. This enzyme cleaves the peptide within 1–2 minutes of secretion, rendering the hormone inactive and explaining its very short natural half-life.</li>
  </ul>

  <figure>
    <img src="https://github.com/user-attachments/assets/c6fdc854-a7f6-45ba-bd26-974c7585d554" alt="GLP-1 Structure">
    <figcaption>Figure 1. Glucagon-like peptide 1 (GLP-1) structure regulating insulin secretion. Generated with PyMol from PDB ID: 1D0R.</figcaption>
  </figure>

  <h3>GLP-1 Receptor</h3>
  <p>The GLP-1 receptor (GLP-1R) is a large, complex protein belonging to the Class B (secretin-like) family of G protein-coupled receptors (GPCRs).</p>
  
  <div class="callout-box">
    <strong>Key Concept:</strong> The receptor's structure is defined by its ability to transition between "closed" inactive states and "extended" active states upon ligand binding.
  </div>

  <p><strong>Signaling Role:</strong> Because it is a transmembrane protein, it can act as a bridge, receiving a signal from the hormone outside the cell and transmitting it to G proteins located on the inside of the cell to trigger a biological response, such as insulin secretion.</p>
  <p><strong>Localisation:</strong> It is primarily found on the surface (plasma membrane) of various cell types, including pancreatic beta cells and certain neurons in the brain. </p>

  <h3>Main Structural Components</h3>
  <p>The receptor is composed of two primary functional domains that work cooperatively:</p>
  <ul>
    <li><strong>Extracellular Domain (ECD):</strong> A large N-terminal "cap" (roughly 120 amino acids) located outside the cell. It contains a "secretin recognition fold" stabilized by three conserved disulfide bonds. Its primary role is to capture the C-terminal end of the GLP-1 hormone.</li>
    <li><strong>Transmembrane Domain (TMD):</strong> The core of the receptor, consisting of seven alpha-helices (TM1–TM7) that span the cell membrane. This domain contains the binding pocket for the N-terminal part of the GLP-1 hormone, which is responsible for triggering the receptor's activity.</li>
    <li><strong>Intracellular Loops (ICLs):</strong> These loops connect the transmembrane helices on the inside of the cell and are the sites where the receptor interacts with G proteins to start cellular signaling.</li>
  </ul>

  <p>In 2026, structural biology classifies the states of GLP-1 and its receptor according to the transition from a disordered free peptide to a structured, active complex.</p>

  <h4>1. Apo State (Inactive GLP-1 Receptor)</h4>
  <p>The "apo" state refers to the full-length human GLP-1 receptor (GLP-1R) without its natural peptide hormone bound. In this state, the receptor is inactive and adopts a "closed" conformation.</p>

  <figure>
    <img src="https://github.com/user-attachments/assets/47305852-10d3-4baf-b9eb-f4210695127b" alt="Inactive GLP-1 Receptor">
    <figcaption>Figure 2. Crystal structure of the full-length receptor in its inactive, peptide-free form. The ECD rests against the transmembrane core.</figcaption>
  </figure>

  <h4>2. GLP-1 Bound State (Active Complex)</h4>
  <p>The active state occurs when the natural GLP-1 hormone binds to the receptor, causing the ECD to move into an "up" position and the transmembrane helices to open for signaling.</p>

  <figure>
    <img src="https://github.com/user-attachments/assets/c7ccc3c1-e101-4e2f-aa84-21924ce761a3" alt="Active GLP-1 Complex">
    <figcaption>Figure 3. The Active Complex state.</figcaption>
  </figure>

  <h3>The Two-Domain Binding Mechanism</h3>
  <ol>
    <li><strong>Capture:</strong> The C-terminal region of the GLP-1 hormone first binds to the ECD, which acts like a fishing hook to secure the hormone.</li>
    <li><strong>Activation:</strong> This initial binding causes the receptor to change shape, allowing the N-terminal end of the hormone to insert deep into the <strong>TMD binding pocket.</strong> This insertion pushes the transmembrane helices apart, creating an opening on the inside of the cell for G-protein coupling.</li>
  </ol>

  <h3>Modern Structural Insights (2025–2026)</h3>
  <ul>
    <li><strong>Dynamic Signaling Hubs:</strong> 2025 research has shown that the GLP-1 receptor does not just stay on the cell surface; once activated, it can move inside the cell to form specialized "signaling hubs" at contact sites between different organelles, such as the mitochondria and endoplasmic reticulum, to enhance insulin secretion.</li>
    <li><strong>Inactive State Structure:</strong> In the absence of a hormone, the receptor maintains a "closed" conformation where the ECD rests against the TMD, effectively blocking the activation site until a hormone arrives.</li>
  </ul>

  <h3>Semaglutide: An artificial GLP-1 analogue</h3>
  <p>Semaglutide was discovered by a research team at the Danish pharmaceutical company Novo Nordisk, led by scientists including Jesper Lau, Thomas Kruse, and Paw Bloch. Its discovery was a process of "rational protein engineering," building on the success of their previous drug, liraglutide (Victoza).</p>
  <p>In the early 2000s, Novo Nordisk had already developed liraglutide, which was the first human-based GLP-1 analog suitable for once-daily dosing. However, researchers wanted a "once-weekly" option to improve patient adherence. Semaglutide was engineered specifically to extend the half-life from liraglutide’s ~13 hours to approximately 7 days.</p>

  <h3>Strategic Structural Modifications</h3>
  <p>To achieve this long-lasting effect, the team made three critical structural changes to the native human GLP-1 molecule (achieving 94% homology):</p>
  <ul>
    <li><strong>DPP-4 Protection:</strong> They replaced the amino acid alanine at position 8 with alpha-aminoisobutyric acid (Aib). This specific change prevents the enzyme DPP-4 from quickly breaking the drug down, which is what happens to natural GLP-1 within minutes.</li>
    <li><strong>Albumin Binding:</strong> They swapped liraglutide’s 16-carbon fatty acid for a 18-carbon fatty diacid. This allowed the drug to bind more tightly but reversibly to albumin (a protein in the blood), which protects it from being filtered out by the kidneys.</li>
    <li><strong>Site-Specific Attachment:</strong> They replaced lysine at position 34 with arginine to ensure the fatty acid chain only attached to the lysine at position 26, optimizing the drug's stability.</li>
  </ul>

  <figure>
    <img src="https://github.com/user-attachments/assets/74c4f730-b51c-43e8-b142-2fda5c725589" alt="Semaglutide vs GLP-1">
    <figcaption>Figure 4. Overlay of GLP1-R-Semaglutide (light teal/orange) with GLP-1 (dark teal/yellow).</figcaption>
  </figure>

  <h3 id="breakthrough-in-oral-delivery">Breakthrough in Oral Delivery</h3>
  <p>In 2019, Novo Nordisk achieved another discovery milestone by co-formulating semaglutide with an absorption enhancer called SNAC. This allowed the large peptide molecule to survive stomach acid and be absorbed into the bloodstream, creating Rybelsus, the first oral GLP-1 medication.</p>
  <p><strong>PF-06882961 (Danuglipron)</strong> is an oral, small-molecule GLP-1 receptor agonist developed by Pfizer for the treatment of obesity and type 2 diabetes. Unlike injectable peptide-based GLP-1s like semaglutide, it is a non-peptide molecule designed for oral delivery without the need for complex absorption enhancers.</p>

  <h4>Key Clinical Findings:</h4>
  <ul>
    <li><strong>Efficacy:</strong> Phase 2b trials (NCT04707313) in adults with obesity showed statistically significant weight loss. Patients receiving twice-daily doses achieved mean weight reductions of 8% to 13% after 32 weeks.</li>
    <li><strong>Tolerability Issues:</strong> Despite its efficacy, the twice-daily formulation faced high discontinuation rates—greater than 50% in some cohorts—primarily due to gastrointestinal side effects like nausea, vomiting, and diarrhea.</li>
    <li><strong>Comparison to Peptides:</strong> Preclinical and Phase 1 data indicated that danuglipron had a glucose-lowering and weight-loss efficacy comparable to injectable GLP-1 agonists.</li>
  </ul>

  <p>In April 2025, Pfizer officially discontinued the clinical development of danuglipron. The decision followed a single case of potential drug-induced liver injury (DILI) in an asymptomatic participant during dose-optimization studies for a once-daily formulation.</p>

  <figure>
    <img src="https://github.com/user-attachments/assets/15413f62-6cb3-44f0-8e44-d40449f9ae9b" alt="Danuglipron Bound">
    <figcaption>Figure 5. PF-06882961 (danuglipron) bound to GLP-1-R.</figcaption>
  </figure>

  <h3 id="status-of-small-molecule-oral-glp-1-agonists-non-peptides">Status of Small-Molecule Oral GLP-1 Agonists (Non-Peptides)</h3>
  <p>In early 2026, the landscape for oral GLP-1 receptor agonists has shifted significantly, with the first oral peptide pill for obesity receiving approval, while the next-generation small-molecule (non-peptide) pills have largely completed Phase 3 trials and are awaiting imminent regulatory decisions.</p>
  
  <p><strong>LY3502970 (Orforglipron)</strong> represents a significant breakthrough in GLP-1 pharmacology. It is a small-molecule, non-peptide agonist that activates the receptor through a mechanism distinct from the native GLP-1 peptide. </p>
  
  <div class="callout-box">
    <strong>Key Difference:</strong> Unlike the native GLP-1 peptide, which is a large molecule that spans the entire extracellular face of the receptor and inserts deep into the transmembrane core, LY3502970 binds in a much more compact, specific pocket.
  </div>

  <figure>
    <img src="https://github.com/user-attachments/assets/debb080e-6b56-4333-ac0e-5735abf738ce" alt="Orforglipron Structure">
    <figcaption>Figure 6. Orforglipron (LY3502970), the first FDA approved oral non-peptide GLP-1 receptor agonist.</figcaption>
  </figure>

  <p>New oral drugs like orforglipron (expected for 2026 approval) activate the receptor differently than natural GLP-1. They bind to a unique pocket involving the ECD and specific transmembrane helices (TM1, 2, 3, and 7), creating a distinct receptor shape that may lead to more targeted signaling.</p>
  
  <p><strong>The "Lid" Mechanism (ECD Role):</strong> A critical feature of its activation is the engagement of the receptor's N-terminal Extracellular Domain (ECD). The ECD effectively clamps down over the small molecule, acting like a "lid" to trap it in the binding pocket, giving a much longer lasting effect.</p>

  <figure>
    <img src="https://github.com/user-attachments/assets/879f677e-c173-4d93-8faa-f35ec4a7b9ce" alt="Orforglipron Binding Mechanism">
    <figcaption>Figure 7. Structural basis for GLP-1 receptor activation by Orforglipron (orange). Source: (2020) Proc Natl Acad Sci U S A 117.</figcaption>
  </figure>
  
  <div class="references">
    <h3 style="font-size:1.3em; margin-top:0;">References</h3>
    <ol style="padding-left:20px;">
      <li>Kawakami, T., et al. (2020). "Structural basis for GLP-1 receptor activation by LY3502970, an orally active nonpeptide agonist." <em>Proceedings of the National Academy of Sciences</em>, 117(47), 29959-29967.</li>
      <li>Pfizer Inc. (2025). "Pfizer Discontinues Development of Twice-Daily Oral GLP-1 Agonist Danuglipron." Press Release.</li>
      <li>Novo Nordisk. (2021). "Semaglutide 2.4 mg for the Treatment of Obesity: Key Clinical Trials." <em>New England Journal of Medicine</em>.</li>
      <li>Zhang, Y., et al. (2020). "Cryo-EM structure of the activated GLP-1 receptor in complex with G protein." <em>Nature</em>, 546, 254-258.</li>
    </ol>
  </div>

</div>

<div class="custom-footer">
  <p><strong>Thomas Knight</strong> &copy; 2026. All rights reserved.</p>
  <p>This article is a writing sample demonstrating technical communication skills for the <strong>Breakthrough T1D</strong> Research & Involvement Officer application.</p>
  <p style="margin-top:20px;">
    <a href="#">Back to Top</a> &nbsp;|&nbsp; 
    <a href="https://www.linkedin.com/" target="_blank">Connect on LinkedIn</a>
  </p>
</div>

</div>
