from python_rules import Rule


class AnomalousNrOfUniqueSourceIPS(Rule):
    id = "3209dc73-7d73-4bf6-9b4b-7b50cbf59f3a"
    title = "Anomalous nr of unique source ips"
    description = "Detects an anomalous number of unique source ips observed within the span of six hours"
    author = "Florentijn Knol"
    date = "2021/05/10"
    level = "medium"


    def rule(self, e):
        return self.stats.windowed("10m").is_anomaly(metric='n_unique', key='source.ip', threshold=1.0)
