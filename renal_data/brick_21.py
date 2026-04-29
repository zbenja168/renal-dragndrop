BRICK = {
    "brick_num": 21,
    "brick_title": "ADH Receptor Antagonists",
    "games": [
        {
            "slug": "adh_antagonist_drugs",
            "title": "ADH Antagonist Drugs",
            "subtitle": "Match each drug to its receptor target, route, and key use",
            "categories": ["Receptor Target", "Route", "Primary Use"],
            "data": {
                "Conivaptan": {
                    "Receptor Target": "Antagonizes both V1 and V2 ADH receptors",
                    "Route": "Intravenous (IV) administration only",
                    "Primary Use": "SIADH, with hypertonic saline for severe hyponatremia"
                },
                "Tolvaptan": {
                    "Receptor Target": "Selective oral V2 ADH receptor antagonist",
                    "Route": "Oral dosing for outpatient use",
                    "Primary Use": "SIADH, CHF hyponatremia, polycystic kidney disease"
                },
                "Demeclocycline": {
                    "Receptor Target": "Tetracycline interfering with ADH signaling pathway",
                    "Route": "Oral administration",
                    "Primary Use": "Chronic SIADH when V2 antagonists are contraindicated"
                }
            }
        },
        {
            "slug": "adh_antagonist_indications",
            "title": "Clinical Indications",
            "subtitle": "Match each condition to its mechanism link and treatment role",
            "categories": ["Underlying Problem", "Why ADH Antagonists Help", "Notes"],
            "data": {
                "SIADH": {
                    "Underlying Problem": "Inappropriate ADH secretion causing euvolemic hyponatremia",
                    "Why ADH Antagonists Help": "Block V2 receptors, reduce water reabsorption, raise sodium",
                    "Notes": "Primary indication; most common cause is hyponatremia"
                },
                "Heart Failure": {
                    "Underlying Problem": "Dilutional hyponatremia from neurohormonal water retention",
                    "Why ADH Antagonists Help": "Promote aquaresis, increase water excretion and GFR",
                    "Notes": "Tolvaptan approved for CHF-related hyponatremia"
                },
                "ADPKD": {
                    "Underlying Problem": "Genetic disorder with progressive renal cyst formation",
                    "Why ADH Antagonists Help": "Tolvaptan reduces cyst growth and slows renal decline",
                    "Notes": "FDA monitors tolvaptan use due to side effects"
                },
                "Cirrhosis Hyponatremia": {
                    "Underlying Problem": "Liver disease with low sodium and fluid overload",
                    "Why ADH Antagonists Help": "Conivaptan can be used; promotes free water excretion",
                    "Notes": "Tolvaptan avoided due to hepatotoxicity risk"
                }
            }
        },
        {
            "slug": "adh_antagonist_adverse",
            "title": "Adverse Effects and Cautions",
            "subtitle": "Match each adverse effect to its cause and management",
            "categories": ["Cause", "Associated Drug", "Mitigation Strategy"],
            "data": {
                "Osmotic Demyelinating Syndrome": {
                    "Cause": "Too-rapid correction of hyponatremia by vaptans",
                    "Associated Drug": "Conivaptan and tolvaptan",
                    "Mitigation Strategy": "Limit sodium rise to under 6-8 mEq/L per 24 hours"
                },
                "Hepatotoxicity": {
                    "Cause": "Elevated transaminases from V2 antagonist therapy",
                    "Associated Drug": "Tolvaptan only, not conivaptan",
                    "Mitigation Strategy": "Avoid in liver disease; limit use to under 30 days"
                },
                "Orthostatic Hypotension": {
                    "Cause": "Blockade of vasoconstricting V1 receptors",
                    "Associated Drug": "Conivaptan",
                    "Mitigation Strategy": "Monitor blood pressure; switch to selective V2 agent"
                },
                "CYP3A4 Drug Interactions": {
                    "Cause": "Vaptans are moderate CYP3A4 inhibitors",
                    "Associated Drug": "Conivaptan and tolvaptan",
                    "Mitigation Strategy": "Avoid ketoconazole, macrolides, ciprofloxacin, diazepam"
                }
            }
        }
    ]
}
