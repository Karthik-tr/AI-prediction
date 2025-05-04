import QuantLib as ql

def calculate_premium(spot, strike, days_to_expiry, risk_free=0.05):
    """Black-Scholes option pricing"""
    option_type = ql.Option.Call
    payoff = ql.PlainVanillaPayoff(option_type, strike)
    exercise = ql.EuropeanExercise(ql.Date().todaysDate() + days_to_expiry)
    option = ql.VanillaOption(payoff, exercise)
    
    # Pricing engine setup
    process = ql.BlackScholesProcess(
        ql.QuoteHandle(ql.SimpleQuote(spot)),
        ql.YieldTermStructureHandle(ql.FlatForward(0, ql.TARGET(), risk_free, ql.Actual365Fixed())),
        ql.BlackVolTermStructureHandle(ql.BlackConstantVol(0, ql.TARGET(), 0.2, ql.Actual365Fixed()))
    )
    option.setPricingEngine(ql.AnalyticEuropeanEngine(process))
    return option.NPV()