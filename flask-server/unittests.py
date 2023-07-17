import unittest

import datainterface
import map
import reduce
import server


class Testing(unittest.TestCase):
    def test_datainterface(self):
        articleData = datainterface.getArticleData()
        latestArticleDate = datainterface.getLatestArticleDate()
        self.assertEqual(isinstance(articleData, list),True)
        self.assertEqual(isinstance(latestArticleDate, str), True)

    def test_map(self):
        testString = "Teststring used for Tests, Tests?!, and  tests."
        expectedValue = [['teststring', 1], ['used', 1], ['for', 1], ['tests', 1], ['tests', 1], ['and', 1], ['tests', 1]]
        self.assertEqual(map.mapper(testString), expectedValue)

    def test_reduce(self):
        testMap = [['teststring', 1], ['used', 1], ['for', 1], ['tests', 1], ['tests', 1], ['and', 1], ['tests', 1]]
        expectedValue = [['teststring', 1], ['used', 1], ['for', 1], ['and', 1], ['tests', 3]]
        self.assertEqual(reduce.reducer(testMap), expectedValue)

    def test_server(self):
        testlist = [['teststring', 1], ['used', 1], ['for', 1], ['and', 1], ['tests', 3]]
        expectedValue = ['teststring : 1', 'used : 1', 'for : 1', 'and : 1', 'tests : 3']
        self.assertEqual(server.createMemberlist(testlist), expectedValue)
        self.assertEqual(isinstance(server.createWordCountMap(), list), True)

    
if __name__ == "__main__":
    unittest.main()