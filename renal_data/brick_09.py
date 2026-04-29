BRICK = {
    "brick_num": 9,
    "brick_title": "Nephron Segmental Physiology",
    "games": [
        {
            "slug": "nephron_segment_functions",
            "title": "Nephron Segment Functions",
            "subtitle": "Match each segment to its primary transport role",
            "categories": ["Main Reabsorption", "Key Transporter", "Water Permeability"],
            "data": {
                "Proximal Tubule": {
                    "Main Reabsorption": "Na+, glucose, amino acids, HCO3-; about 65% filtered load",
                    "Key Transporter": "SGLT2 (early), NHE-3, Na+/K+ ATPase basolateral",
                    "Water Permeability": "Highly water-permeable; isosmotic reabsorption maintained"
                },
                "Thick Ascending Limb": {
                    "Main Reabsorption": "Na+, K+, Cl- actively; Ca2+ and Mg2+ paracellularly",
                    "Key Transporter": "NKCC2 cotransporter; furosemide pharmacologic target",
                    "Water Permeability": "Completely impermeable to water; diluting segment"
                },
                "Distal Convoluted Tubule": {
                    "Main Reabsorption": "NaCl (5-8% filtered Na+); regulated Ca2+ via PTH",
                    "Key Transporter": "NCC cotransporter; thiazide diuretic target",
                    "Water Permeability": "Early DCT relatively impermeable to water"
                },
                "Collecting Duct": {
                    "Main Reabsorption": "Na+ via ENaC; final urine composition checkpoint",
                    "Key Transporter": "ENaC (aldosterone), ROMK (K+ secretion), AQP2",
                    "Water Permeability": "ADH-dependent via AQP2 channel insertion"
                },
                "Thin Descending Limb": {
                    "Main Reabsorption": "Water exits osmotically; concentrates tubular fluid",
                    "Key Transporter": "Aquaporins; passive water movement only",
                    "Water Permeability": "Highly permeable to water, impermeable to solutes"
                }
            }
        },
        {
            "slug": "permeability_and_osmolality",
            "title": "Permeability and Tubular Osmolality",
            "subtitle": "How segment properties shape filtrate composition",
            "categories": ["Water Permeability", "Effect on Tubular Fluid", "Tight Junction Property"],
            "data": {
                "Proximal Tubule": {
                    "Water Permeability": "Very high; AQP1 plus leaky paracellular pathways",
                    "Effect on Tubular Fluid": "Stays isosmotic to plasma (~300 mOsm/kg)",
                    "Tight Junction Property": "Leaky claudins; allow paracellular Na+ and water"
                },
                "Thin Descending Limb": {
                    "Water Permeability": "High water permeability; impermeable to NaCl",
                    "Effect on Tubular Fluid": "Concentrated to ~1200 mOsm/kg in deep medulla",
                    "Tight Junction Property": "Selective; permits water but not solute"
                },
                "Thick Ascending Limb": {
                    "Water Permeability": "Completely water-impermeable; the diluting segment",
                    "Effect on Tubular Fluid": "Falls sharply to ~100 mOsm/kg entering DCT",
                    "Tight Junction Property": "Cation-selective; reabsorbs Mg2+ and Ca2+ paracellularly"
                },
                "Collecting Duct (no ADH)": {
                    "Water Permeability": "Low water permeability without ADH signaling",
                    "Effect on Tubular Fluid": "Dilute urine, as low as ~50 mOsm/kg excreted",
                    "Tight Junction Property": "Tight junctions seal off paracellular leakage"
                },
                "Collecting Duct (with ADH)": {
                    "Water Permeability": "High; AQP2 inserted into apical membrane",
                    "Effect on Tubular Fluid": "Concentrated urine up to ~1200 mOsm/kg",
                    "Tight Junction Property": "Tight junctions; transcellular water flow only"
                }
            }
        },
        {
            "slug": "transport_maximum_and_splay",
            "title": "Transport Maximum and Splay",
            "subtitle": "Predicting solute appearance in urine",
            "categories": ["Definition or Value", "Mechanism", "Clinical Consequence"],
            "data": {
                "Transport Maximum (Tm)": {
                    "Definition or Value": "Maximum tubular reabsorption rate per unit time (mg/min)",
                    "Mechanism": "Reflects saturation of carrier proteins like SGLT2",
                    "Clinical Consequence": "Above Tm, excess solute spills into urine"
                },
                "Glucose Tm": {
                    "Definition or Value": "Approximately 375 mg/min in adults",
                    "Mechanism": "SGLT2 (early PCT) and SGLT1 (late PCT) cotransporters",
                    "Clinical Consequence": "Glucosuria once filtered load exceeds threshold"
                },
                "Splay": {
                    "Definition or Value": "Curved transition where excretion begins gradually",
                    "Mechanism": "Heterogeneity of nephron Tm and SGLT affinity differences",
                    "Clinical Consequence": "Glucosuria starts before Tm fully saturated"
                },
                "Filtered Load": {
                    "Definition or Value": "Product of GFR and plasma solute concentration",
                    "Mechanism": "GFR ~125 mL/min times plasma glucose ~100 mg/dL",
                    "Clinical Consequence": "Normal load ~125 mg/min, well below glucose Tm"
                },
                "Diabetes Mellitus": {
                    "Definition or Value": "Plasma glucose rises above ~180 mg/dL threshold",
                    "Mechanism": "Filtered load exceeds Tm; SGLT transporters saturate",
                    "Clinical Consequence": "Osmotic diuresis with polyuria and electrolyte loss"
                },
                "Fanconi Syndrome": {
                    "Definition or Value": "Generalized PCT dysfunction from injury or toxins",
                    "Mechanism": "Reduced effective Tm for glucose, amino acids, phosphate",
                    "Clinical Consequence": "Glucosuria with normal plasma glucose plus aminoaciduria"
                }
            }
        }
    ]
}
