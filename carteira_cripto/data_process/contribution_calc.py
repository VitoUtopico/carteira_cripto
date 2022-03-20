from carteira_cripto.blueprints.external_api.resources import CoingeckoPrice

import pandas as pd
import re

def contribution_calc(contribution,\
                      cryptocurrencies,
                      cryptos_wallet):

    df_cryptos = pd.DataFrame(cryptocurrencies['Cryptocurrencies'])
    df_cryptos_wallet = pd.DataFrame(cryptos_wallet['Cryptos Wallet'])
    tb_contribution = df_cryptos_wallet.join(df_cryptos.set_index('id_cryptocurrency')[['cd_cryptocurrency', 'nm_cryptocurrency']],
                                      on='id_cryptocurrency',
                                      how='left')
    
    nm_cryptocurrencies = tb_contribution['nm_cryptocurrency'].to_list()
    nm_cryptocurrencies = re.sub(r"\'|\[|\]|\ ", "", str(nm_cryptocurrencies))
    
    get_price = CoingeckoPrice()
    current_price = get_price.get(nm_cryptocurrencies,'brl')
    df_current_price = pd.DataFrame(current_price)
    df_current_price = df_current_price.melt(var_name='nm_cryptocurrency',
                          value_vars=df_current_price.columns,
                          value_name='nr_current_price')

    tb_contribution = tb_contribution.join(
        df_current_price.set_index('nm_cryptocurrency')['nr_current_price'],
        on='nm_cryptocurrency'
    )
    tb_contribution = tb_contribution.astype({'nr_current_amount': 'float64'})


    # tb_contribution = pd.DataFrame(
    #     {
    #         'nm_cryptocurrency': ['BTC', 'ADA'],
    #         'nr_current_amount': [10, 11],
    #         'nr_rating': [100, 70],
    #         'nr_current_price': [2000.0, 1300.0]
    #     }
    # )

     # Calcular valor atual na moeda fiduciária para cada cripto
    tb_contribution['nr_fiat_currency'] = tb_contribution['nr_current_amount'] * tb_contribution['nr_current_price']

    # Calcular valor total na moeda fiduciária já aportado
    total_fiat_currency = tb_contribution['nr_fiat_currency'].sum()

    # Calcular soma de total_fiat_currency e contribution
    total_fiat_currency_plus_contribution = total_fiat_currency + contribution

    # Calcular soma das notas nr_rating
    total_nr_rating = tb_contribution['nr_rating'].sum()

    # Calcular percentual para cada criptomoeda de acordo com suas notas
    tb_contribution['nr_percent'] = tb_contribution['nr_rating'] / total_nr_rating

    # Calcular total ideal de cada criptomoeda após porte
    tb_contribution['nr_total_with_contribution'] = total_fiat_currency_plus_contribution * tb_contribution['nr_percent']

    # Calcular quanto aportar em cada criptomoeda
    tb_contribution['nr_contribution'] = tb_contribution['nr_total_with_contribution'] - tb_contribution['nr_fiat_currency']

    # tb_contribution = tb_contribution[[
    #     'cd_cryptocurrency',
    #     'nm_cryptocurrency',
    #     'nr_current_amount',
    #     'nr_rating',
    #     'nr_current_price',
    #     'nr_percent',
    #     'nr_contribution'
    # ]]
    tb_contribution.to_json(orient='records')
