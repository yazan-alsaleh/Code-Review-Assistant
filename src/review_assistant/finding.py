# Before this file, every rule returns a dictionary. That works, but the problem that each rule
# must manually creates dictionaries. Also if you want to add another feature to the dictionary, you have to update this to all other rules 


class Finding:

    def __init__(self, rule, message, line, severity = "warning", category="quality"):

        self.rule = rule,
        self.message = message,
        self.line = line,
        self.severity = severity
        self.category = category


    # Instead of every rule creating its own dictionary, now we have one standard format.
    # Every rule creates a Finding object.
    def to_dict(self): 

        return {
            "rule": self.rule,
            "message": self.message,
            "line": self.line,
            "severity": self.severity,
            "category": self.category
        }





