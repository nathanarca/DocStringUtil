from Teste import Teste


class Converters:

    def __init__(self):
        self.keyDescription = 'description'
        self.keyParameters = 'parameters'
        self.keyReturns = 'returns'

    def toDict(self, docString):

        lines = docString.splitlines()

        result = {}

        result[self.keyDescription] = self.getDescription(lines)
        result[self.keyParameters] = self.getParameters(lines)
        result[self.keyReturns] = self.getReturns(lines)

        return result

    def getDescription(self, lines):

        nextLineIsDescription = None

        description = ''

        for line in lines:

            line = line.strip()

            if (line == ''):
                continue

            if (nextLineIsDescription != None and line.endswith(':')):
                break

            if nextLineIsDescription:
                description += line

            if line.replace(":", "") == self.keyDescription:
                nextLineIsDescription = True

        return description

    def getParameters(self, lines):

        nextLineIsParameter = None

        parameters = []

        for line in lines:

            line = line.strip()

            if (line == ''):
                continue

            if (nextLineIsParameter != None and line.endswith(':')):
                break

            if nextLineIsParameter:
                parameters.append(self.extractParameter(line))

            if line.replace(":", "") == self.keyParameters:
                nextLineIsParameter = True

        return parameters

    def extractParameter(self, line):

        parameter = {}

        parameter['name'] = line.split('(')[0].strip()
        parameter['type'] = line.split('(')[1].split(')')[0].strip()
        parameter['description'] = line.split(')')[1].strip()

        return parameter

    def getReturns(self, lines):

        nextLineIsReturns = None

        description = {}

        for line in lines:

            line = line.strip()

            if (line == ''):
                continue

            if (nextLineIsReturns != None and line.endswith(':')):
                break

            if nextLineIsReturns:
                description = self.extractParameter(line)

            if line.replace(":", "") == self.keyReturns:
                nextLineIsReturns = True

        return description
        

        return None


conv = Converters()


result = conv.toDict(Teste.test.__doc__)

print(result)
