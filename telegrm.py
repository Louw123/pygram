from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import ast
import astor

def concat_list(input: list):
    return "".join(str(element) for element in input)

def traverse(node, indent=0):
    print(" " * indent + f"({type(node).__name__}")
    for child_node in ast.iter_child_nodes(node):
        traverse(child_node, indent + 2)
        print(" " * indent + ")")
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello there')

async def tst(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello there')


async def Pythontree(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(context.args)
    print(ast.parse(concat_list(context.args)))
    print(astor.dump_tree(ast.parse(concat_list(context.args))))
    await update.message.reply_text(astor.dump_tree(ast.parse(concat_list(context.args))))

async def PythonEval(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(context.args) == 0:
         raise EOFError("No input found. Please specify python code")
    else:
        print(context.args)
        print(' '.join(context.args))
        await update.message.reply_text(exec(' '.join(context.args)))




async def AhShitHereWeGoAgain(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"{context.error}")


if __name__ == "__main__":
    app = ApplicationBuilder().token(.).build()
    print("cmd")
    app.add_handler(CommandHandler("hello", hello))
    # app.add_handler(CommandHandler("uxn", uxn))
    app.add_handler(CommandHandler("showTree", Pythontree))
    app.add_handler(CommandHandler("pythonexec", PythonEval))
    app.add_error_handler(AhShitHereWeGoAgain)

    app.run_polling()