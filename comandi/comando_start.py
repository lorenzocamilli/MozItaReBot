
def start(update: Update, context: CallbackContext):
    '''Comando start, mostra messaggio di benvenuto e indirizza al menu'''
    buttons = [
        [InlineKeyboardButton(str(frasi["button_start"]), callback_data="help")]]

    reply_markup = InlineKeyboardMarkup(buttons)
    update.message.reply_text(
        str(frasi["start"]), reply_markup=reply_markup, parse_mode="MARKDOWN")

