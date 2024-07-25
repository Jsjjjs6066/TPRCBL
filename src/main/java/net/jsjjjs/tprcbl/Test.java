package net.jsjjjs.tprcbl;

import net.jsjjjs.tprcbl.registries.FGRegistry;

public class Test {
    public static void main(String[] args) {
        System.out.println(FGRegistry.RED.color() + "Interrupted!" + FGRegistry.RESET.color());
        System.out.println(FGRegistry.YELLOW.color() + "Get warned!" + FGRegistry.RESET.color());
        System.out.println(FGRegistry.GREEN.color() + "Actually, you are alright!" + FGRegistry.RESET.color());
        System.out.println("Bye!");
    }
}
 