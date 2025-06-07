class Product(object):

    def get_product_status_by_id(self,product_id):
        """通过商品id获取商品信息"""
        pass
    def buy_product(self,product_id):
        """购买商品"""
        product = get_product_status_by_id(product_id)

        if product.get("num")>=1:
            result = {"status": 0, "msg": "购买成功！"}
        else:
            result={"status": 1, "msg": "购买失败,库存不足！"}
        return result