# -*- encoding: utf-8 -*-

import itertools
from bs4 import BeautifulSoup
from odoo import api, fields, models, _
from odoo import tools
import logging
import re

_logger = logging.getLogger(__name__)

def clear_string(strng, strip=False):
    if strip:
        return strng.strip()
    val = strng.replace('\n','')
    val = val.replace('\r','')
    val = val.strip()
    return val

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""

email_body = '''
<p>
Hello %s,
</p>
<p>
A lead has been generated with reference number %s.
</p>
<p>
Thanks.
</p>
'''

class crm_lead(models.Model):
    _inherit = "crm.lead"


    @api.model
    def create(self, vals):
        result = super(crm_lead, self).create(vals)
        if vals.get('email_from'):
            if '<' and '>' in vals.get('email_from'):
                plainemail = vals.get('email_from').split('<')
                plainmail2 = plainemail[1].replace("u'"," ")
                email = plainmail2.replace(">'","").replace('>','')
                result.email_from = email
            else:
                result.email_from = vals.get('email_from')
        return result



    @api.model
    def _create_from_table5(self,html_body):
        """ This Method returns plain text dict for Template Comparisa - Uw groei, onze ambiti - Sub:Aanvraag van Comparisa
        """
        names = ["Voornaam",'Naam', "E-mail", "Telefoon", "Adres", "Postcode", "Stad", "Land", "Straat"]
        plain_text_body = tools.html2plaintext(html_body)
        aa = find_between_r(plain_text_body, 'Lead Nr.', '1.').split('\n')
        if aa and len(aa) > 1:
            if plain_text_body.find("Type bedrijf") != -1 and plain_text_body.find("ROPA") == -1:
                return {}
            newdict = {}
            for idx, word in enumerate(aa):
                for name in names:
                    if name in word:
                        newdict[name+":"] = aa[idx + 1]
            if len(aa) == 1:
                return {}
        else:
            bb = find_between_r(plain_text_body, 'Informatie', 'Uitvoerdatum').split('\n')
            if len(bb) == 1:
                return {}
            newdict = {}
            l =[]
            for i in bb:
                if i and i != '\n':
                    l.append(i)
            for i in l:
                splitted = i.split(':')
                if len(splitted) > 1:
                    newdict[splitted[0].strip()+':'] = splitted[1]
        return newdict

    @api.model
    def _create_from_table4(self,html_body):
        """ This Method returns plain text dict for Template
        """
        plain_text_body = tools.html2plaintext(html_body)
        newdict = {}
        aa = find_between_r(plain_text_body, '- Aanvraag', '- Koopwijzer').split('\n')
        if len(aa) == 1:
            return {}
        l =[]
        for i in aa:
            if i and i != '\n':
                l.append(i)
        for i in l:
            splitted = i.split(':')
            if len(splitted) > 1:
                newdict[splitted[0]+':'] = splitted[1]
        return newdict

    @api.model
    def _create_from_table3(self,html_body):
        """ This Method returns plain text dict for Template
        """
        plain_text_body = tools.html2plaintext(html_body)
        newdict = {}
        aa = find_between_r(plain_text_body, '-----------------', 'Welke muuroppervlakte ').split('\n')
        if len(aa) == 1:
            return {}
        l =[]
        for i in aa:
            if i and i != '\n':
                l.append(i)
        for i in l:
            splitted = i.split(':')
            if len(splitted) == 1:
                if 'Telefoon' in i:
                    newdict['Telefoon:'] = i[9:]
            if len(splitted) > 1:
                newdict[splitted[0]+':'] = splitted[1]
        return newdict

    @api.model
    def _create_from_table6(self,html_body):
        """ This Method returns plain text dict for Template
        """
        plain_text_body = tools.html2plaintext(html_body)
        newdict = {}
        aa = find_between_r(plain_text_body, 'Aanvraag', 'Opties').split('\n')
        if len(aa) == 1:
            return {}
        l =[]
        for i in aa:
            if i and i != '\n':
                l.append(i)
        for i in l:
            splitted = i.split(':')
            if len(splitted) > 1:
                newdict[splitted[0]+':'] = splitted[1].replace('*','')
        if newdict.get('Telefoon:', ''):
            phone = clear_string(newdict.get('Telefoon:', ''), True)
            splitted_phone = phone.split()
            if len(splitted_phone) > 1:
                phone = splitted_phone[0]
            newdict['Telefoon:'] = phone
        if newdict.get('Straat:', ''):
            straat = clear_string(newdict.get('Straat:', ''), True)
            splitted_straat = straat.split()
            if len(splitted_straat) > 1:
                straat = splitted_straat[0]
            newdict['Straat:'] = straat
        return newdict

    @api.model
    def _create_from_table7(self,html_body):
        """ This Method returns plain text dict for Template Solvari
        """
        plain_text_body = tools.html2plaintext(html_body)
        newdict = {}
        aa = find_between_r(plain_text_body, 'Leaddetails', 'Met vriendelijke groet,').split('\n')
        if len(aa) == 1:
            return {}
        if 'Aanvraagdatum:' in aa:
            newdict['Aanvraagdatum:'] = aa[aa.index('Aanvraagdatum:') + 1]
        if 'E-mailadres:' in aa:
            newdict['E-mailadres:'] = aa[aa.index('E-mailadres:') + 1]
        if 'Leadnummer:' in aa:
            newdict['Leadnummer:'] = aa[aa.index('Leadnummer:') + 1]
        if 'Naam:' in aa:
            newdict['Naam:'] = aa[aa.index('Naam:') + 1]
