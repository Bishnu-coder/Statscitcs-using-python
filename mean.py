from rich.console import Console
from rich.table import Table
from rich import print
console=Console()
class mean:
    def __init__(self):
        self.x=input('data?')
        self.l_x=[float(i) for i in self.x.split(',') if i!=' ']
        self.f=input('frequency?')
        self.l_f=[float(i) for i in self.f.split(',') if i!=' ']
        self.l_fx=[self.l_f[i]*j for i,j in enumerate(self.l_x)]
        self.sfx=0
        self.n=0
    def set_values(self):
        for i in self.l_f:
            self.n+=i
        for j in self.l_fx:
            self.sfx+=j
    def get_table(self):
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
        print("[green]solution,[/green]")
        print(f'[magenta]   mean=Σfx/n[/magenta]')
        print(f'[magenta]    ={self.sfx/self.n}->answer[/magenta]')         
means=mean()
means.get_table()
means.get_solution()
