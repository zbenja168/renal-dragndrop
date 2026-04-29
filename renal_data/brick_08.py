BRICK = {
    "brick_num": 8,
    "brick_title": "Regulation of Renal Blood Flow",
    "games": [
        {
            "slug": "renal_vascular_segments",
            "title": "Renal Vascular Segment Roles",
            "subtitle": "Match each renal vessel to its function and resistance role",
            "categories": ["Location/Path", "Resistance Role", "Key Function"],
            "data": {
                "Afferent arteriole": {
                    "Location/Path": "Branches from interlobular artery to glomerulus",
                    "Resistance Role": "Major resistance vessel regulating glomerular inflow",
                    "Key Function": "Controls blood flow entering glomerular capillaries"
                },
                "Efferent arteriole": {
                    "Location/Path": "Exits glomerulus toward peritubular capillaries or vasa recta",
                    "Resistance Role": "Controls outflow resistance from glomerulus",
                    "Key Function": "Determines glomerular hydrostatic pressure and filtration"
                },
                "Glomerular capillaries": {
                    "Location/Path": "Tuft between afferent and efferent arterioles",
                    "Resistance Role": "Minimal change to total resistance",
                    "Key Function": "Site of filtration; alters Kf via surface area"
                },
                "Peritubular capillaries": {
                    "Location/Path": "Surround proximal and distal tubules in cortex",
                    "Resistance Role": "Offer minimal resistance under normal conditions",
                    "Key Function": "Support reabsorption around cortical nephron tubules"
                },
                "Vasa recta": {
                    "Location/Path": "Long looping vessels following loop of Henle into medulla",
                    "Resistance Role": "Low-resistance medullary vessels",
                    "Key Function": "Supply juxtamedullary nephrons and concentrate urine"
                }
            }
        },
        {
            "slug": "autoregulation_mechanisms",
            "title": "Autoregulation: Myogenic vs TGF",
            "subtitle": "Compare intrinsic mechanisms maintaining stable RBF",
            "categories": ["Trigger/Sensor", "Speed of Onset", "Effector Action"],
            "data": {
                "Myogenic response": {
                    "Trigger/Sensor": "Stretch of afferent arteriole smooth muscle by pressure",
                    "Speed of Onset": "Engages within seconds, faster of two mechanisms",
                    "Effector Action": "Stretch-activated calcium channels constrict afferent arteriole"
                },
                "Tubuloglomerular feedback": {
                    "Trigger/Sensor": "Macula densa senses NaCl concentration in tubular fluid",
                    "Speed of Onset": "Engages over 10 to 15 seconds, slower",
                    "Effector Action": "Adenosine and ATP release constricts afferent arteriole"
                },
                "High MAP response": {
                    "Trigger/Sensor": "Increased wall tension and elevated NaCl at macula densa",
                    "Speed of Onset": "Combined response within seconds",
                    "Effector Action": "Afferent constriction reduces GFR back to baseline"
                },
                "Low MAP response": {
                    "Trigger/Sensor": "Reduced stretch and decreased NaCl delivery sensed",
                    "Speed of Onset": "Rapid myogenic followed by slower TGF adjustment",
                    "Effector Action": "Afferent dilation restores GFR despite lower pressure"
                },
                "Autoregulatory range": {
                    "Trigger/Sensor": "Operates when MAP is between 80 and 180 mmHg",
                    "Speed of Onset": "Independent of neural and hormonal input",
                    "Effector Action": "Maintains relatively constant RBF and GFR"
                }
            }
        },
        {
            "slug": "vasoactive_molecules",
            "title": "Vasoactive Molecules on Renal Tone",
            "subtitle": "Identify primary site of action and effect on RBF",
            "categories": ["Primary Site of Action", "Vascular Effect", "Clinical/Functional Role"],
            "data": {
                "Angiotensin II": {
                    "Primary Site of Action": "Primarily efferent arteriole via AT1 receptors",
                    "Vascular Effect": "Constricts efferent more than afferent arteriole",
                    "Clinical/Functional Role": "Maintains GFR during reduced renal perfusion"
                },
                "Nitric oxide": {
                    "Primary Site of Action": "Both afferent and efferent arterioles",
                    "Vascular Effect": "Dilates afferent and efferent arterioles",
                    "Clinical/Functional Role": "Endothelial-derived; opposes basal vasoconstrictor tone"
                },
                "Prostaglandins": {
                    "Primary Site of Action": "Particularly afferent arterioles",
                    "Vascular Effect": "Dilate afferent arterioles to preserve flow",
                    "Clinical/Functional Role": "Protect GFR in low-perfusion states; NSAIDs block"
                },
                "Sympathetic norepinephrine": {
                    "Primary Site of Action": "Alpha1-adrenergic receptors throughout renal vasculature",
                    "Vascular Effect": "Strong afferent and moderate efferent constriction",
                    "Clinical/Functional Role": "Reduces RBF during hemorrhagic shock and stress"
                },
                "Adenosine (renal)": {
                    "Primary Site of Action": "Afferent arteriole via A1 receptors",
                    "Vascular Effect": "Causes afferent arteriolar constriction",
                    "Clinical/Functional Role": "Mediates tubuloglomerular feedback signal"
                },
                "Dopamine (low dose)": {
                    "Primary Site of Action": "D1 receptors on renal vessels",
                    "Vascular Effect": "Dilates renal vessels",
                    "Clinical/Functional Role": "Increases renal blood flow at low doses"
                }
            }
        },
        {
            "slug": "arteriolar_tone_effects",
            "title": "Arteriolar Tone Effects on RBF, GFR, FF",
            "subtitle": "Predict hemodynamic consequences of arteriolar changes",
            "categories": ["Effect on RBF", "Effect on GFR", "Effect on Filtration Fraction"],
            "data": {
                "Afferent constriction": {
                    "Effect on RBF": "Decreased renal blood flow",
                    "Effect on GFR": "Decreased glomerular filtration rate",
                    "Effect on Filtration Fraction": "Variable filtration fraction change"
                },
                "Efferent constriction": {
                    "Effect on RBF": "Decreased renal blood flow",
                    "Effect on GFR": "Increased or unchanged GFR",
                    "Effect on Filtration Fraction": "Increased filtration fraction"
                },
                "Both constricted": {
                    "Effect on RBF": "Markedly decreased renal blood flow",
                    "Effect on GFR": "Decreased glomerular filtration rate",
                    "Effect on Filtration Fraction": "Variable filtration fraction change"
                },
                "Afferent dilation": {
                    "Effect on RBF": "Increased renal blood flow",
                    "Effect on GFR": "Increased glomerular filtration rate",
                    "Effect on Filtration Fraction": "Variable filtration fraction change"
                },
                "Efferent dilation": {
                    "Effect on RBF": "Increased renal blood flow",
                    "Effect on GFR": "Decreased or unchanged GFR",
                    "Effect on Filtration Fraction": "Decreased filtration fraction"
                }
            }
        }
    ]
}
