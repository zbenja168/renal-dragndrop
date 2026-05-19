BRICK = {
    "brick_num": 64,
    "brick_title": "Micturition",
    "games": [
        {
            "slug": "storage_vs_voiding_phase",
            "title": "Storage vs Voiding Phase Functions",
            "subtitle": "Match each bladder component to its state during storage, voiding, and key role.",
            "categories": ["Storage Phase", "Voiding Phase", "Key Role"],
            "data": {
                "Detrusor Muscle": {
                    "Storage Phase": "Relaxed and compliant, accommodating rising volume without major pressure increase",
                    "Voiding Phase": "Contracts strongly to drive bladder emptying through the urethra",
                    "Key Role": "Sets bladder pressure; main effector of urine storage versus expulsion"
                },
                "Internal Urethral Sphincter": {
                    "Storage Phase": "Contracted to maintain continence and prevent leakage of urine",
                    "Voiding Phase": "Opens passively as the bladder neck descends with detrusor contraction",
                    "Key Role": "Smooth muscle valve providing involuntary outlet resistance during storage"
                },
                "External Urethral Sphincter": {
                    "Storage Phase": "Tonically contracted via pudendal nerve to keep urethral outlet closed",
                    "Voiding Phase": "Actively released by voluntary withdrawal of somatic motor activity",
                    "Key Role": "Skeletal muscle providing voluntary control of urinary continence"
                },
                "Bladder Pressure": {
                    "Storage Phase": "Remains low despite increasing volume because of detrusor compliance",
                    "Voiding Phase": "Rises sharply as detrusor contracts to generate flow against gravity",
                    "Key Role": "Volume-pressure relationship determines bladder safety and urine flow"
                },
                "Phase Coordination": {
                    "Storage Phase": "Detrusor relaxed plus sphincters contracted maintains a closed compliant bladder",
                    "Voiding Phase": "Detrusor contraction must occur simultaneously with sphincter relaxation",
                    "Key Role": "Failure of coordination, called dyssynergia, causes incomplete or obstructed voiding"
                },
                "Phase Transition": {
                    "Storage Phase": "Storage continues until voluntary decision and bladder volume cross threshold",
                    "Voiding Phase": "Voiding voluntarily initiated; the reflex self-sustains until bladder is empty",
                    "Key Role": "Switch-like brainstem neural event driven by pons and modulated by cortex"
                }
            }
        },
        {
            "slug": "autonomic_micturition_pathways",
            "title": "Autonomic and Somatic Micturition Pathways",
            "subtitle": "Match each pathway to its target, receptor and signaling, and net effect.",
            "categories": ["Target", "Receptor and Signaling", "Net Effect"],
            "data": {
                "Sympathetic to Detrusor": {
                    "Target": "Smooth muscle of the detrusor at level T10 to L2",
                    "Receptor and Signaling": "Norepinephrine binds beta-3 receptors raising cAMP in smooth muscle",
                    "Net Effect": "Detrusor relaxation supporting low-pressure storage of urine"
                },
                "Sympathetic to Internal Sphincter": {
                    "Target": "Internal urethral sphincter smooth muscle innervated from T10 to L2",
                    "Receptor and Signaling": "Norepinephrine binds alpha-1 receptors via Gq/IP3 pathway",
                    "Net Effect": "Internal sphincter contraction to maintain continence during bladder filling"
                },
                "Somatic Pudendal Nerve": {
                    "Target": "Skeletal muscle of the external urethral sphincter from S2 to S4",
                    "Receptor and Signaling": "Acetylcholine binds nicotinic receptors on the striated muscle",
                    "Net Effect": "External sphincter contraction providing voluntary continence control"
                },
                "Parasympathetic M3 to Detrusor": {
                    "Target": "Smooth muscle of detrusor receiving pelvic splanchnic nerves S2 to S4",
                    "Receptor and Signaling": "Acetylcholine binds M3 receptors activating Gq/PLC and raising calcium",
                    "Net Effect": "Sustained detrusor contraction generating voiding pressure"
                },
                "Parasympathetic M2 to Detrusor": {
                    "Target": "Same detrusor smooth muscle innervated from S2 to S4",
                    "Receptor and Signaling": "Acetylcholine binds M2 receptors lowering cAMP in detrusor cells",
                    "Net Effect": "Amplifies M3 contraction by suppressing cAMP-mediated muscle relaxation"
                },
                "Withdrawal of Autonomic Tone": {
                    "Target": "Internal urethral sphincter and external urethral sphincter together",
                    "Receptor and Signaling": "Loss of alpha-1 and pudendal nicotinic signaling during voiding",
                    "Net Effect": "Sphincter relaxation, allowing bladder emptying to begin"
                }
            }
        },
        {
            "slug": "neural_control_loop_micturition",
            "title": "Neural Control Loop of Micturition",
            "subtitle": "Match each component to its location, functional role, and clinical relevance.",
            "categories": ["Location", "Functional Role", "Clinical Relevance"],
            "data": {
                "A-delta Afferents": {
                    "Location": "Myelinated sensory fibers within the bladder wall transmitting via pelvic nerve",
                    "Functional Role": "Detect mechanical stretch and encode bladder volume and wall tension",
                    "Clinical Relevance": "Loss of A-delta signaling impairs perception of bladder fullness"
                },
                "Periaqueductal Gray (PAG)": {
                    "Location": "Midbrain processing center receiving ascending bladder afferent input",
                    "Functional Role": "Integrates afferent signals and relays to prefrontal cortex and limbic system",
                    "Clinical Relevance": "Activates pontine micturition center once bladder fullness threshold is reached"
                },
                "Pontine Micturition Center": {
                    "Location": "Brainstem nucleus, also called Barrington nucleus, in the pontine tegmentum",
                    "Functional Role": "Triggers parasympathetic outflow while suppressing pudendal and sympathetic activity",
                    "Clinical Relevance": "Pontine lesion produces loss of coordinated detrusor-sphincter activation"
                },
                "Cortical Modulation": {
                    "Location": "Prefrontal cortex and limbic regions providing top-down control of micturition",
                    "Functional Role": "Allows voluntary deferral or initiation of voiding under social control",
                    "Clinical Relevance": "Cortical injury or dementia disrupts socially appropriate continence"
                },
                "Guarding Reflex": {
                    "Location": "Spinal loop in the sacral cord using interneurons to pudendal motor neurons",
                    "Functional Role": "Reinforces EUS contraction when bladder pressure rises or coughing occurs",
                    "Clinical Relevance": "Local reflex preserves some continence after incomplete spinal cord injury"
                },
                "Detrusor Overactivity": {
                    "Location": "Pathologic state of the detrusor arising from disrupted neural control",
                    "Functional Role": "Loss of inhibitory cortical control allows uncontrolled detrusor contractions",
                    "Clinical Relevance": "Common cause of urinary urgency and urge incontinence in older adults"
                }
            }
        }
    ]
}
