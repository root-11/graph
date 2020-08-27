from graph import Graph


def graph01():
    """
    :return: Graph.
    """
    d = {1: {2: 10, 3: 5},
         2: {4: 1, 3: 2},
         3: {2: 3, 4: 9, 5: 2},
         4: {5: 4},
         5: {1: 7, 4: 6}}
    return Graph(from_dict=d)


def graph3x3():
    """
    1 -> 2 -> 3
    |    |    |
    v    v    v
    4 -> 5 -> 6
    |    |    |
    v    v    v
    7 -> 8 -> 9

    :return: :return:
    """
    d = {1: {2: 1, 4: 1},
         2: {3: 1, 5: 1},
         3: {6: 1},
         4: {5: 1, 7: 1},
         5: {6: 1, 8: 1},
         6: {9: 1},
         7: {8: 1},
         8: {9: 1}
         }
    return Graph(from_dict=d)


def graph4x4():
    edges = [
        (1, 2, 1), (2, 3, 1), (3, 4, 1), (1, 5, 1),
        (5, 6, 1), (6, 7, 1), (7, 8, 1), (2, 6, 1),
        (3, 7, 1), (4, 8, 1), (5, 9, 1), (9, 10, 1),
        (10, 11, 1), (11, 12, 1), (6, 10, 1), (7, 11, 1),
        (8, 12, 1), (9, 13, 1), (13, 14, 1), (14, 15, 1),
        (15, 16, 1), (10, 14, 1), (11, 15, 1), (12, 16, 1)
    ]
    g = Graph()
    for s, e, d in edges:
        g.add_edge(s, e, d, bidirectional=True)
    return g


def graph5x5():
    edges = [
        (1, 2), (2, 3), (3, 4), (4, 5),
        (1, 6), (2, 7), (3, 8), (4, 9), (5, 10),
        (6, 7), (7, 8), (8, 9), (9, 10),
        (6, 11), (7, 12), (8, 13), (9, 14), (10, 15),
        (11, 12), (12, 13), (13, 14), (14, 15),
        (11, 16), (12, 17), (13, 18), (14, 19), (15, 20),
        (16, 17), (17, 18), (18, 19), (19, 20),
        (16, 21), (17, 22), (18, 23), (19, 24), (20, 25),
        (21, 22), (22, 23), (23, 24), (24, 25)
    ]
    g = Graph()
    for s, e in edges:
        g.add_edge(s, e, 1, bidirectional=True)
    return g


def graph03():
    d = {1: {2: 1, 3: 9, 4: 4, 5: 13, 6: 20},
         2: {1: 7, 3: 7, 4: 2, 5: 11, 6: 18},
         3: {8: 20, 4: 4, 5: 4, 6: 16, 7: 16},
         4: {8: 15, 3: 4, 5: 9, 6: 11, 7: 21},
         5: {8: 11, 6: 2, 7: 17},
         6: {8: 9, 7: 5},
         7: {8: 3},
         8: {7: 5}}
    return Graph(from_dict=d)


def graph04():
    d = {1: {2: 1, 3: 9, 4: 4, 5: 11, 6: 17},
         2: {1: 7, 3: 7, 4: 2, 5: 9, 6: 15},
         3: {8: 17, 4: 4, 5: 4, 6: 14, 7: 13},
         4: {8: 12, 3: 4, 5: 9, 6: 9, 7: 18},
         5: {8: 9, 6: 2, 7: 15},
         6: {8: 9, 7: 5},
         7: {8: 3},
         8: {7: 5}}
    return Graph(from_dict=d)


def graph05():
    """
    0 ---- 1 ---- 5
     +      +---- 6 ---- 7
      +            +     |
       +            +---- 8
        +
         +- 2 ---- 3 ---- 9
             +      +     |
              4      +---10
    """
    links = [
        (0, 1, 1),
        (0, 2, 1),
        (1, 5, 1),
        (1, 6, 1),
        (2, 3, 1),
        (2, 4, 1),
        (3, 9, 1),
        (3, 10, 1),
        (9, 10, 1),
        (6, 7, 1),
        (6, 8, 1),
        (7, 8, 1),
        (0, 1, 1),
        (0, 1, 1),
        (0, 1, 1),
    ]
    return Graph(from_list=links)


def graph_cycle_5():
    """ cycle of 5 nodes """
    links = [
        (1, 2, 1),
        (2, 3, 1),
        (3, 4, 1),
        (4, 5, 1),
        (5, 1, 1),
    ]
    links.extend([(n2, n1, d) for n1, n2, d in links])
    return Graph(from_list=links)


def graph_cycle_6():
    """
    cycle of 6 nodes
    """
    links = [
        (1, 2, 1),
        (2, 3, 1),
        (3, 4, 1),
        (4, 5, 1),
        (5, 6, 1),
        (6, 1, 1),
    ]
    links.extend([(n2, n1, d) for n1, n2, d in links])
    return Graph(from_list=links)


def fully_connected_4():
    """
    fully connected graph with 4 nodes.
    """
    L = [
        (0, 3, 1), (0, 2, 1), (0, 1, 1), (3, 2, 1), (3, 1, 1), (3, 0, 1),
        (2, 3, 1), (2, 1, 1), (2, 0, 1), (1, 0, 1), (1, 2, 1), (1, 3, 1),
        (0,), (1,), (2,), (3,)
    ]
    g = Graph(from_list=L)
    return g


