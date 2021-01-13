class Mother(object):
    def learningAWS(self):
        print('I am learning AWS')

    def softSkills(self):
        print('Managing people, leadership, conflict resolution, time-management')

class Father(object):
    def completingCertification(self):
        print('I am getting a certification.')
    
    def softSkills(self):
        print('Communication, organization, agenda-setting')

class Child(Mother, Father):
    def childSkills(self):
        self.learningAWS()
        self.completingCertification()
        print('I am learning Python and ML.')

    def softSkills(self):
        Mother.softSkills(self)
        Father.softSkills(self)
        print('Organization, documentation')

if __name__ == "__main__":
    c = Child()
    c.childSkills()
    print()
    c.softSkills()
