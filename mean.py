#importing modules
from rich.console import Console#->using rich console for fancy look

from rich.table import Table#->using rich.table.Table to create Table

from rich import print#->redifining default print function

import click#->using click module for creating command line

#--decelaring console variable----
console=Console()

#---class for finding mean with data and frequency
class Mean_x_f:
    '''class for finding mean'''
    def __init__(self):
        """declearing variables"""
        self.x=input('data{x value}?')#---inputing data from user
        self.l_x=[float(i) for i in self.x.split(',') if i!=' ']#---changing data into list with float variables
        self.f=input('frequency?')#--inputing frequency 
        self.l_f=[float(i) for i in self.f.split(',') if i!=' ']#---changing frequency into list with floats 
        self.l_fx=[self.l_f[i]*j for i,j in enumerate(self.l_x)]#-----calculating fx value
        self.sfx=0#---total of fx is stored here 
        self.n=0#------total of x is stored here
        self.set_values()#  |
        self.get_table()#   |->calling functions
        self.get_solution()#|
    def set_values(self):
        """setting values"""
        for i in self.l_f:
            self.n+=i
        for j in self.l_fx:
            self.sfx+=j
    def get_table(self):
        '''function fo creating table'''
        table = Table(title="Table for mean")
        table.add_column("x", justify="mid", style="cyan", no_wrap=True)
        table.add_column("f", style="magenta")
        table.add_column("fx", justify="mid", style="green")
        for i,j in enumerate(self.l_x):
            table.add_row(str(j),str(self.l_f[i]),str(self.l_fx[i]))
        self.set_values()
        table.add_row(" ",f'n={self.n}',f'Σfx={self.sfx}')
        console.print(table)
    def get_solution(self):
        """finally printing solution"""
        print("[green]solution,[/green]")
        print('[magenta]   mean=Σfx/n[/magenta]')
        print(f'[magenta]    ={round(self.sfx/self.n,2)}->answer[/magenta]')         

#---class for finding mean with data only
class Mean_x():
    """class for finding mean only with data"""
    def __init__(self):
        """defining values"""
        self.x=input('data{x value}?')#---inputing data from user
        self.l_x=[float(i) for i in self.x.split(',') if i != ' ']#---changing data into list with float 
        #-variables
        self.n=len(self.l_x)
        self.s_x=0
        #-----claculating sum of data----------
        for i in self.l_x:
            self.s_x+=i
        #--------------------------------------
        self.get_solution()
    def get_solution(self):
        """finally printing solution"""
        print("[green]solution,[/green]")
        print('[magenta]   mean=Σx/n[/magenta]')
        print(f'[magenta]   mean={self.s_x}/{self.n}[/magenta]')
        print(f'[magenta]    ={round(self.s_x/self.n,2)}->answer[/magenta]')         

# dictinory holding all types of mean functions
TYPE_MEAN={
    'xf':Mean_x_f,
    'x':Mean_x
        }

#using click to add function of being used as command line tool
@click.command()
@click.argument('typeo',type=click.Choice(TYPE_MEAN.keys()),default='x')
def Handle_types(typeo):
    '''selecting function to run'''
    TYPE_MEAN[typeo]()

Handle_types()#->>>>>>Finally calling main functions