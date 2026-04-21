# Onboard one more LOB (Multi-LOB Usecase)

Let’s say a customer already has 2 LOBs: Life Insurance and Home Loans and customer gives us the requirement to onboard more LOBs for example: Mutual Funds, Finance Loans, and Health Insurance.

First we need to understand what is the scope of each of the new LOBs? The scope understanding we need to go each LOB wise.

Let’s start with PartnerIQ

- Is Seller Onboarding needed?
- Is Recruitment needed?
- Is Recruitment + Onboarding entire package is needed?
- Do we need both DIY and Assisted Seller Onboarding?
- Is Partner Relationship Management (PRM) needed?

**Only Seller Onboarding is needed + Only DIY Journey**

In Summary for enabling “Seller Onboarding + Only DIY Journey for a LOB” following changes are required

- A dedicated Onboarding Application Module for that LOB
- Adding of this new LOB in the “Entities” config in Global JSON
- Adding of this new LOB and Module in PortalsV2 Configuration
- Adding various relevant configs in the
- Configuring Stepper Workflow in the Onboarding Application module for this new LOB
    - States/Milestones > Steps > Actions > Input Fields
    - Configuring a stepper state

Detailed Things to Do

- Have a dedicated Onboarding Applications Module in the client instance.
    - If it’s already there then we can use it..
    - If not then add the module at the client instance level. When adding the module this will be module of type “lead”
- Global JSON Configuration
    
    In the Global JSON Configuration we need to do config changes in following models
    
    - Entities
    - Portals V2
    - Entities Config
        - In this config model we will add our new LOB here.
        - We will define a dedicated entity code for this new LOB and we will also give it a name and description.
    - PortalsV2 Config
        - In this config model we will map the new LOB with the new onboarding application module we created.
        - We will define the unique identifier which will be PAN incase of Seller Onboarding India.
        - We will define a default user-code to whom should the lead be assigned to. This user can be something like LOB SPOC.
- Module Level JSON Configuration
    - States/Workflow/Lead Lifecycle/Milestone
        - Use the Lead Lifecycle UI here to easily configure the states/milestones
    - Steps, defining steps
        - Name and unique code for each of the steps
        - Map each step with a state using state code
        - Configure the Enable IF and ApplicableIF conditions for each of the steps.
    - Actions, defining actions
        - Name and unique code for each of the actions
        - Action Type: Form Filling, Profile Integration, Callback Integration
        - Map the input fields to each of the actions
        - Configure the Enable IF and ApplicableIF conditions for each of the actions.
    - Step Action Mapping
        - To map multiple actions with a step.
    - Input Fields Configuration
        - When configuring input fields. First configure the field using the “Field Configuration UI” and add all the fields in the Stepper State
        - Fields that are required to create an onboarding lead in Vymo should be present in the Add Form / Add/New State.
        - Plus fields needed for the Candidate Dropped State should be present in that respective state only.
        - Rest all the fields needed for the onboarding journey should be present in the Stepper State.
    - Unique Identifier Config
        - We will define unique identifier for an onboarding lead which will be PAN
        - In this config we have property called ignoreForStates > here we will enter the lost/drop state of the onboarding module.
        - Because our usecase is
            - The system should check based on “PAN” that there shouldn’t be any existing OPEN or WON onboarding lead in Vymo.
            - Having a drop/lost lead for the same PAN is okh, hence in ignoreForStates we have added the drop state there.
            - But already a running lead or onboarded/won lead shouldn’t be there. If condition is satisfied then an onbaording lead should get created else through an error.
    - Field Replication Config
        - This config allows us to automatically update seller/distributor profile based on certain rules.
        - Here we need to define two rules
            - Update the distributor record which is nothing but a user record when consent action is COMPLETED
            - Second, update the distributor/user record when the candidate is ONBOARDED/the onboarding lead has reached Onboarded state/milestone.
    - In summary we would need this configs to be done —> *Lead Lifecycle Configuration, Input Fields, Steps, Actions, Step Action Mapping, Field Replication, Unique Identifier Config*
- Once all the above changes are done then this new LOB will start showing up in the Multi LOB Onboarding Portal.
- The candidate will be able to create an onboarding lead in vymo by selecting the new LOB.