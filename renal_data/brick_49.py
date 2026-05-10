BRICK = {
    "brick_num": 49,
    "brick_title": "Diabetic Kidney Disease",
    "games": [
        {
            "slug": "dkd_pathophysiology_mechanisms",
            "title": "DKD Pathophysiology Mechanisms",
            "subtitle": "Match each pathogenic mechanism to its trigger, effect on glomerulus, and downstream consequence.",
            "categories": ["Trigger", "Effect on Glomerulus", "Downstream Consequence"],
            "data": {
                "Glomerular Hyperfiltration": {
                    "Trigger": "Angiotensin II constricts efferent arteriole, raising intraglomerular pressure early in diabetes course.",
                    "Effect on Glomerulus": "Sustained high pressure stresses capillaries, mesangium, and podocytes, promoting mesangial expansion.",
                    "Downstream Consequence": "Glomerular hypertrophy, large early kidneys, protein leakage, fibrosis, and progressive GFR decline."
                },
                "Nonenzymatic Glycation": {
                    "Trigger": "Chronic hyperglycemia allows glucose to bind proteins without enzymes forming advanced glycation end products.",
                    "Effect on Glomerulus": "AGEs cross-link basement membrane proteins and bind RAGE receptors on renal mesangial cells.",
                    "Downstream Consequence": "Cytokine release including TGF-beta drives mesangial proliferation, inflammation, and nodular glomerular damage."
                },
                "Hyaline Arteriolosclerosis": {
                    "Trigger": "Coexisting hypertension and diabetes act synergistically to injure renal afferent and efferent arterioles.",
                    "Effect on Glomerulus": "Hyaline material deposits within arteriolar walls, reduces capillary lumen size, and disrupts blood flow.",
                    "Downstream Consequence": "Accelerated nephropathy, ischemic glomerular injury, and worsening fall in glomerular filtration rate."
                },
                "Cytokine-Driven Inflammation": {
                    "Trigger": "AGE-RAGE binding stimulates renal cells to release reactive oxygen species and proinflammatory cytokines.",
                    "Effect on Glomerulus": "TGF-beta proliferates mesangial cells, expands matrix, and recruits macrophages into glomerular tubules.",
                    "Downstream Consequence": "Fibroblasts deposit collagen and fibronectin, producing nodular Kimmelstiel-Wilson lesions on biopsy specimens."
                },
                "Basement Membrane Thickening": {
                    "Trigger": "Chronic glycation and inflammation alter glomerular basement membrane composition and integrity over time.",
                    "Effect on Glomerulus": "Abnormal collagen types I, III, IV, V, VI with laminin and fibronectin thicken the GBM.",
                    "Downstream Consequence": "Linear IgG staining on immunofluorescence, podocyte effacement, and increased filtration barrier protein leakage."
                }
            }
        },
        {
            "slug": "dkd_diagnostic_findings",
            "title": "DKD Diagnostic Findings",
            "subtitle": "Match each diagnostic test or finding to its method, significance, and clinical use.",
            "categories": ["Method or Threshold", "Significance", "Clinical Use"],
            "data": {
                "Albuminuria Screening": {
                    "Method or Threshold": "Spot urine albumin-to-creatinine ratio greater than 30 mg/g indicates abnormal albumin excretion.",
                    "Significance": "First sign of DKD in most patients, reflecting early glomerular filtration barrier injury.",
                    "Clinical Use": "Check yearly in all diabetic patients to screen for early reversible kidney disease."
                },
                "Nephrotic-Range Proteinuria": {
                    "Method or Threshold": "Albumin-to-creatinine ratio greater than 3500 mg/g detected on spot urine sample testing.",
                    "Significance": "Indicates advanced DKD with severe glomerular damage and far worse long-term prognosis.",
                    "Clinical Use": "Identifies progressed disease less likely to reverse with ACE inhibitors and glucose control."
                },
                "Estimated GFR": {
                    "Method or Threshold": "Serum creatinine used to calculate eGFR less than 60 mL/min/1.73 m2 sustained over three months.",
                    "Significance": "Abnormally low filtration in diabetes without other causes most likely indicates diabetic kidney disease.",
                    "Clinical Use": "Diagnoses CKD in diabetics even when urine albumin excretion remains entirely within normal range."
                },
                "Kimmelstiel-Wilson Nodules": {
                    "Method or Threshold": "Spherical pink hyaline nodules of extracellular matrix seen on renal biopsy light microscopy.",
                    "Significance": "Pathognomonic histopathologic feature of advanced diabetic nephropathy with mesangial nodular expansion.",
                    "Clinical Use": "Confirms diabetic nephropathy in atypical presentations such as sudden edema with heavy proteinuria."
                },
                "Linear IgG Immunofluorescence": {
                    "Method or Threshold": "Immunofluorescence microscopy shows linear staining along glomerular basement membranes for immunoglobulin G.",
                    "Significance": "Reflects nonspecific trapping in thickened GBM, differs from anti-GBM by absent C3 and crescents.",
                    "Clinical Use": "Helps distinguish DKD from anti-GBM antibody-mediated glomerulonephritis on biopsy specimens."
                },
                "Hyperkalemia and Type 4 RTA": {
                    "Method or Threshold": "Serum electrolyte panel reveals elevated potassium and hyperchloremic metabolic acidosis in DKD patients.",
                    "Significance": "Reflects impaired distal tubular potassium and acid handling in advanced diabetic kidney injury.",
                    "Clinical Use": "Monitor electrolytes regularly, especially when prescribing ACE inhibitors or angiotensin receptor blockers."
                }
            }
        },
        {
            "slug": "dkd_management_strategies",
            "title": "DKD Management Strategies",
            "subtitle": "Match each therapy to its target, mechanism of benefit, and key clinical caution.",
            "categories": ["Therapeutic Target", "Mechanism of Benefit", "Key Caution"],
            "data": {
                "Tight Glucose Control": {
                    "Therapeutic Target": "Maintain blood glucose 70 to 100 mg/dL with HbA1c below 7.0 percent in most diabetics.",
                    "Mechanism of Benefit": "Limits nonenzymatic glycation, slowing AGE formation and progression of kidney injury.",
                    "Key Caution": "Therapy must be individualized; detailed diabetes management is covered in the endocrine course."
                },
                "ACE Inhibitor or ARB": {
                    "Therapeutic Target": "Blood pressure less than 130 systolic and less than 80 diastolic in DKD patients.",
                    "Mechanism of Benefit": "Dilates efferent arteriole, reduces hyperfiltration injury, lowers proteinuria, and slows disease progression.",
                    "Key Caution": "Monitor for hyperkalemia; add diuretic or low-potassium diet if serum potassium becomes elevated."
                },
                "SGLT2 Inhibitor": {
                    "Therapeutic Target": "Use in type 2 diabetes with eGFR over 20 and albuminuria above 200 mg/g.",
                    "Mechanism of Benefit": "Reduces CKD progression along with major cardiovascular events and heart failure hospitalizations.",
                    "Key Caution": "Avoid in type 1 diabetes due to diabetic ketoacidosis risk and insufficient protection evidence."
                },
                "GLP-1 Receptor Agonist": {
                    "Therapeutic Target": "Add when albuminuria persists despite ACE inhibitor, ARB, and SGLT2 inhibitor therapy at maximum doses.",
                    "Mechanism of Benefit": "Provides complementary metabolic, cardiovascular, and renal effects on top of standard DKD therapy.",
                    "Key Caution": "Used as add-on therapy to enhance combination DKD progression management against residual albuminuria."
                },
                "Nonsteroidal MR Antagonist": {
                    "Therapeutic Target": "Add when albuminuria stays above 30 mg/g despite maximally tolerated ACE inhibitor or ARB.",
                    "Mechanism of Benefit": "Blocks mineralocorticoid receptor with greater specificity than spironolactone, reducing inflammation and fibrosis.",
                    "Key Caution": "Watch for hyperkalemia given concurrent renin-angiotensin blockade in patients with advanced kidney disease."
                },
                "Renal Replacement Therapy": {
                    "Therapeutic Target": "Initiate in patients with end-stage kidney disease defined by GFR requiring dialysis or transplantation.",
                    "Mechanism of Benefit": "Substitutes for failed renal function with kidney transplant offering best survival benefit when feasible.",
                    "Key Caution": "Over 280,000 US DKD patients require treatment yearly at cost exceeding 20 billion dollars."
                }
            }
        }
    ]
}
