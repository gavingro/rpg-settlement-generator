class Settlement:
    """
    A parent Settlement class to interface with the generation of settlements.

    Other Settlements will derive from this class.
    """

    def __init__(self):
        self.generate_attributes()
        self.template = self.generate_template()

    # Generator scripts to ovverride in subclasses.
    #
    #

    def generate_attributes(self):
        """ Randomly generates settlement components for filling template."""
        pass

    def generate_template(self):
        """ Randomly Generates a settlement template to fill with attributes."""
        return "This is the base settlement generator."

    def fill_template(self, template):
        """ Replaces placeholders in template with their attributes"""
        return template

    def generate(self):
        """Returns prepared template, all filled in."""
        return self.fill_template(self.template)

    # Common methods that multiple subclasses use.
    #
    #