#         if 'Adres:' in aa:
#             newdict['Adres:'] = aa[aa.index('Adres:') + 1]
#             if aa[aa.index('Adres:')]:
#                 address = aa[aa.index('Adres:') + 4]
#                 add = address.split(' ')
#                 if len(add) > 1:
#                     newdict['Postcode:'] = add[0]
#                     newdict['Stad:'] = add[1]
        if 'Adres:' in aa:
            street = aa[aa.index('Adres:') + 1]
            postcode = aa[aa.index('Adres:') + 5]
            newdict['Adres:'] = street
            if len(postcode) > 1:
                new_postcode = postcode[0:6]
                newdict['Postcode:'] = new_postcode
                city = postcode[6:]
                newdict['Plaats:'] = city
            else:
                postcode = aa[aa.index('Adres:') + 4]
                new_postcode = postcode[0:6]
                newdict['Postcode:'] = new_postcode
                city = postcode[6:]
                newdict['Plaats:'] = city
                
        if 'Telefoonnummer:' in aa:
            if aa[aa.index('Telefoonnummer:') + 1]:
                if len(aa[aa.index('Telefoonnummer:') + 1]) ==19:
                    phonenumber = aa[aa.index('Telefoonnummer:') + 1]
                    newdict['Telefoonnummer:'] = phonenumber[:15]
                if len(aa[aa.index('Telefoonnummer:') + 1]) ==18:
                    phonenumber = aa[aa.index('Telefoonnummer:') + 1]
                    newdict['Telefoonnummer:'] = phonenumber[:14]
                if len(aa[aa.index('Telefoonnummer:') + 1]) ==10:
                    phonenumber = aa[aa.index('Telefoonnummer:') + 1]
                    newdict['Telefoonnummer:'] = phonenumber
            else:
                telephone = aa[aa.index('Telefoonnummer:') + 1].split(' ')
                if len(telephone) > 1:
                    newdict['Telefoonnummer:'] = telephone[0]
                if len(telephone) == 1:
                    newdict['Telefoonnummer:'] = telephone[0]
        if 'Product:' in aa:
            newdict['Product:'] = aa[aa.index('Product:') + 1]
        #if 'Campagne:' in aa:
        #    newdict['Campagne:'] = aa[aa.index('Campagne:') + 1]
        if 'Toelichting:' in aa:
            newdict['Toelichting:'] = aa[aa.index('Toelichting:') + 1]
        return newdict


    @api.model
    def _create_from_table2(self,html_body):
        """ This Method returns plain text dict for Template
        """
        plain_text_body = tools.html2plaintext(html_body)
        newdict = {}
        aa = find_between_r(plain_text_body, 'Gelieve binnen 24 uur contact op te nemen voor het beste resultaat.', 'Google maps').split('\n')
        if len(aa) == 1:
            return {}
        l = []
        for i in aa:
            if i and i != '\n':
                l.append(i)
        if len(l) == 8:
            newdict['Naam:'] = l[2]
            newdict['Adres:'] = l[3]
            newdict['Postcode:'] = l[4][0:6]
            newdict['Woonplaats:'] = l[4][7:]
            newdict['E-mail:'] = l[6]
            newdict['Telefoon:'] = l[7]
        return newdict

    @api.model
    def _create_from_table(self,html_body):
        """ This Method returns plain text dict for Template IsolatieVergelijker-Aanvraag, Asbest-Asbest-Offertes.nl
        """
        soup = BeautifulSoup(html_body)
        all_tables_rows = soup.find_all("tr")
        if not len(all_tables_rows) > 0:
            newSoup = BeautifulSoup(html_body.replace('<br>', '\r\n').replace('<br/>', '\r\n').replace('</br>', '\r\n'))
            all_text = [newSoup.get_text()]
        else:
            all_text = []
        datasets = []
        newdict = {}
        def clear_string(strng):
            val = strng.replace('\n','')
            val = val.replace('\r','')
            val = val.strip()
            return val

        if len(all_text) > 0:
            get = []
            b = ''
            getline = []
            for i in all_text:
                b = i.replace('\r\n',',')
            get.append(b)
            for line in get:
                getline = line.split(',')
            for lin in getline:
                myline = lin.split(':')
                if len(myline) == 2:
                    key = myline[0] + ':'
                    value = myline[1]
                    newdict[key] = value

        for row in all_tables_rows:
            sub_datasets = []
            for td in row.find_all("td"):
                tds = td.get_text().replace('\n','')
                sub_datasets.append(tds)
            datasets.append(dict(itertools.izip_longest(*[iter(sub_datasets)] * 2, fillvalue="")))
        for dict_val in datasets:
            for dict_key in dict_val.keys():
                key = ''
                val = ''
                if dict_key:
                    val = clear_string(dict_val[dict_key]) if dict_val[dict_key] else ''
                    key = clear_string(dict_key)
                    newdict.update({key:val})
        return newdict



    @api.model
    def _create_from_table8(self,html_body):
        """ This Method returns plain text dict for Template Solvari
        """
        plain_text_body = tools.html2plaintext(html_body)
        newdict = {}
        a = find_between_r(plain_text_body, 'Product', 'Telefoonnummer 2').split('\n')
        if len(a) > 1:
            plain_campgne = a[2].replace('*','')
            naamindex = [i for i, s in enumerate(a) if 'Naam' in s]
            if naamindex and naamindex[0]:
                plain_naam = a[naamindex[0]].replace('*','')
                naam = plain_naam.split('Naam')
                if len(naam) == 2:
                    # newdict['Campagne:'] = naam[1]
                    newdict['Naam:'] = naam[1]
            adresindex = [i for i, s in enumerate(a) if 'Adres' in s]
            if adresindex and adresindex[0]:
                plain_adres = a[adresindex[0]].replace('*','')
                adres = plain_adres.split('Adres')
                if len(adres) == 2:
                    newdict['Adres:'] = adres[1]
                if adresindex[0] + 1:
                    adres_second = a[adresindex[0] + 1].split(' ')
                    if len(adres_second) == 2:
                        newdict['Postcode:'] = adres_second[0]
                        newdict['Plaatsnaam:'] = adres_second[1]
            emailindex = [i for i, s in enumerate(a) if 'E-mail' in s]
            if emailindex and emailindex[0]:
                plain_email = a[emailindex[0]].replace('*','')
                email = plain_email.split('E-mail')
                if len(email) == 2:
                    newdict['E-mail:'] = email[1]
            phoneindex = [i for i, s in enumerate(a) if 'Telefoonnummer 1' in s]
            if phoneindex and phoneindex[0]:
                plain_telephone = a[phoneindex[0]].replace('*','')
                telephone = plain_telephone.split('Telefoonnummer 1')
                if len(telephone) == 2:
                    if telephone[1]:
                        if telephone[1].strip()[-3] == '[':
                            tele = telephone[1].split(telephone[1].strip()[-3])
                            if len(tele) == 2:
                                newdict['Telefoonnummer 1'] = tele[0]
                        else:
                            newdict['Telefoonnummer 1'] = telephone[1]
        elif not len(a) > 1:
            a = find_between_r(plain_text_body, 'Onlangs heb', 'terug').split(',')
            newdict['Toelichting:'] = a[0].replace('[1]','') + 'terug.'
        return newdict

    @api.model
    def _create_from_table_valideas(self,html_body):
        """ This Method returns plain text dict for Valideas
        """
        plain_text_body = tools.html2plaintext(html_body)
        newdict = {}
        a = find_between_r(plain_text_body, 'LeadID', 'Extra info').split('\n')
        if len(a) > 1:
            addresindex = [i for i, s in enumerate(a) if 'Adres' in s]
            if addresindex and addresindex[0]:
                plain_adres = a[addresindex[0]].replace('*','')
                adres = plain_adres.split('Adres')
                if len(adres) == 2:
                    # newdict['Campagne:'] = naam[1]
                    if '[' in adres[1]:
                        address_split = adres[1].split('[')
                        newdict['Adres:'] = address_split[0]
                    else:
                        newdict['Adres:'] = adres[1]
            postcodeindex = [i for i, s in enumerate(a) if 'Postcode' in s]
            if postcodeindex and postcodeindex[0]:
                plain_postcode = a[postcodeindex[0]].replace('*','')
                postcode = plain_postcode.split('Postcode')
                if len(postcode) == 2:
                    # newdict['Campagne:'] = naam[1]
                    if '[' in postcode[1]:
                        postcode_split = postcode[1].split('[')
                        newdict['Postcode:'] = postcode_split[0]
                    else:
                        newdict['Postcode:'] = postcode[1]

            cityindex = [i for i, s in enumerate(a) if 'Woonplaats' in s]
            if cityindex and cityindex[0]:
                plain_city = a[cityindex[0]].replace('*','')
                city = plain_city.split('Woonplaats')
                if len(city) == 2:
                    # newdict['Campagne:'] = naam[1]
                    if '[' in city[1]:
                        city_split = city[1].split('[')
                        newdict['Woonplaats:'] = city_split[0]
                    else:
                        newdict['Woonplaats:'] = city[1]

            telephoneindex = [i for i, s in enumerate(a) if 'Telefoonnummer' in s]
            if telephoneindex and telephoneindex[0]:
                plain_telephone = a[telephoneindex[0]].replace('*','')
                telephone = plain_telephone.split('Telefoonnummer')
                if len(telephone) == 2:
                    # newdict['Campagne:'] = naam[1]
                    newdict['Telefoonnummer:'] = telephone[1]
            emailindex = [i for i, s in enumerate(a) if 'Email Adres' in s]
            if emailindex and emailindex[0]:
                plain_email = a[emailindex[0]].replace('*','')
                email = plain_email.split('Email Adres')
                if len(email) == 2:
                    # newdict['Campagne:'] = naam[1]
                    newdict['Email adres:'] = email[1]

            first_name = ''
            last_name = ''
            pre_fix = ''
            prefix_index = [i for i, s in enumerate(a) if 'Aanhef' in s]
            if prefix_index and prefix_index[0]:
                plain_prefix = a[prefix_index[0]].replace('*','')
                prefix = plain_prefix.split('Aanhef')
                if len(prefix) == 2:
                    # newdict['Campagne:'] = naam[1]
                    pre_fix = prefix[1]

            first_index = [i for i, s in enumerate(a) if 'Voornaam' in s]
            if first_index and first_index[0]:
                plain_first = a[first_index[0]].replace('*','')
                voorname = plain_first.split('Voornaam')
                if len(voorname) == 2:
                    # newdict['Campagne:'] = naam[1]
                    first_name = voorname[1]

            last_index = [i for i, s in enumerate(a) if 'Achternaam' in s]
            if last_index and last_index[0]:
                plain_last = a[last_index[0]].replace('*','')
                achternaam = plain_last.split('Achternaam')
                if len(achternaam) == 2:
                    # newdict['Campagne:'] = naam[1]
                    last_name = achternaam[1]
            newdict['Voornaam:'] = pre_fix + first_name + last_name

            descindex = [i for i, s in enumerate(a) if 'Extra info' in s]
            if descindex and descindex[0]:
                plain_desc = a[descindex[0]].replace('*','')
                extrainfo = plain_desc.split('Extra info')
                if len(extrainfo) == 2:
                    # newdict['Campagne:'] = naam[1]
                    newdict['Toelichting:'] = extrainfo[1]

        return newdict


    @api.model
    def _build_valid_dict(self,newdict):
        valid_dict = {}

        contactNames = []
        if newdict.get('Voornaam:', '') or newdict.get('Voornaam', ''):
            contactNames.append(clear_string(newdict.get('Voornaam:', '') or newdict.get('Voornaam', ''), True))
        if newdict.get('Naam:', '') or newdict.get('Naam', ''):
            contactNames.append(clear_string(newdict.get('Naam:', '') or newdict.get('Naam', ''), True))
        if newdict.get('Achternaam:', '') or newdict.get('Achternaam', ''):
            contactNames.append(clear_string(newdict.get('Achternaam:', '') or newdict.get('Achternaam', ''), True))
        if newdict.get('Contact:', ''):
            contactNames.append(clear_string(newdict.get('Contact:', ''), True))
        # As per Randhir this should not go in contact_name so commenting this portion.
        # if newdict.get('Campagne:', '') or newdict.get('Campagne', ''):
        #     valid_dict['contact_name'] = clear_string(newdict.get('Campagne:', '') or newdict.get('Campagne', ''), True)
        if contactNames:
            valid_dict['contact_name'] = ' '.join(contactNames)

        if newdict.get('E-mail:', ''):
            email = clear_string(newdict.get('E-mail:', ''), True)
            splitted_email = email.split()
            if len(splitted_email) > 1:
                email = splitted_email[0]
            valid_dict['email_from'] = email
        if newdict.get('E-mailadres:', ''):
            email = clear_string(newdict.get('E-mailadres:', ''), True)
            splitted_email = email.split()
            if len(splitted_email) > 1:
                email = splitted_email[0]
            valid_dict['email_from'] = email
        if newdict.get('E-mail adres:', ''):
            email = clear_string(newdict.get('E-mail adres:', ''), True)
            splitted_email = email.split()
            if len(splitted_email) > 1:
                email = splitted_email[0]
            valid_dict['email_from'] = email
        if newdict.get('Email adres:', ''):
            email = clear_string(newdict.get('Email adres:', ''), True)
            splitted_email = email.split()
            if len(splitted_email) > 1:
                email = splitted_email[0]
            valid_dict['email_from'] = email
        if newdict.get('Telefoon:', '') or newdict.get('Telefoonnummer:', '') or  newdict.get('Telefoonnummer 1', ''): valid_dict['phone'] = clear_string(newdict.get('Telefoon:', '') or newdict.get('Telefoonnummer:', '') or newdict.get('Telefoonnummer 1', ''), True)
        if newdict.get('Mobiel:', ''): valid_dict['mobile'] = clear_string(newdict.get('Mobiel:', ''), True)

        if newdict.get('Adres:', '') or newdict.get('Straat:', ''):
            valid_dict['street'] = clear_string(newdict.get('Adres:', '') or newdict.get('Straat:', ''), True)

        if newdict.get('Straatnaam:', ''):
            if 'google' in newdict.get('Straatnaam:', '').lower():
                street = newdict.get('Straatnaam:', '')
                street = re.sub(r'\([^)]*\)', '', street)
            else:
                street = newdict.get('Straatnaam:', '')
            valid_dict['street'] = clear_string(street, True)

        if newdict.get('Postcode:', ''): valid_dict['zip'] = clear_string(newdict.get('Postcode:', ''), True)
        if newdict.get('Postal:', ''): valid_dict['zip'] = clear_string(newdict.get('Postal:', ''), True)

        if newdict.get('Woonplaats:', '') or newdict.get('Plaats:', '') or newdict.get('Stad:', '') or newdict.get('Plaatsnaam:', '') : valid_dict['city'] = clear_string(newdict.get('Woonplaats:', '') or newdict.get('Plaats:', '') or newdict.get('Stad:', '') or newdict.get('Plaatsnaam:', ''), True)
        if newdict.get('Toelichting:', '') : valid_dict['description'] = clear_string(newdict.get('Toelichting:', ''), True)
        return valid_dict

    @api.model
    def create_lead_from_email_body(self):
        mm_obj = self.env['mail.message']
        m_mail_obj = self.env['mail.mail']
        user_obj = self.env['res.users']
        lead_obj = self.env['crm.lead']
        ir_model_data = self.env['ir.model.data']
        email_template_obj = self.env['mail.template']
        mail_comp_obj = self.env['mail.compose.message']
        message_ids = mm_obj.search([('res_id', '=', self.id), ('model', '=', 'crm.lead')])
        _logger.info("%s create crm lead from mail %s", len(message_ids), self.id)
        if len(message_ids) < 1: return True
        html_body = message_ids.read(['body'])[0].get('body')
