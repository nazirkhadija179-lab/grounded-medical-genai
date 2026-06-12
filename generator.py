def generate_report(evidence):

    report = ["FINDINGS:\n"]

    for item in evidence["image_evidence"]:

        if item["confidence"] >= 0.80:

            report.append(
                f"- {item['finding']} in {item['region']} "
                f"(confidence={item['confidence']})"
            )

        else:
            report.append(
                f"- {item['finding']} → INSUFFICIENT EVIDENCE (REFUSED)"
            )

    report.append("\nPRIOR REPORTS:")

    report.extend(evidence["text"])
