<head>
  <title>The Future of GLP-1 Research | Thomas Knight</title>
  
  <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🧬</text></svg>">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&family=Open+Sans:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
  
  <meta property="og:title" content="The Future of GLP-1 Research">
  <meta property="og:description" content="An analysis of emerging T1D therapies by Thomas Knight.">
</head>

<style>
  /* --- RESET & LAYOUT --- */
  .wrapper { width: 100% !important; margin: 0 !important; max-width: 100% !important; }
  header, footer { display: none !important; }
  section { width: 100% !important; max-width: 100% !important; padding: 0 !important; display: block !important; }
  body { background-color: #F7F7F7 !important; margin: 0 !important; padding: 0 !important; }
  html { scroll-behavior: smooth; }

  /* --- TYPOGRAPHY (MATCHING BREAKTHROUGH T1D) --- */
  .custom-body {
    font-family: 'Open Sans', Helvetica, Arial, sans-serif; /* Body Text */
    color: #333;
    background-color: #F7F7F7;
    line-height: 1.7;
    width: 100%;
  }

  h1, h2, h3, h4 { 
    color: #0B1157; /* Navy */
    font-family: 'Montserrat', sans-serif; /* Headings */
    margin-top: 45px;
  }

  h3 {
    color: #002BFF; /* Breakthrough Blue */
    border-bottom: 3px solid #78DCFF; /* Cyan Highlight */
    padding-bottom: 10px;
    font-size: 1.7em;
    font-weight: 800; /* Bolder to match news style */
    text-transform: none; /* Keep mixed case for readability */
  }
  
  h4 {
    font-size: 1.3em;
    font-weight: 700;
    color: #0B1157;
    margin-bottom: 15px;
  }

  /* --- HEADER WITH GRADIENT --- */
  .custom-header {
    background: linear-gradient(135deg, #002BFF 0%, #0020c2 100%);
    color: white;
    padding: 80px 20px;
    text-align: center;
    border-bottom: 8px solid #0B1157;
    width: 100%;
  }

  .custom-header h1 {
    font-weight: 800;
    font-size: 3.2em;
    margin: 0 0 15px 0;
    text-transform: uppercase;
    letter-spacing: 1px;
    line-height: 1.1;
    color: white;
    text-shadow: 0 2px 10px rgba(0,0,0,0.2);
  }

  .custom-header p {
    font-family: 'Montserrat', sans-serif;
    font-size: 1.4em;
    opacity: 0.95;
    font-weight: 500;
    margin: 0;
    color: white;
  }

  /* --- PAGE CONTAINER --- */
  .page-container {
    display: flex;
    justify-content: center;
    align-items: flex-start;
    gap: 30px;
    max-width: 1200px;
    margin: -60px auto 50px;
    position: relative;
    z-index: 10;
    padding: 0 20px;
  }

  /* --- MAIN CONTENT CARD --- */
  .main-content {
    flex: 1;
    max-width: 800px;
    background: white;
    padding: 70px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.1);
    border-radius: 8px;
  }

  /* --- SIDEBAR STYLES --- */
  .sidebar {
    width: 280px; /* Slightly wider to accommodate text */
    background: white;
    padding: 25px;
    border-radius: 8px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    border-top: 4px solid #002BFF;
    font-family: 'Montserrat', sans-serif;
    position: sticky;
    top: 20px;
  }

  .sidebar-title {
    font-size: 1.1em;
    font-weight: 800;
    color: #0B1157;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 2px solid #f0f0f0;
    text-transform: uppercase;
  }

  .sidebar-item {
    margin-bottom: 30px;
    text-align: left;
  }

  .sidebar-item h5 {
    font-size: 0.95em;
    color: #002BFF;
    margin: 0 0 8px 0;
    font-weight: 700;
    line-height: 1.3;
  }

  .sidebar-text {
    font-size: 0.85em;
    color: #555;
    font-family: 'Open Sans', sans-serif;
    margin-top: 5px;
    line-height: 1.5;
  }
  
  .sidebar-citation {
    font-size: 0.7em;
    color: #888;
    font-style: italic;
    margin-top: 8px;
    display: block;
    border-left: 2px solid #ddd;
    padding-left: 8px;
  }
  
  /* Sidebar Links */
  .sidebar-citation a {
    color: #888;
    text-decoration: none;
    transition: color 0.2s;
  }
  .sidebar-citation a:hover {
    color: #002BFF;
    text-decoration: underline;
  }

  /* --- NAVIGATION BAR --- */
  .nav-bar {
    background: #0B1157;
    color: white;
    padding: 15px 30px;
    font-size: 0.85em;
    text-align: right;
    letter-spacing: 0.5px;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
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

  /* --- PRINT BUTTON --- */
  .print-btn {
    background: white;
    color: #002BFF;
    border: 2px solid #002BFF;
    padding: 8px 16px;
    border-radius: 20px;
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    font-size: 0.85em;
    cursor: pointer;
    float: right;
    transition: all 0.2s;
    margin-top: -10px;
  }
  .print-btn:hover {
    background: #002BFF;
    color: white;
  }

  /* --- COMPONENTS --- */
  figure {
    margin: 45px 0;
    text-align: center;
    background: #f8faff;
    padding: 25px;
    border-radius: 8px;
    border: 1px solid #eef2f7;
    transition: transform 0.2s;
  }
  figure:hover { transform: translateY(-2px); }

  img { max-width: 100%; height: auto; border-radius: 4px; }
  
  figcaption { 
    font-size: 0.9em; 
    color: #555; 
    margin-top: 15px; 
    font-family: 'Open Sans', sans-serif; 
    font-style: italic; 
  }

  .callout-box {
    background-color: #E6F0FF;
    border-left: 6px solid #002BFF;
    padding: 25px;
    margin: 35px 0;
    font-size: 1.1em;
    border-radius: 0 6px 6px 0;
  }
  
  /* --- FOOTER --- */
  .custom-footer {
    background-color: #0B1157;
    color: white;
    padding: 60px 20px;
    text-align: center;
    font-family: 'Montserrat', sans-serif;
    font-size: 0.9em;
  }
  .custom-footer a { color: #78DCFF; text-decoration: none; font-weight: 600; }
  .custom-footer a:hover { color: white; text-decoration: underline; }

  /* --- PRINT STYLES --- */
  @media print {
    .nav-bar, .custom-footer, .print-btn, .sidebar { display: none !important; }
    .page-container { margin: 0; padding: 0; display: block; }
    .custom-header { padding: 30px; background: white; color: #002BFF; border-bottom: 2px solid #002BFF; }
    .custom-header h1 { color: #002BFF; font-size: 24pt; text-shadow: none; }
    .custom-header p { color: #333; }
    .main-content { box-shadow: none; margin: 0; padding: 0; max-width: 100%; }
    body { background: white !important; }
    a { text-decoration: none; color: black; }
  }

  /* Mobile Adjustments */
  @media (max-width: 1100px) {
    .page-container { flex-direction: column; align-items: center; margin-top: -30px; }
    .main-content { width: 100%; padding: 40px 30px; order: 1; }
    .sidebar { width: 100%; max-width: 800px; margin-bottom: 30px; position: static; order: 2; display: flex; justify-content: space-around; flex-wrap: wrap; gap: 20px; }
    .sidebar-item { flex: 1 1 30%; margin: 0; }
    .custom-header h1 { font-size: 2em; }
    .nav-bar { text-align: center; padding: 15px; }
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

<div class="page-container">

  <div class="sidebar">
    <div class="sidebar-title">Global Impact</div>
    
    <div style="text-align: center; margin-bottom: 30px;">
      <span style="font-size: 2.5em; display: block; margin-bottom: 10px;">🧬</span>
      <span style="font-size: 1.8em; font-weight: 800; color: #002BFF; display: block;">400+</span>
      <span class="sidebar-text">Active research studies funded worldwide</span>
    </div>
    
    <div style="text-align: center; margin-bottom: 30px;">
      <span style="font-size: 2.5em; display: block; margin-bottom: 10px;">🌍</span>
      <span style="font-size: 1.8em; font-weight: 800; color: #002BFF; display: block;">21</span>
      <span class="sidebar-text">Countries where research is taking place</span>
    </div>
  </div>

  <div class="main-content">

    <button class="print-btn" onclick="window.print()">🖨️ Save as PDF</button>

    <div style="border-left: 4px solid #002BFF; padding-left: 15px; margin-bottom: 40px; color: #555; overflow: hidden;">
      <img src="profile.jpg" alt="Thomas Knight" style="width: 80px; height: 80px; border-radius: 50%; margin-right: 20px; float: left; box-shadow: 0 4px 8px rgba(0,0,0,0.1); object-fit: cover;">
      <p style="margin-top: 0;">
        <strong>By Thomas Knight</strong><br>
        <a href="https://www.linkedin.com/in/tom-knight-340784151/" target="_blank" style="color: #002BFF; font-weight: 600; text-decoration: none;">Connect on LinkedIn</a><br>
        Research & Involvement Candidate | January 2026<br>
        <em>Reading time: approx. 6 minutes</em>
      </p>
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
      <li><strong>Promotes Fullness:</strong> It targets satiety centres in the brain to reduce hunger and "food noise" (persistent thoughts about eating).</li>
      <li><strong>Slows Digestion:</strong> It delays gastric emptying, meaning food stays in the stomach longer, which leads to feeling full faster and for longer periods.</li>
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

    <h4>The GLP-1 Peptide</h4>
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

    <figure>
      <img src="https://github.com/user-attachments/assets/c6fdc854-a7f6-45ba-bd26-974c7585d554" alt="GLP-1 Structure">
      <figcaption>Figure 1. Glucagon-like peptide 1 (GLP-1) structure regulating insulin secretion. Generated with PyMol from PDB ID: 1D0R.</figcaption>
    </figure>

    <h3>GLP-1 Receptor</h3>
    <p>The GLP-1 receptor (GLP-1R) is a large, complex protein belonging to the Class B (secretin-like) family of G protein-coupled receptors (GPCRs).</p>
    
    <div class="callout-box">
      <strong>Key Concept:</strong> The receptor's structure is defined by its ability to transition between "closed" inactive states and "extended" active states upon ligand binding.
    </div>

    <p><strong>Signalling Role:</strong> Because it is a transmembrane protein, it can act as a bridge, receiving a signal from the hormone outside the cell and transmitting it to G proteins located on the inside of the cell to trigger a biological response, such as insulin secretion.</p>

    <h3>Breakthrough in Oral Delivery</h3>
    <p>In 2019, Novo Nordisk achieved another discovery milestone by co-formulating semaglutide with an absorption enhancer called SNAC. This allowed the large peptide molecule to survive stomach acid and be absorbed into the bloodstream, creating Rybelsus, the first oral GLP-1 medication.</p>
    <p><strong>PF-06882961 (Danuglipron)</strong> is an oral, small-molecule GLP-1 receptor agonist developed by Pfizer for the treatment of obesity and type 2 diabetes. Unlike injectable peptide-based GLP-1s like semaglutide, it is a non-peptide molecule designed for oral delivery without the need for complex absorption enhancers.</p>

    <figure>
      <img src="https://github.com/user-attachments/assets/15413f62-6cb3-44f0-8e44-d40449f9ae9b" alt="Danuglipron Bound">
      <figcaption>Figure 5. PF-06882961 (danuglipron) bound to GLP-1-R.</figcaption>
    </figure>

    <h3>Status of Small-Molecule Oral GLP-1 Agonists (Non-Peptides)</h3>
    <p>In early 2026, the landscape for oral GLP-1 receptor agonists has shifted significantly, with the first oral peptide pill for obesity receiving approval, while the next-generation small-molecule (non-peptide) pills have largely completed Phase 3 trials and are awaiting imminent regulatory decisions.</p>
    
    <p><strong>LY3502970 (Orforglipron)</strong> represents a significant breakthrough in GLP-1 pharmacology. It is a small-molecule, non-peptide agonist that activates the receptor through a mechanism distinct from the native GLP-1 peptide. </p>
    
    <figure>
      <img src="https://github.com/user-attachments/assets/879f677e-c173-4d93-8faa-f35ec4a7b9ce" alt="Orforglipron Binding Mechanism">
      <figcaption>Figure 7. Structural basis for GLP-1 receptor activation by Orforglipron (orange). Source: Kawakami et al. [1].</figcaption>
    </figure>
    
    <div style="font-size: 0.85em; color: #666; border-top: 1px solid #eee; padding-top: 20px; margin-top: 60px;">
      <h3 style="font-size:1.3em; margin-top:0;">References</h3>
      <ol style="padding-left:20px;">
        <li>Kawakami, T., et al. (2020). "Structural basis for GLP-1 receptor activation by LY3502970." <em>Proceedings of the National Academy of Sciences</em>, 117(47).</li>
        <li>Pfizer Inc. (2025). "Pfizer Discontinues Development of Twice-Daily Oral GLP-1 Agonist Danuglipron." Press Release.</li>
        <li>Wilding, J.P.H., et al. (2021). "Once-Weekly Semaglutide in Adults with Overweight or Obesity." <em>New England Journal of Medicine</em>, 384:989-1002.</li>
        <li>Zhang, Y., et al. (2017). "Cryo-EM structure of the activated GLP-1 receptor in complex with G protein." <em>Nature</em>, 546, 254-258.</li>
      </ol>
    </div>

  </div>

  <div class="sidebar">
    <div class="sidebar-title">Progress 2026 & Beyond</div>
    
    <div class="sidebar-item">
      <h5>Affordable Insulin</h5>
      <p class="sidebar-text">
        Civica Rx's insulin glargine-yfgn (interchangeable with Lantus) became available on Jan 1, 2026, offering a low-cost option (under $55 for five pens) for all, regardless of insurance.
      </p>
      <span class="sidebar-citation">
        <a href="https://www.breakthrought1d.org/news-and-updates/civica-long-acting-insulin-available-on-january-1-2026/" target="_blank">Ref: Civica Rx Press Release (2026)</a>
      </span>
    </div>

    <div class="sidebar-item">
      <h5>Engineered Islets</h5>
      <p class="sidebar-text">
        <strong>Sana Biotechnology</strong> showed promising data in late 2024/early 2025 with transplanted islets (from deceased donors) that produce insulin without needing immunosuppression.
      </p>
      <span class="sidebar-citation">
        <a href="https://ir.sana.com/news-releases/news-release-details/sana-biotechnology-announces-publication-new-england-journal/" target="_blank">Ref: Sana Biotechnology, NEJM (2025)</a>
      </span>
      
      <p class="sidebar-text" style="margin-top:15px;">
        <strong>Stem Cell Success:</strong> A Chinese patient study (early 2025) demonstrated success using reprogrammed stem cells to create islet cells for transplantation, potentially curing T1D.
      </p>
      <span class="sidebar-citation">
        <a href="https://www.cell.com/cell/fulltext/S0092-8674(24)00966-2" target="_blank">Ref: Wang, S. et al. Cell 187 (2024)</a>
      </span>
    </div>

    <div class="sidebar-item">
      <h5>"Smart" Insulins</h5>
      <p class="sidebar-text">
        Researchers funded by the Type 1 Diabetes Grand Challenge developed novel insulin-glucagon molecules designed to prevent dangerous low blood sugars (hypoglycemia).
      </p>
      <span class="sidebar-citation">
        <a href="https://pubs.acs.org/doi/10.1021/acsptsci.5c00362" target="_blank">Ref: Weiss, M.A. et al. ACS Pharmacol. Transl. Sci. (2025)</a>
      </span>
    </div>
    
  </div>

</div> <div class="custom-footer">
  <p><strong>Thomas Knight</strong> &copy; 2026. All rights reserved.</p>
  <p>This article is a writing sample demonstrating technical communication skills for the <strong>Breakthrough T1D</strong> Research & Involvement Officer application.</p>
  <p style="margin-top:20px;">
    <a href="#">Back to Top</a> &nbsp;|&nbsp; 
    <a href="https://www.linkedin.com/in/tom-knight-340784151/" target="_blank">Connect on LinkedIn</a>
  </p>
</div>

</div>
