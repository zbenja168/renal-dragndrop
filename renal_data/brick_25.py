BRICK = {
    "brick_num": 25,
    "brick_title": "Magnesium Homeostasis",
    "games": [
        {
            "slug": "renal_mg_handling_segments",
            "title": "Renal Magnesium Handling by Nephron Segment",
            "subtitle": "Match each nephron segment to its Mg2+ reabsorption profile",
            "categories": ["% Mg2+ Reabsorbed", "Transport Pathway", "Key Driver or Channel"],
            "data": {
                "Proximal Tubule": {
                    "% Mg2+ Reabsorbed": "About 10-20% of filtered magnesium reabsorbed here",
                    "Transport Pathway": "Paracellular passive movement with water flow",
                    "Key Driver or Channel": "Solvent drag down electrochemical gradient"
                },
                "Thick Ascending Limb": {
                    "% Mg2+ Reabsorbed": "Major site, up to 70% of filtered Mg2+",
                    "Transport Pathway": "Paracellular via tight junctions",
                    "Key Driver or Channel": "Lumen-positive charge through claudin-16 and claudin-19"
                },
                "Distal Convoluted Tubule": {
                    "% Mg2+ Reabsorbed": "Fine-tunes balance, reabsorbs 10-20%",
                    "Transport Pathway": "Active transcellular transport across cells",
                    "Key Driver or Channel": "Apical TRPM6 channel with basolateral NCX and PMCA"
                },
                "Final Urine": {
                    "% Mg2+ Reabsorbed": "Only 0-10% of filtered Mg2+ excreted",
                    "Transport Pathway": "No reabsorption; this is excretion",
                    "Key Driver or Channel": "Reflects net renal handling along entire nephron"
                }
            }
        },
        {
            "slug": "causes_of_mg_wasting",
            "title": "Causes of Magnesium Wasting",
            "subtitle": "Match each cause to its mechanism and source of loss",
            "categories": ["Source of Loss", "Mechanism", "Effect on Mg2+ Handling"],
            "data": {
                "Loop Diuretics": {
                    "Source of Loss": "Renal magnesium wasting in thick ascending limb",
                    "Mechanism": "Inhibit NKCC2 cotransporter in TAL",
                    "Effect on Mg2+ Handling": "Disrupts lumen-positive charge driving paracellular Mg2+ uptake"
                },
                "Cetuximab": {
                    "Source of Loss": "Renal wasting in distal convoluted tubule",
                    "Mechanism": "Blocks epidermal growth factor (EGF) receptor",
                    "Effect on Mg2+ Handling": "Decreases TRPM6 activity, lowering DCT Mg2+ reabsorption"
                },
                "Gitelman Disease": {
                    "Source of Loss": "Renal wasting in distal convoluted tubule",
                    "Mechanism": "Defective NCC cotransporter lowers DCT sodium reuptake",
                    "Effect on Mg2+ Handling": "Reduces Mg2+ reabsorption in the DCT"
                },
                "Proton Pump Inhibitors": {
                    "Source of Loss": "Gastrointestinal magnesium wasting",
                    "Mechanism": "Inhibit gut TRPM6/7 activity",
                    "Effect on Mg2+ Handling": "Reduce intestinal magnesium absorption"
                },
                "Chronic Diarrhea": {
                    "Source of Loss": "Gastrointestinal magnesium wasting",
                    "Mechanism": "Accelerates intestinal transit time",
                    "Effect on Mg2+ Handling": "Excessive magnesium loss in stool"
                },
                "Chronic Pancreatitis": {
                    "Source of Loss": "Gastrointestinal magnesium wasting",
                    "Mechanism": "Fat saponification binds magnesium in gut",
                    "Effect on Mg2+ Handling": "Increases fecal magnesium losses"
                }
            }
        },
        {
            "slug": "mg_disorders_features_and_management",
            "title": "Magnesium Disorders: Features and Management",
            "subtitle": "Match each clinical scenario to its features and treatment",
            "categories": ["Clinical Features", "Key Lab or ECG Finding", "Management"],
            "data": {
                "Mild Hypomagnesemia": {
                    "Clinical Features": "Asymptomatic or mild muscle cramps and tetany",
                    "Key Lab or ECG Finding": "Serum Mg2+ above 1.0 mEq/L without severe ECG changes",
                    "Management": "Oral magnesium replacement preferred for stable patients"
                },
                "Severe Symptomatic Hypomagnesemia": {
                    "Clinical Features": "Seizures, arrhythmias, or torsades de pointes",
                    "Key Lab or ECG Finding": "Prolonged QT interval with low serum Mg2+",
                    "Management": "Intravenous magnesium for arrhythmia or severe symptoms"
                },
                "Refractory Hypokalemia with Low Mg2+": {
                    "Clinical Features": "Persistent low K+ despite oral potassium repletion",
                    "Key Lab or ECG Finding": "ROMK disinhibition causes ongoing distal K+ loss",
                    "Management": "Correct magnesium first, then replete potassium and calcium"
                },
                "Hypomagnesemia in CKD with PPI": {
                    "Clinical Features": "Tremor and palpitations from chronic Mg2+ depletion",
                    "Key Lab or ECG Finding": "Frequent PVCs with low Mg2+, K+, and Ca2+",
                    "Management": "Cautious IV Mg2+ with ECG and reflex monitoring; stop PPI"
                },
                "Hypermagnesemia": {
                    "Clinical Features": "Weakness, decreased reflexes, lethargy, hypotension",
                    "Key Lab or ECG Finding": "Peaked T waves and prolonged QRS on ECG",
                    "Management": "Stop Mg2+ sources; dialysis if renal failure or severe toxicity"
                }
            }
        }
    ]
}
