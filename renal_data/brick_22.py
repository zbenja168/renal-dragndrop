BRICK = {
    "brick_num": 22,
    "brick_title": "Hypokalemia",
    "games": [
        {
            "slug": "hypokalemia_causes",
            "title": "Causes of Hypokalemia",
            "subtitle": "Match each cause to its mechanism and clinical context",
            "categories": ["Mechanism", "Clinical Context", "Key Feature"],
            "data": {
                "Thiazide/Loop Diuretics": {
                    "Mechanism": "Increase distal Na delivery causing renal K wasting",
                    "Clinical Context": "Most common cause; 20-50% risk in users",
                    "Key Feature": "Often paired with metabolic alkalosis and chloride depletion"
                },
                "Diarrhea/Laxative Abuse": {
                    "Mechanism": "Direct GI potassium loss in stool",
                    "Clinical Context": "Chronic diarrhea or extensive laxative use",
                    "Key Feature": "Stool moves fast leaving little time for K reabsorption"
                },
                "Vomiting": {
                    "Mechanism": "Renal K wasting from volume depletion and HCl loss",
                    "Clinical Context": "Upper GI losses with metabolic alkalosis",
                    "Key Feature": "Aldosterone stimulation drives urinary K loss"
                },
                "Hyperaldosteronism": {
                    "Mechanism": "Aldosterone increases K secretion via ROMK channels",
                    "Clinical Context": "Adrenal adenoma or hyperplasia",
                    "Key Feature": "Hypertension with unexplained hypokalemia"
                },
                "Poor Dietary Intake": {
                    "Mechanism": "Insufficient potassium consumption (40-60 mEq daily needed)",
                    "Clinical Context": "Anorexia, alcohol use disorder, malnutrition",
                    "Key Feature": "Kidneys compensate but fail with severe deficiency"
                },
                "Intracellular Shift": {
                    "Mechanism": "Insulin or beta-2 agonists drive K into cells",
                    "Clinical Context": "Insulin therapy, albuterol, alkalosis",
                    "Key Feature": "Total body K normal but serum level low"
                }
            }
        },
        {
            "slug": "hypokalemia_genetic_disorders",
            "title": "Genetic Tubular Defects",
            "subtitle": "Match each inherited syndrome to its mechanism and effect",
            "categories": ["Acts Like", "Mechanism", "Clinical Effect"],
            "data": {
                "Gitelman Syndrome": {
                    "Acts Like": "Thiazide diuretic",
                    "Mechanism": "SLC12A3 mutation impairs Na/Cl cotransporter (NCC)",
                    "Clinical Effect": "Hypokalemia from increased distal sodium delivery"
                },
                "Bartter Syndrome": {
                    "Acts Like": "Loop diuretic",
                    "Mechanism": "Defective sodium transport in thick ascending limb",
                    "Clinical Effect": "Hypokalemia with promoted diuresis"
                },
                "Liddle Syndrome": {
                    "Acts Like": "Primary hyperaldosteronism",
                    "Mechanism": "Permanently open ENaC channel in principal cell",
                    "Clinical Effect": "Hypertension and hypokalemia from sodium reabsorption"
                },
                "Hypomagnesemia": {
                    "Acts Like": "Refractory potassium-losing state",
                    "Mechanism": "Magnesium normally inhibits ROMK potassium secretion",
                    "Clinical Effect": "More potassium secreted into urine causing hypokalemia"
                }
            }
        },
        {
            "slug": "hypokalemia_diagnosis_treatment",
            "title": "Diagnosis and Treatment",
            "subtitle": "Match each finding or therapy to its role",
            "categories": ["Type", "Finding or Use", "Clinical Significance"],
            "data": {
                "Serum Potassium": {
                    "Type": "First-line laboratory test",
                    "Finding or Use": "Level below 3.5 mEq/L confirms hypokalemia",
                    "Clinical Significance": "Symptoms typically appear when below 3.0 mEq/L"
                },
                "24-Hour Urine K": {
                    "Type": "Quantitative urine study",
                    "Finding or Use": "Greater than 25-30 mEq/day suggests renal loss",
                    "Clinical Significance": "Distinguishes renal from extrarenal potassium loss"
                },
                "ECG Changes": {
                    "Type": "Electrocardiogram findings",
                    "Finding or Use": "Shallow T waves, U waves, ST depression",
                    "Clinical Significance": "Severe cases risk supraventricular or ventricular tachycardia"
                },
                "Potassium Chloride": {
                    "Type": "Default oral or IV replacement",
                    "Finding or Use": "Co-repletes chloride in alkalosis or volume depletion",
                    "Clinical Significance": "First choice for diuretic or vomiting-induced hypokalemia"
                },
                "Spironolactone": {
                    "Type": "Potassium-sparing diuretic",
                    "Finding or Use": "Blocks aldosterone receptor at collecting duct",
                    "Clinical Significance": "Treats both hypokalemia and hypertension in hyperaldosteronism"
                },
                "Magnesium Repletion": {
                    "Type": "Concurrent electrolyte therapy",
                    "Finding or Use": "Restores ROMK inhibition to retain potassium",
                    "Clinical Significance": "Required for refractory hypokalemia with hypomagnesemia"
                }
            }
        }
    ]
}
