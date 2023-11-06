package BackEnd;

public class Plane {
    private final String name;
    private final String purpose;
    private final String armament;
    private final String maxSpeed;
    private final String maxRange;

    public Plane(String name, String purpose, String armament, String maxSpeed, String maxRange) {
        this.name = name;
        this.purpose = purpose;
        this.armament = armament;
        this.maxSpeed = maxSpeed;
        this.maxRange = maxRange;
    }

    public String getName() {
        return name;
    }

    public String getPurpose() {
        return purpose;
    }

    public String getArmament() {
        return armament;
    }

    public String getMaxSpeed() {
        return maxSpeed;
    }

    public String getMaxRange() {
        return maxRange;
    }
}
