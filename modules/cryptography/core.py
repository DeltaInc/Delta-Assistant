class crypt:
    #This Is PPP1,And This Is The Frist Verion Of PPP
    aZ = {"a":"1","b":"2","c":"3","d":"4","e":"5","f":"6","g":"7","h":"8","i":"9","j":"111","k":"11","l":"12","m":"13","n":"14","o":"15","p":"16","q":"17","r":"18","s":"19","t":"211","u":"21","v":"22","w":"23","x":"24","y":"25","z":"26","A":"27","B":"28","C":"29","D":"311","E":"31","F":"32","G":"33","H":"34","I":"35","J":"36","K":"37","L":"38","M":"39","N":"411","O":"41","P":"42","Q":"43","R":"44","S":"45","T":"46","U":"47","V":"48","W":"49","X":"511","Y":"51","Z":"52"}
    Za = {"1":"a","2":"b","3":"c","4":"d","5":"e","6":"f","7":"g","8":"h","9":"i","111":"j","11":"k","12":"l","13":"m","14":"n","15":"o","16":"p","17":"q","18":"r","19":"s","211":"t","21":"u","22":"v","23":"w","24":"x","25":"y","26":"z","27":"A","28":"B","29":"C","311":"D","31":"E","32":"F","33":"G","34":"H","35":"I","36":"J","37":"K","38":"L","39":"M","411":"N","41":"O","42":"P","43":"Q","44":"R","45":"S","46":"T","47":"U","48":"V","49":"W","511":"X","51":"Y","52":"Z"}
    def crypt(op:str,CODE):
        Code = CODE
        if op=="decrypt":
            return crypt.decrypt(Code)
        elif op=="encrypt":
            return crypt.encrypt(Code)
        else:
            return "crypt.ParametersError: Please Check Your Parameters"
    def encrypt(code):
        decrypt_str = ""
        for inp in str(code):
            if inp in crypt.aZ:
                inp_val =  crypt.aZ.get(inp)
                decrypt_str += f"{inp_val}0"
        return str(decrypt_str)
    
    def decrypt(code):
        decrypt_str = ""
        for inp in str(code).split("0"):
            if inp in crypt.Za:
                inp_val =  crypt.Za.get(inp)
                decrypt_str += inp_val
        return str(decrypt_str)



