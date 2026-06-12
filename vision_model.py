def get_image_findings(image):
    """
    Simulated medical vision model
    (Replace later with CheXzero / BioViL)
    """

    return [
        {
            "finding": "Right Lower Lobe Opacity",
            "region": "RLL",
            "confidence": 0.92
        },
        {
            "finding": "Pleural Effusion",
            "region": "Left Base",
            "confidence": 0.45
        }
    ]
