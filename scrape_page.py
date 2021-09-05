from bs4 import BeautifulSoup
import csv


def read_html(html, substitutes, img_s):
    soup = BeautifulSoup(html, 'lxml')
    try:
        product_name = soup.select_one('h1.text-h5.font-weight-medium').text.strip()
    except:
        product_name = ''
    try:
        price = soup.select_one('.row.text-caption.text--secondary~ div.row div.col div div.row.no-gutters').text.strip()
    except:
        price = ''
    try:
        stock = soup.select_one('div.flex-shrink-1.col.col-auto div div').text.strip()
    except:
        stock = ''
    try:
        manufacture = soup.select_one('a.text--secondary').text.strip()
    except:
        manufacture = ''
    item_cat_ups = soup.select('div.row.text-caption.text--secondary div')
    try:
        item = item_cat_ups[0].text.strip()
    except:
        item = ''
    try:
        cat = item_cat_ups[1].text.strip()
    except:
        cat = ''
    try:
        ups = item_cat_ups[2].text.strip()
    except:
        ups = ''
    try:
        description = soup.select_one('div.text--secondary.col.col-12').text.strip()
    except:
        description = ''

    try:
        product_categories = soup.select('ul.v-breadcrumbs.pa-0.theme--light li + a')
        sub_categories = ''
        for i in product_categories:
            sub_categories += i.text.strip() + ' / '
    except:
        sub_categories = ''

    try:
        htm = BeautifulSoup(substitutes, 'lxml')
        substitutes_products = htm.select(".v-window.v-item-group.theme--light div[class='col-md-9 col-lg-7 col-8'] a")
        substitutes_product = ''
        for t in substitutes_products:
            substitutes_product += 'https://www.rexelusa.com' + t.get('href') + ' \n '
    except:
        substitutes_product = ''
    try:
        product_overview = soup.select_one('div.row.mt-4').text.strip()
    except:
        product_overview = ''
    try:
        attachments_pdfs = soup.select('div.col.col-12 ~div.col.col-12 a')
        attachments_pdf = ''
        for y in attachments_pdfs:
            try:
                attachments_pdf += y.get('href').strip() + '\n    '
            except:
                continue
    except:
        attachments_pdf = ''
    try:
        associateds = soup.select('div.v-slide-group__wrapper')[0].select('div div a')
        associated = ''
        for x in associateds:
            try:
                associated += 'https://www.rexelusa.com/' + x.get('href').strip() + '\n    '
            except:
                continue
    except:
        associated = ''
    try:
        frequently_s = soup.select('div.v-slide-group__wrapper')[1].select('div div a')
        frequently_ = ''
        for x in frequently_s:
            try:
                frequently_ += 'https://www.rexelusa.com/' + x.get('href').strip() + '\n    '
            except:
                continue
    except:
        frequently_ = ''

    try:
        specifications = soup.select('.d-none.d-md-block.col.col-6 div div tr')
        specification = ''
        for o in specifications:
            specification += o.text.strip().replace('\n', '').replace('              ', '') + '\n'
    except:
        specification = ''





    data = {
        'product_name': product_name,
        'manufacture': manufacture,
        'item': item,
        'cat': cat,
        'ups': ups,
        'price': price,
        'stock': stock,
        'description': description,
        'img': img_s,
        'substitutes_product': substitutes_product,
        'product_categories': sub_categories,
        'product_overview': product_overview,
        'attachments_pdf': attachments_pdf,
        'associated': associated,
        'frequently_': frequently_,
        'specifications': specification
    }

    write_csv(data)


def write_csv(data):
    with open('data.csv', 'a', encoding='UTF-8', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow((data['product_name'],
                         data['manufacture'],
                         data['item'],
                         data['cat'],
                         data['ups'],
                         data['price'],
                         data['stock'],
                         data['description'],
                         data['img'],
                         data['substitutes_product'],
                         data['product_categories'],
                         data['product_overview'],
                         data['attachments_pdf'],
                         data['associated'],
                         data['frequently_'],
                         data['specifications'],

                         ))
