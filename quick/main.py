import click
import os

class ComplexCLI(click.MultiCommand):
    #ovrewriting the class
    def list_commands(self, ctx):
        #returns the list of commands from the commands folder
        commands_list = []
        for filename in os.listdir( os.path.join(os.path.dirname(__file__),"commands")):
            if filename.endswith(".py") and not filename.startswith("__"):
                commands_list.append(filename.replace(".py",''))
        commands_list.sort()
        return commands_list
    
    def get_command(self, ctx, name):
        try:
            mod = __import__(f"quick.commands.{name}", None, None, ["cli"])
        except ImportError:
            return
        return mod.cli

#entry point function
@click.command(cls=ComplexCLI)
def main():
    """Welcome to quick!"""
    pass