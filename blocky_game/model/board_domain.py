import pddl


class BoardDomain:
    def __init__(self, domain_definition_path: str):
        self.domain = pddl.parse_domain(domain_definition_path)