#         if 'alt="Solvari"' in html_body:
#             print "HTML BODY**********************",html_body
        newdict = {}
        try:
            valideas_string = 'src="http://www.valideas.nl/wp-content/uploads/2017/03/valideaslogo-640br-378-hg.jpeg'
            newdict = self._create_from_table5(html_body)
            if not newdict and not 'alt="Solvari"' in html_body and not valideas_string in html_body:
                newdict = self._create_from_table7(html_body)
            if not newdict and not 'alt="Solvari"' in html_body and not valideas_string in html_body:
                newdict = self._create_from_table4(html_body)
            if not newdict and not 'alt="Solvari"' in html_body and not valideas_string in html_body:
                newdict = self._create_from_table3(html_body)
            if not newdict and not 'alt="Solvari"' in html_body and not valideas_string in html_body:
                newdict = self._create_from_table2(html_body)
            if not newdict and not 'alt="Solvari"' in html_body and not valideas_string in html_body:
                newdict = self._create_from_table(html_body)
            if not newdict and not 'alt="Solvari"' in html_body and not valideas_string in html_body:
                newdict = self._create_from_table6(html_body)
            if 'alt="Solvari"' in html_body:
                newdict = self._create_from_table8(html_body)
            if valideas_string in html_body:
                newdict = self._create_from_table_valideas(html_body)
            if newdict:
                valid_dict = self._build_valid_dict(newdict)
                if valid_dict:
                    self.write(valid_dict)
                    # Set Default values on partner
                    lead = lead_obj.search([('id', '=', self.id)])
                    partner = lead.partner_id if lead.partner_id else None
                    if partner:
                        netherlands = self.env['res.country'].search([('name', '=', 'Netherlands')])
                        binnenland = self.env['account.fiscal.position'].search([('name', '=', 'Binnenland')])
                        days15 = self.env['account.payment.term'].search([('name', '=', '15 Days')])
                        partner.country_id = netherlands
                        partner.property_account_position_id = binnenland
                        partner.lang = 'nl_NL'
                        partner.property_payment_term_id = days15

                    email_to = valid_dict.get('email_from')
                    if email_to:
                        mail_ids = []
                        email_template = ir_model_data.get_object_reference('create_crm_lead', 'email_template_lead_create_welcome_mail')[1]
                        template = mail_comp_obj.generate_email_for_composer(email_template,self.id)
                        vals = {'auto_delete': True, 'email_to': email_to, 'subject': template['subject'],
                            'body_html': template['body']}
                        mail_id = m_mail_obj.create(vals)
                        mail_id.send()
            
        except:
            '''
            Silently pass,
            Email format is not known hence it will perform lead creation in OpenERP's default way,
            that is, using the header information of the email.
            '''
            pass
        return True

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

