import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_variables(self) : 
        runtimes = movies_df["runtime"]
        val = runtimes.loc["Split"]
        self.assertTrue( np.abs( split_runtime - val )<1e-7, "you have set the variable split_runtime incorrectly"  ) 
        metascore = movies_df["metascore"]
        val = metascore.loc["Prometheus"]
        self.assertTrue( np.abs( prometheus_metascore - val )<1e-7, "you have set the variable prometheus_metascore incorrectly"  ) 
        rating = movies_df["rating"]
        val = rating.loc["Arrival"]
        self.assertTrue( np.abs( arrival_rating - val )<1e-7, "you have set the variable arrival_rating incorrectly"  )
        takings = movies_df["revenue_millions"]
        val = takings.loc["Moana"]
        self.assertTrue( np.abs( moana_takings - val )<1e-7, "you have set the variable moana_takings incorrectly"  )
        votes = movies_df["votes"]
        val = votes.loc["Colossal"]
        self.assertTrue( np.abs( colossal_votes - val )<1e-7, "you have set the variable colossal_votes incorrectly" )
