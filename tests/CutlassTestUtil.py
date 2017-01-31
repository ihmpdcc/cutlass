class CutlassTestUtil(object):
    def boolPropertyTest(self, test, obj, prop):
        value1 = True
        success1 = False

        try:
            setattr(obj, prop, value1)
            success1 = True
        except:
            pass

        test.assertTrue(success1, "Able to use the %s setter to True" % prop)

        retrieved1 = getattr(obj, prop)

        test.assertEqual(retrieved1, value1,
                         "Property getter for '%s' works." % prop)

        value2 = False
        success2 = False

        try:
            setattr(obj, prop, value2)
            success2 = True
        except:
            pass

        test.assertTrue(success2, "Able to use the %s setter to False" % prop)

        retrieved2 = getattr(obj, prop)

        test.assertEqual(retrieved2, value2,
                         "Property getter for '%s' works." % prop)


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

    def boolTypeTest(self, test, obj, prop):
        # test a string
        with test.assertRaises(Exception):
            setattr(obj, prop, "test")

        # test an int
        with test.assertRaises(Exception):
            setattr(obj, prop, 1)

        # test a list
        with test.assertRaises(Exception):
            setattr(obj, prop, ["test"])

        # test a dictionary
        with test.assertRaises(Exception):
            setattr(obj, prop, {})

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
