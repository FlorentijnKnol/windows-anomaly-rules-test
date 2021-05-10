from python_rules import Rule


class AnomalousNrOfMessages(Rule):
    id = "c6c5990e-61df-455f-9638-34100263b028"
    title = "Anomalous nr of messages"
    description = "Detects an anomalous amount of messages observed within the span of six hours"
    author = "Florentijn Knol"
    date = "2021/05/10"
    level = "medium"


    def rule(self, e):
        return self.stats.windowed("6H").is_anomaly('total_count', threshold=1.5)
