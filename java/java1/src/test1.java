import java.io.*;
import java.util.Calendar;
import java.util.GregorianCalendar;

/**
 * @author he
 * @date 2021/9/22
 * @time 10:08
 * @message
 */
public class test1 {

    public static void main(String[] args) {

        try{
            byte[] write={1,2,3,4,5,6,7};
            File f=new File("C:\\Users\\11691\\Desktop\\123.txt");
            FileOutputStream fop=new FileOutputStream(f);
            OutputStreamWriter writer=new OutputStreamWriter(fop,"UTF-8");
            for(byte x:write){
                writer.append(String.valueOf(x));
            }
            writer.close();
            fop.close();
            FileInputStream fin=new FileInputStream(f);
            InputStreamReader reader=new InputStreamReader(fin,"UTF-8");
            StringBuffer sb=new StringBuffer();
            while (reader.ready()){
                sb.append((char) reader.read());
            }
            System.out.println(sb.toString());
            reader.close();
            fin.close();
        }catch (IOException e){
            System.out.println("!");
        }
    }
}
