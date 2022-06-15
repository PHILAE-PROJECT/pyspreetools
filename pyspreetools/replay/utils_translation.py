def translation(endpoint, method, body):
    method = method.lower()
    if "/api/v2/storefront/cart" in endpoint:
        if method == 'post' and '/api/v2/storefront/cart/add_item' in endpoint:
            return "addAnItemToCart"
        if method == 'patch' and '/api/v2/storefront/cart/set_quantity' in endpoint:
            return "setLineItemQuantity"

        if method == 'delete' and '/api/v2/storefront/cart/remove_line_item' in endpoint:
            return "removeALineItem"

        if method =='patch' and '/api/v2/storefront/cart/associate' in endpoint:
            return "associateACartWithAUser"
        if method == 'get':
            return "retrieveACart"

        if method =='post' :
            return "createACart"
    if "/api/v2/storefront/taxons" in endpoint:
        if method == 'get':
            return "listAllTaxons"

    if "/api/v2/storefront/products" in endpoint:
        if method == 'get':
            if 'filter' in body.keys() and 'filter[taxons]' in body['filter'].keys():
                if 'sort' in body['filter']:
                    return "listAllProducts_SpecificTaxonFilter"
                else:
                    return "listAllProducts_SpecificTaxonFilter_SortByPrice"
            else:
                return "retrieveAProduct"
    if "/api/v2/storefront/products" in endpoint and len(endpoint) > len("/api/v2/storefront/products/"):
        return "retrieveAProduct"

    if "/api/v2/storefront/account" in endpoint:
        if '/api/v2/storefront/account/addresses' in endpoint and method =='post':
            return "createAnAddress"

        if method =='post':
            return "createAnAccount"
        if method=='get' and '/api/v2/storefront/account/orders' in endpoint :
            return "retrieveAnOrder"

    if "spree_oauth/token" in endpoint:
        if method=='post':
            return "createOrRefreshAToken"


    if  '/api/v2/storefront/checkout' in endpoint:
        if "order" in body.keys() and "email" in body['order'].keys():
            return "updateCheckout_UpdateEmailInformation"
        if "order" in body.keys() and "bill_address_attributes" in body['order'].keys():
            return "updateCheckout_UpdateBillingInformation"
        if "order" in body.keys() and "ship_address_attributes" in body['order'].keys():
            return "updateCheckout_UpdateShippingInformation"
        if "order" in body.keys() and "shipments_attributes" in body['order'].keys():
            return "updateCheckout_ChooseAShippingRate"
        if "order" in body.keys() and "payments_attributes" in body['order'].keys():
            return "updateCheckout_UpdatePaymentMethod"
        if '/api/v2/storefront/checkout/next' in endpoint and method=='patch':
            return "nextCheckoutStep"
        if '/api/v2/storefront/checkout/advance' in endpoint and method=='patch':
            return "advanceCheckout"
        if  '/api/v2/storefront/checkout/complete' in endpoint and method=='patch':
            return"completeCheckout"
        if '/api/v2/storefront/checkout/shipping_rates' in endpoint and method=='get':
            return "listShippingRates"
    return "notFound"




if __name__ == '__main__':
    translations = []
    import json

    f = open('../data/spree_5000_sessions_wo_responses.json')
    data = json.load(f)
    f.close()
    for i, (k, v) in enumerate(data.items()):

        endpoint = v['url']

        method = v['method']
        # print(method+" "+endpoint)
        try:
            body = v['body']
        except:
            body = {}
        t=translation(endpoint, method, body)
        translations.append(t)
        if t=='notFound':
            print(endpoint)

        if i > 300000:
            break

    words=list(set(translations))
    print(sorted(words))
    print(len(words))