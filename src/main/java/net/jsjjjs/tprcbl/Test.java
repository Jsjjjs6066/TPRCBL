package net.jsjjjs.tprcbl;

import net.jsjjjs.tprcbl.registries.FGRegistry;
import org.fusesource.jansi.Ansi;

public class Test {
    public static void main(String[] args) {
//        System.out.println(FGRegistry.RED.color() + "Interrupted!" + FGRegistry.RESET.color());
//        System.out.println(FGRegistry.YELLOW.color() + "Get warned!" + FGRegistry.RESET.color());
//        System.out.println(FGRegistry.GREEN.color() + "Actually, you are alright!" + FGRegistry.RESET.color());
//        System.out.println("Bye!");
        System.out.println(Ansi.ansi().fg(Ansi.Color.BLUE).a("(i) info"));
        System.out.println(Ansi.ansi().fgBright(Ansi.Color.BLUE).a("(i) info"));
        System.out.println(Ansi.ansi().fg(Ansi.Color.WHITE).a("> Test"));
        System.out.println(Ansi.ansi().fgBright(Ansi.Color.WHITE).a("> test"));
        System.out.println(Ansi.ansi().fg(Ansi.Color.RED).a("(i) Critical"));
        System.out.println(Ansi.ansi().fgBright(Ansi.Color.RED).a("(i) info"));
        System.out.println(Ansi.ansi().fg(Ansi.Color.YELLOW).a("/!\\ Warning!"));
        System.out.println(Ansi.ansi().fgBright(Ansi.Color.YELLOW).a("/!\\ Warning!"));
    }
}
 