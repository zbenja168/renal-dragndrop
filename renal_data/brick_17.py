BRICK = {
    "brick_num": 17,
    "brick_title": "Water Regulation",
    "games": [
        {
            "slug": "nephron_segments_water",
            "title": "Nephron Segments and Water Handling",
            "subtitle": "Match nephron segments to permeability and function",
            "categories": ["Water Permeability", "Sodium Handling", "Key Feature"],
            "data": {
                "Thin Descending Limb": {
                    "Water Permeability": "Permeable to water; water exits into interstitium",
                    "Sodium Handling": "Cannot reabsorb sodium",
                    "Key Feature": "Concentrates tubular fluid as water leaves"
                },
                "Thick Ascending Limb": {
                    "Water Permeability": "Impermeable to water; diluting segment",
                    "Sodium Handling": "Actively reabsorbs sodium via NKCC2",
                    "Key Feature": "Builds medullary gradient, dilutes tubular fluid"
                },
                "Collecting Duct": {
                    "Water Permeability": "ADH-regulated via aquaporin channels",
                    "Sodium Handling": "Minor sodium reabsorption",
                    "Key Feature": "Final urine concentration up to 1250 mOsm/kg"
                },
                "Proximal Tubule": {
                    "Water Permeability": "Freely permeable; reabsorbs two-thirds of filtrate",
                    "Sodium Handling": "Reabsorbs sodium isotonically with water",
                    "Key Feature": "Bulk reabsorption keeping plasma osmolality unchanged"
                }
            }
        },
        {
            "slug": "water_balance_disorders",
            "title": "Clinical Disorders of Water Balance",
            "subtitle": "Match each disorder to ADH status and cause",
            "categories": ["ADH Status", "Main Cause", "Result on Water"],
            "data": {
                "Central Diabetes Insipidus": {
                    "ADH Status": "Insufficient ADH release from posterior pituitary",
                    "Main Cause": "CNS injury or pituitary damage",
                    "Result on Water": "Excessive water loss, dilute urine"
                },
                "Nephrogenic Diabetes Insipidus": {
                    "ADH Status": "Adequate ADH but kidney resistance",
                    "Main Cause": "Lithium use or chronic hypercalcemia",
                    "Result on Water": "Excessive water loss despite ADH presence"
                },
                "SIADH": {
                    "ADH Status": "Inappropriate excess release of ADH",
                    "Main Cause": "Dilution of plasma in absence of osmotic stimuli",
                    "Result on Water": "Water retention causing hyponatremia"
                },
                "Hypernatremia": {
                    "ADH Status": "Increased serum sodium and high osmolality",
                    "Main Cause": "Net water loss or hypotonic free water loss",
                    "Result on Water": "High plasma osmolality, cellular dehydration"
                },
                "Hyponatremia": {
                    "ADH Status": "Often elevated ADH inappropriately",
                    "Main Cause": "Reduced water excretion plus excessive intake",
                    "Result on Water": "Low plasma osmolality, cells swell"
                }
            }
        },
        {
            "slug": "thirst_adh_triggers",
            "title": "Triggers of Thirst and ADH Release",
            "subtitle": "Match each trigger to its sensor and effect",
            "categories": ["Sensor Location", "Stimulus Type", "Body Response"],
            "data": {
                "High Serum Osmolality": {
                    "Sensor Location": "Osmoreceptors in the hypothalamus",
                    "Stimulus Type": "Increased solute concentration in plasma",
                    "Body Response": "Triggers thirst and ADH release from posterior pituitary"
                },
                "Low Blood Volume": {
                    "Sensor Location": "Baroreceptors sensing volume and pressure",
                    "Stimulus Type": "Hemorrhage or volume depletion",
                    "Body Response": "Stimulates thirst response and water conservation"
                },
                "Increased Angiotensin II": {
                    "Sensor Location": "Hypothalamic circumventricular organs",
                    "Stimulus Type": "RAAS activation from low renal perfusion",
                    "Body Response": "Drives thirst response to drink more water"
                },
                "ADH at Collecting Duct": {
                    "Sensor Location": "Vasopressin receptors on principal cells",
                    "Stimulus Type": "Circulating ADH from posterior pituitary",
                    "Body Response": "Inserts aquaporin channels increasing water reabsorption"
                }
            }
        },
        {
            "slug": "gradient_disruptors",
            "title": "Conditions Disrupting the Medullary Gradient",
            "subtitle": "Match each condition to its mechanism and effect",
            "categories": ["Mechanism", "Affected Process", "Clinical Effect"],
            "data": {
                "Loop Diuretic Use": {
                    "Mechanism": "Blocks NKCC2 transporter in thick ascending limb",
                    "Affected Process": "Prevents sodium reabsorption building gradient",
                    "Clinical Effect": "Medullary gradient cannot form, dilute urine"
                },
                "Acute Tubular Necrosis": {
                    "Mechanism": "Damages tubular cells impairing reabsorption",
                    "Affected Process": "Disrupts sodium and urea reabsorption in loop",
                    "Clinical Effect": "Loss of osmotic gradient despite adequate ADH"
                },
                "Severe Hypokalemia": {
                    "Mechanism": "Blunts countercurrent multiplication mechanism",
                    "Affected Process": "Impairs medullary concentrating ability",
                    "Clinical Effect": "Reduced water reabsorption despite ADH presence"
                },
                "Hypercalcemia": {
                    "Mechanism": "Interferes with sodium transport in loop of Henle",
                    "Affected Process": "Reduces medullary gradient formation",
                    "Clinical Effect": "Polyuria and impaired urine concentration"
                },
                "Low Urea State": {
                    "Mechanism": "Reduces urea contribution to interstitial osmolality",
                    "Affected Process": "Lowers maximal concentration capacity",
                    "Clinical Effect": "Decreased maximal urine osmolality below 1250"
                }
            }
        }
    ]
}
