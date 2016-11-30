class CutlassTestUtil(object):
    def stringPropertyTest(self, test, obj, prop):
        value = "random"
        success = False

        try:
            setattr(obj, prop, value)
            success = True
        except:
            pass

        test.assertTrue(success, "Able to use the %s setter" % prop)

        retrieved = getattr(obj, prop)

        test.assertEqual(retrieved, value,
                         "Property getter for '%s' works." % prop)

    def intPropertyTest(self, test, obj, prop):
        value = 1313
        success = False

        try:
            setattr(obj, prop, value)
            success = True
        except:
            pass

        test.assertTrue(success, "Able to use the %s setter" % prop)

        retrieved = getattr(obj, prop)

        test.assertEqual(retrieved, value,
                         "Property getter for '%s' works." % prop)

    def intTypeTest(self, test, obj, prop):
        # test a string
        with test.assertRaises(Exception):
            setattr(obj, prop, "test")

        # test a list
        with test.assertRaises(Exception):
            setattr(obj, prop, ["test"])

        # test a dictionary
        with test.assertRaises(Exception):
            setattr(obj, prop, {})


    def stringTypeTest(self, test, obj, prop):
        # test an int
        with test.assertRaises(Exception):
            setattr(obj, prop, 1)

        # test a list
        with test.assertRaises(Exception):
            setattr(obj, prop, ["test"])

        # test a dictionary
        with test.assertRaises(Exception):
            setattr(obj, prop, {})
