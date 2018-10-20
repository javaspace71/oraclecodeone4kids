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
public class Triangle extends Shape {
	
	//field
	private double height;
	private double base;
	
	//final immutable field.  So this is a constant
	private final String description = "This Shape is a Triangle";

	public Triangle() {
		super();
		this.height = 1;
		this.base = 1;
		// Usually a constructor can be used to initialize the object creation
	}

	@Override
	public double getArea() {
		//System.out.println("Base: " + base);
		//System.out.println("Height: " + height);
		double area = base * height * 0.5;  // (area = b x h / 2)
		return area;
	}
	
	public double getArea(double base, double height) {
		this.setBase(base);
		this.setHeight(height);
		//we do not need to compute the formula again
		//double area = (1/2) * base * height;
		
		//we can call the getArea() method now
		//the default value of 1 for base and height is now overwritten
		//by the vale we set in this method
		return getArea();
	}

	public double getHeight() {
		return height;
	}

	public void setHeight(double height) {
		this.height = height;
	}

	public double getBase() {
		return base;
	}

	public void setBase(double base) {
		this.base = base;
	}

	public String getDescription() {
		return description;
	}
	
} // end of the class
