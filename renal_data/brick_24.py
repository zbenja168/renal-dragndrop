BRICK = {
    "brick_num": 24,
    "brick_title": "Renal Calcium and Phosphate Regulation",
    "games": [
        {
            "slug": "nephron_segment_handling",
            "title": "Nephron Segment Handling",
            "subtitle": "Match nephron segments to calcium/phosphate reabsorption",
            "categories": ["Calcium Reabsorbed", "Phosphate Reabsorbed", "Transport Mechanism"],
            "data": {
                "Proximal Tubule": {
                    "Calcium Reabsorbed": "About 70% of filtered calcium reclaimed here",
                    "Phosphate Reabsorbed": "Roughly 85% of filtered phosphate, primary site",
                    "Transport Mechanism": "Paracellular calcium driven by positive luminal potential"
                },
                "Thick Ascending Limb": {
                    "Calcium Reabsorbed": "About 20% via paracellular route",
                    "Phosphate Reabsorbed": "No phosphate reabsorption in this segment",
                    "Transport Mechanism": "Paracellular driven by positive lumen, calcium sensor present"
                },
                "Distal Convoluted Tubule": {
                    "Calcium Reabsorbed": "About 10% of filtered calcium reclaimed",
                    "Phosphate Reabsorbed": "No phosphate reabsorption occurs in DCT",
                    "Transport Mechanism": "Transcellular, regulated by PTH and calcitriol"
                },
                "Collecting Duct": {
                    "Calcium Reabsorbed": "Roughly 10% reabsorbed in late nephron",
                    "Phosphate Reabsorbed": "No phosphate reabsorption, 10% excreted in urine",
                    "Transport Mechanism": "Final fine-tuning of calcium handling"
                }
            }
        },
        {
            "slug": "hormonal_regulation",
            "title": "Hormones and Factors",
            "subtitle": "Match regulators to their effects on calcium and phosphate",
            "categories": ["Effect on Calcium", "Effect on Phosphate", "Source or Trigger"],
            "data": {
                "PTH": {
                    "Effect on Calcium": "Increases tubular calcium reabsorption in DCT",
                    "Effect on Phosphate": "Decreases proximal phosphate reabsorption, raises excretion",
                    "Source or Trigger": "Parathyroid glands respond to low serum calcium"
                },
                "Calcitriol": {
                    "Effect on Calcium": "Increases calcium reabsorption alongside PTH in DCT",
                    "Effect on Phosphate": "Promotes phosphate reabsorption indirectly via gut absorption",
                    "Source or Trigger": "Activated vitamin D from kidney 1-alpha-hydroxylase"
                },
                "FGF-23": {
                    "Effect on Calcium": "Indirect, lowers calcitriol reducing calcium absorption",
                    "Effect on Phosphate": "Reduces proximal phosphate reabsorption, increases urinary excretion",
                    "Source or Trigger": "Osteocytes release it when serum phosphate is high"
                },
                "Calcium-Sensing Receptor": {
                    "Effect on Calcium": "High calcium triggers less reabsorption in loop",
                    "Effect on Phosphate": "No direct phosphate effect from this receptor",
                    "Source or Trigger": "Thick ascending limb senses interstitial calcium levels"
                },
                "Metabolic Acidosis": {
                    "Effect on Calcium": "Promotes bone resorption releasing calcium into blood",
                    "Effect on Phosphate": "Reduces phosphate reabsorption to buffer urinary acid",
                    "Source or Trigger": "Kidneys use phosphate as titratable acid carrier"
                }
            }
        },
        {
            "slug": "ckd_mbd_and_management",
            "title": "CKD-MBD and Disorders",
            "subtitle": "Match conditions to mechanisms and management",
            "categories": ["Key Mechanism", "Lab Findings", "Management"],
            "data": {
                "Hypercalcemia": {
                    "Key Mechanism": "Excess calcium from bone resorption or absorption",
                    "Lab Findings": "Elevated serum calcium with often volume depletion polyuria",
                    "Management": "IV isotonic fluids, bisphosphonates, calcitonin, treat underlying cause"
                },
                "Mild Hypophosphatemia": {
                    "Key Mechanism": "Decreased intake or transient cellular shift",
                    "Lab Findings": "Phosphate 2.5 to 1 mg/dL, often asymptomatic",
                    "Management": "Oral phosphate replacement, monitor closely"
                },
                "Severe Hypophosphatemia": {
                    "Key Mechanism": "Marked depletion below 1 mg/dL with symptoms",
                    "Lab Findings": "Muscle weakness, respiratory compromise, low phosphate",
                    "Management": "Intravenous phosphate repletion until stable"
                },
                "Hyperphosphatemia": {
                    "Key Mechanism": "Impaired phosphate excretion, often from chronic kidney disease",
                    "Lab Findings": "Elevated phosphate, low calcium, cardiovascular complications",
                    "Management": "Dietary restriction, phosphate binders, vitamin D analogs"
                },
                "CKD-MBD": {
                    "Key Mechanism": "Phosphate retention raises FGF23, lowers calcitriol, raises PTH",
                    "Lab Findings": "High phosphate, low calcium, secondary hyperparathyroidism, weak bones",
                    "Management": "Vitamin D supplementation, calcitriol if PTH stays elevated"
                }
            }
        }
    ]
}
