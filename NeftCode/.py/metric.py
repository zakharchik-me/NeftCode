def count_oil_rate(model_liq, model_wat, X, liq, water, density=0.874):
    oil_real = density * liq * (1 - water / 100)
    
    oil_pred = density * model_liq.predict(X) * (1 - model_wat.predict(X) / 100)
    
    return oil_real, oil_pred
#     return mean_absolute_percentage_error(oil_real, oil_pred)

def count_oil_rate(liq_real, liq_pred, water_real, water_pred, density=0.874):
    oil_real = density * liq_real * (1 - water_real / 100)
    oil_pred = density * liq_pred * (1 - water_pred / 100)
    
    return oil_real, oil_pred


def smape(y_real, y_pred):
    return 100 * np.mean(
        np.abs(y_real - y_pred) / (np.abs(y_real) + np.abs(y_pred))
    )
