/**
 * This is a sub-class class of the Shape class and provides a concrete
 * implementation for getArea() method and also overrides getDescription()
 * getParentClassName() and getClassname() will magically work correctly
 * and are inherited from Shape class
 */
 

/**
 * @author gvenkat
 *
 */
public class Circle extends Shape {
	
	//field
	private double radius;
	
	//final immutable field.  So this is a constant
	private final String description = "This Shape is a Circle";

	public Circle() {
		super();
		this.radius = 1;
		// Usually a constructor can be used to initialize the object creation
	}

	@Override
	public double getArea() {
		// TODO Auto-generated method stub
		double area = Math.PI * radius * radius;
		return area;
	}
	
	public double getArea(double r) {
		// TODO Auto-generated method stub
		this.setRadius(r);
		double area = Math.PI * radius * radius;
		return area;
	}

	public double getRadius() {
		return radius;
	}

	public void setRadius(double radius) {
		this.radius = radius;
	}

	public String getDescription() {
		return description;
	}
	
	
} // end of the class