def mountain_river_map():
    """ Detailed mountain river map. Contributed by Harry Darby & Hartmut Mause """
    L = [(0,), (0, 164, 1), (1,), (1, 235, 1), (2,), (2, 1, 1), (3,), (3, 196, 1), (4,), (4, 3, 1), (5,), (5, 225, 1),
         (6,), (6, 5, 1), (7,), (7, 5, 1), (8,), (8, 211, 1), (9,), (9, 8, 1), (10,), (10, 144, 1), (11,), (11, 10, 1),
         (12,), (12, 234, 1), (13,), (13, 12, 1), (14,), (14, 172, 1), (15,), (15, 14, 1), (16,), (16, 14, 1), (17,),
         (17, 184, 1), (18,), (18, 17, 1), (19,), (19, 226, 1), (20,), (20, 19, 1), (21,), (21, 14, 1), (22,),
         (22, 222, 1), (23,), (23, 22, 1), (24,), (24, 240, 1), (25,), (25, 24, 1), (26,), (26, 241, 1), (27,),
         (27, 26, 1), (28,), (28, 71, 1), (29,), (29, 28, 1), (30,), (30, 28, 1), (31,), (31, 198, 1), (32,),
         (32, 31, 1), (33,), (33, 67, 1), (34,), (34, 33, 1), (35,), (35, 247, 1), (36,), (36, 35, 1), (37,),
         (37, 194, 1), (38,), (38, 37, 1), (39,), (39, 193, 1), (40,), (40, 39, 1), (41,), (41, 39, 1), (42,),
         (42, 39, 1), (43,), (43, 230, 1), (44,), (44, 43, 1), (45,), (45, 233, 1), (46,), (46, 45, 1), (47,),
         (47, 238, 1), (48,), (48, 47, 1), (49,), (49, 47, 1), (50,), (50, 215, 1), (51,), (51, 50, 1), (52,),
         (52, 166, 1), (53,), (53, 52, 1), (54,), (54, 170, 1), (55,), (55, 54, 1), (56,), (56, 231, 1), (57,),
         (57, 56, 1), (58,), (58, 56, 1), (59,), (59, 206, 1), (60,), (60, 59, 1), (61,), (61, 188, 1), (62,),
         (62, 61, 1), (63,), (63, 56, 1), (64,), (64, 229, 1), (65,), (65, 64, 1), (66,), (66, 223, 1), (67,),
         (67, 40, 1), (68,), (68, 2, 1), (68, 4, 1), (69,), (69, 66, 1), (70,), (70, 74, 1), (71,), (71, 65, 1), (72,),
         (72, 76, 1), (73,), (73, 66, 1), (74,), (74, 244, 1), (75,), (75, 78, 1), (76,), (76, 221, 1), (77,),
         (77, 66, 1), (78,), (78, 202, 1), (79,), (79, 85, 1), (80,), (80, 81, 1), (81,), (81, 204, 1), (82,),
         (82, 86, 1), (83,), (83, 66, 1), (84,), (84, 87, 1), (85,), (85, 220, 1), (86,), (86, 250, 1), (87,),
         (87, 248, 1), (88,), (88, 89, 1), (89,), (89, 251, 1), (90,), (90, 91, 1), (91,), (91, 186, 1), (92,),
         (92, 95, 1), (93,), (93, 94, 1), (94,), (94, 175, 1), (95,), (95, 180, 1), (96,), (96, 97, 1), (97,),
         (97, 209, 1), (98,), (98, 100, 1), (99,), (99, 102, 1), (100,), (100, 227, 1), (101,), (101, 106, 1), (102,),
         (102, 185, 1), (103,), (103, 107, 1), (104,), (104, 106, 1), (105,), (105, 109, 1), (106,), (106, 181, 1),
         (107,), (107, 135, 1), (108,), (108, 112, 1), (109,), (109, 224, 1), (110,), (110, 113, 1), (111,),
         (111, 47, 1), (112,), (112, 236, 1), (113,), (113, 190, 1), (114,), (114, 117, 1), (115,), (115, 116, 1),
         (116,), (116, 218, 1), (117,), (117, 183, 1), (118,), (118, 117, 1), (119,), (119, 120, 1), (120,),
         (120, 201, 1), (121,), (121, 122, 1), (122,), (122, 243, 1), (123,), (123, 127, 1), (124,), (124, 125, 1),
         (125,), (125, 197, 1), (126,), (126, 129, 1), (127,), (127, 217, 1), (128,), (128, 125, 1), (129,),
         (129, 68, 1), (130,), (130, 132, 1), (131,), (131, 136, 1), (132,), (132, 216, 1), (133,), (133, 117, 1),
         (134,), (134, 138, 1), (135,), (135, 46, 1), (135, 105, 1), (136,), (136, 173, 1), (137,), (137, 117, 1),
         (138,), (138, 191, 1), (139,), (139, 117, 1), (140,), (140, 141, 1), (141,), (141, 213, 1), (142,),
         (142, 141, 1), (143,), (143, 147, 1), (144,), (144, 15, 1), (145,), (145, 152, 1), (146,), (146, 154, 1),
         (146, 167, 1), (147,), (147, 141, 1), (148,), (148, 155, 1), (149,), (149, 141, 1), (150,), (150, 141, 1),
         (151,), (151, 141, 1), (152,), (152, 242, 1), (153,), (153, 157, 1), (154,), (154, 228, 1), (155,),
         (155, 195, 1), (156,), (156, 162, 1), (156, 163, 1), (157,), (157, 249, 1), (158,), (158, 159, 1), (159,),
         (159, 189, 1), (160,), (160, 161, 1), (161,), (161, 228, 1), (162,), (162, 0, 1), (163,), (163, 245, 1),
         (164,), (164, 165, 1), (165,), (165, 187, 1), (166,), (166, 57, 1), (167,), (167, 200, 1), (168,),
         (168, 214, 1), (169,), (169, 205, 1), (170,), (170, 60, 1), (170, 62, 1), (171,), (171, 177, 1), (172,),
         (172, 23, 1), (173,), (173, 137, 1), (174,), (174, 210, 1), (175,), (175, 44, 1), (175, 103, 1), (176,),
         (176, 118, 1), (177,), (177, 252, 1), (178,), (178, 179, 1), (179,), (179, 239, 1), (180,), (180, 96, 1),
         (181,), (181, 93, 1), (182,), (183,), (183, 146, 1), (184,), (184, 9, 1), (184, 20, 1), (185,), (185, 104, 1),
         (186,), (186, 134, 1), (186, 171, 1), (187,), (187, 169, 1), (188,), (188, 63, 1), (189,), (189, 160, 1),
         (190,), (190, 115, 1), (191,), (191, 139, 1), (192,), (193,), (193, 70, 1), (194,), (194, 42, 1), (195,),
         (195, 121, 1), (195, 123, 1), (196,), (196, 7, 1), (197,), (197, 126, 1), (198,), (198, 36, 1), (198, 38, 1),
         (199,), (199, 151, 1), (200,), (201,), (201, 148, 1), (202,), (202, 79, 1), (202, 82, 1), (203,),
         (203, 149, 1), (204,), (204, 83, 1), (205,), (205, 245, 1), (206,), (206, 58, 1), (207,), (207, 246, 1),
         (208,), (208, 207, 1), (209,), (209, 98, 1), (209, 99, 1), (210,), (210, 200, 1), (211,), (211, 11, 1),
         (211, 13, 1), (212,), (212, 142, 1), (213,), (213, 145, 1), (214,), (214, 176, 1), (215,), (215, 72, 1),
         (215, 75, 1), (216,), (216, 133, 1), (217,), (217, 128, 1), (218,), (218, 88, 1), (218, 168, 1), (219,),
         (219, 140, 1), (220,), (220, 77, 1), (221,), (221, 69, 1), (222,), (222, 25, 1), (222, 27, 1), (223,),
         (223, 92, 1), (224,), (224, 111, 1), (225,), (225, 18, 1), (226,), (226, 21, 1), (227,), (227, 101, 1), (228,),
         (228, 156, 1), (229,), (229, 32, 1), (229, 34, 1), (230,), (230, 48, 1), (231,), (231, 51, 1), (232,),
         (232, 119, 1), (233,), (233, 49, 1), (234,), (234, 16, 1), (235,), (235, 6, 1), (236,), (236, 90, 1),
         (236, 110, 1), (237,), (237, 150, 1), (238,), (238, 108, 1), (239,), (239, 130, 1), (239, 131, 1), (240,),
         (240, 29, 1), (241,), (241, 30, 1), (242,), (242, 153, 1), (243,), (243, 124, 1), (244,), (244, 53, 1),
         (244, 55, 1), (245,), (245, 208, 1), (246,), (246, 174, 1), (247,), (247, 41, 1), (248,), (248, 73, 1), (249,),
         (249, 158, 1), (250,), (250, 80, 1), (250, 84, 1), (251,), (251, 114, 1), (252,), (252, 178, 1)]
    g = Graph(from_list=L)
    return g


