BRICK = {
    "brick_num": 37,
    "brick_title": "Renal Laboratory Tests",
    "games": [
        {
            "slug": "renal_blood_tests_gfr",
            "title": "Blood Tests and GFR Estimation",
            "subtitle": "Match each renal blood test to its key features",
            "categories": ["What It Measures", "Key Feature", "Limitation or Use"],
            "data": {
                "Serum Creatinine": {
                    "What It Measures": "Filtration marker; byproduct of muscle creatine breakdown",
                    "Key Feature": "Freely filtered, not absorbed, minimally secreted",
                    "Limitation or Use": "Depends on muscle mass, age, sex, race"
                },
                "Blood Urea Nitrogen": {
                    "What It Measures": "Urea solute level; surrogate marker of GFR",
                    "Key Feature": "Filtered but reabsorbed and varies with diet",
                    "Limitation or Use": "Influenced by GI bleeding, catabolism, high protein intake"
                },
                "24-Hour Creatinine Clearance": {
                    "What It Measures": "GFR via timed urine creatinine collection",
                    "Key Feature": "Formula uses urine volume, urine and plasma Cr",
                    "Limitation or Use": "Cumbersome but historically gold standard for GFR"
                },
                "MDRD Equation": {
                    "What It Measures": "Estimated GFR using SCr and demographics",
                    "Key Feature": "Uses age, gender, ethnicity, and standard SCr",
                    "Limitation or Use": "Older equation, less accurate at higher GFR values"
                },
                "CKD-EPI Equation (2021)": {
                    "What It Measures": "Estimated GFR using SCr without race variable",
                    "Key Feature": "Uses age, gender, and serum creatinine only",
                    "Limitation or Use": "Most accurate and current eGFR equation used"
                },
                "Cockcroft-Gault Equation": {
                    "What It Measures": "Estimated creatinine clearance from SCr",
                    "Key Feature": "Uses age, weight, sex, and gender coefficient",
                    "Limitation or Use": "Often used for renal drug dose adjustments"
                }
            }
        },
        {
            "slug": "urine_dipstick_findings",
            "title": "Urine Dipstick Findings",
            "subtitle": "Match each dipstick parameter to its meaning",
            "categories": ["Normal Range or Value", "Abnormal Means", "Clinical Clue"],
            "data": {
                "Urine pH": {
                    "Normal Range or Value": "Normally 4.5 to 8.0",
                    "Abnormal Means": "Low pH means acidic; high pH means alkaline",
                    "Clinical Clue": "Helps detect renal tubular acidosis or stone risk"
                },
                "Specific Gravity": {
                    "Normal Range or Value": "Ranges from 1.005 to 1.030",
                    "Abnormal Means": "Low is dilute (isosthenuria); high is concentrated",
                    "Clinical Clue": "Reflects hydration and tubular concentrating ability"
                },
                "Glucose": {
                    "Normal Range or Value": "Should be negative on dipstick normally",
                    "Abnormal Means": "Positive means glucose exceeds reabsorption capacity",
                    "Clinical Clue": "Seen in diabetes and Fanconi syndrome"
                },
                "Ketones": {
                    "Normal Range or Value": "Should be negative on dipstick normally",
                    "Abnormal Means": "Detects acetoacetate and beta-hydroxybutyrate",
                    "Clinical Clue": "Positive in DKA, starvation, or alcoholic ketoacidosis"
                },
                "Bilirubin and Urobilinogen": {
                    "Normal Range or Value": "Trace urobilinogen; bilirubin negative",
                    "Abnormal Means": "Detects conjugated bilirubin or its metabolites",
                    "Clinical Clue": "Seen in hepatocellular or biliary tree liver disease"
                },
                "Leukocyte Esterase and Nitrites": {
                    "Normal Range or Value": "Both should be negative normally",
                    "Abnormal Means": "Esterase shows WBCs; nitrites show bacteria",
                    "Clinical Clue": "Together strongly suggest urinary tract infection"
                }
            }
        },
        {
            "slug": "urine_microscopy_findings",
            "title": "Urine Microscopy Findings",
            "subtitle": "Match each finding to its associated condition",
            "categories": ["Microscopy Finding", "Associated Condition", "Key Clue"],
            "data": {
                "Dysmorphic RBCs": {
                    "Microscopy Finding": "Misshapen red blood cells in urine",
                    "Associated Condition": "Glomerular disease such as glomerulonephritis",
                    "Key Clue": "Squeeze through damaged glomerular basement membrane"
                },
                "RBC Casts": {
                    "Microscopy Finding": "Cylindrical molds containing red blood cells",
                    "Associated Condition": "Pathognomonic for glomerulonephritis",
                    "Key Clue": "Made from protein and cellular debris in tubule"
                },
                "WBC Casts": {
                    "Microscopy Finding": "Cylindrical casts containing white blood cells",
                    "Associated Condition": "Pyelonephritis or interstitial nephritis",
                    "Key Clue": "Form when WBCs exit inflamed renal tubules"
                },
                "Granular Casts": {
                    "Microscopy Finding": "Degenerated renal tubule epithelial casts",
                    "Associated Condition": "Hallmark of acute tubular necrosis (ATN)",
                    "Key Clue": "Result from toxic or hypoxic tubular injury"
                },
                "Calcium Oxalate Crystals": {
                    "Microscopy Finding": "Dumbbell or envelope-shaped urine crystals",
                    "Associated Condition": "Kidney stones or ethylene glycol intoxication",
                    "Key Clue": "Most common crystal type in urinary tract stones"
                },
                "Cystine Crystals": {
                    "Microscopy Finding": "Hexagonal crystals visible on microscopy",
                    "Associated Condition": "Pathognomonic for cystinuria",
                    "Key Clue": "Form from insoluble cystine in acidic urine"
                }
            }
        }
    ]
}
