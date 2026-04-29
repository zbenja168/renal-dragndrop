BRICK = {
    "brick_num": 7,
    "brick_title": "Renal Clearance",
    "games": [
        {
            "slug": "renal_handling_classification",
            "title": "Classifying Renal Handling",
            "subtitle": "Compare Cx to GFR to determine net transport",
            "categories": ["Cx vs GFR", "Net Transport", "Example Solutes"],
            "data": {
                "Net Reabsorption": {
                    "Cx vs GFR": "Cx is less than GFR",
                    "Net Transport": "Negative value; substance returned to blood",
                    "Example Solutes": "Glucose, amino acids, sodium under normal conditions"
                },
                "Filtration Only": {
                    "Cx vs GFR": "Cx equals GFR",
                    "Net Transport": "Zero; neither reabsorbed nor secreted",
                    "Example Solutes": "Inulin"
                },
                "Net Secretion": {
                    "Cx vs GFR": "Cx is greater than GFR",
                    "Net Transport": "Positive value; transported from blood to tubule",
                    "Example Solutes": "PAH, organic acids, penicillin"
                },
                "Tubular Reabsorption": {
                    "Cx vs GFR": "Cx less than GFR by reabsorbed amount",
                    "Net Transport": "Substances return from tubule to peritubular capillaries",
                    "Example Solutes": "Glucose under normal physiologic conditions"
                }
            }
        },
        {
            "slug": "clearance_markers",
            "title": "Clearance Markers for GFR and RPF",
            "subtitle": "Inulin, creatinine, and PAH renal handling",
            "categories": ["Renal Handling", "What It Measures", "Practical Use"],
            "data": {
                "Inulin": {
                    "Renal Handling": "Freely filtered, no reabsorption or secretion",
                    "What It Measures": "Gold standard for true GFR",
                    "Practical Use": "Research only; needs IV infusion and timed collection"
                },
                "Creatinine": {
                    "Renal Handling": "Freely filtered plus small tubular secretion",
                    "What It Measures": "Estimates GFR; overestimates true GFR by 10-20%",
                    "Practical Use": "Clinical standard; endogenous, easily measured from serum"
                },
                "PAH": {
                    "Renal Handling": "Filtered and nearly completely secreted by proximal tubule",
                    "What It Measures": "Effective renal plasma flow with about 90% extraction",
                    "Practical Use": "Research; requires exogenous administration and sampling"
                },
                "eGFR (CKD-EPI)": {
                    "Renal Handling": "Based on serum creatinine handling",
                    "What It Measures": "Estimated GFR adjusted for age, sex, body size",
                    "Practical Use": "Routine clinical use; improves accuracy over raw creatinine"
                }
            }
        },
        {
            "slug": "filtration_fraction_conditions",
            "title": "Filtration Fraction in Disease",
            "subtitle": "How GFR/RPF ratio changes across conditions",
            "categories": ["FF Change", "Mechanism", "Clinical Note"],
            "data": {
                "Normal": {
                    "FF Change": "15-20%",
                    "Mechanism": "Balanced glomerular filtration and renal plasma flow",
                    "Clinical Note": "Healthy baseline filtration fraction"
                },
                "Congestive Heart Failure": {
                    "FF Change": "Increased",
                    "Mechanism": "RPF drops more than GFR; efferent arteriolar constriction",
                    "Clinical Note": "Angiotensin II preserves GFR despite poor perfusion"
                },
                "Pregnancy": {
                    "FF Change": "Decreased",
                    "Mechanism": "RPF rises proportionally more than GFR",
                    "Clinical Note": "Vasodilatory state increases renal perfusion"
                },
                "Nephrotic Syndrome": {
                    "FF Change": "Variable",
                    "Mechanism": "Depends on the specific underlying pathophysiology",
                    "Clinical Note": "Direction depends on glomerular injury pattern"
                },
                "Chronic Kidney Disease": {
                    "FF Change": "Variable",
                    "Mechanism": "Often decreased early; may rise in advanced disease",
                    "Clinical Note": "Reflects evolving balance of GFR and RPF loss"
                }
            }
        },
        {
            "slug": "tubular_transport_drugs",
            "title": "Tubular Transport and Drug Clearance",
            "subtitle": "How altered tubular handling impacts drug elimination",
            "categories": ["Effect on Transport", "Impact on Drug Clearance", "Example or Note"],
            "data": {
                "Competition for Transporters": {
                    "Effect on Transport": "Reduced uptake or efflux at shared carrier",
                    "Impact on Drug Clearance": "Decreased clearance of affected drugs",
                    "Example or Note": "Two drugs share OAT or OCT pathway"
                },
                "Transporter Saturation": {
                    "Effect on Transport": "Maximum transport rate reached",
                    "Impact on Drug Clearance": "Non-linear elimination kinetics",
                    "Example or Note": "Dose-dependent clearance behavior"
                },
                "Renal Disease": {
                    "Effect on Transport": "Decreased transporter expression and function",
                    "Impact on Drug Clearance": "Reduced clearance of secreted drugs",
                    "Example or Note": "Requires dose adjustment in CKD"
                },
                "Genetic Polymorphisms": {
                    "Effect on Transport": "Altered transporter activity between individuals",
                    "Impact on Drug Clearance": "Interindividual variability in clearance",
                    "Example or Note": "Pharmacogenomic differences in OAT/OCT activity"
                },
                "Urine pH Changes": {
                    "Effect on Transport": "Altered ionization state of drug molecules",
                    "Impact on Drug Clearance": "Changed passive reabsorption (ion trapping)",
                    "Example or Note": "Non-ionized forms diffuse back more readily"
                }
            }
        }
    ]
}
