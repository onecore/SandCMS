import sqlite3
import datetime


class knightclient:

    connection = sqlite3.connect("knightstudio", check_same_thread=False)
    cursor = connection.cursor()

    def closedb(self):
        """
        Need to be close out of scope
        """
        self.connection.close()

    def timestamp(self):
        """
        Returns timestamp
        """
        return datetime.datetime.now()

    def update_data(self, table, column, newvalue, where, v):
        """
        Update existing data
        """
        q = 'UPDATE {table} SET {column} = {value} WHERE '
        pass

    def update_credential(self, uname, newpwd):
        """
        Only for Account password update
        """
        try:
            q = "UPDATE users SET passw = '{value}' WHERE username = '{uname}';".format(
                value=newpwd, uname=uname)
            print(q)
            self.cursor.execute(q)
            print("update success")
            self.connection.commit()
            return True
        except Exception as e:
            print("update_credential() error ", e)
            return False

    def get_cred(self, username, passw):
        self.gc_fetch = self.cursor.execute("SELECT * FROM users")
        self.gc_data = self.gc_fetch.fetchall()

        return self.gc_data

    def load_data_index(self, which):
        """
        Loads data from DB, function calls in main page
        """
        self.fetch_control = self.cursor.execute("SELECT * FROM control")
        self.site_data = self.fetch_control.fetchall()

        # site_type:
        # 0 - Restaurant (Single Menu)
        # 1 - Restaurant (Multi Menu)
        # 2 - Article/Blog style
        # 3 - Shopping site
        # 4 - Business
        # 99 - Load ALL
        all_data = {  # 0 - Off, 1 - On
            "sitedescription": self.site_data[0][0],
            "sitename": self.site_data[0][1],
            "footercopyright": self.site_data[0][2],
            "logo": self.site_data[0][3],
            "uparrow": self.site_data[0][4],
            "domain": self.site_data[0][5],
            "socialshare": self.site_data[0][6],
            "popup": self.site_data[0][7],
            "meta_description": self.site_data[0][8],
            "meta_keywords": self.site_data[0][9],
            "favicon": self.site_data[0][10],
            "site_type": self.site_data[0][11],
        }

        # adds menu_list in dict if either single, multi, otherwise False
        if "0" in all_data['site_type']:  # single
            self.menu = self.cursor.execute("SELECT * FROM menu_single")
            all_data['menu_list'] = self.menu.fetchall()

        elif "1" in all_data['site_type']:  # multi
            self.menu = self.cursor.execute("SELECT * FROM menu")
            all_data['menu_list'] = self.menu.fetchall()

        # Add more condition depends on site_type

        return all_data

    def insert_data(self, quer):
        pass
