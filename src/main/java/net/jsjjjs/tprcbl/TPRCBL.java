package net.jsjjjs.tprcbl;

import net.jsjjjs.tprcbl.registries.FGRegistry;
import org.fusesource.jansi.AnsiConsole;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.InvocationTargetException;

public class TPRCBL {
    public static void main(String[] args) {
        AnsiConsole.systemInstall();
        JSONParser parser = new JSONParser();
        if (args.length >= 1) {
            try (FileReader fr = new FileReader(args[0]) ) {
                JSONObject json = (JSONObject) parser.parse(fr);
                PageBuilder pageBuilder = new PageBuilder(json);
                pageBuilder.build();
            }catch (FileNotFoundException e) {
                System.out.println(FGRegistry.RED + "File \"" + args[0] + "\" does not exist!" + FGRegistry.RESET);
            } catch (ParseException e) {
                System.out.println(FGRegistry.RED + "File not structured correctly!" + FGRegistry.RESET);
            } catch (IOException e) {
                System.out.println(FGRegistry.RED + "Interrupted!" + FGRegistry.RESET);
            } catch (InvocationTargetException | NoSuchMethodException | InstantiationException |
                     IllegalAccessException e) {

            }
        }
    }
}