def london_underground():
    """ the london underground network """
    london_underground_stations = {  # id:(latitude,longitude,station name),
        1: (51.5028, -0.2801, "Acton Town"),
        2: (51.5143, -0.0755, "Aldgate"),
        3: (51.5154, -0.0726, "Aldgate East"),
        4: (51.5107, -0.013, "All Saints"),
        5: (51.5407, -0.2997, "Alperton"),
        7: (51.5322, -0.1058, "Angel"),
        8: (51.5653, -0.1353, "Archway"),
        9: (51.6164, -0.1331, "Arnos Grove"),
        10: (51.5586, -0.1059, "Arsenal"),
        11: (51.5226, -0.1571, "Baker Street"),
        12: (51.4431, -0.1525, "Balham"),
        13: (51.5133, -0.0886, "Bank"),
        14: (51.5204, -0.0979, "Barbican"),
        15: (51.5396, 0.081, "Barking"),
        16: (51.5856, 0.0887, "Barkingside"),
        17: (51.4905, -0.2139, "Barons Court"),
        18: (51.5121, -0.1879, "Bayswater"),
        19: (51.5148, 0.0613, "Beckton"),
        20: (51.5087, 0.055, "Beckton Park"),
        21: (51.5403, 0.127, "Becontree"),
        22: (51.5504, -0.1642, "Belsize Park"),
        24: (51.527, -0.0549, "Bethnal Green"),
        25: (51.512, -0.1031, "Blackfriars"),
        26: (51.5867, -0.0417, "Blackhorse Road"),
        27: (51.5079, -0.0066, "Blackwall"),
        28: (51.5142, -0.1494, "Bond Street"),
        29: (51.5011, -0.0943, "Borough"),
        30: (51.4956, -0.325, "Boston Manor"),
        31: (51.6071, -0.1243, "Bounds Green"),
        32: (51.5273, -0.0208, "Bow Church"),
        33: (51.5269, -0.0247, "Bow Road"),
        34: (51.5766, -0.2136, "Brent Cross"),
        36: (51.5248, -0.0119, "Bromley-By-Bow"),
        38: (51.6028, -0.2641, "Burnt Oak"),
        39: (51.5481, -0.1188, "Caledonian Road"),
        40: (51.5392, -0.1426, "Camden Town"),
        42: (51.5051, -0.0209, "Canary Wharf"),
        44: (51.5113, -0.0904, "Cannon Street"),
        45: (51.6078, -0.2947, "Canons Park"),
        47: (51.5441, -0.1538, "Chalk Farm"),
        48: (51.5185, -0.1111, "Chancery Lane"),
        49: (51.508, -0.1247, "Charing Cross"),
        51: (51.6177, 0.0755, "Chigwell"),
        52: (51.4946, -0.2678, "Chiswick Park"),
        54: (51.4618, -0.1384, "Clapham Common"),
        55: (51.4649, -0.1299, "Clapham North"),
        56: (51.4527, -0.148, "Clapham South"),
        58: (51.5955, -0.2502, "Colindale"),
        59: (51.418, -0.1778, "Colliers Wood"),
        60: (51.5129, -0.1243, "Covent Garden"),
        61: (51.4957, -0.0144, "Crossharbour & London Arena"),
        63: (51.5095, 0.0276, "Custom House"),
        65: (51.5085, 0.064, "Cyprus"),
        66: (51.5443, 0.1655, "Dagenham East"),
        67: (51.5417, 0.1469, "Dagenham Heathway"),
        70: (51.5223, -0.0173, "Devons Road"),
        71: (51.552, -0.2387, "Dollis Hill"),
        72: (51.5152, -0.3017, "Ealing Broadway"),
        73: (51.5101, -0.2882, "Ealing Common"),
        74: (51.492, -0.1973, "Earl's Court"),
        75: (51.5765, -0.397, "Eastcote"),
        76: (51.5168, -0.2474, "East Acton"),
        77: (51.5874, -0.165, "East Finchley"),
        78: (51.5394, 0.0518, "East Ham"),
        79: (51.5093, -0.0021, "East India"),
        80: (51.4586, -0.2112, "East Putney"),
        81: (51.6137, -0.275, "Edgware"),
        82: (51.5199, -0.1679, "Edgware Road (B)"),
        83: (51.5203, -0.17, "Edgware Road (C)"),
        84: (51.4943, -0.1001, "Elephant & Castle"),
        85: (51.5496, 0.1977, "Elm Park"),
        87: (51.5074, -0.1223, "Embankment"),
        89: (51.5282, -0.1337, "Euston"),
        90: (51.526, -0.1359, "Euston Square"),
        91: (51.596, 0.0912, "Fairlop"),
        92: (51.5203, -0.1053, "Farringdon"),
        93: (51.6012, -0.1932, "Finchley Central"),
        94: (51.5472, -0.1803, "Finchley Road"),
        95: (51.5642, -0.1065, "Finsbury Park"),
        96: (51.4804, -0.195, "Fulham Broadway"),
        97: (51.5096, 0.0716, "Gallions Reach"),
        98: (51.5765, 0.0663, "Gants Hill"),
        99: (51.4945, -0.1829, "Gloucester Road"),
        100: (51.5724, -0.1941, "Golders Green"),
        101: (51.5018, -0.2267, "Goldhawk Road"),
        102: (51.5205, -0.1347, "Goodge Street"),
        103: (51.6132, 0.0923, "Grange Hill"),
        104: (51.5238, -0.1439, "Great Portland Street"),
        105: (51.5423, -0.3456, "Greenford"),
        107: (51.5067, -0.1428, "Green Park"),
        108: (51.4915, -0.2754, "Gunnersbury"),
        109: (51.603, 0.0933, "Hainault"),
        110: (51.4936, -0.2251, "Hammersmith"),
        111: (51.5568, -0.178, "Hampstead"),
        112: (51.5302, -0.2933, "Hanger Lane"),
        113: (51.5362, -0.2575, "Harlesden"),
        114: (51.5925, -0.3351, "Harrow & Wealdston"),
        115: (51.5793, -0.3366, "Harrow-on-the-Hill"),
        116: (51.4669, -0.4227, "Hatton Cross"),
        117: (51.4713, -0.4524, "Heathrow Terminals 1, 2 & 3"),
        118: (51.4598, -0.4476, "Heathrow Terminal 4"),
        119: (51.5829, -0.2259, "Hendon Central"),
        120: (51.5033, -0.0215, "Heron Quays"),
        122: (51.5009, -0.1925, "High Street Kensington"),
        123: (51.546, -0.104, "Highbury & Islington"),
        124: (51.5777, -0.1458, "Highgate"),
        125: (51.5538, -0.4499, "Hillingdon"),
        126: (51.5174, -0.12, "Holborn"),
        127: (51.5075, -0.206, "Holland Park"),
        128: (51.5526, -0.1132, "Holloway Road"),
        129: (51.5539, 0.2184, "Hornchurch"),
        130: (51.4713, -0.3665, "Hounslow Central"),
        131: (51.4733, -0.3564, "Hounslow East"),
        132: (51.4734, -0.3855, "Hounslow West"),
        133: (51.5027, -0.1527, "Hyde Park Corner"),
        134: (51.5619, -0.4421, "Ickenham"),
        135: (51.4871, -0.0101, "Island Gardens"),
        136: (51.4884, -0.1053, "Kennington"),
        137: (51.5304, -0.225, "Kensal Green"),
        138: (51.4983, -0.2106, "Kensington (Olympia)"),
        139: (51.5507, -0.1402, "Kentish Town"),
        140: (51.5816, -0.3162, "Kenton"),
        141: (51.477, -0.285, "Kew Gardens"),
        142: (51.5471, -0.2047, "Kilburn"),
        143: (51.5351, -0.1939, "Kilburn Park"),
        144: (51.5846, -0.2786, "Kingsbury"),
        145: (51.5308, -0.1238, "King's Cross St. Pancras"),
        146: (51.5015, -0.1607, "Knightsbridge"),
        147: (51.5172, -0.2107, "Ladbroke Grove"),
        148: (51.4991, -0.1115, "Lambeth North"),
        149: (51.5119, -0.1756, "Lancaster Gate"),
        150: (51.5139, -0.2172, "Latimer Road"),
        151: (51.5113, -0.1281, "Leicester Square"),
        153: (51.5566, -0.0053, "Leyton"),
        154: (51.5683, 0.0083, "Leytonstone"),
        155: (51.5123, -0.0396, "Limehouse"),
        156: (51.5178, -0.0823, "Liverpool Street"),
        157: (51.5052, -0.0864, "London Bridge"),
        159: (51.53, -0.1854, "Maida Vale"),
        160: (51.5712, -0.0958, "Manor House"),
        161: (51.5122, -0.094, "Mansion House"),
        162: (51.5136, -0.1586, "Marble Arch"),
        163: (51.5225, -0.1631, "Marylebone"),
        164: (51.5249, -0.0332, "Mile End"),
        165: (51.6082, -0.2103, "Mill Hill East"),
        166: (51.5108, -0.0863, "Monument"),
        167: (51.5186, -0.0886, "Moorgate"),
        168: (51.6294, -0.432, "Moor Park"),
        169: (51.4022, -0.1948, "Morden"),
        170: (51.5342, -0.1387, "Mornington Crescent"),
        171: (51.4902, -0.0145, "Mudchute"),
        172: (51.5542, -0.2503, "Neasden"),
        173: (51.5756, 0.0899, "Newbury Park"),
        176: (51.4995, -0.3142, "Northfields"),
        177: (51.5483, -0.3687, "Northolt"),
        178: (51.5784, -0.3184, "Northwick Park"),
        179: (51.6111, -0.424, "Northwood"),
        180: (51.6004, -0.4092, "Northwood Hills"),
        181: (51.5237, -0.2597, "North Acton"),
        182: (51.5175, -0.2887, "North Ealing"),
        184: (51.5846, -0.3626, "North Harrow"),
        185: (51.5621, -0.3034, "North Wembley"),
        186: (51.5094, -0.1967, "Notting Hill Gate"),
        188: (51.5263, -0.0873, "Old Street"),
        190: (51.4813, -0.3522, "Osterley"),
        191: (51.4819, -0.113, "Oval"),
        192: (51.515, -0.1415, "Oxford Circus"),
        193: (51.5154, -0.1755, "Paddington"),
        194: (51.527, -0.2841, "Park Royal"),
        195: (51.4753, -0.2011, "Parsons Green"),
        196: (51.5366, -0.3232, "Perivale"),
        197: (51.5098, -0.1342, "Picadilly Circus"),
        198: (51.4893, -0.1334, "Pimlico"),
        199: (51.5926, -0.3805, "Pinner"),
        200: (51.5313, 0.0172, "Plaistow"),
        201: (51.5077, -0.0173, "Poplar"),
        202: (51.572, -0.2954, "Preston Road"),
        203: (51.5093, 0.0336, "Prince Regent"),
        205: (51.4682, -0.2089, "Putney Bridge"),
        206: (51.5341, -0.2047, "Queen's Park"),
        207: (51.5942, -0.2861, "Queensbury"),
        208: (51.5107, -0.1877, "Queensway"),
        209: (51.4942, -0.2359, "Ravenscourt Park"),
        210: (51.5753, -0.3714, "Rayners Lane"),
        211: (51.5763, 0.0454, "Redbridge"),
        212: (51.5234, -0.1466, "Regent's Park"),
        213: (51.4633, -0.3013, "Richmond"),
        215: (51.6171, 0.0439, "Roding Valley"),
        216: (51.501, -0.0525, "Rotherhithe"),
        217: (51.5084, 0.0465, "Royal Albert"),
        218: (51.519, -0.188, "Royal Oak"),
        219: (51.5091, 0.0181, "Royal Victoria"),
        220: (51.5715, -0.4213, "Ruislip"),
        222: (51.5732, -0.4125, "Ruislip Manor"),
        223: (51.523, -0.1244, "Russell Square"),
        224: (51.5822, -0.0749, "Seven Sisters"),
        225: (51.5117, -0.056, "Shadwell"),
        226: (51.5046, -0.2187, "Shepherd's Bush (C)"),
        227: (51.5058, -0.2265, "Shepherd's Bush (H)"),
        228: (51.5227, -0.0708, "Shoreditch"),
        229: (51.4924, -0.1565, "Sloane Square"),
        230: (51.5808, 0.0216, "Snaresbrook"),
        231: (51.4454, -0.2066, "Southfields"),
        234: (51.5011, -0.3072, "South Ealing"),
        235: (51.5646, -0.3521, "South Harrow"),
        236: (51.4941, -0.1738, "South Kensington"),
        237: (51.5701, -0.3081, "South Kenton"),
        238: (51.5007, -0.0191, "South Quay"),
        239: (51.5569, -0.3988, "South Ruislip"),
        240: (51.4154, -0.1919, "South Wimbledon"),
        241: (51.5917, 0.0275, "South Woodford"),
        242: (51.495, -0.2459, "Stamford Brook"),
        243: (51.6194, -0.3028, "Stanmore"),
        244: (51.5221, -0.047, "Stepney Green"),
        245: (51.4723, -0.123, "Stockwell"),
        246: (51.5439, -0.2759, "Stonebridge Park"),
        247: (51.5416, -0.0042, "Stratford"),
        248: (51.4994, -0.1335, "St. James's Park"),
        249: (51.5347, -0.174, "St. John's Wood"),
        250: (51.5146, -0.0973, "St. Paul's"),
        251: (51.5569, -0.3366, "Sudbury Hill"),
        252: (51.5507, -0.3156, "Sudbury Town"),
        253: (51.4933, -0.0478, "Surrey Quays"),
        254: (51.5432, -0.1738, "Swiss Cottage"),
        255: (51.5111, -0.1141, "Temple"),
        257: (51.4361, -0.1598, "Tooting Bec"),
        258: (51.4275, -0.168, "Tooting Broadway"),
        259: (51.5165, -0.131, "Tottenham Court Road"),
        260: (51.5882, -0.0594, "Tottenham Hale"),
        262: (51.5106, -0.0743, "Tower Gateway"),
        263: (51.5098, -0.0766, "Tower Hill"),
        264: (51.5567, -0.1374, "Tufnell Park"),
        265: (51.4951, -0.2547, "Turnham Green"),
        266: (51.5904, -0.1028, "Turnpike Lane"),
        267: (51.559, 0.251, "Upminster"),
        268: (51.5582, 0.2343, "Upminster Bridge"),
        269: (51.5385, 0.1014, "Upney"),
        270: (51.5352, 0.0343, "Upton Park"),
        271: (51.5463, -0.4786, "Uxbridge"),
        272: (51.4861, -0.1253, "Vauxhall"),
        273: (51.4965, -0.1447, "Victoria"),
        274: (51.583, -0.0195, "Walthamstow Central"),
        275: (51.5775, 0.0288, "Wanstead"),
        276: (51.5043, -0.0558, "Wapping"),
        277: (51.5247, -0.1384, "Warren Street"),
        278: (51.5235, -0.1835, "Warwick Avenue"),
        279: (51.5036, -0.1143, "Waterloo"),
        281: (51.5519, -0.2963, "Wembley Central"),
        282: (51.5635, -0.2795, "Wembley Park"),
        283: (51.521, -0.2011, "Westbourne Park"),
        284: (51.5097, -0.0265, "Westferry"),
        285: (51.501, -0.1254, "Westminster"),
        286: (51.518, -0.2809, "West Acton"),
        287: (51.4872, -0.1953, "West Brompton"),
        288: (51.6095, -0.1883, "West Finchley"),
        289: (51.5287, 0.0056, "West Ham"),
        290: (51.5469, -0.1906, "West Hampstead"),
        291: (51.5795, -0.3533, "West Harrow"),
        292: (51.507, -0.0203, "West India Quay"),
        293: (51.4907, -0.2065, "West Kensington"),
        294: (51.5696, -0.4376, "West Ruislip"),
        295: (51.5194, -0.0612, "Whitechapel"),
        296: (51.512, -0.2239, "White City"),
        297: (51.5492, -0.2215, "Willesden Green"),
        298: (51.5326, -0.2478, "Willesden Junction"),
        299: (51.4214, -0.2064, "Wimbledon"),
        300: (51.4343, -0.1992, "Wimbledon Park"),
        301: (51.607, 0.0341, "Woodford"),
        302: (51.6179, -0.1856, "Woodside Park"),
        303: (51.5975, -0.1097, "Wood Green"),
        35: (51.4627, -0.1145, "Brixton"),
        6: (51.6736, -0.607, "Amersham"),
        23: (51.4979, -0.0637, "Bermondsey"),
        50: (51.7052, -0.611, "Chesham"),
        46: (51.6679, -0.561, "Chalfont & Latimer"),
        53: (51.6543, -0.5183, "Chorleywood"),
        214: (51.6404, -0.4733, "Rickmansworth"),
        62: (51.647, -0.4412, "Croxley"),
        280: (51.6573, -0.4177, "Watford"),
        221: (51.5606, -0.4103, "Ruislip Gardens"),
        121: (51.6503, -0.1943, "High Barnet"),
        261: (51.6302, -0.1791, "Totteridge & Whetstone"),
        57: (51.6517, -0.1496, "Cockfosters"),
        187: (51.6476, -0.1318, "Oakwood"),
        232: (51.6322, -0.128, "Southgate"),
        88: (51.6937, 0.1139, "Epping"),
        256: (51.6717, 0.1033, "Theydon Bois"),
        68: (51.6455, 0.0838, "Debden"),
        158: (51.6412, 0.0558, "Loughton"),
        37: (51.6266, 0.0471, "Buckhurst Hill"),
        204: (51.5343, -0.0139, "Pudding Mill Lane"),
        233: (51.501, -0.1052, "Southwark"),
        41: (51.4982, -0.0502, "Canada Water"),
        43: (51.5147, 0.0082, "Canning Town"),
        183: (51.5005, 0.0039, "North Greenwich"),
        64: (51.4827, -0.0096, "Cutty Sark"),
        106: (51.4781, -0.0149, "Greenwich"),
        69: (51.474, -0.0216, "Deptford Bridge"),
        86: (51.4693, -0.0174, "Elverson Road"),
        152: (51.4657, -0.0142, "Lewisham"),
        174: (51.4767, -0.0327, "New Cross"),
        175: (51.4757, -0.0402, "New Cross Gate"),
    }

    london_underground_lines = {  # line: "name"
        1: "Bakerloo Line",
        3: "Circle Line",
        6: "Hammersmith & City Line",
        7: "Jubilee Line",
        11: "Victoria Line",
        2: "Central Line",
        4: "District Line",
        5: "East London Line",
        8: "Metropolitan Line",
        9: "Northern Line",
        10: "Piccadilly Line",
        12: "Waterloo & City Line",
        13: "Docklands Light Railway",
    }

    london_underground_connections = {  # (station1,station2): (line, time)
        (11, 163): (1, 1),
        (11, 212): (1, 2),
        (49, 87): (1, 1),
        (49, 197): (1, 2),
        (82, 163): (1, 2),
        (82, 193): (1, 3),
        (84, 148): (1, 3),
        (87, 279): (1, 2),
        (113, 246): (1, 2),
        (113, 298): (1, 2),
        (114, 140): (1, 2),
        (137, 206): (1, 3),
        (137, 298): (1, 3),
        (140, 237): (1, 2),
        (143, 159): (1, 2),
        (143, 206): (1, 2),
        (148, 279): (1, 1),
        (159, 278): (1, 1),
        (185, 237): (1, 2),
        (185, 281): (1, 2),
        (192, 197): (1, 2),
        (192, 212): (1, 2),
        (193, 278): (1, 2),
        (246, 281): (1, 3),
        (13, 156): (2, 2),
        (13, 250): (2, 2),
        (16, 91): (2, 2),
        (16, 173): (2, 2),
        (24, 156): (2, 3),
        (24, 164): (2, 2),
        (28, 162): (2, 1),
        (28, 192): (2, 1),
        (37, 158): (2, 3),
        (37, 301): (2, 3),
        (48, 126): (2, 1),
        (48, 250): (2, 2),
        (51, 103): (2, 2),
        (51, 215): (2, 2),
        (68, 158): (2, 2),
        (68, 256): (2, 3),
        (72, 286): (2, 3),
        (76, 181): (2, 2),
        (76, 296): (2, 3),
        (88, 256): (2, 2),
        (91, 109): (2, 2),
        (98, 173): (2, 3),
        (98, 211): (2, 2),
        (103, 109): (2, 3),
        (105, 177): (2, 2),
        (105, 196): (2, 2),
        (112, 181): (2, 3),
        (112, 196): (2, 2),
        (126, 259): (2, 2),
        (127, 186): (2, 2),
        (127, 226): (2, 1),
        (149, 162): (2, 3),
        (149, 208): (2, 1),
        (153, 154): (2, 3),
        (153, 247): (2, 2),
        (154, 230): (2, 2),
        (154, 275): (2, 2),
        (164, 247): (2, 4),
        (177, 239): (2, 3),
        (181, 286): (2, 2),
        (186, 208): (2, 2),
        (192, 259): (2, 2),
        (211, 275): (2, 2),
        (215, 301): (2, 3),
        (221, 239): (2, 1),
        (221, 294): (2, 3),
        (226, 296): (2, 3),
        (230, 241): (2, 2),
        (241, 301): (2, 2),
        (2, 156): (3, 2),
        (2, 263): (3, 4),
        (11, 83): (3, 3),
        (11, 104): (3, 3),
        (14, 92): (3, 1),
        (14, 167): (3, 2),
        (18, 186): (3, 2),
        (18, 193): (3, 2),
        (25, 161): (3, 1),
        (25, 255): (3, 2),
        (44, 161): (3, 1),
        (44, 166): (3, 2),
        (83, 193): (3, 3),
        (87, 255): (3, 2),
        (87, 285): (3, 2),
        (90, 104): (3, 2),
        (90, 145): (3, 2),
        (92, 145): (3, 4),
        (99, 122): (3, 4),
        (99, 236): (3, 1),
        (122, 186): (3, 3),
        (156, 167): (3, 2),
        (166, 263): (3, 2),
        (229, 236): (3, 2),
        (229, 273): (3, 2),
        (248, 273): (3, 2),
        (248, 285): (3, 2),
        (3, 263): (4, 2),
        (3, 295): (4, 2),
        (15, 78): (4, 4),
        (15, 269): (4, 2),
        (17, 110): (4, 1),
        (17, 293): (4, 2),
        (18, 186): (4, 2),
        (18, 193): (4, 2),
        (21, 67): (4, 3),
        (21, 269): (4, 2),
        (25, 161): (4, 1),
        (25, 255): (4, 2),
        (33, 36): (4, 2),
        (33, 164): (4, 1),
        (36, 289): (4, 2),
        (44, 161): (4, 1),
        (44, 166): (4, 2),
        (52, 1): (4, 2),
        (52, 265): (4, 2),
        (66, 67): (4, 4),
        (66, 85): (4, 3),
        (72, 73): (4, 4),
        (73, 1): (4, 2),
        (74, 99): (4, 3),
        (74, 122): (4, 3),
        (74, 138): (4, 2),
        (74, 287): (4, 2),
        (74, 293): (4, 1),
        (78, 270): (4, 2),
        (80, 205): (4, 2),
        (80, 231): (4, 2),
        (83, 193): (4, 3),
        (85, 129): (4, 2),
        (87, 255): (4, 2),
        (87, 285): (4, 2),
        (96, 195): (4, 2),
        (96, 287): (4, 1),
        (99, 236): (4, 1),
        (108, 141): (4, 3),
        (108, 265): (4, 3),
        (110, 209): (4, 2),
        (122, 186): (4, 3),
        (129, 268): (4, 2),
        (141, 213): (4, 3),
        (164, 244): (4, 2),
        (166, 263): (4, 2),
        (195, 205): (4, 3),
        (200, 270): (4, 2),
        (200, 289): (4, 2),
        (209, 242): (4, 2),
        (229, 236): (4, 2),
        (229, 273): (4, 2),
        (231, 300): (4, 3),
        (242, 265): (4, 1),
        (244, 295): (4, 3),
        (248, 273): (4, 2),
        (248, 285): (4, 2),
        (267, 268): (4, 3),
        (299, 300): (4, 3),
        (4, 70): (13, 2),
        (4, 201): (13, 2),
        (13, 225): (13, 2),
        (19, 97): (13, 2),
        (20, 65): (13, 2),
        (20, 217): (13, 2),
        (27, 79): (13, 2),
        (27, 201): (13, 2),
        (32, 70): (13, 2),
        (32, 204): (13, 2),
        (42, 120): (13, 2),
        (42, 292): (13, 2),
        (43, 79): (13, 2),
        (43, 219): (13, 2),
        (61, 171): (13, 2),
        (61, 238): (13, 2),
        (63, 203): (13, 2),
        (63, 219): (13, 2),
        (64, 106): (13, 2),
        (64, 135): (13, 2),
        (65, 97): (13, 2),
        (69, 86): (13, 2),
        (69, 106): (13, 2),
        (86, 152): (13, 2),
        (120, 238): (13, 2),
        (135, 171): (13, 2),
        (155, 225): (13, 2),
        (155, 284): (13, 2),
        (201, 284): (13, 2),
        (201, 292): (13, 2),
        (203, 217): (13, 2),
        (204, 247): (13, 2),
        (225, 262): (13, 2),
        (284, 292): (13, 2),
        (41, 216): (5, 1),
        (41, 253): (5, 2),
        (174, 253): (5, 4),
        (175, 253): (5, 4),
        (216, 276): (5, 1),
        (225, 276): (5, 1),
        (225, 295): (5, 2),
        (228, 295): (5, 2),
        (3, 156): (6, 4),
        (3, 295): (6, 2),
        (11, 83): (6, 3),
        (11, 104): (6, 3),
        (14, 92): (6, 1),
        (14, 167): (6, 2),
        (15, 78): (6, 4),
        (33, 36): (6, 2),
        (33, 164): (6, 1),
        (36, 289): (6, 2),
        (78, 270): (6, 2),
        (83, 193): (6, 4),
        (90, 104): (6, 2),
        (90, 145): (6, 2),
        (92, 145): (6, 4),
        (101, 110): (6, 2),
        (101, 227): (6, 1),
        (147, 150): (6, 1),
        (147, 283): (6, 2),
        (150, 227): (6, 2),
        (156, 167): (6, 2),
        (164, 244): (6, 2),
        (193, 218): (6, 1),
        (200, 270): (6, 2),
        (200, 289): (6, 2),
        (218, 283): (6, 2),
        (244, 295): (6, 3),
        (11, 28): (7, 2),
        (11, 249): (7, 4),
        (23, 41): (7, 2),
        (23, 157): (7, 3),
        (28, 107): (7, 2),
        (41, 42): (7, 3),
        (42, 183): (7, 3),
        (43, 183): (7, 3),
        (43, 289): (7, 3),
        (45, 207): (7, 2),
        (45, 243): (7, 2),
        (71, 172): (7, 2),
        (71, 297): (7, 2),
        (94, 254): (7, 2),
        (94, 290): (7, 1),
        (107, 285): (7, 3),
        (142, 290): (7, 2),
        (142, 297): (7, 2),
        (144, 207): (7, 2),
        (144, 282): (7, 4),
        (157, 233): (7, 2),
        (172, 282): (7, 4),
        (233, 279): (7, 1),
        (247, 289): (7, 3),
        (249, 254): (7, 1),
        (279, 285): (7, 2),
        (2, 156): (8, 2),
        (6, 46): (8, 4),
        (11, 94): (8, 6),
        (11, 104): (8, 3),
        (14, 92): (8, 1),
        (14, 167): (8, 2),
        (46, 50): (8, 8),
        (46, 53): (8, 4),
        (53, 214): (8, 4),
        (62, 168): (8, 4),
        (62, 280): (8, 3),
        (75, 210): (8, 2),
        (75, 222): (8, 2),
        (90, 104): (8, 2),
        (90, 145): (8, 2),
        (92, 145): (8, 4),
        (94, 282): (8, 7),
        (115, 178): (8, 2),
        (115, 184): (8, 3),
        (115, 291): (8, 2),
        (125, 134): (8, 2),
        (125, 271): (8, 3),
        (134, 220): (8, 3),
        (156, 167): (8, 2),
        (168, 179): (8, 3),
        (168, 214): (8, 4),
        (178, 202): (8, 2),
        (179, 180): (8, 2),
        (180, 199): (8, 2),
        (184, 199): (8, 3),
        (202, 282): (8, 3),
        (210, 291): (8, 3),
        (220, 222): (8, 2),
        (7, 145): (9, 2),
        (7, 188): (9, 3),
        (8, 124): (9, 3),
        (8, 264): (9, 2),
        (12, 56): (9, 2),
        (12, 257): (9, 1),
        (13, 157): (9, 2),
        (13, 167): (9, 3),
        (22, 47): (9, 2),
        (22, 111): (9, 2),
        (29, 84): (9, 1),
        (29, 157): (9, 2),
        (34, 100): (9, 3),
        (34, 119): (9, 2),
        (38, 58): (9, 2),
        (38, 81): (9, 3),
        (40, 47): (9, 2),
        (40, 89): (9, 3),
        (40, 139): (9, 2),
        (40, 170): (9, 1),
        (49, 87): (9, 1),
        (49, 151): (9, 2),
        (54, 55): (9, 2),
        (54, 56): (9, 2),
        (55, 245): (9, 1),
        (58, 119): (9, 3),
        (59, 240): (9, 2),
        (59, 258): (9, 2),
        (77, 93): (9, 4),
        (77, 124): (9, 2),
        (84, 136): (9, 2),
        (87, 279): (9, 2),
        (89, 145): (9, 2),
        (89, 170): (9, 2),
        (89, 277): (9, 1),
        (93, 165): (9, 3),
        (93, 288): (9, 2),
        (100, 111): (9, 4),
        (102, 259): (9, 1),
        (102, 277): (9, 2),
        (121, 261): (9, 3),
        (136, 191): (9, 2),
        (136, 279): (9, 3),
        (139, 264): (9, 2),
        (151, 259): (9, 1),
        (167, 188): (9, 1),
        (169, 240): (9, 4),
        (191, 245): (9, 3),
        (257, 258): (9, 2),
        (261, 302): (9, 3),
        (288, 302): (9, 1),
        (1, 73): (10, 2),
        (1, 234): (10, 4),
        (1, 265): (10, 3),
        (5, 194): (10, 3),
        (5, 252): (10, 2),
        (9, 31): (10, 3),
        (9, 232): (10, 3),
        (10, 95): (10, 2),
        (10, 128): (10, 1),
        (17, 74): (10, 3),
        (17, 110): (10, 2),
        (30, 176): (10, 2),
        (30, 190): (10, 3),
        (31, 303): (10, 2),
        (39, 128): (10, 2),
        (39, 145): (10, 5),
        (57, 187): (10, 4),
        (60, 126): (10, 1),
        (60, 151): (10, 1),
        (73, 182): (10, 3),
        (74, 99): (10, 2),
        (75, 210): (10, 2),
        (75, 222): (10, 2),
        (95, 160): (10, 2),
        (99, 236): (10, 1),
        (107, 133): (10, 2),
        (107, 197): (10, 1),
        (110, 265): (10, 2),
        (116, 117): (10, 3),
        (116, 118): (10, 3),
        (116, 132): (10, 4),
        (117, 118): (10, 5),
        (125, 134): (10, 2),
        (125, 271): (10, 3),
        (126, 223): (10, 2),
        (130, 131): (10, 2),
        (130, 132): (10, 2),
        (131, 190): (10, 2),
        (133, 146): (10, 2),
        (134, 220): (10, 3),
        (145, 223): (10, 2),
        (146, 236): (10, 3),
        (151, 197): (10, 2),
        (160, 266): (10, 3),
        (176, 234): (10, 1),
        (182, 194): (10, 2),
        (187, 232): (10, 3),
        (210, 235): (10, 3),
        (220, 222): (10, 2),
        (235, 251): (10, 2),
        (251, 252): (10, 3),
        (266, 303): (10, 2),
        (26, 260): (11, 2),
        (26, 274): (11, 2),
        (35, 245): (11, 2),
        (89, 145): (11, 2),
        (89, 277): (11, 1),
        (95, 123): (11, 2),
        (95, 224): (11, 4),
        (107, 192): (11, 2),
        (107, 273): (11, 2),
        (123, 145): (11, 4),
        (192, 277): (11, 2),
        (198, 272): (11, 1),
        (198, 273): (11, 3),
        (224, 260): (11, 3),
        (245, 272): (11, 3),
        (13, 279): (12, 4),
    }

    g = Graph()
    for sid, station in london_underground_stations.items():
        g.add_node(sid, obj=station)
    for (n1, n2), (line, time) in london_underground_connections.items():
        g.add_edge(n1, n2, time, bidirectional=True)
    return g



