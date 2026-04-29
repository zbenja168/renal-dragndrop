BRICK = {
    "brick_num": 10,
    "brick_title": "Sodium Homeostasis",
    "games": [
        {
            "slug": "nephron_sodium_handling",
            "title": "Nephron Segments and Sodium Reabsorption",
            "subtitle": "Match each nephron segment to its sodium handling",
            "categories": ["% Na+ Reabsorbed", "Transporter/Mechanism", "Drug/Hormone Effect"],
            "data": {
                "Proximal Tubule": {
                    "% Na+ Reabsorbed": "About 65-80% of filtered sodium load",
                    "Transporter/Mechanism": "NHE3 antiporter; couples with glucose, amino acids, bicarbonate",
                    "Drug/Hormone Effect": "Angiotensin II stimulates Na+ reabsorption here"
                },
                "Thick Ascending Limb": {
                    "% Na+ Reabsorbed": "About 10-20% of filtered sodium load",
                    "Transporter/Mechanism": "NKCC2 cotransporter; impermeable to water",
                    "Drug/Hormone Effect": "Loop diuretics like furosemide inhibit NKCC2"
                },
                "Distal Convoluted Tubule": {
                    "% Na+ Reabsorbed": "About 10% of filtered sodium load",
                    "Transporter/Mechanism": "Na+/Cl- cotransporter (NCC)",
                    "Drug/Hormone Effect": "Thiazide diuretics inhibit NCC; first-line for hypertension"
                },
                "Collecting Duct": {
                    "% Na+ Reabsorbed": "Remaining 2-5% of filtered sodium load",
                    "Transporter/Mechanism": "Epithelial sodium channels (ENaC); fine-tunes balance",
                    "Drug/Hormone Effect": "Aldosterone from adrenal gland upregulates ENaC"
                }
            }
        },
        {
            "slug": "sodium_regulators",
            "title": "Hormonal and Neural Sodium Regulators",
            "subtitle": "Compare extrarenal mechanisms of sodium control",
            "categories": ["Stimulus", "Mechanism", "Net Effect on Na+"],
            "data": {
                "RAAS": {
                    "Stimulus": "Low blood volume, low BP, renal hypoperfusion",
                    "Mechanism": "Ang II and aldosterone act on PT and collecting duct",
                    "Net Effect on Na+": "Increased Na+ and water reabsorption; raises BP"
                },
                "Sympathetic Nervous System": {
                    "Stimulus": "Low BP or trauma detected by baroreceptors",
                    "Mechanism": "Norepinephrine activates JG renin and tubular reabsorption",
                    "Net Effect on Na+": "Increased Na+ reabsorption, similar to RAAS"
                },
                "ANP / BNP": {
                    "Stimulus": "Volume overload stretches atrial and ventricular chambers",
                    "Mechanism": "Dilates afferent arteriole; inhibits renin and tubular Na+",
                    "Net Effect on Na+": "Natriuresis; increases urinary sodium loss"
                },
                "ADH (vasopressin)": {
                    "Stimulus": "Rising plasma osmolality after sodium intake",
                    "Mechanism": "Posterior pituitary release; promotes water reabsorption",
                    "Net Effect on Na+": "Retains water to dilute serum Na+ concentration"
                }
            }
        },
        {
            "slug": "intrarenal_autoregulation",
            "title": "Intrarenal Autoregulation Mechanisms",
            "subtitle": "Glomerulotubular balance and tubuloglomerular feedback",
            "categories": ["Sensor / Location", "Trigger", "Renal Response"],
            "data": {
                "Glomerulotubular Balance": {
                    "Sensor / Location": "Peritubular capillaries near proximal tubule",
                    "Trigger": "Increased GFR raises peritubular oncotic pressure",
                    "Renal Response": "Proximal tubule reabsorbs more Na+ to match filtration"
                },
                "Tubuloglomerular Feedback": {
                    "Sensor / Location": "Macula densa cells in distal tubule",
                    "Trigger": "High Na+/Cl- delivery signals excess filtration",
                    "Renal Response": "Constricts afferent arteriole; lowers GFR and Na+ filtration"
                },
                "Pressure Natriuresis": {
                    "Sensor / Location": "Renal vasculature sensing systemic blood pressure",
                    "Trigger": "Elevated arterial pressure increases renal perfusion",
                    "Renal Response": "Reduces tubular Na+ reabsorption; increases excretion"
                },
                "Macula Densa Renin Release": {
                    "Sensor / Location": "Juxtaglomerular cells adjacent to afferent arteriole",
                    "Trigger": "Low Na+/Cl- delivery indicates underperfusion",
                    "Renal Response": "Releases renin; activates RAAS to retain sodium"
                }
            }
        }
    ]
}
