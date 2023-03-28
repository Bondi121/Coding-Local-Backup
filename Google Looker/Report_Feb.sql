CREATE TABLE IF NOT EXISTS Report_Feb (
    `DATE` VARCHAR(10) CHARACTER SET utf8,
    `CURRENCY` VARCHAR(3) CHARACTER SET utf8,
    `TOTAL_BET_REAL_MONEY_RNG` NUMERIC(16, 8),
    `TOTAL_WIN_REAL_MONEY_RNG` NUMERIC(10, 2),
    `TOTAL_BET_REAL_MONEY_LIVE` INT,
    `TOTAL_WIN_REAL_MONEY_LIVE` INT,
    `WAN_JACKPOT_INCREMENTS` INT,
    `JACKPOT_HITS_RNG` INT,
    `TOTAL_BET_BONUS_MONEY` NUMERIC(16, 9),
    `TOTAL_WIN_BONUS_MONEY` NUMERIC(9, 2),
    `CONVERTED_BONUS_MONEY_AFTER_PLAYTHROUGH` NUMERIC(9, 2),
    `TOTAL_GGR` NUMERIC(17, 10),
    `DEPOSITS_PSP` NUMERIC(9, 2),
    `MANUAL_DEPOSITS` NUMERIC(17, 12),
    `WITHDRAWS_PROCESSED` NUMERIC(16, 9),
    `WITHDRAWS_PENDING` INT,
    `CONVERTED_BONUS_MONEY_AFTER_PLAYTHROUGH_1` NUMERIC(9, 2),
    `MANUAL_ADJUSTMENTS` NUMERIC(7, 2),
    `REAL_MONEY_WALLET_STARTING_BALANCE` NUMERIC(10, 2),
    `REAL_MONEY_WALLET_ENDING_BALANCE` NUMERIC(10, 2),
    `REAL_MONEY_WALLET_MOVEMENT` NUMERIC(18, 12),
    `DIFFERENCE` INT,
    `BONUS_AWARDED` NUMERIC(16, 10),
    `CANCELLED_BONUS` NUMERIC(16, 11),
    `BONUS_STARTING_BALANCE` NUMERIC(16, 9),
    `BONUS_ENDING_BALANCE` NUMERIC(17, 10)
);
INSERT INTO Report_Feb VALUES ('2023-02-01','CHF',3611873.08,3545890.42,0,0,0,0,257346.03,294759.62,45772.57,20210.09,446942.88,1165.5,-276090.57,0,45772.57,-1165.5,2514185.8,2665993.52,151807.72,0,22298.25,3485.69,129724.61,140178.19),
	('2023-02-02','CHF',2960627.12,2824513,0,0,0,0,255580.66,271186.22,34245.53,101868.59,389524.75,600,-312958.38,0,34245.53,-386.4,2665993.52,2641291.3,-24702.22,0,12571.9,1585.64,140178.19,132524.48),
	('2023-02-03','CHF',3384072.73,3203084.58,0,0,0,0,476577.38,496077.27,67357.3,113630.85,400191.31,550,-407217.34,0,67357.3,-323.64,2641291.3,2521184.42,-120106.88,0,64283.5,4725.43,132524.48,144225.14),
	('2023-02-04','CHF',2618370.4,2390794.28,0,0,0,0,477371.24,530040.8,82512.92,145063.2,342245.63,0,0,0,82512.92,0,2521184.42,2718366.85,197182.43,0,41592.08,1639.86,144225.14,154334),
	('2023-02-05','CHF',3063080.07,2911804.22,0,0,0,0,243045.71,279812.61,68199.6,83076.25,320517.08,16.67,0,0,68199.6,-16.67,2718366.85,2955824.35,237457.5,0,16936.07,2179.63,154334,137657.74),
	('2023-02-06','CHF',2799056.99,2665669.4,0,0,0,0,204958.31,222758.46,31615.62,101771.97,350071.82,210,-680808.12,0,31615.62,526.77,2955824.35,2523526.08,-432298.27,0,9754.25,3434.22,137657.74,130162.3),
	('2023-02-07','CHF',2555762.29,2395206.87,0,0,0,0,105837.05,119882.94,29180.14,131375.28,323929.59,6023,-247376.78,0,29180.14,-6023,2523526.08,2474726.61,-48799.47,0,8522.75,1779.07,130162.3,121771.73),
	('2023-02-08','CHF',2547864.4,2480638.61,0,0,0,0,101932.89,134462.44,34904.73,32321.06,295694.16,1450,-214457.51,0,34904.73,-1450,2474726.61,2525092.2,50365.59,0,5354.29,2253.01,121771.73,122497.83),
	('2023-02-09','CHF',2451264.24,2342849.45,0,0,0,0,88750.22,92151.19,11092.13,97322.66,320039.42,1250,-248070.74,0,11092.13,-1250,2525092.2,2500988.22,-24103.98,0,9500.23,1362.74,122497.83,122944.16),
	('2023-02-10','CHF',2381876.5,2226697.11,0,0,0,0,140355.49,150626.47,13855.65,141323.74,323421.83,2235,-249800.2,0,13855.65,-1633.38,2500988.22,2435521.11,-65467.11,0,8178,244.33,122944.16,127293.16),
	('2023-02-11','CHF',2332563.36,2239428.03,0,0,0,0,130270.92,127790.4,10090.69,83044.64,284774.22,200,0,0,10090.69,-200,2435521.11,2637450.69,201929.58,0,10685,1119.49,127293.16,124287.46),
	('2023-02-12','CHF',2369114.8,2240578.37,0,0,0,0,128730.69,135133.01,21871.07,106665.36,263989.35,0,0,0,21871.07,0,2637450.69,2794774.68,157323.99,0,7394,554.77,124287.46,115657.94),
	('2023-02-13','CHF',2474326.1,2357152.08,0,0,0,0,74823.55,83456.84,7528.56,109645.46,277991.88,3950,-497259.25,0,7528.56,-3950,2794774.68,2469811.85,-324962.83,0,7116.4,831.19,115657.94,123047.88),
	('2023-02-14','CHF',1975104.29,1852665.06,0,0,0,0,107071.07,121662.75,18041.34,104397.89,257101.14,1540,-203696.16,0,18041.34,-1540,2469811.85,2420358.94,-49452.91,0,6024,610.4,123047.88,125011.82),
	('2023-02-15','CHF',2196852.62,2066869.98,0,0,0,0,96153.27,116432.48,29663.23,100319.41,271581.02,2940,-164316.9,0,29663.23,-799.79,2420358.94,2430243.65,9884.71,0,13315.25,6370.93,125011.82,122572.12),
	('2023-02-16','CHF',2107557.28,2023995.36,0,0,0,0,80303.48,82582.04,10060.66,73501.26,269333.77,3220,-175038.48,0,10060.66,-3220,2430243.65,2454257.68,24014.03,0,5353.8,663.22,122572.12,119480.6),
	('2023-02-17','CHF',2184532.94,2081713.54,0,0,0,0,71147.26,76369.48,11155.97,91663.43,267166.57,1070,-179181.18,0,11155.97,-1070,2454257.68,2451649.64,-2608.04,0,7553.25,605.74,119480.6,120494.36),
	('2023-02-18','CHF',2121841.87,1987359.43,0,0,0,0,76214.94,86424.61,15497.07,118985.37,234504.61,0,0,0,15497.07,0,2451649.64,2567168.88,115519.24,0,6182.4,899.12,120494.36,120490.24),
	('2023-02-19','CHF',2018549.65,1946804.49,0,0,0,0,97983.38,102245.05,18266.63,53478.53,201343.21,0,0,0,18266.63,0,2567168.88,2715033.56,147864.68,0,8386.99,2098.22,120490.24,112774.05),
	('2023-02-20','CHF',1907260.48,1840306.76,0,0,0,0,43455.23,41801.93,5801.53,61152.19,248702.14,50,-488910.35,0,5801.53,-50,2715033.56,2413723.16,-301310.4,0,4543.5,198.22,112774.05,109664.5),
	('2023-02-21','CHF',2156396.39,2036529.77,0,0,0,0,316158.79,365789.63,50703.97,69162.65,263839.24,1880,-168174.82,0,50703.97,-1880,2413723.16,2442104.93,28381.77,0,43671.45,2556.12,109664.5,149706.7),
	('2023-02-22','CHF',2124102.26,1994182.94,0,0,0,0,333469.4,377096.94,75609.98,54309.34,247206.34,2520,-199621.48,0,75609.98,-2520,2442104.93,2437900.45,-4204.48,0,34338.2,3338.54,149706.7,148723.92),
	('2023-02-23','CHF',2354366.64,2247030.87,0,0,0,0,282279.99,313642.01,54243.58,53092.19,260890.29,750,-190527.13,0,54243.58,2150,2437900.45,2455921.42,18020.97,0,24177.13,4675.27,148723.92,145344.22),
	('2023-02-24','CHF',3486385.54,3210122.35,0,0,0,0,429736.59,475405.79,72079.91,204183.28,501894.42,300,-214159.47,0,72079.91,-300,2455921.42,2539773.09,83851.67,0,52675.7,7292.99,145344.22,164316.22),
	('2023-02-25','CHF',4147743.51,3874891.24,0,0,0,0,360348.02,405834.25,72227.91,200624.36,462492.4,50,0,0,72227.91,-50,2539773.09,2801691.13,261918.04,0,35177.1,3455.1,164316.22,169296.54),
	('2023-02-26','CHF',3265573.2,3106404.19,0,0,0,0,324942.95,377129.76,77225.47,81943.54,347377.04,0,0,0,77225.47,0,2801691.13,3067124.63,265433.5,0,25969.91,1615.34,169296.54,168612.45),
	('2023-02-27','CHF',3031230.04,2903575.95,0,0,0,0,221384.57,231461.44,36963.26,90690.83,363955.57,4866.2,-810090.26,0,36963.26,-4866.2,3067124.63,2535165.31,-531959.32,0,23016.74,7924.97,168612.45,156817.83),
	('2023-02-28','CHF',2992324.25,2860647.18,0,0,0,0,229069.07,243920.2,28116.13,103560.94,370521.22,7654,-289254.49,0,28116.13,-7654,2535165.31,2520525.1,-14640.21,0,19750.9,2449.37,156817.83,160854.36),
	('TOTAL','CHF',73619673.03999999,69857405.53,0,0,0,0,5755298.149999999,6355936.63,1033883.15,2728384.3599999994,8907242.9,44490.369999999995,-6217009.610000001,0,1033883.15,-37671.81,72110854.15,72117193.45,6339.299999999894,0,534323.0399999999,69948.62000000001,3759612.190000001,3790741.9400000004);
