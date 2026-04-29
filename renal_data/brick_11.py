BRICK = {
    "brick_num": 11,
    "brick_title": "Potassium Homeostasis",
    "games": [
        {
            "slug": "k_shift_factors",
            "title": "Factors Shifting Potassium Across Cells",
            "subtitle": "Match each factor to its direction and mechanism",
            "categories": ["Direction of K+ Shift", "Mechanism", "Resulting Plasma K+"],
            "data": {
                "Insulin": {
                    "Direction of K+ Shift": "Drives K+ into the cells from the ECF",
                    "Mechanism": "Stimulates Na+/K+-ATPase pump activity in cells",
                    "Resulting Plasma K+": "Lowers serum K+; treats acute hyperkalemia"
                },
                "Catecholamines (beta2)": {
                    "Direction of K+ Shift": "Drives K+ into the cells via beta2 receptors",
                    "Mechanism": "Activates Na+/K+-ATPase through cAMP-mediated signaling",
                    "Resulting Plasma K+": "Lowers serum K+; albuterol used for hyperkalemia"
                },
                "Hyperosmolarity": {
                    "Direction of K+ Shift": "Drives K+ out of cells into the ECF",
                    "Mechanism": "Osmotic drag pulls water out, raising intracellular K+",
                    "Resulting Plasma K+": "Raises serum K+; seen in DKA hyperglycemia"
                },
                "Acidemia": {
                    "Direction of K+ Shift": "Drives K+ out of cells into the ECF",
                    "Mechanism": "H+ enters cells; K+ exits to maintain electroneutrality",
                    "Resulting Plasma K+": "Raises serum K+; often causes hyperkalemia"
                },
                "Alkalemia": {
                    "Direction of K+ Shift": "Drives K+ into the cells from the ECF",
                    "Mechanism": "H+ exits cells; K+ enters to maintain electroneutrality",
                    "Resulting Plasma K+": "Lowers serum K+; can cause hypokalemia"
                },
                "Exercise": {
                    "Direction of K+ Shift": "Drives K+ out of muscle cells into ECF",
                    "Mechanism": "ATP depletion opens K+ channels in muscle cells",
                    "Resulting Plasma K+": "Raises local K+; acts as vasodilator metabolite"
                }
            }
        },
        {
            "slug": "nephron_k_handling",
            "title": "Potassium Handling Along the Nephron",
            "subtitle": "Match each segment to its role in K+ transport",
            "categories": ["Process", "Approximate Amount", "Transport Mechanism"],
            "data": {
                "Glomerulus": {
                    "Process": "Free filtration of K+ from plasma into Bowman space",
                    "Approximate Amount": "Filters about 720 mEq/day of K+ load",
                    "Transport Mechanism": "Passive filtration not regulated by body K+"
                },
                "Proximal Convoluted Tubule": {
                    "Process": "Major site of K+ reabsorption from filtrate",
                    "Approximate Amount": "Reabsorbs roughly 70% of filtered K+",
                    "Transport Mechanism": "Paracellular transport driven by sodium reabsorption"
                },
                "Thick Ascending Limb": {
                    "Process": "Secondary site of K+ reabsorption from tubular fluid",
                    "Approximate Amount": "Reabsorbs about 20% of filtered K+",
                    "Transport Mechanism": "NKCC2 cotransporter drives K+ uptake"
                },
                "Cortical Collecting Duct": {
                    "Process": "Main regulated site of K+ secretion into urine",
                    "Approximate Amount": "Variable secretion to match dietary K+ load",
                    "Transport Mechanism": "Principal cells use ROMK and BK channels"
                },
                "Distal Nephron (low K+)": {
                    "Process": "Reabsorbs K+ when dietary intake is low",
                    "Approximate Amount": "Variable reclamation during hypokalemia or deficit",
                    "Transport Mechanism": "Intercalated cells use H+/K+-ATPase pump"
                }
            }
        },
        {
            "slug": "distal_k_secretion_regulators",
            "title": "Regulators of Distal K+ Secretion",
            "subtitle": "Effects on cortical collecting duct K+ excretion",
            "categories": ["Effect on K+ Secretion", "Mechanism", "Clinical Example"],
            "data": {
                "Aldosterone": {
                    "Effect on K+ Secretion": "Increases K+ secretion into the tubular lumen",
                    "Mechanism": "Upregulates ENaC, Na+/K+-ATPase, ROMK and BK channels",
                    "Clinical Example": "RAAS blockade lowers aldosterone causing hyperkalemia"
                },
                "High Distal Na+ Delivery": {
                    "Effect on K+ Secretion": "Increases K+ secretion into the urine",
                    "Mechanism": "Enhances ENaC-driven Na+ uptake creating lumen negativity",
                    "Clinical Example": "Loop and thiazide diuretics cause hypokalemia"
                },
                "High Tubular Flow Rate": {
                    "Effect on K+ Secretion": "Increases K+ secretion into the urine",
                    "Mechanism": "Sweeps away luminal K+ and activates BK flow channels",
                    "Clinical Example": "Diuresis promotes urinary potassium losses"
                },
                "Acidemia": {
                    "Effect on K+ Secretion": "Decreases K+ secretion into the tubular lumen",
                    "Mechanism": "Reduces luminal K+ permeability, increases H+ secretion",
                    "Clinical Example": "Lactic acidosis worsens accompanying hyperkalemia"
                },
                "Alkalemia": {
                    "Effect on K+ Secretion": "Increases K+ secretion into the urine",
                    "Mechanism": "Raises luminal K+ permeability, lowers H+ secretion",
                    "Clinical Example": "Metabolic alkalosis amplifies diuretic-induced hypokalemia"
                },
                "High Plasma K+": {
                    "Effect on K+ Secretion": "Increases K+ secretion to excrete excess load",
                    "Mechanism": "Stimulates aldosterone release from adrenal cortex",
                    "Clinical Example": "High K+ diet drives matched urinary excretion"
                }
            }
        }
    ]
}
